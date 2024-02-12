--Знайти середній бал на потоці (по всій таблиці оцінок).

SELECT ROUND(AVG(Grades.grade), 2) AS average_grade
FROM Grades;