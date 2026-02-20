full_name = "Ankit Biswas"
age = 21
sgpa = 8.25
is_student = True

print(f"Hello! {full_name}")
print(f"What's your age? {age}")
print(f"What's your SGPA?! {sgpa}")
print(f"Are you a student? {is_student}") 

if is_student:
    print("You are a student")
else:
    print("You are not a student!")


# for type casting
# variable = datatype(variable)

var1 = 3.222
var1 = int(var1)

print(var1)

# Loops

for i in range(91, 101):
    print(i-90)