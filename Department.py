class Department:
    id_departament = 0

    @classmethod
    def autoincrement(cls):
        cls.id_departament += 1
        return cls.id_departament

    def __init__(self, name):
        self.__id = Department.autoincrement()
        self.name = name

    def get_id(self):
        return self.__id



