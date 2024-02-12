--Зна[jlbvj] оцінки студентів у окремій групі з певного предмета, гр - 3, предмет - 3
SELECT Students.name, Grades.grade, Grades.date_received
FROM Students
JOIN Grades ON Students.student_id = Grades.student_id
WHERE Students.group_id = 3 AND Grades.subject_id = 3;