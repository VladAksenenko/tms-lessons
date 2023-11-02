from datetime import date
class Person:
    DATA = str(date.today()).split('-')

    def __init__(self, full_name, age, gender: str):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        print(f"Person: {self.full_name} ({self.gender}), {self.age} years old")

    # def get_birth_year(self):
    #     return 2023 - self.age

    def get_birth_year(self):
        return int(self.DATA[0]) - self.age



p = Person("Vladislav", 26, 'M')
print(p.full_name)
print(p.age)
print(p.gender)
print(p.get_birth_year())