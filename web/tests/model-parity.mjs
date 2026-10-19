import fs from 'node:fs';
import assert from 'node:assert/strict';
import {analyze} from '../src/inference.js';
const model=JSON.parse(fs.readFileSync(new URL('../public/model.json',import.meta.url)));
const checks=JSON.parse(fs.readFileSync(new URL('./parity.json',import.meta.url)));
let maxError=0;
for(let i=0;i<checks.texts.length;i++){
 const result=analyze(checks.texts[i],model);
 maxError=Math.max(maxError,Math.abs(result.score-checks.expected[i]));
 assert(Math.abs(result.score-checks.expected[i])<1e-10);
 assert(Math.abs(model.intercept+result.contributions.reduce((s,x)=>s+x.contribution,0)-Math.log(result.score/(1-result.score)))<1e-9);
}
assert.equal(analyze('',model).knownTokens,0);
assert.equal(analyze('!!!!',model).knownTokens,0);
console.log(`Python/JavaScript eşdeğerliği: ${checks.texts.length} metin, en büyük fark ${maxError}`);
