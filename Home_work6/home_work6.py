import sqlite3
from faker import Faker
import random

# Ініціалізуємо Faker
fake = Faker()

# Підключаємось до бази даних (створюється файл database.db)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Створення таблиць
cursor.execute('''
CREATE TABLE IF NOT EXISTS groups (
    group_id INTEGER PRIMARY KEY,
    group_name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (group_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS subjects (
    subject_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
    grade_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date TEXT,
    FOREIGN KEY (student_id) REFERENCES students (student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
)
''')


# Генерація груп
groups = ['Group A', 'Group B', 'Group C']
for group in groups:
    cursor.execute('INSERT INTO groups (group_name) VALUES (?)', (group,))

# Генерація викладачів
teachers = [fake.name() for _ in range(5)]
for teacher in teachers:
    cursor.execute('INSERT INTO teachers (name) VALUES (?)', (teacher,))

# Генерація предметів
subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature', 'Art']
for subject in subjects:
    teacher_id = random.randint(1, 5)
    cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (subject, teacher_id))

# Генерація студентів
for _ in range(50):
    name = fake.name()
    group_id = random.randint(1, 3)
    cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (name, group_id))

# Генерація оцінок
for student_id in range(1, 51):
    for subject_id in range(1, len(subjects) + 1):
        for _ in range(random.randint(10, 20)):
            grade = random.randint(1, 100)
            date = fake.date_this_year()
            cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)', (student_id, subject_id, grade, date))


# Запити до бази даних

with open('query_1.sql', 'r') as file:
    query = file.read()
cursor.execute(query)
top_5_students = cursor.fetchall()
print("5 студентів із найбільшим середнім балом з усіх предметів:")
print(top_5_students)

# Знайти студента із найвищим середнім балом з певного предмета
subject_id = 1  # Наприклад, subject_id = 1
with open('query_2.sql', 'r') as file:
    query = file.read()
cursor.execute(query, (subject_id,))
top_student_subject = cursor.fetchone()
print(f"Студент із найвищим середнім балом з предмета {subject_id}:")
print(top_student_subject)

# Знайти середній бал у групах з певного предмета
with open('query_3.sql', 'r') as file:
    query = file.read()
cursor.execute(query)
avg_grade_by_group = cursor.fetchall()
print(f"Середній бал у групах з предмета {subject_id}:")
print(avg_grade_by_group)

# Знайти середній бал на потоці (по всій таблиці оцінок)
with open('query_4.sql', 'r') as file:
    query = file.read()
cursor.execute(query)
avg_grade_overall = cursor.fetchone()
print("Середній бал на потоці:")
print(avg_grade_overall)

# Знайти які курси читає певний викладач
teacher_id = 1
with open('query_5.sql', 'r') as file:
    query = file.read().strip()
cursor.execute(query, (teacher_id,))
courses_by_teacher = cursor.fetchall()
print(f"Курси, які читає викладач {teacher_id}:")
print(courses_by_teacher)

# Знайти список студентів у певній групі
group_id = 1  # Наприклад, group_id = 1
with open('query_6.sql', 'r') as file:
    query = file.read().strip()
cursor.execute(query, (group_id,))
students_in_group = cursor.fetchall()
print(f"Список студентів у групі {group_id}:")
print(students_in_group)

# Знайти оцінки студентів у окремій групі з певного предмета
with open('query_7.sql', 'r') as file:
    query = file.read()
cursor.execute(query)
grades_in_group_subject = cursor.fetchall()
print(f"Оцінки студентів у групі {group_id} з предмета {subject_id}:")
print(grades_in_group_subject)

# Знайти середній бал, який ставить певний викладач зі своїх предметів
with open('query_8.sql', 'r') as file:
    query = file.read()
cursor.execute(query)
avg_grade_by_teacher = cursor.fetchone()
print(f"Середній бал, який ставить викладач {teacher_id}:")
print(avg_grade_by_teacher)

# Знайти список курсів, які відвідує студент

with open('query_9.sql', 'r') as file:
    query = file.read()
cursor.execute(query)
courses_by_student = cursor.fetchall()
print(f"Список курсів, які відвідує студент {student_id}:")
print(courses_by_student)

# Список курсів, які певному студенту читає певний викладач
with open('query_10.sql', 'r') as file:
    query = file.read()
cursor.execute(query)
courses_by_student_teacher = cursor.fetchall()
print(f"Список курсів, які студенту {student_id} читає викладач {teacher_id}:")
print(courses_by_student_teacher)
# Підтвердження змін і закриття з'єднання
conn.commit()
conn.close()
