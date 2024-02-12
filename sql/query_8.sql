--Знайти середній бал, який ставить певний викладач (example #4) зі своїх предметів. 
SELECT Lectors.name, ROUND(AVG(Grades.grade), 2) AS average_grade
FROM Lectors
JOIN Subjects ON Lectors.lector_id = Subjects.lector_id
JOIN Grades ON Subjects.subject_id = Grades.subject_id
WHERE Lectors.lector_id = 4
GROUP BY Lectors.lector_id;
