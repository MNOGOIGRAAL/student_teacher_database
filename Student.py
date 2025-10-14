class Student:
    id_student = 0

    def __init__(self,
                 first_name,
                 last_name,
                 phone,
                 ticket_number,
                 faculty,
                 speciality,
                 group,
                 budget=True,
                 patronymic=None,
                 set_of_lessons=None):
        self.__id = Student.autoincrement()
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone = phone
        self.ticket_number = ticket_number
        self.budget = budget
        self.faculty = faculty
        self.speciality = speciality
        self.group = group
        self.set_of_lessons = set_of_lessons

    @classmethod
    def autoincrement(cls):
        cls.id_student += 1
        return cls.id_student

    def get_info(self):

        def selection_set_of_lessons():
            lessons_list = []

            for subject, (teacher, grade) in self.set_of_lessons.items():
                # print(self.set_of_lessons.items())
                lesson_string = (f"Предмет: {subject.name}, "
                                f"Преподаватель: {teacher.fist_name}, "
                                f"Средняя оценка: {grade}")
                lessons_list.append(lesson_string)
            return lessons_list

        return (f"ID: {self.id_student}\n"
                f"Имя: {self.first_name}\n"
                f"Фамилия: {self.last_name}\n"
                f"Отчество: {self.patronymic}\n"
                f"Телефон: {self.phone}\n"
                f"Номер студенческого билета: {self.ticket_number}\n"
                f"Бюждет: {self.budget}\n"
                f"Факультет: {self.faculty.name}\n"
                f"Специальность: {self.speciality.name}\n"
                f"Группа: {self.group.name}\n"
                f"Набор предметов: {selection_set_of_lessons()}")



