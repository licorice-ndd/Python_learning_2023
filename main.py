# how to use str in py : str = represent for string byte convert int to string

# retake fall Hoalac 2022
# Q1
# an ordered number is a number in which the digits in the number appear in the ascending order. For example 12345 is an ordered number but 14235 is not.
# write a program that will accept an positive integeral number then print out "true" if the number is an ordered number, otherwise print out "false"
# if the user enters anything other than a positive integeral number put out an appropriate message and ignore the number. for example
# Enter an intergeral number : -1234
# please enter a positive intergeral number
# Enter an intergeral number : 12345
# true
# Enter an intergeral number : 13524
# false

# Q1 solu
# def isAscending(n):
#     if n < 10:
#         return True
#     while n > 0:
#         last1 = n % 10
#         n //= 10
#         last2 = n % 10
#         if last1 < last2:
#             return False
#     return True
# while True:
#     try:
#         n = int(input('Enter a positive integer: '))
#         if isinstance(n, int) and n > 0:
#             break
#         else:
#             print('Please enter a positive integer.')
#     except:
#         print('Please enter a positive integer.')
# if isAscending(n):
#     print('True')
# else:
#     print('False')

# Q2 solu

# file = input("Enter file: ")                # This line prompts the user to enter the name of a file and stores the input in the variable
# f = open(file, "r")                         # This line opens the file specified by the user in read-only mode ("r") and assigns the file object to the variable 'f'. If the file cannot be opened, an error will be raised.
# line = f.readline()                         # This line reads the first line of the file (f) and assigns it to the variable line. If the file is empty, this line will set line to an empty string.
# print('The content of the file:',line)
# A = line.split(' ')                         # This line splits the string in line into a list of substrings at every space character (' ') and assigns the list to the variable A.
# list_null=[]                                # This line initializes an empty list called list_null.
# for i in A:                                 # This loop iterates over each substring (i) in the list A,
#     list_null.append(int(i))                # converts it to an integer using the int() function, and appends the integer to the list list_null.
# def Average(lst):
#     return sum(lst) / len(lst)
# average = Average(list_null)
# print('Avg =',average)

# Q3 solu
# write a program to manage list of course list of a school using database file Course.sqlite
# the program read data from the file subject.txt and course.txt and then save to the tables subject and course respectively
# subject(sid, sname) course (cid, cname, sid)
# the program prints the course list which belong to "database" or "english" subject
# and sorted in ascending order by cname

# import sqlite3
# import re
# lines = open('Course.txt', 'r')
# conn = sqlite3.connect('COURSE.sqlite')
# conn.executescript(
# '''
# drop table if exists Course;
# create table Course(
# CID text not null ,
# CName text not null,
# SID text not null
# );
# '''
# )
# count = 1
# for line in lines:
#     if count == 1:
#         count = count + 1
#         continue
#     else:
#         fields = re.split('\\s+', line)
#         conn.execute('insert into Course values (?, ?, ?);', (fields[0], fields[1]+' '+fields[2], fields[3]))
#         lines2 = open('Subject.txt', 'r')
#         conn.executescript(
#             '''
#             drop table if exists Subject;
#             create table Subject(
#             SID text not null ,
#             SName text not null
#             );
#             '''
#         )
# count = 1
# for line in lines2:
#     if count == 1:
#         count = count + 1
#         continue
#     else:
#         fields = re.split('\\s+', line)
#         conn.execute('insert into Subject values (?, ?);', (fields[0], fields[1]))
#         conn.commit()
#         table = conn.execute('select c.CID, c.CName, s.SName from Subject s join Course c on s.SID = c.SID '
#                                 'where SName = ? or SName = ? '
#                                 'order by SName asc', ('Database', 'English'))
# print("Course list:")
# print("ID".ljust(10, ' '), "Course Name".rjust(10, ' '), "Subject Name".rjust(10, ' '))
# for row in table:
#     print(str(row[0]).ljust(10, ' '), str(row[1]).rjust(10, ' '), str(row[2]).rjust(10, ' '))


# pe 4-12-2022
# Q1 you are required to develop a python program that will throw two
# dice until the top faces of the two dice total to a specified number
# the output belike
# enter an integer number of total : 8
# dice thrower
# ============
# result of throw : 1 1 + 3
# result of throw : 2 6 + 5
# result of throw : 3 4 + 3
# result of throw : 4 6 + 2
# you got ur total in 4 throws

