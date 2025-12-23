# PEP_8.
name = input("What's your name: ")

if name == "" :
        print("Is your name empty? " + str(name))
        name = input("What's your real name: ")

print("your name has " + str(len(name)) + " letters")
print("Hello " + name)
py_3 = " python"
version = " 1.0"

print("This " + "is" + py_3 + version + " ha" * int(len(name)) + "!" * int(len(name)))

num_one = int(input("input num1: "))
print(type (num_one))
num_two = int(input("input num2: "))
print(type(num_two))

print(str(num_one) + " & " + str(num_two))

print(min(num_one , num_two))

print(max(num_one , num_two))

print(bool(num_one))

print(bool(num_two))

print("x plus + y evaluates to...")
print(num_one + num_two)

print("x minus - y evaluates to...")
print(num_one - num_two)

print("x times * y evaluates to...")
print(num_one * num_two)

print("x to the power of ** y evaluates to...")
print(num_one ** num_two)

print("x divided by / y evaluates to...")
print(round(num_one / num_two))
print(abs(num_one / num_two))

print("x floor divided by // rounds of to nearest whole y evaluates to...")
print(num_one // num_two)

print("x modulo % gives remainder y evaluates to...")
print(num_one % num_two)
