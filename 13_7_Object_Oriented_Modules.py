from Student import Student

Yakubi = Student(name="Yakubi", surname="Ronaldo", birthday=2011)
Yakubi.add_score(100)
Yakubi.add_score(94)
Yakubi.add_score(100)
print(Yakubi.full_name())
print(Yakubi.birthday)
print(Yakubi.score)
print(Yakubi.score_average())

Leo = Student("Omer", "Messi", 2011)
Leo.add_score(100)
Leo.add_score(94)
Leo.add_score(99)
print(Leo.full_name())
print(Leo.birthday)
print(Leo.score)
print(Leo.score_average())

Mesut = Student("Mesut", "Ozil", "2018")
print(Mesut.score_average())
print(Mesut.full_name())