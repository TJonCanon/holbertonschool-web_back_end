export default function getListStudentIds(students) {
  let ids = [];
  if (Array.isArray(students)) ids = students.map((data) => data.id);
  return ids;
}
