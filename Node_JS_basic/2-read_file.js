// reads csv file synchronously
const fs = require('fs');

function countStudents(path) {
  // counts # of students
  try {
    const data = fs.readFileSync(path, 'utf8');

    let lines = data.split('\n');
    lines = lines.filter((line) => line !== '').slice(1);

    console.log(`Number of students: ${lines.length}`);

    const fields = {};
    for (const line of lines) {
      if (line) {
        const student = line.split(',');
        if (!fields[student[3]]) {
          fields[student[3]] = [];
        }
        fields[student[3]].push(student[0]);
      }
    }

    for (const field in fields) {
      if (field) {
        console.log(
          `Number of students in ${field}: ${
            fields[field].length
          }. List: ${fields[field].join(', ')}`,
        );
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
