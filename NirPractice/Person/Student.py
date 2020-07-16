from NirPractice.Person import person1 as student1


class Student():
    def __init__(self, person, graduationyear):
        self.person = student1
        self.graduationyear = graduationyear
    def speak(self):
        student1.speak()
        m = "I am a {} year graduate from Vandegrift Highschool"
        print(m.format(self.graduationyear))


nir = Student(student1, 2021)

nir.speak()


