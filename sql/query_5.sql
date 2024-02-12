SELECT Subjects.name AS course_name
FROM Subjects
JOIN Lectors ON Subjects.lector_id = Lectors.lector_id
WHERE Subjects.lector_id = 3;