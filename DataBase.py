from Student import Student
from Teacher import Teacher
from AcademicSubject import AcademicSubject
from Group import Group
from Speciality import Speciality
from Faculty import Faculty
from Department import Department

class DataBase:
    def __init__(self):
        self.data = []

    def add_data(self, object):
        self.data.append(object)

    def remove(self, object):
        if object in self.data:
            self.data.remove(object)

    def upgrade(self, object, attr, new_value):
        try:
            if object in self.data:
                index_object = self.data.index(object)
                setattr(self.data[index_object], attr, new_value)
        except ValueError:
            print("Этот объект отсутствует в базе данных")

    def get_all(self):
        all_last_name = []
        for i in self.data:
            all_last_name.append(i.last_name)
        return all_last_name

    def get_by_param(self, attr, value):
        result = []
        for obj in self.data:
            pass

class StudentTable(DataBase):
    def creat_student(self,
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
        student = Student(first_name,
                          last_name,
                          phone,
                          ticket_number,
                          faculty,
                          speciality,
                          group,
                          budget,
                          patronymic,
                          set_of_lessons)
        return student

    # def get_all_students_param(self, param):
    #     if

class TeacherTable(DataBase):
    def creat_teacher(self,
                      fist_name,
                      last_name,
                      phone,
                      academic_degree,
                      department,
                      patronymic=None):
        teacher = Teacher(fist_name,
                          last_name,
                          phone,
                          academic_degree,
                          department,
                          patronymic)
        return teacher

class AcademicSubjectTable(DataBase):
    def creat_academic_subject(self, name):
        items = AcademicSubject(name)
        return items

class GroupTable(DataBase):
    def creat_group(self, name):
        group = Group(name)
        return group

class SpecialitiTable(DataBase):
    def creat_speciality(self, name):
        speciality = Speciality(name)
        return speciality

class FacultyTable(DataBase):
    def creat_faculty(self, name):
        faculty = Faculty(name)
        return faculty

class DepartmentTable(DataBase):
    def creat_department(self, name):
        department = Department(name)
        return department
