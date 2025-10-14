from DataBase import (StudentTable,
                      TeacherTable,
                      AcademicSubjectTable,
                      DepartmentTable, FacultyTable, GroupTable,
                      SpecialitiTable)

#Создание таблиц
student_table = StudentTable()
teacher_table = TeacherTable()
academic_subject_table = AcademicSubjectTable()
department_table = DepartmentTable()
faculty_table = FacultyTable()
group_table = GroupTable()
speciality_table = SpecialitiTable()

#Создание предметов
academic_subject_informat = academic_subject_table.creat_academic_subject("Информатика")
academic_subject_math = academic_subject_table.creat_academic_subject("Математика")
academic_subject_physics = academic_subject_table.creat_academic_subject("Физика")
academic_subject_chemistry = academic_subject_table.creat_academic_subject("Химия")

#Добавление ранее созданных предметов в таблицу
academic_subject_table.add_data(academic_subject_informat)
academic_subject_table.add_data(academic_subject_math)
academic_subject_table.add_data(academic_subject_physics)
academic_subject_table.add_data(academic_subject_chemistry)

#Создание кафедры
department_inf_tehnolodgi = department_table.creat_department("Кафедра Информационных технологий")
department_artistic_art = department_table.creat_department("Кафедра Художественного искуства")

#Добавление ранее созданной кафедры в таблицу
department_table.add_data(department_inf_tehnolodgi)
department_table.add_data(department_artistic_art)

#Создание факультета
faculty_programming = faculty_table.creat_faculty("Программирование")
faculty_design = faculty_table.creat_faculty("Дизайн")

#Добавление ранее созданного факультета в таблицу
faculty_table.add_data(faculty_programming)
faculty_table.add_data(faculty_design)

#Создание групп
group_100 = group_table.creat_group("100")
group_200 = group_table.creat_group("200")
group_300 = group_table.creat_group("300")
group_400 = group_table.creat_group("400")

#Добавление ранее созданных групп в таблицу
group_table.add_data(group_100)
group_table.add_data(group_200)
group_table.add_data(group_300)
group_table.add_data(group_400)

#Создание специальностей
speciality_programm_backend = speciality_table.creat_speciality("Разработка бэкенда")
speciality_programm_frontend = speciality_table.creat_speciality("Разработка фронтенд")

#Добавление специальностей в таблицу
speciality_website_designer = speciality_table.creat_speciality("Дизайн сайта")
speciality_game_designer = speciality_table.creat_speciality("Дизайн игр")

#Создание учителей
teacher_ivan = teacher_table.creat_teacher("Иван",
                                           "Волков",
                                           "8(987)475-56-00",
                                           "Кандидат наук",
                                           department_inf_tehnolodgi)

teacher_сatherine = teacher_table.creat_teacher(fist_name="Екатерина",
                                                last_name="Мизулина",
                                                phone="8(900)777-88-99",
                                                academic_degree="Доктор наук",
                                                department=department_inf_tehnolodgi)

teacher_igor = teacher_table.creat_teacher(fist_name="Игорь",
                                           last_name="Ерохин",
                                           patronymic="Викторович",
                                           phone="8(900)254-88-56",
                                           academic_degree="Доктор наук",
                                           department=department_artistic_art)

teacher_vasily = teacher_table.creat_teacher(fist_name="Василий",
                                             last_name="Жуков",
                                             patronymic="Иванович",
                                             phone="8(937)876-52-88",
                                             academic_degree="Дктор наук",
                                             department=department_artistic_art)

#Добавление преподавателей в таблицу
teacher_table.add_data(teacher_ivan)
teacher_table.add_data(teacher_igor)
teacher_table.add_data(teacher_сatherine)
teacher_table.add_data(teacher_vasily)

set_of_items_student_maria = {academic_subject_informat: (teacher_ivan, 4.5),
                              academic_subject_math: (teacher_ivan, 4.0),
                              academic_subject_physics: (teacher_сatherine, 4.5)}
student_maria = student_table.creat_student(first_name="Мария",
                                            last_name="Петрова",
                                            patronymic="Александровна",
                                            phone="8(900)567-78-00",
                                            ticket_number="01",
                                            faculty=faculty_design,
                                            speciality=speciality_game_designer,
                                            group=group_100,
                                            budget=True,
                                            set_of_lessons=set_of_items_student_maria)

#Создание студентов с набором предметов, преподавателем и средней оценкой
set_of_items_student_gosha = {academic_subject_informat: (teacher_ivan, 4.5),
                              academic_subject_math: (teacher_ivan, 4.0),
                              academic_subject_physics: (teacher_igor, 4.5)}
student_gosha = student_table.creat_student(first_name="Георгий",
                                            last_name="Макаров",
                                            patronymic="Алексеевич",
                                            phone="8(900)726-00-02",
                                            ticket_number="02",
                                            faculty=faculty_design,
                                            speciality=speciality_website_designer,
                                            group=group_200,
                                            budget=False,
                                            set_of_lessons=set_of_items_student_gosha)

set_of_items_student_yana = {academic_subject_informat: (teacher_ivan, 4.5),
                              academic_subject_math: (teacher_vasily, 4.0),
                              academic_subject_physics: (teacher_сatherine, 4.5)}
student_yana = student_table.creat_student(first_name="Яна",
                                            last_name="Корнеева",
                                            patronymic="Викторовна",
                                            phone="8(900)876-22-99",
                                            ticket_number="03",
                                            faculty=faculty_programming,
                                            speciality=speciality_programm_frontend,
                                            group=group_300,
                                            budget=True,
                                            set_of_lessons=set_of_items_student_yana)

set_of_items_student_victor = {academic_subject_informat: (teacher_vasily, 4.5),
                              academic_subject_math: (teacher_vasily, 4.0),
                              academic_subject_physics: (teacher_ivan, 4.0)}
student_victor = student_table.creat_student(first_name="Виктор",
                                            last_name="Мухин",
                                            patronymic="Викторович",
                                            phone="8(900)529-12-88",
                                            ticket_number="04",
                                            faculty=faculty_programming,
                                            speciality=speciality_programm_backend,
                                            group=group_400,
                                            budget=True,
                                            set_of_lessons=set_of_items_student_yana)

set_of_items_student_kolya = {academic_subject_informat: (teacher_vasily, 5.0),
                              academic_subject_math: (teacher_vasily, 4.0),
                              academic_subject_chemistry: (teacher_igor, 4.0)}
student_kolya = student_table.creat_student(first_name="Николай",
                                            last_name="Марков",
                                            patronymic="Анатольевич",
                                            phone="8(900)928-56-00",
                                            ticket_number="05",
                                            faculty=faculty_programming,
                                            speciality=speciality_programm_backend,
                                            group=group_200,
                                            budget=False,
                                            set_of_lessons=set_of_items_student_kolya)

#Добавление студентов в таблицу
student_table.add_data(student_maria)
student_table.add_data(student_yana)
student_table.add_data(student_victor)
student_table.add_data(student_gosha)
student_table.add_data(student_kolya)

# print(student_kolya.first_name)
# print(student_table.data)
# print(student_kolya)
# student_table.remove(student_kolya)
# print(student_table.data)

# print(teacher_table.get_all())

# student_table.upgrade(student_kolya, "first_name", "New_Николай")
# print(student_kolya.first_name)

print(student_table.get_by_param("group_table", "200"))