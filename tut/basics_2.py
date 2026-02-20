for i in range(10,0, -1):
    print(i)
print("HAPPY NEW YEAR!")

fruits = ["apple", "banana", "litchi", "mango"]

for fruit in fruits:
    print(fruit)

# to add another fruit in fruits

fruits.append("Guava")

for fruit in fruits:
    print(fruit)

# to remove any fruit
fruits.remove("banana")

for fruit in fruits:
    print(fruit)

#to remove any fruit using indexing, use pop
#fruits.pop(0)

#to clear the list
fruits.clear()

