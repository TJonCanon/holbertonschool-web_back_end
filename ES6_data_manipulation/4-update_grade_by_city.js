// returns an array of students in a city with their grade
export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((data) => data.location === city)
    .map((data) => {
      const dupe = data;
      dupe.grade = 'N/A';
      for (const prop of newGrades) {
        if (dupe.id === prop.studentId) dupe.grade = prop.grade;
      }
      return dupe;
    });
}
