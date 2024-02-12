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

sub=5 #кількість предметів
group=3#кількість груп
student=50#кількість студентів груп
min_grade=60
max_grade=100
quantity_grade=20
quantity_lector=5

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

cursor.execute('''CREATE TABLE IF NOT EXISTS Lectors (
                    lector_id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Subjects (
                    subject_id INTEGER PRIMARY KEY,
                    name TEXT,
                    lector_id INTEGER,
                    FOREIGN KEY (lector_id) REFERENCES Lectors(lector_id)
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
tables = ['Students', 'Groups', 'Lectors', 'Subjects', 'Grades']
for table in tables:
    cursor.execute(f"DELETE FROM {table}")
conn.commit()


for _ in range(group): # Створення груп
    group_name = 'Group ' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))
    cursor.execute("INSERT INTO Groups (name) VALUES (?)", (group_name,))
conn.commit()

for _ in range(5): # Створення викладачів
    cursor.execute("INSERT INTO Lectors (name) VALUES (?)", (fake.name(),))
conn.commit()


# Створення випадкового порядку лекторів та предметів
random_lectors = list(range(1, quantity_lector + 1))
random.shuffle(random_lectors)
random_subjects = list(range(1, sub + 1))
random.shuffle(random_subjects)

# Створення предметів для кожного викладача
for lector_id in random_lectors:
    subject_id = random_subjects.pop(0)  # Вибираємо перший предмет із перемішаного списку
    subject_name = fake.job()
    cursor.execute("INSERT INTO Subjects (name, lector_id) VALUES (?, ?)", (subject_name, lector_id))
conn.commit()


for group_id in range(1, group+1): # Створення студентів груп
    for _ in range(student):
        name = fake.name()
        cursor.execute("INSERT INTO Students (name, group_id) VALUES (?, ?)", (name, group_id))
conn.commit()

# Створення оцінок для студентів
start_date = datetime.date(2023, 9, 1)  # Початкова дата
students_ids = list(range(1, student*group+1))  #Створення оцінок для студентів
subjects_ids = list(range(1, sub+1))   
for student_id in range(1, student * group + 1):
    # Випадкова кількість оцінок для кожного студента (від 5 до 20)
    num_grades = random.randint(5, 20)
    for _ in range(num_grades):
        subject_id = random.randint(1, sub)  # Випадковий предмет
        grade = random.randint(min_grade, max_grade)  # Випадкова оцінка
        date_received = fake.date_between(start_date=start_date, end_date='today')  # Випадкова дата
        cursor.execute("INSERT INTO Grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)",
                       (student_id, subject_id, grade, date_received))

conn.commit()





def export_to_csv(table_name): # Експорт таблиць до CSV
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
