class Speciality:
    id_speciality = 0

    @classmethod
    def autoincrement(cls):
        cls.id_speciality += 1
        return cls.id_speciality

    def __init__(self, name):
        self.__id = Speciality.autoincrement()
        self.name = name

    def get_id(self):
        return self.__id


