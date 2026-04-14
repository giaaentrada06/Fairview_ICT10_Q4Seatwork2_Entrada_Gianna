class Classmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject

    def introduce(self):
        return f"Hi I'm {self.name} from {self.section} My favorite subject is {self.subject}"


# sample data
c1 = Classmate("Kristine", "Amethyst", "Math")
c2 = Classmate("Jean", "Amethyst", "Science")

classmates = [c1, c2]

for c in classmates:
    print(c.introduce())