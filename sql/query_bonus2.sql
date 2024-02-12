--Оцінки студентів у певній групі з певного предмета на останньому занятті.
SELECT ROUND(AVG(Grades.grade), 2) as grade_end_group
FROM Grades
JOIN Students ON Grades.student_id = Students.student_id
JOIN Groups ON Students.group_id = Groups.group_id
JOIN Subjects ON Grades.subject_id = Subjects.subject_id
WHERE Groups.group_id = 2 AND Subjects.subject_id = 2
ORDER BY Grades.date_received DESC;