--Список курсів, які певному студент - 55 у читає певний викладач-2
SELECT DISTINCT Subjects.name AS subject_name
FROM Subjects
JOIN Grades ON Subjects.subject_id = Grades.subject_id
JOIN Students ON Grades.student_id = Students.student_id
WHERE Students.student_id = 55 AND Subjects.lector_id = 2;
