class Cow:
    def __init__(self, name, voicetext):
        self.name = name
        self.voicetext = voicetext

    def voice(self):
        print(f"{self.name}:{self.voicetext}")


cow = Cow('Milka', 'Muu muu')
cow.voice()


class Dog:
    def __init__(self, name, voicetext):
        self.name = name
        self.voicetext = voicetext

    def voice(self):
        print(f"{self.name}:{self.voicetext}")


dog = Dog('Chappie', 'Gaf Gaf')
dog.voice()


class Bear:
    def __init__(self, name, voicetext):
        self.name = name
        self.voicetext = voicetext

    def voice(self):
        print(f"{self.name}:{self.voicetext}")


bear = Bear('Misha228', 'Grrr grrr')
bear.voice()


class Cat:
    def __init__(self, name, voicetext):
        self.name = name
        self.voicetext = voicetext

    def voice(self):
        print(f"{self.name}:{self.voicetext}")


cat = Cat('Kisa', 'Mew mew')
cat.voice()
