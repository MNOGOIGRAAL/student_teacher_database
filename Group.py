class Group:
    id_group = 0

    @classmethod
    def autoincrement(cls):
        cls.id_group += 1
        return cls.id_group

    def __init__(self, name):
        self.__id = Group.autoincrement()
        self.name = name

    def get_id(self):
        return self.__id

