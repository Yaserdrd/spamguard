import assert from 'node:assert/strict';
import {upsertRecord} from '../src/utils/records.js';
const first=upsertRecord([],{id:'a',text:'first',updatedAt:'before'});
const edited=upsertRecord(first,{id:'a',text:'changed',updatedAt:'after'});
assert.equal(edited.length,1);assert.equal(edited[0].text,'changed');
assert.equal(edited[0].createdAt,'before');assert.equal(first[0].text,'first');
assert.equal(upsertRecord(edited,{id:'b',updatedAt:'now'}).length,2);
console.log('Record add/update and duplicate prevention: passed');
