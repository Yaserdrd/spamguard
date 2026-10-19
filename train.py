"""SpamGuard: gerçek UCI SMS verisiyle tekrarlanabilir eğitim ve değerlendirme."""
from pathlib import Path
import json, re, hashlib, platform, io, zipfile, urllib.request
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.dummy import DummyClassifier
import joblib

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'outputs'
OUT.mkdir(exist_ok=True)
FEATURES = ['character_count', 'word_count', 'digit_count', 'exclamation_count', 'uppercase_ratio', 'url_count']

def features(text):
    letters = [c for c in text if c.isalpha()]
    return [len(text), len(text.split()), sum(c.isdigit() for c in text), text.count('!'),
            sum(c.isupper() for c in letters)/max(len(letters),1), len(re.findall(r'https?://|www\.', text.lower()))]

def measure(y, pred):
    return {name: float(fn(y,pred,zero_division=0)) for name,fn in [('precision',precision_score),('recall',recall_score),('f1',f1_score)]} | {'accuracy':float(accuracy_score(y,pred))}

def run():
    # Ham SMS metinleri public depoda tutulmaz; resmi veri kaynağından alınır.
    data_path = ROOT/'data/SMSSpamCollection'
    if not data_path.exists():
        data_path.parent.mkdir(exist_ok=True)
        with urllib.request.urlopen('https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip', timeout=60) as response:
            archive = zipfile.ZipFile(io.BytesIO(response.read()))
        data_path.write_bytes(archive.read('SMSSpamCollection'))
    # Bölme öncesi benzer yazımlı tam kopyalar tek örneğe indirilir.
    raw = pd.read_csv(ROOT/'data/SMSSpamCollection', sep='\t', names=['label','text'], quoting=3, keep_default_na=False)
    raw['key'] = raw.text.map(lambda s: re.sub(r'\s+',' ',s.strip().lower()))
    empty = (raw.key=='') | ~raw.label.isin(['ham','spam'])
    conflicting = raw.groupby('key').label.nunique()
    conflicts = set(conflicting[conflicting>1].index)
    clean = raw[~empty & ~raw.key.isin(conflicts)].drop_duplicates('key').copy().reset_index(drop=True)
    clean['target'] = (clean.label=='spam').astype(int)
    for i,col in enumerate(FEATURES): clean[col] = clean.text.map(lambda s: features(s)[i])
    clean['id'] = np.arange(len(clean))
    train, rest = train_test_split(clean.id, test_size=.4, random_state=42, stratify=clean.target)
    val, test = train_test_split(rest, test_size=.5, random_state=42, stratify=clean.loc[rest,'target'])
    clean['split']='train'; clean.loc[val,'split']='validation'; clean.loc[test,'split']='test'
    clean.drop(columns='key').to_csv(ROOT/'data/sms_features.csv',index=False)
    clean[['id','label','text','split']].to_csv(ROOT/'data/sms_text.csv',index=False)
    X=clean[FEATURES]; y=clean.target
    choices=[]
    for depth in [3,5,8]:
        m=DecisionTreeClassifier(max_depth=depth,min_samples_leaf=5,class_weight='balanced',random_state=42).fit(X.loc[train],y.loc[train])
        choices.append((f1_score(y.loc[val],m.predict(X.loc[val])),depth,m))
    _,depth,tree=max(choices,key=lambda x:x[0])
    # Vectorizer yalnızca eğitim bölümünde öğrenir.
    vectorizer=TfidfVectorizer(lowercase=True,token_pattern=r'[a-z0-9_]{2,}',max_features=5000,sublinear_tf=True)
    Ztrain=vectorizer.fit_transform(clean.loc[train,'text'])
    Zval=vectorizer.transform(clean.loc[val,'text'])
    Ztest=vectorizer.transform(clean.loc[test,'text'])
    lr_choices=[]
    for C in [.5,1.,2.,4.]:
        m=LogisticRegression(C=C,class_weight='balanced',max_iter=1000,random_state=42).fit(Ztrain,y.loc[train])
        lr_choices.append((f1_score(y.loc[val],m.predict(Zval)),C,m))
    _,C,lr=max(lr_choices,key=lambda x:x[0])
    nb_choices=[]
    for alpha in [.1,.5,1.]:
        m=MultinomialNB(alpha=alpha).fit(Ztrain,y.loc[train])
        nb_choices.append((f1_score(y.loc[val],m.predict(Zval)),alpha,m))
    _,alpha,nb=max(nb_choices,key=lambda x:x[0])
    dummy=DummyClassifier(strategy='most_frequent').fit(X.loc[train],y.loc[train])
    predictions={'Majority baseline':dummy.predict(X.loc[test]),'Decision Tree':tree.predict(X.loc[test]),'TF-IDF + Logistic Regression':lr.predict(Ztest),'TF-IDF + Naive Bayes':nb.predict(Ztest)}
    metrics={name:measure(y.loc[test],pred) for name,pred in predictions.items()}
    report={'source':'https://archive.ics.uci.edu/dataset/228/sms+spam+collection','license':'CC BY 4.0',
      'raw_rows':len(raw),'removed_empty_invalid':int(empty.sum()),'conflicting_keys':len(conflicts),'clean_rows':len(clean),
      'duplicates_removed':int((~empty & ~raw.key.isin(conflicts)).sum()-len(clean)),
      'class_counts':clean.label.value_counts().to_dict(),'split_counts':clean.split.value_counts().to_dict(),
      'hyperparameters':{'tree_max_depth':depth,'tree_min_samples_leaf':5,'lr_C':C,'nb_alpha':alpha},
      'validation_f1':{'Decision Tree':max(x[0] for x in choices),'Logistic Regression':max(x[0] for x in lr_choices),'Naive Bayes':max(x[0] for x in nb_choices)},
      'metrics':metrics,'environment':{'python':platform.python_version(),'sklearn':sklearn.__version__},
      'data_sha256':hashlib.sha256((ROOT/'data/SMSSpamCollection').read_bytes()).hexdigest()}
    (OUT/'metrics.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    split_rows=[]
    for model_name, fitted_model in [('Logistic Regression',lr),('Naive Bayes',nb)]:
        for split_name, indices in [('train',train),('validation',val),('test',test)]:
            split_pred=fitted_model.predict(vectorizer.transform(clean.loc[indices,'text']))
            split_rows.append({'model':model_name,'split':split_name,'n':len(indices),**measure(y.loc[indices],split_pred)})
    pd.DataFrame(split_rows).to_csv(OUT/'split_comparison.csv',index=False)

    pd.DataFrame(metrics).T.to_csv(OUT/'model_comparison.csv')
    clean[FEATURES].describe().to_csv(OUT/'feature_summary.csv')
    clean.groupby('label')[FEATURES].mean().to_csv(OUT/'group_means.csv')
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    colors=['#168A78','#E08245']
    fig,ax=plt.subplots(figsize=(6,4)); clean.label.value_counts().reindex(['ham','spam']).plot.bar(ax=ax,color=colors,rot=0)
    ax.set(title='Mesaj sınıflarının dağılımı',xlabel='Sınıf',ylabel='Mesaj sayısı'); fig.tight_layout(); fig.savefig(OUT/'class_distribution.png',dpi=160); plt.close(fig)
    fig,ax=plt.subplots(figsize=(6,4))
    for label,color in zip(['ham','spam'],colors): ax.hist(clean.loc[clean.label==label,'character_count'],bins=np.arange(0,1000,25),alpha=.55,label=label,color=color,density=True)
    ax.set(title='Sınıflara göre mesaj uzunluğu',xlabel='Karakter sayısı',ylabel='Yoğunluk'); ax.legend(); fig.tight_layout(); fig.savefig(OUT/'length_distribution.png',dpi=160); plt.close(fig)
    fig,ax=plt.subplots(figsize=(6,4)); clean.groupby('label')[['digit_count','exclamation_count','url_count']].mean().T.plot.bar(ax=ax,color=colors,rot=0)
    ax.set(title='Sınıflara göre ortalama özellik değerleri',xlabel='Özellik',ylabel='Mesaj başına ortalama'); fig.tight_layout(); fig.savefig(OUT/'feature_means.png',dpi=160); plt.close(fig)
    for name,pred in predictions.items():
        if name=='Majority baseline':continue
        fig,ax=plt.subplots(figsize=(4.5,4)); ConfusionMatrixDisplay(confusion_matrix(y.loc[test],pred),display_labels=['ham','spam']).plot(ax=ax,colorbar=False,cmap='Blues')
        ax.set(title=name,xlabel='Tahmin',ylabel='Gerçek sınıf'); fig.tight_layout(); fig.savefig(OUT/('cm_'+('tree' if name=='Decision Tree' else 'lr' if 'Logistic' in name else 'nb')+'.png'),dpi=160); plt.close(fig)
    errors=clean.loc[test,['id','label','text']].copy(); errors['prediction']=np.where(predictions['TF-IDF + Logistic Regression']==1,'spam','ham')
    errors['spam_score']=lr.predict_proba(Ztest)[:,1]; errors[errors.label!=errors.prediction].to_csv(OUT/'lr_errors.csv',index=False)
    examples=['Can we meet at the library at six this evening?', 'Congratulations! Claim your free prize now. Call 09001234567!', 'Your order will arrive tomorrow. Thank you for shopping with us.']
    E=pd.DataFrame([features(t) for t in examples],columns=FEATURES)
    ep=pd.DataFrame({'text':examples,'tree_prediction':np.where(tree.predict(E)==1,'spam','ham'),'lr_prediction':np.where(lr.predict(vectorizer.transform(examples))==1,'spam','ham')})
    ep.to_csv(OUT/'new_examples.csv',index=False)
    joblib.dump({'tree':tree,'features':FEATURES},ROOT/'python/model.joblib')
    joblib.dump({'vectorizer':vectorizer,'lr':lr,'nb':nb},ROOT/'ml/models.joblib')
    export={'vocabulary':{k:int(v) for k,v in vectorizer.vocabulary_.items()},'idf':vectorizer.idf_.tolist(),'weights':lr.coef_[0].tolist(),'intercept':float(lr.intercept_[0]),'threshold':.5,'metrics':metrics['TF-IDF + Logistic Regression'],'training_rows':len(train),'test_rows':len(test),'source':report['source']}
    (ROOT/'web/public/model.json').write_text(json.dumps(export),encoding='utf-8')
    # Tarayıcı modeliyle sayısal eşdeğerlik için sabit doğrulama örnekleri.
    checks=clean.loc[test,'text'].iloc[:25].tolist()+examples
    (OUT/'browser_parity.json').write_text(json.dumps({'texts':checks,'expected':lr.predict_proba(vectorizer.transform(checks))[:,1].tolist()}))
    print(json.dumps(report,indent=2))
    print(ep.to_string(index=False))
    return report

if __name__=='__main__': run()
