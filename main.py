from time import sleep


class Animals:
    def __init__(self, name, kind, gender, weight):
        self.name = name
        self.kind = kind
        self.gender = gender
        self.weight = weight

    def move(self, steps, place):
        print(f"{self.name} made {steps} steps in the {place}")

    def eat(self, food):
        print(f"{self.name} ate {food}")

    def sleeping(self, t):
        print(f"{self.name} fall asleep for {t} second(s)")
        sleep(t)


class Mammals(Animals):
    def __init__(self, name, kind, gender, weight, predator="no"):
        super().__init__(name, kind, gender, weight)
        self.predator = predator

    def feedmilk(self, mammal):
        if isinstance(mammal, Mammals):
            if self.gender.lower() == "female":
                print(f"{self.name} is feeding {mammal.name}")
            else:
                print("No milk!")

    def hunt(self):
        if self.predator == "yes":
            print(f"{self.name} is hunting...")


class Human(Mammals):
    def __init__(self, name, kind, gender, weight, predator, eyes_color, hair_color):
        super().__init__(name, kind, gender, weight, predator)
        self.eyes_color = eyes_color
        self.hair_color = hair_color

    def think(self):
        print(f"{self.name} is thinking...")


class Dog(Mammals):
    def __init__(self, name, kind, gender, weight, predator, owner):
        super().__init__(name, kind, gender, weight, predator)
        self.owner = owner

    def say(self):
        print("woof!")

    def play(self):
        print(f"{self.name} is playing with its owner {self.owner}")


class Cat(Mammals):
    def __init__(self, name, kind, gender, weight, predator, favorite_game):
        super().__init__(name, kind, gender, weight, predator)
        self.favorite_game = favorite_game

    def say(self):
        print("Nyanyame nyanyajyuunyanya do no nyarabi de "
              "nyaku nyaku inyanyaku nyanyahan nyanyadai nyan nyaku")

    def _destroy_the_kitchen(self, hours):
        if hours == "3 am":
            print("DESTROY TIME, NYYYAAAAAAA-HA-HAAAAA!")
        else:
            print("It's not time yet!")


class Student(Human):
    def __init__(self, name, kind, gender, weight, predator, eyes_color, hair_color, hworks):
        super().__init__(name, kind, gender, weight, predator, eyes_color, hair_color)
        self.hworks = hworks

    def study(self, subject):
        print(f"{self.name} is studying {subject}")

    def __eq__(self, student):
        return self.hworks == student.hworks

    def __lt__(self, student):
        return self.hworks < student.hworks

    def __gt__(self, student):
        return self.hworks > student.hworks


leo = Animals('Leonardo', 'Turtle', 'Male', 80)
leo.move(100, "City")
leo.eat('Pizza')
leo.sleeping(2)

print()
medoed = Mammals('Vitya', 'Honey badger', 'Male', 9, 'yes')
medoed.eat('honey')
medoed.hunt()

print()
medoedka = Mammals('Valya', 'Honey badger', 'Female', 13, 'yes')
medoedka.eat('honey')
medoedka.hunt()
medoedka.feedmilk(medoed)

print()
human = Human('Garik', 'Human', 'Male', 70, 'no', 'Blue', 'Red')
human.think()
human.sleeping(2)

print()
cat = Cat('Tsubasa', 'Cat', 'Female', 18, 'Black-white', 'revenge')
cat.say()

print()
dog = Dog('Barbos', 'Dog', 'Male', 2, 'yes', 'Stas')
dog.say()
dog.play()

print()
vasya = Student('Vasya', 'Human', 'Male', 55, 'no', 'Brown', 'Brown', 25)
tolya = Student('Tolya', 'Human', 'Male', 56, 'no', 'Blue', 'Grey', 24)

print(vasya == tolya)
print(vasya > tolya)
print(vasya < tolya)
