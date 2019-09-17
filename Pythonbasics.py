# lucky_numbers = [4, 8, "fifteen", 16, 23, 42.0]
# lucky_numbers[0] = 90
# print(lucky_numbers[0])
# print(lucky_numbers[1])
# print(lucky_numbers[-1])
# print(lucky_numbers[2:])
# print(lucky_numbers[2:4])
# print(len(lucky_numbers))

# 2 Dimension list #
# numberGrid = [[3,6],[5,7]]
# numberGrid[0][1] = 99
# print(numberGrid[0][0])
# print(numberGrid[0][1])
# print(numberGrid[1][0])
# print(numberGrid[1][1])

# List Function #
# name_list = []
# name_list.append("Ajay")
# name_list.append("Naresh")
# name_list.insert(1,"Selvi")
# name_list.append("Sridhar")
# print(name_list)
# print(name_list.index("Naresh"))
# print(name_list.count("Naresh"))
# name_list.sort()
# print(name_list)


# Tuples #
# lucky_numbers = (4, 8, "fifteen", 16, 23, 42.0)
#       indexes  0  1       2      3   4   5
# lucky_numbers[0] = 90
# print(lucky_numbers[0])
# print(lucky_numbers[1])
# print(lucky_numbers[-1])
# print(lucky_numbers[2:])
# print(lucky_numbers[2:4])
# print(len(lucky_numbers))


# Functions #
# def add_numbers (num1, num2=77):
#     return num1 + num2
# a = int(input("Enter the first value: "))
# b =int(input("Enter the second value: "))
# sum = add_numbers(a,b)
# print(sum)



# def add_numbers(num1, num2=99):
#     return num1 + num2
# sum = add_numbers(4, 3)
# print(sum)

# Control statement : IF #
# is_student = False
# is_smart = True
#
# if is_student and is_smart:
# 	print("You are a student")
# elif is_student and not(is_smart):
# 	print("You are not a smart student")
# else:
# 	print("You are not a student and not smart")


# >, <, >=, <=, !=, ==
# if 4 != 4:
#     print("number comparison was true")
# else:
#     print("number comparison was false")
#
#
# if "cat" == "cat":
#    print("string comparison was true")
# else:
#     print("string comparison was false")


# Dictionaries #
# test_grades = {
#     "Andy" : "B+",
#     "Stanley" : "C",
#     "Ryan" : "A",
#     3 : 95.2
# }
# print( test_grades["Andy"] )
# print( test_grades.get("Ryan", "No Student Found") )
# print( test_grades[3] )

# new_dic = { "Rajesh" : "A", "Vignesh" : "B", "Rajagopal" : "C"}
# print(new_dic["Rajesh"])
# print(new_dic["Rajagopal"])
# print(new_dic.get("B","No Key found"))

#While Loops#
# index = 1
# while index <= 5:
# 	print("-")
# 	index += 1

#ForLoop#
# for index in range(5):
#     print(index)
#
# lucky_nums = [4, 8, 15, 16, 23, 42]
# for lucky_num in lucky_nums:
#     print(lucky_num)
#
# for letter in "Giraffe":
#     print(letter)
#
# for index in range(100):
#     print(index)

# Exceptional Catching#
# try:
#     answer = 10 / int(input("Enter Number: "))
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as error:
#     print("Invalid input")
# except:
#     print("Invalid Input")

# Class #
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def read_book(self):
#          print("Reading", self.title, "by", self.author)
#
# book1 = Book("Harry Potter", "JK Rowling");
# # book1.title = "Half-Blood Prince"
#
# print(book1.title)
# print(book1.author)
# book1.read_book()

# class Alien:
#     def __init__(self,place,year,govtname):
#         self.place = place
#         self.year = year
#         self.govtname = govtname
#
#     def algovt(self):
#         print("The govt which have links with alien civilization is", self.govtname, "which was found during the year", self.year, "at",self.place)
# alien1 = Alien("Rosewell","1947","US");
#
# print(alien1.place)
# print(alien1.govtname)
# print(alien1.year)
# alien1.algovt()


# class Car(object):
#   """
#     blueprint for car
#   """
#
#   def __init__(self, model, color, company, speed_limit):
#     self.color = color
#     self.company = company
#     self.speed_limit = speed_limit
#     self.model = model
#
#   def start(self):
#     print("started")
#
#   def stop(self):
#     print("stopped")
#
#   def accelarate(self):
#     print("accelarating...")
#     "accelarator functionality here"
#
#   def change_gear(self, gear_type):
#     print("gear changed")
#     " gear related functionality here"
#
# maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
# audi = Car("A6", "red", "audi", 80)
#
# print(maruthi_suzuki.model)
# maruthi_suzuki.start()
# maruthi_suzuki.accelarate()
# maruthi_suzuki.change_gear("Manual")
# maruthi_suzuki.stop()

# class Book:
#     def __init__(self, title, author):
#         self.title = title;
#         self.author = author
#
#     @property
#     def title(self):
#         print("getting title")
#         return self._title
#
#     @title.setter
#     def title(self, value):
#         print("setting title")
#         self._title = value
#
#     @title.deleter
#     def title(self):
#         del self._title
#
#
#     def read_book(self):
#          print("Reading", self.title, "by", self.author)
#
# book1 = Book("Harry Potter", "JK Rowling");
# # book1.title = "Half-Blood Prince"
#
# print(book1.title)
# book1.read_book()


# Python program showing the use of
# @property
# class Technology:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     # using property decorator
#     # a getter function
#
#     @property
#     def get_tech(self):
#         print("Getter method executed")
#         return self.name
#
#     # @get_tech.setter
#     def set_tech(self, name):
#         self.name = name
#         print("Setter code executed")
#         print("The name is", name)
#
#     # @set_tech.deleter
#     # def delete(self):
#     #     del self.set_tech
#     #     print("Delete function executed")
#
#
# name1 = Technology("Ajay","28")
#
# name1.set_tech("Naresh")

# Inheritance Functionality#
# from Inheritance import inheritance
#
# myinheritance = inheritance("Naresh","27","402187","Systems")
# myinheritance.getage()

# inheritance 2
# from Inheritance import inheritance
# myinherit = inheritance("Ajay","28","402187","Systems")
# Ageof = myinherit.age
# print(Ageof)

#Exponential Function

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result *= base_num
#     return result
#
# result = raise_to_power(10,2)
# print("The result is: ", result)
#

# def raise_to_thepower (base_num,pow_num):
#     result = 1
#     for index in range(pow_num)
#         result *= base_num
#     return result

# def least_difference(a, b, c):
#     diff1 = abs(a - b)
#     diff2 = abs(b - c)
#     diff3 = abs(a - c)
#     return min(diff1, diff2, diff3)

# print(
#     least_difference(1, 10, 100),
#     least_difference(1, 10, 10),
#     least_difference(5, 6, 7),
#     # Python allows trailing commas in argument lists. How nice is that?
# )

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n', # '\n' is the newline character - it starts a new line
)