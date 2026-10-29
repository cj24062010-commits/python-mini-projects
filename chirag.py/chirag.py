# first_name="Tony"
# last_name= "Stark"
# age=53
# Height="1.85m"
# superhero_name =input("what is Tony superhero name?")
# print(type ("Tony is secretly a superhero and his supheroname is "+ superhero_name))

# age=input("enter your age: ")
# print(age,type(age))
# age=int(age)
# print(age+1)e

# print(1+2.5)
# name="Tony stark"
# print(name.upper())
# print(name)
# print (name.replace ("Tony stark","Ironman"))

# price_of_product1=int(input("enter the price 1:"))
# price_of_product2=int(input("enter the price 2:"))
# price_of_product3=int(input("enter the price 3:"))
# totalbillamount=price_of_product1 +price_of_product2+price_of_product3
# print(totalbillamount)
# averageprice=totalbillamount/3
# print(averageprice)


# superhero_name=input("enter the superhero name:")
# print(superhero_name) 
# name=input("enter your name:")
# print(name.find("ony"))

# name=input("enter your name:")
# print(name.replace("Tony stark","Ironman"))
# print("k" in name )

# print(5//3)
# intendation   
# age=22
# if age>=18:
#     print("i am an adult")
# elif age <=17:
#     print("i am not an adult")
#     # here the solution will be i am an adult as age is greater than 18

# marks=60
# if marks>80:
#     print("distinction")
# elif marks>=60:
#     print("grade B")    
# elif marks<60:
#     print("grade c")
# elif marks>90:
#     print("toppers")


# # num=range(10)   
# # print(num)
# # #1 to 5
# # num=range(1,6)
# # print(num)
# # # range(start=0,stop, step=1) 

# i =1
# while i<=5:
#         print(i) #infinite loops 
        
    
# number =1
# while number<=5:        
#         print("chirag:")
# number+=2 #finite loop

#logical operators
# statement_1=3>5
# statement_2=3>4
# print(statement_1 or statement_2)
                
# #for loops 
# #0-4

# #1 to 5 
# for i in range(1,5001):
#     print(i)



# multiple of 4
# for i in range(0, 51, 4):
#     if (i==16):
#         continue
#     print(i

#print odd number from 1 to 20

# for i in range (1,21,2):
#     print(i)

# #print the table 57
# for i in range (57,571,57):
#     print(i)

# print ("table of 57 is printed")
# for i in range(0, 51, 3):
#     if i == 15:
#         continue
#     print(i)
# print("multiples of 3 are printed")  # output will be multiples of 3 are printed but not 15 as we have used continue statement
    
# for i in range (0,51,3):
#     print(i)
#     if (i == 15):
#         continue

# print("multiples of 3 are printed") 
# # you meant this kind of codes?

# a = int(input("enter the value of a: "))
# b = int(input("enter the value of b: "))
# c = int(input("enter the value of c: "))

# if a == 0 and b == 0:
#     print("a & b both are zero")
# elif c%a==0 and c%b==0:
#     print("c is divisible by both a and b")
# else:
#     print("c is not divisible by both a and b")

# #Set :
# name={"chirag_jain",22,"weight:""58 kilograms","height:5.8 feet"}
# print(name)
# # {'height:5.8 feet', 'weight:58 kilograms', 'chirag_jain', 22}

# #Dictionary:
# student_details = {
#     "name": "chirag_jain",
#     'height':"5.8 feet",
#     'weight':"58 kilograms",
#     'age':22,
#     "university": "Jain University"
# }

# student_details["school"]="B.B.U.L JAIN VIDAYLAYA"
# print(student_details)

# familydetails={
#     "father name": "Arvind Kumar Jain",
#     "mother name": "Tanuja Devi Jain",
#     "Elder sister name": "Dhwani Jain",
#     "Younger sister name ": "Palak Jain",
#     "my name": "Chirag Jain",
#     "family members": 5

# }
# print(familydetails)

# 1. Defining the function
# def greet_user(name):
#     message = f"Hello, {name}!"
#     print(message)

# greet_user("Chirag")
# greet_user("Tony")
# greet_user("Steve")

# def add_names(name):
#     message = f"hello, my best friend is {name}!"
#     print(message)

# add_names("Alice")
# add_names("Bob")
# add_names("Charlie")

# from operator import add


# name="chirag_jain"
# age=22
# print("my name is  "+ name+" and my age is "+str(age))

# name="lionel messi"
# age=37
# print(f"{name} is the greatest footballer of all time and his age is {age}")
# 
# 
# def calculate_area(length, width):
#     area = length * width
#     return area 

# area=calculate_area(5, 10)
# print(f"The area of the rectangle is: {area}")

# def calculate_perimeter_of_rectangle(length, width):
#     perimeter = 2 * (length + width)
#     return perimeter

