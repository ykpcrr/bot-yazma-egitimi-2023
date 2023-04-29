
class Student:
    def __init__(self, name, surname, birthday):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.score = []

    def add_score(self, score):
        self.score.append(score)

    def score_average(self):

        if not self.score:
            return "Please add a score first"

        average = sum(self.score) / len(self.score)

        return average

    def full_name(self):
        return f"{self.name} {self.surname}"

