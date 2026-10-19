from pathlib import Path
import json,re
import numpy as np,pandas as pd
from sklearn.preprocessing import normalize
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
import joblib
r=Path(__file__).resolve().parent;p=r/'web/public/model.json'
b=joblib.load(r/'ml/models.joblib')
m={'vocabulary':{k:int(v) for k,v in b['vectorizer'].vocabulary_.items()},'idf':b['vectorizer'].idf_.tolist(),'weights':b['lr'].coef_[0].tolist(),'intercept':float(b['lr'].intercept_[0]),'threshold':.5,'training_rows':3095,'test_rows':1032,'source':'https://archive.ics.uci.edu/dataset/228/sms+spam+collection'}
keep=sorted((i,t) for t,i in m['vocabulary'].items() if re.fullmatch(r'[a-z]{2,20}',t))
indices=[i for i,t in keep];removed=len(m['vocabulary'])-len(keep)
m['vocabulary']={t:j for j,(i,t) in enumerate(keep)}
m['idf']=[m['idf'][i] for i in indices];m['weights']=[m['weights'][i] for i in indices]
b=joblib.load(r/'ml/models.joblib');data=pd.read_csv(r/'data/sms_text.csv');test=data[data.split=='test'];y=(test.label=='spam').astype(int).to_numpy()
def scores(texts):
 z=normalize(b['vectorizer'].transform(texts)[:,indices]); logits=np.asarray(z @ np.array(m['weights'])).ravel()+m['intercept'];return 1/(1+np.exp(-logits))
s=scores(test.text);pred=s>=.5
m['metrics']={n:float(f(y,pred)) for n,f in [('accuracy',accuracy_score),('precision',precision_score),('recall',recall_score),('f1',f1_score)]}
cm=confusion_matrix(y,pred);m['error_counts']={'false_positive':int(cm[0,1]),'false_negative':int(cm[1,0])}
m['release_note']='Public web release: digit-containing and non-letter vocabulary tokens removed; scores re-evaluated after vocabulary filtering. Original ML comparison is separate.'
p.write_text(json.dumps(m))
checks=json.loads((r/'web/tests/parity.json').read_text());checks['expected']=scores(checks['texts']).tolist();(r/'web/tests/parity.json').write_text(json.dumps(checks))
ui=r/'web/src/pages/Workspace.jsx';t=ui.read_text();t=t.replace('Testte 5 normal mesaj spam olarak işaretlendi ve 6 spam mesaj kaçırıldı.','Testte {model?.error_counts?.false_positive ?? 5} normal mesaj spam olarak işaretlendi ve {model?.error_counts?.false_negative ?? 6} spam mesaj kaçırıldı.')
t=t.replace('Parametreler doğrulama bölümünde seçildi.','Parametreler doğrulama bölümünde seçildi. Public web sürümünde sayı içeren sözlük tokenları çıkarıldı; aşağıdaki metrikler bu sürüm için yeniden ölçüldü.')
ui.write_text(t)
assert all(re.fullmatch('[a-z]{2,20}',x) for x in m['vocabulary'])
print('Removed vocabulary tokens:',removed,'remaining:',len(keep));print('Web release metrics:',m['metrics']);print('Errors:',m['error_counts'])