# length = 5
# width = 10
# perimeter = calculate_perimeter_of_rectangle(length, width)
# print(f"The perimeter of the rectangle is: {perimeter}")


# def calculate_perimeter_of_rectangle(length, width):
#     return 2 * (length + width)

# length = 5
# width = 10

# # Call the function right inside the curly braces {}
# print(f"The perimeter of the rectangle is: {calculate_perimeter_of_rectangle(length, width)}")

# def calc_sum(a,b): # parameter 1 & parameter 2
#     sum=a+b
#     print(sum)
#     return sum

# calc_sum(444,555)

# calc_sum(100,300)
# calc_sum(10000,6000)
# total = addition_of_two_numbers(10000, 6000)
# if total > 15000:
#     tax = total * 0.1
#     print("Final total with tax:", total + tax)


# def calculate_area_of_rectangle(length, width):
#     return length * width  # return value

# area_of_a_rectangle = calculate_area_of_rectangle(65, 75)
# print(area_of_a_rectangle)

# def calculate_the_perimeter_of_a_rectangle(length, breadth):
#     perimeter_of_a_rectangle = 2 * (length + breadth)  # return value or solution
#     return perimeter_of_a_rectangle

# perimeter_of_a_rectangle = calculate_the_perimeter_of_a_rectangle(5.5, 7.2)
# print(perimeter_of_a_rectangle)

# def calculate_the_perimeter_of_a_rectangle(length ,breadth):
#     return 2 * (length + breadth)

# print(calculate_the_perimeter_of_a_rectangle(5.5,8.0))
# print(calculate_the_perimeter_of_a_rectangle(10.0,6.5))
# print(calculate_the_perimeter_of_a_rectangle(11.7,16.5))
#VS CODE 
# #average of three numbers 
# def calculate_the_average_of_threenumbers(num1,num2,num3):
#     return (num1 + num2 + num3) / 3
# average = calculate_the_average_of_threenumbers(100, 55, 666)
# print(average)

# # YOUR CODE
# def calculate_the_average_of_threenumbers(num1,num2,num3):
#     return(num1+num2+num3/3)
# average=calculate_the_average_of_threenumbers

# print(average)

 
# print("chirag", end=" ")
# print("jain")
# print(len.__name__)

# def calculate_the_product_of(a,b=7):
#     print(a*b)

# calculate_the_product_of(1)
# calculate_the_product_of(6)

# total = calculate_the_product_of(1) + 5  # This will give an error!

# def multiply(a,b):
#     return a*b
# answer=multiply(3,4)
# final_total_answer=answer+6
# print(final_total_answer)

# answer=multiply(10,20)


# def multiply (c,d):
#     return c *d 

# answer1=multiply(10,60)
# total1=answer1 + 61
# print(total1)


# answer2=multiply(40,80)
# total2=answer1 + 6
# print(total2)



# def calc_prod(b, a=7):
#     print(b * a)
#     return b * a

# calc_prod(8)

# name=["parameters"]
# print(len (name))

# def printlen(cities):
#     print(len(cities))  # this is the code/ line in which the length function is been used 
#     return(len(cities))
# cities= "mumbai","bengaluru","goa","dubai","varkalasivagiri"
# printlen(cities)


# def printlen(numbers):
#     print(len(numbers))# this is the code/ line in which the length function is been used 
#     return(len(numbers))

# numbers=5,6,7,8,9
# print(len(numbers))


# Write a function to print the elements of a list in a single
# line (list is the parameter).

# def print_items(items):
#     for item in items:
#         print(item, end=" ")


# player_name = ["lionel", "messi"]
# print_items(player_name)

# def show_welcome_message():
#     print("Welcome to the system!")

# # Calling with empty parentheses
# show_welcome_message()

# # 1. Defining the function
# def add_numbers(num1, num2):
#     sum_result = num1 + num2
#     return sum_result  # Handing the answer back!

# # 2. Calling the fun()
# my_total=add_numbers(5,3)# 3. Using that variable later in your code

# print(my_total)  # Output: 8

# # You can reuse that saved variable anywhere else:
# # final_price = my_total + 10
# # # print(final_price)  # Output: 18

# def add_numbers(num1 ,num2):
#     sum=num1+num2
#     return(sum)

# total=add_numbers(5,10)
# total1=add_numbers(6,11)
# print(total)
# print(total1)


# def add_wrong(a, b):
#     print(a + b)
# result = add_wrong(5, 5)  # This will print "10" on your screen

# converter =usd into inr 
# def converter(usd_value):   
#     return(usd_value*83)

# usd_value=55
# value=converter(55)
# print(value)


# def exchange_rate(inr_value):
#     return(inr_value/83)

# value=exchange_rate(55)
# print(value)
