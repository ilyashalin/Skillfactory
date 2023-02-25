from cat import Cat

cat_1 = Cat("Baron", "boy", 2)
cat_2 = Cat("Sam", "boy", 2)

print(cat_1.get_name(), cat_1.get_gender(), cat_1.get_age())
print(cat_2.get_name(), cat_2.get_gender(), cat_2.get_age())

class Dog(Cat):
    def get_pet(self):
        return f'{self.get_name()} {self.get_age()}'

dog_1=Dog("Felix","boy",2)
print(dog_1.get_pet())