# Q1 solu
# import random
# while True:
#     n = int(input("Enter an integer number of total: "))
#     if n < 2 or n >12:
#         print("Total of 2 dices must in range 2, 12")
#     else:
#         break
# count = 1
# while True:
#     n1 = random.randint(1, 6)
#     n2 = random.randint(1, 6)
#     print(f"Result of throw : {count} _ {n1}+{n2}")
#     if n1+n2 == n:
#         break
#     else:
#         count = count +1
# print(f"Your got your total in {count} throws")
# Text.txt
# Q2 read file and combinations number in that
# file = input("Enter file: ")
# f = open(file, "r")
# line = f.readline()
# A = line.split(', ')
# print(f'The original list from the file is: {A}')
# num_list = []
# n = len(A)
# for i in range (n-1):
#     for j in range (i+1, n):
#         num = 10*int(A[i]) + int(A[j])
#         num_list.append(num)
# print(num_list)

# (PE) SPRING 22 CA 13H-16H30

#khai bao bien trong python
"""""
domain = "mr a welcome"
print(domain)

linkwebsite = "https://soundcloud.com/cocailon/tracks"
print(linkwebsite)

"""""
#xoa bien trong python : xóa xong thì print sẽ bị lỗi
"""""
delete_bien = "checked or unchecked"
del delete_bien
print(delete_bien)

"""""
# các kiểu comment
# 1 line
"""""
checkline 1
checkline 2
checkline 3
"""""

# các kiểu dữ liệu, dữ liệu chuỗi nằm trong nháy đơn or kép
"""""
age = 30 #kiểu number
str = 'Hello World!' # string
print(str)  # In ra toàn bộ chuỗi
print(str[0])  # In phân tử đầu tiên của chuỗi
print(str[2:5])  # In phần tử thứ 3 đến thứ 6, tại vì chỉ mục bắt đầu từ 0
print(str[2:])  # In từ vị trí thứ 3 đến cuối chuỗi
print(str * 2)  # In chuỗi hai lần :  dấu * để lặp chuỗi
print(str + "TEST")  # Nối chuỗi : dấu + để nối chuỗi

"""""

# kiểu dữ liệu list
"""""

domains = ["freetuts.net", "kephimonline.com", "zip.freeetuts.net"]
infor1 = ["cuong", 31]
infor2 = {'name': 'Cường','domain': 'freetuts.net', 'age': 31}
print(domains)

"""""
# ép kiểu data
# 1. ép kiểu ngầm
"""""

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("Kiểu dữ liệu của num_int:", type(num_int))
print("Kiểu dữ liệu của num_flo:", type(num_flo))

print("Giá trị của num_new:", num_new)
print("Kiểu dữ liệu của num_new:", type(num_new))

num_int = 123
num_str = "456"

print("Kiểu dữ liệu của num_int:", type(num_int))
print("Kiểu dữ liệu của num_str:", type(num_str))

# Dòng này sẽ lỗi vì string và number không chuyển ngầm được
print(num_int + num_str)

"""""

# 2. ép kiểu public

# num_int = 123
# num_str = "456"
#
# print("Kiểu dữ liệu của num_int:", type(num_int))
# print("Kiểu dữ liệu của num_str trước khi ép kiểu:", type(num_str))
#
# num_str = int(num_str)
# print("Kiểu dữ liệu của num_str sau khi ép kiểu:", type(num_str))
#
# num_sum = num_int + num_str
#
# print("Tổng của num_int và num_str:", num_sum)
# print("Kiểu dữ liệu của sum:", type(num_sum))

# 3. table of trans data in python
# STT	Function & Description
# 1	    int(x [,base]) ép kiểu int
# 2	    long(x [,base] ) ép kiểu long int.
# 3	    float(x) ép kiểu float.
# 4	    complex(real [,imag]) ép kiểu complex number.
# 5	    str(x) ép kiểu string.
# 6	    repr(x) ép thành chuỗi biểu thức.
# 7	    eval(str) ép chuỗi sang object.
# 8	    tuple(s) ép kiểu tuple.
# 9	    list(s) ép kiểu list.
# 10	set(s) ép kiểu set.
# 11	dict(d) ép kiểu dictionary.
# 12	frozenset(s) ép kiểu frozen set.
# 13	chr(x) ép kiểu in sang kiểu char
# 14	unichr(x) ép kiểu int sang Unicode character.
# 15	ord(x) ép ký tự sang kiểu int.
# 16	hex(x) ép kiểu integer sang chuỗi thập lục phân.
# 17	oct(x) ép kiểu integer chuỗi bát phân.

