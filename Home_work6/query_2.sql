SELECT students.name, AVG(grades.grade) as avg_grade
FROM students
JOIN grades ON students.student_id = grades.student_id
WHERE grades.subject_id = ?  -- Вставте ідентифікатор предмета
GROUP BY students.student_id
ORDER BY avg_grade DESC
LIMIT 1;
