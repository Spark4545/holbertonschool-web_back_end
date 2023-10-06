export default function updateStudentGradeByCity(students, city, newGrades) {
  const filteredStudents = students.filter((student) => student.location === city);

  const updatedStudents = filteredStudents.map((student) => {
    const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);

    const grade = matchingGrade ? matchingGrade.grade : 'N/A';

    return {
      ...student,
      grade,
    };
  });

  return updatedStudents;
}
