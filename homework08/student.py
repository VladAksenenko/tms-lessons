class Student:
    def __init__(self, full_name, average_mark):
        self.full_name = full_name
        self.average_mark = average_mark

    def get_scholarship(self):
        if self.average_mark < 6:
            return 60
        if 6 <= self.average_mark < 8:
            return 80
        else:
            return 100

    def is_excellent(self):
        return self.average_mark >= 9


vlad = Student('Vlad', 7)
print(vlad.get_scholarship())
print(vlad.is_excellent())