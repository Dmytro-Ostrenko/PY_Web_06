--Знайти список курсів, які відвідує студент - id 55.
SELECT Subjects.name
FROM Subjects
JOIN Grades ON Subjects.subject_id = Grades.subject_id
JOIN Students ON Grades.student_id = Students.student_id
WHERE Students.student_id = 55
GROUP BY Subjects.name;