--Знайти студента із найвищим середнім балом з певного предмета (оберемо предмет - 2)
SELECT Students.name, ROUND(AVG(Grades.grade), 2) AS average_grade
FROM Students
JOIN Grades ON Students.student_id = Grades.student_id
WHERE Grades.subject_id = 2
GROUP BY Students.student_id
ORDER BY average_grade DESC
LIMIT 1;