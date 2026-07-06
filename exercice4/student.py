class Student:
    def __init__(self, name, notes):
        self.name = name
        self.notes = notes

    def average(self):
        return sum(self.notes) / len(self.notes)

s1 = Student("Alice", [85, 90, 78, 92, 88])
print(s1.name)
print(s1.average())