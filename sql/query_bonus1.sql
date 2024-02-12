--Середній бал, який певний викладач ставить певному студентові.
SELECT ROUND(AVG(Grades.grade), 2) AS average_grade
FROM Grades
JOIN Subjects ON Grades.subject_id = Subjects.subject_id
JOIN Lectors ON Subjects.lector_id = Lectors.lector_id
WHERE Lectors.lector_id = 2 AND Grades.student_id = 11;