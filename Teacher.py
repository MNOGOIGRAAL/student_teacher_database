class Teacher:
    id_teacher = 0

    def __init__(self,
                 fist_name,
                 last_name,
                 phone,
                 academic_degree,
                 department,
                 patronymic=None):
        self.__id = Teacher.autoincrement()
        self.fist_name = fist_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone = phone
        self.academic_degree = academic_degree
        self.departament = department

    @classmethod
    def autoincrement(cls):
        cls.id_teacher += 1
        return cls.id_teacher
