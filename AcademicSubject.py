class AcademicSubject:
    id_academic_subject = 0

    @classmethod
    def autoincrement(cls):
        cls.id_academic_subject += 1
        return cls.id_academic_subject

    def __init__(self, name):
        self.__id = AcademicSubject.autoincrement()
        self.name = name

    def get_id(self):
        return self.__id


