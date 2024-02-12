import sqlite3
from faker import Faker
import random
import string
import datetime
import csv

# Підключення до бази даних
conn = sqlite3.connect('database_HW6.db')
cursor = conn.cursor()

fake = Faker()

# Створення схеми бази даних
cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                    student_id INTEGER PRIMARY KEY,
                    name TEXT,
                    group_id INTEGER,
                    FOREIGN KEY (group_id) REFERENCES Groups(group_id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Groups (
                    group_id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Professors (
                    professor_id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Subjects (
                    subject_id INTEGER PRIMARY KEY,
                    name TEXT,
                    professor_id INTEGER,
                    FOREIGN KEY (professor_id) REFERENCES Professors(professor_id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Grades (
                    grade_id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    date_received DATE,
                    FOREIGN KEY (student_id) REFERENCES Students(student_id),
                    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
                )''')

conn.commit()

# Очищення таблиць перед заповненням новими даними
tables = ['Students', 'Groups', 'Professors', 'Subjects', 'Grades']
for table in tables:
    cursor.execute(f"DELETE FROM {table}")
conn.commit()

# Створення груп
for _ in range(3):
    group_name = 'Group ' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    cursor.execute("INSERT INTO Groups (name) VALUES (?)", (group_name,))
conn.commit()

# Створення викладачів
for _ in range(5):
    cursor.execute("INSERT INTO Professors (name) VALUES (?)", (fake.name(),))
conn.commit()

# Створення предметів та їх призначення викладачам
for _ in range(5):
    subject_name = fake.job()
    professor_id = random.randint(1, 5)
    cursor.execute("INSERT INTO Subjects (name, professor_id) VALUES (?, ?)", (subject_name, professor_id))
conn.commit()

# Створення студентів та їх призначення до груп
for group_id in range(1, 4):
    for _ in range(30):
        name = fake.name()
        cursor.execute("INSERT INTO Students (name, group_id) VALUES (?, ?)", (name, group_id))
conn.commit()

# Створення оцінок для студентів
students_ids = list(range(1, 91))  # 30 студентів у кожній групі
subjects_ids = list(range(1, 6))
for student_id in students_ids:
    for subject_id in subjects_ids:
        for _ in range(20):
            grade = random.randint(60, 100)
            date_received = fake.date_time_this_year(before_now=True, after_now=False)
            date_received = date_received.date()  # Отримання лише дати без часу
            cursor.execute("INSERT INTO Grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)",
                           (student_id, subject_id, grade, date_received))
conn.commit()

# Експорт таблиць до CSV
def export_to_csv(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    with open(f'{table_name}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([i[0] for i in cursor.description])  # Запис заголовків стовбців
        csv_writer.writerows(cursor.fetchall())

for table in tables:
    export_to_csv(table)

# Закриття підключення до бази даних
cursor.close()
conn.close()
