class Cat:
    def __init__(self, name, sex, age ):
        self.name = name
        self.sex = sex
        self.age = age

    def show_cat(self):
        if (self.sex == "b" or self.sex == "g") and isinstance(self.age, int):
            if self.sex == "g":
                print(f"{self.name} is a girl and she is {self.age} years old")
            if self.sex == "b":
                print(f"{self.name} is a boy and he is {self.age} years old")
        else:
            print("Incorrect data")





