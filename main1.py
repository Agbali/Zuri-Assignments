class Student:

    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self):
        return self.name

    def change_age(self):
        return self.age

    def add_track(self):
        return self.tracks

    def get_score(self):
        return self.score     

Bob = Student("Bob", 26, ["FE","BE"], 20.90)

print(Bob.change_name())
print(Bob.change_age())
print(Bob.add_track())
print(Bob.get_score())

Peter = Student("Peter", 34, ["UI/UX"], 39.79)

print(Peter.change_name())
print(Peter.change_age())
print(Peter.add_track())
print(Peter.get_score())

print(Student.change_name(Peter))
print(Student.change_age(Peter))
print(Student.add_track(Peter))
print(Student.get_score(Peter))

# # Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()


