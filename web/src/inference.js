// scikit-learn TF-IDF (sublinear_tf=true, L2) ve Logistic Regression eşdeğeri.
export function analyze(text, model) {
  const tokens = text.toLowerCase().match(/[a-z0-9_]{2,}/g) || [];
  const counts = new Map();
  for (const token of tokens) if (Object.hasOwn(model.vocabulary, token)) counts.set(token, (counts.get(token) || 0) + 1);
  const values = [...counts].map(([token,count]) => {const index=model.vocabulary[token]; return {token,index,value:(1+Math.log(count))*model.idf[index]};});
  const norm=Math.sqrt(values.reduce((sum,x)=>sum+x.value*x.value,0)) || 1;
  const contributions=values.map(x=>({...x, contribution:x.value/norm*model.weights[x.index]}));
  const logit=model.intercept+contributions.reduce((sum,x)=>sum+x.contribution,0);
  const score=1/(1+Math.exp(-logit));
  return {score,label:score>=model.threshold?'spam':'ham',contributions:contributions.sort((a,b)=>Math.abs(b.contribution)-Math.abs(a.contribution)),knownTokens:values.length,totalTokens:tokens.length};
}
