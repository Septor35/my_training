# Даны списки оценок и множество студентов
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество студентов в отсортированный список
students_list = sorted(students)

# Создаем пустой словарь для хранения результата
average_grades = {}

# Проходим по каждому студенту и его оценкам
for i in range(len(students_list)):
    student = students_list[i]  # Имя текущего студента
    student_grades = grades[i]  # Оценки этого студента

    # Считаем средний балл
    average_grade = sum(student_grades) / len(student_grades)

    # Добавляем в словарь: ключ - имя студента, значение - его средний балл
    average_grades[student] = average_grade
print(average_grades)