--Знаходимо середній бал у групах з певного предмета (№4).
SELECT Groups.name, ROUND(AVG(Grades.grade), 2) AS average_grade
FROM Groups
JOIN Students ON Groups.group_id = Students.group_id
JOIN Grades ON Students.student_id = Grades.student_id
WHERE Grades.subject_id = 5
GROUP BY Groups.name;