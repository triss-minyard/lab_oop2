class Animal:
    def make_sound(self):
      pass
      

class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

class Cow(Animal):
    def make_sound(self):
        return "Муу!"

def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())


if __name__== "__main__":
    animals = [
        Dog(), 
        Cat(),  
        Cow()   
    ]
    
    animal_sounds(animals)        
