SELECT subjects.name
FROM subjects
JOIN grades ON subjects.subject_id = grades.subject_id
WHERE grades.student_id = 3 AND subjects.teacher_id = 2  -- Вставте ідентифікатори студента і викладача
GROUP BY subjects.subject_id;
