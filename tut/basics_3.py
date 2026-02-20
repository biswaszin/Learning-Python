# this is tuple

fruits = ("apple", "orange", "banana", "coconut")

# immutable and fast asf

for fruit in fruits:
    print(fruit)

# immutable essentially means, cannot be changed so no append / delete / pop

print("\n\n\n")

# now sets, mutable (can add / remove) but they are unordered

cars = {"fortuner", "omni", "brezza"}
for car in cars:
    print(car)

#if i print cars again and again, it'll be random and unordered

cars.add("lambo") # cannot append as we'd need the last index, 
                  # but since set is unordered, we cannot
for car in cars: 
    print(car)

