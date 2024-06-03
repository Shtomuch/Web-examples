SELECT groups.group_name, AVG(grades.grade) as avg_grade
FROM groups
JOIN students ON groups.group_id = students.group_id
JOIN grades ON students.student_id = grades.student_id
WHERE grades.subject_id = 5
GROUP BY groups.group_id;
