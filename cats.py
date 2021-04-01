from main import Cat

cat1 = Cat("Vera","g",5)
cat2 = Cat("Sam","b",2)
cat3 = Cat("Sally","g",3)
cat4 = Cat("Ben","b",6)


cats=[cat1, cat2, cat3, cat4]

for cat in cats:
    cat.show_cat()