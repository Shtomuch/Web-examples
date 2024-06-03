SELECT students.name, grades.grade
FROM students
JOIN grades ON students.student_id = grades.student_id
WHERE students.group_id = 1 AND grades.subject_id = 2;  -- Вставте ідентифікатори групи і предмета
