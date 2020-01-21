#!/usr/bin/python3 

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--action", "-a", help='what action animal should do')
ap.add_argument("--quantity", "-q", help='how much times they should do actions')
# этих двух параметров не было
ap.add_argument("--type", "-t", help='Animal type : cat, dog, cow')
ap.add_argument("--name", "-n", default = "Friskey", help='name, optional')


class Animal:
    # ВАШ КОД ЗДЕСЬ
    def __init__(self, name):
        self.name = name
    def voice(self):
        print(f"{self.type} say: {self.sound}")
    def say_name(self):
        print(f"I am {self.type}, my name is {self.name.capitalize()}")
    def feed(self, q : int):
        q = int(q)
        if (q ==0):
            return "I'm still want to eat"
        elif (q==1):
            return "Not so much food"
        elif (q==2):
            return "I am feeling good"
        elif (q>2):
            return "Is today a holiday?"
        else: #  Ну, а вдруг?
            return "Negative food dont exist" 


class Dog(Animal):
    # ВАШ КОД ЗДЕСЬ
    sound = "woof!"
    def __init__(self, name):
        self.type = "dog";
        super(Dog,self).__init__(name)
    pass

    def play_with_ball(self):
        print(f"{self.name.capitalize()} run to a ball and become happy")


class Cat(Animal):
    # ВАШ КОД ЗДЕСЬ
    sound = "meeooow"
    def __init__(self, name):
        self.type = "cat";
        super(Cat,self).__init__(name)
    pass

    def nightrunner(self):
        print(f"Everybody wake up, {self.name} is happy")


class Cow(Animal):
    # ВАШ КОД ЗДЕСЬ
    sound = "moooo"
    def __init__(self, name):
        self.type = "cow";
        super(Cow,self).__init__(name)
    pass

    def walking_with_bell(self):
        print(f"Cow walking on the grass")


def main():
    # ВАШ КОД ЗДЕСЬ
    animals = {"Dog": Dog, "Cat":Cat, "Cow":Cow}
    try:
        desiredAnimal = animals[str.capitalize(args.type)];
        animal = desiredAnimal(args.name)
        animal.say_name()
        print(f"{animal.feed(args.quantity)}")
        methodToCall = getattr(animal, args.action)
        methodToCall()
    except KeyError:
        print(f"{args.type} is not supported animal")
    except AttributeError:
        print(f"{args.type} can't {args.action}!")
    except TypeError as e:
        print(f"Some of parametrs might be are missing : {e}")
    pass


if __name__ == '__main__':
    args = ap.parse_args()
    main()
