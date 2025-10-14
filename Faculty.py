class Faculty:
    id_faculty = 0

    @classmethod
    def autoincrement(cls):
        cls.id_faculty += 1
        return cls.id_faculty

    def __init__(self, name):
        self.__id = Faculty.autoincrement()
        self.name = name

    def get_id(self):
        return self.__id