# Toán tử trong Python
# Toán tử	        Ý nghĩa
#    +	            Cộng
#    -	            Trừ
#    *	            Nhân
#    /	            Chia
#    %	            Chia lấy dư
#    **	            Tính lũy thừa
#    ==	            Trả về True nếu A bằng B, False nếu a khác B
#    !=	            Trả về True nếu A khác B, False nếu A bằng B
#    <>	            Giống với toán tử !=
#    >	            Trả về True nếu A > B, False nếu A bé hơn hoặc bằng B
#    <	            Trả về True nếu A < B, False nếu A lớn hơn hoặc bằng B
#    >=	            Trả vè True nếu A lớn hơn hoặc bằng B, ngược lại trả về False
#    <=	            Trả về True nếu A bé hơn hoặc bằng B, ngược lại trả về False
#    c = a + b	    Gán giá trị a + b vào biến c
#    a += b	        Tương đương với a = a + b
#    a -= b	        Tương đương với a = a - b
#    a *= b	        Tương đương với a = a * b
#    a /= b	        Tương đương với a = a / b
#    a %= b	        Tương đương với a = a % b
#    a **= b	    Tương đương với a = a ** b

# a = 10
# b = 20
# print("Cộng: " + str(a + b))
# print("Trừ: " + str(a - b))
# print("Nhân: " + str(a * b))
# print("Chia: " + str(a / b))
# print("Chia lấy dư: " + str(a % b))
# print("Số mũ: " + str(a ** b))
# print("So sánh bằng: "              + str(a == b))
# print("So sánh không bằng: "        + str(a != b))
# print("So sánh lớn hơn: "           + str(a > b))
# print("So sánh bé hơn: "            + str(a < b))
# print("So sánh lớn hơn hoặc bằng: " + str(a >= b))
# print("So sánh bé hơn hoặc bằng: "  + str(a <= b))

# a = 4
# b = 2
# c = a + b  # c = 6
# a += b  # a = a + b = 6
# a -= b  # a = a - b = -2
# a *= b  # a = a * b = 8
# a /= b  # a = a / b = 2
# a %= b  # a = a % b = 0
# a **= b  # a = a ** b = 16

# A = True
# B = False
#
# print(A and B)  # False
# print(A or B)  # True
# print(not A)  # False

 # -------------------------------------------------------------------------------------------

# EX 1
# Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5,
# nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200).
# Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.

# print("bai 1--------")
# j = [] #Tạo một danh sách rỗng để lưu kết quả
# for i in range (2000,3200):             #Duyệt qua tất cả các số trong đoạn từ 2000 đến 3200
#     if (i % 7 == 0) and (i %5 != 0):    #Kiểm tra xem số i có chia hết cho 7 và không phải là bội số của 5 không
#         j.append(str(i))                #Nếu đúng, thì thêm số i vào danh sách result
# print("--- de answer")
# print(','.join(j))                      #In ra màn hình danh sách result, các phần tử cách nhau bằng dấu phẩy

# EX 2
# Viết một chương trình có thể tính giai thừa của một số cho trước.
# Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
# Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

# print("bai 2--------")
# x = int(input("enter de number of giai thua : "))
# def fact(x):                            # def = khai báo hàm , fact(x) tính giai thừa của 1 số nguyên dương x
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
# print(fact(x))

# EX 3
# Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i)
# như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này.

# print("bai 3--------")
# n = int(input("enter de number : "))
# d = dict()
# for i in range(1,n+1):
#     d[i] = i*i
# print(d)

# EX 4
# Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển,
# tạo ra một danh sách và một tuple chứa mọi số.

# print("bai 4--------")
# values = input("Nhập vào các giá trị : ")
# l = values.split(",")
# t = tuple(l)
# print (l)
# print (t)

# EX 5
# Định nghĩa một class có ít nhất 2 method:
# getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
# printString: in chuỗi vừa nhập sang chữ hoa.
# Thêm vào các hàm kiểm tra đơn giản để kiểm tra method của class.
# Chuỗi nhập vào là nguyenduy.com thì đầu ra phải là: NGUYENDUY.COM
# Sử dụng __init__ để xây dựng các tham số.

# print("bai 5--------")
# class InputToUpperCase(object):
#     def __int__(self):
#         self.s = ""
#     def getString(self):
#         self.s = input("Enter string want to upgrade : ")
#     def printString(self):
#         print(self.s.upper())
# strObj = InputToUpperCase()
# strObj.getString()
# strObj.printString()

# EX 6 find square x

# x = int(input("enter de number : "))
# def square(num):
#     return num ** 2
# print(square(x))

