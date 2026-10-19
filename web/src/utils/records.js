// Update the existing analysis instead of duplicating it on repeated saves.
export function upsertRecord(records, record) {
  const existing=records.find(item=>item.id===record.id);
  const next={...existing,...record,createdAt:existing?.createdAt||record.updatedAt};
  return existing?records.map(item=>item.id===record.id?next:item):[next,...records];
}
