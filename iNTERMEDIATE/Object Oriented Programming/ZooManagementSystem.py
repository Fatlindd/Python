class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def move(self):
        print(f"{self.name} moves around.")

    def __str__(self):
        return f"Animal ('{self.name}', '{self.species})"


class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} the {self.species} growls.")

    def __str__(self):
        return f"Mammal('{self.name}, '{self.species}', '{self.fur_color}'"


class Bird(Animal):
    def __init__(self, name, species, wing_span):
        super().__init__(name, species)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} the {self.species} chirps.")

    def move(self):
        print(f"{self.name} flies around.")

    def __str__(self):
        return f"Bird('{self.name}', '{self.species}', '{self.wing_span}')"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} the {animal.species} to the zoo.")

    def list_animals(self):
        print("Zoo animals:")
        for animal in self.animals:
            print(animal)


def main():
    # Create zoo
    zoo = Zoo()

    # Create animals
    lion = Mammal('Leo', 'Lion', 'Golden')
    eagle = Bird('Eddy', 'Eagle', '2 meters')

    # add animal to the zoo
    zoo.add_animal(lion)
    zoo.add_animal(eagle)

    # Perform operations on animals
    lion.make_sound()
    lion.move()
    eagle.make_sound()
    eagle.move()

    # List all animals  in the zoo
    zoo.list_animals()


if __name__ == '__main__':
    main()




