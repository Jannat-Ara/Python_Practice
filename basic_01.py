# first code
print("Hello World")

# type conversion
birth_year = input("Enter your birth year:")
age = 2021 - int(birth_year)
print(age)
# Exercise_01: Basic calculator
num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
sum = float(num1) + int(num2)
print(sum)
# another way
number1 = input("Enter the first number:")
number2 = input("Enter the second number:")
sum1 = float(number1)+float(number2)
print("", str(sum1))

# some methods
course = "Python for beginners"
  # print the line
print(course)
  # print in uppercase
print(course.upper())
  # print in lower case
print(course.lower())
  # find a word or letter
print(course.find('y')) #answer:1
print(course.find('for')) #answer:7
  # replace a word or letter with another
print(course.replace("for", '4'))


# in function(give answer in boolean)
print("Python" in course) #answer:true