# Ex 7
# Python có nhiều hàm được tích hợp sẵn, nếu không biết cách sử dụng nó, bạn có thể đọc tài liệu trực tuyến hoặc tìm vài cuốn sách.
# Nhưng Python cũng có sẵn tài liệu về hàm cho mọi hàm tích hợp trong Python.
# Yêu cầu của bài tập này là viết một chương trình để in tài liệu về một số hàm Python được tích hợp sẵn như abs(), int(), input() và thêm tài liệu cho hàm bạn tự định nghĩa.

# print (abs.__doc__)
# print (int.__doc__)
# print (input.__doc__)
# def square(num):
#  return num ** 2
# print (square.__doc__)

# Ex 8
# Defines a class that includes a class parameter and the same instance parameter

# class Person:
#     # định nghĩ class "name"
#     name = "Person"
#     def __init__(self, name = None):
#         self.name = name               # self.name là biến instance
# mra = Person("MrA")
# print("%s name is %s" % (Person.name, mra.name))
# mrb = Person()
# mrb.name = "MrB"
# print("%s name is %s" % (Person.name, mrb.name))

# Ex 9
# Calculate age based on the date of birth entered. dateofbirth enter or smth else

# import datetime
# print("enter ur date to calculate age")
# day = int(input("Day : "))
# month = int(input("Month : "))
# year = int(input("Year : "))
#
# current_day = datetime.date.today().day
# current_month = datetime.date.today().month
# current_year = datetime.date.today().year
#
# age_day = abs(current_day - day)
# age_month = abs(current_month - month)
# age_year = current_year - year
#
# print("your age exactly : ",age_day,"days ",age_month,"months",age_year,"years old")

# Ex 10
# Viết chương trình nhập: số giờ làm mỗi tuần, thù lao trên mỗi giờ làm tiêu chuẩn, từ đó tính ra số tiền thực lĩnh của nhân viên.
# Biết rằng: số giờ tiêu chuẩn mỗi tuần là 44 giờ, và mỗi giờ vượt chuẩn được trả gấp rưỡi so với giờ làm chuẩn.
# Write a program to input: the number of hours worked per week, the standard hourly remuneration, from which to calculate the actual amount of the employee's salary.
# Know that: the standard hours per week are 44 hours, and each overtime hour is paid one-and-a-half times the standard hourly rate.
# or input de gio tieu chuan

# so_gio_lam = float(input("Nhap so gio lam moi tuan : "))
# luong_gio = float(input("Nhap thu lao tren moi gio lam tieu chuan : "))
#
# gio_tieu_chuan = 44
# gio_tieu_chuan_input = int(input("nhap so gio tieu chuan : "))
#
# gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
# gio_vuot_chuan_input = max(0, so_gio_lam - gio_tieu_chuan_input)
#
# final_salary = gio_vuot_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
# final_salary_input = gio_vuot_chuan_input * luong_gio + gio_vuot_chuan_input * luong_gio * 1.5
# print(f"Last salary per month : {final_salary}")
# print(f"Last salary per month : {final_salary_input}")

# Ex 11
# Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H]) (bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H].
# Với giá trị cố định của C là 50, H là 30. D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng, các giá trị của D được phân cách bằng dấu phẩy.
# Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.
# Gợi ý:
# Nếu đầu ra nhận được là một số dạng thập phân, bạn cần làm tròn thành giá trị gần nhất, ví dụ 26.0 sẽ được in là 26.
# Trong trường hợp dữ liệu đầu vào được cung cấp cho câu hỏi, nó được giả định là đầu vào do người dùng nhập từ giao diện điều khiển.

# import math
# c = 50
# h = 30
# value = []
# items = [x for x in input("nhap gia tri d : ").split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# print(', '.join(value))

# Ex 12
# Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều.
# Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.
# Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.
# Ví dụ: Giá trị X, Y nhập vào là 3,5 thì
# đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# input_str = input("nhap x, y : ")
# dimensions = [int(x) for x in input_str.split(',')]
# rowNum = dimensions[0]
# colNum = dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col] = row * col
# print(multilist)

# Ex 13
# Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau bởi dấu phẩy và
# in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.
# Giả sử đầu vào được nhập là: without,hello,bag,world, thì
# đầu ra sẽ là: bag,hello,without,world.

input_str = input("Nhập một chuỗi các phần tử, cách nhau bởi dấu phẩy: ")
items = [x.strip() for x in input_str.split(',')]
items.sort()
items.reverse() # if dont do dis one, the string will set by alphabet, else will set by alphabet
output_str = ','.join(items)
print(output_str)
