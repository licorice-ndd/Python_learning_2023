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
#                                 'order by SName desc', ('Database', 'English')) # or asc
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

# Q1 solu
# def DecimalToBinary(num):
#     if num >= 1:
#         DecimalToBinary(num//2)
#     if num != 0:
#         print(num % 2, end = '')
#
# def DecimalToHexadecimal(num):
#     if num >= 16:
#         DecimalToHexadecimal(num // 16)
#     if num != 0:
#         val = num % 16
#         if val < 10:
#             print(val, end='')
#         else:
#             print(chr(ord('A') + val - 10), end='')
#
# def decimalToOctal(num):
#     if num >= 8:
#         decimalToOctal(num // 8)
#     if num != 0:
#         print(num % 8, end='')

# while True:
#     number = input("Enter a positive integer number : ")
#     try:
#         usVal = int(number)
#         if usVal < 0:
#             print("the number must be positive.")
#             continue
#         break
#
#     except ValueError:
#         print("the number must be a positive integer")
#
# print("%d is converted to binary : " %usVal, end = "")
# DecimalToHexadecimal(usVal)

# Q2 solu
# import re
# fname = input("enter file : ")
# fhand = open(fname, "r")
# list = []
#
# print("troubleshoot wired LAN related issues:")
#
# for line in fhand:
#     line = line.strip()
#     if line.startswith("Name: "):
#         name = line[20:].split("-")[0]
#         list.append(name)
#
# def countFreq(mylist):
#     freq = {}
#     for item in mylist:
#         if (item in freq):
#             freq[item] += 1
#         else:
#             freq[item] = 1
#
#     for i in sorted(freq):
#         print(str(i) + ": " + str(freq[i]))
#
# countFreq(1)

# 12/12/2021 Q2
def isOrdered(words_list):

    result = []
    for word in words_list:
        # print(word)

        i = 0
        l = len(word) - 1
        check = True
        while i < l:

            if ord(word[i]) > ord(word[i + 1]):

                check = False
                break
            else:
                i += 1

        if check:
            result.append(word)

    return result

filename =input("Enter file: ")
words_list = []
with open(filename) as file_in:
    globals()
    for word in file_in.readlines():
        words_list.append(word.strip('\n'))


answer = isOrdered(words_list)
print("The ordered words: ")
print(answer)

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

# input_str = input("Nhập một chuỗi các phần tử, cách nhau bởi dấu phẩy: ")
# items = [x.strip() for x in input_str.split(',')]
# items.sort()
# items.reverse() # if dont do dis one, the string will set by alphabet, else will set by alphabet
# output_str = ','.join(items)
# print(output_str)

# EX 14
# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định
# là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

# lines = []
# while True:
#    s = input()
#    if s:
#       lines.append(s.upper())
#    else:
#       break;
# for sentence in lines:
#     print(sentence)

# EX 15
# Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng, loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.
# Giả sử đầu vào là: hello world and practice makes perfect and hello world again
# Thì đầu ra là: again and hello makes perfect practice world

# s = input("Nhập chuỗi của bạn: ")
# words = [word for word in s.split(" ")]
# print(" ".join(sorted(list(set(words)))))

# EX 16
# Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không.
# Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.
# Ví dụ đầu vào là: 0100,0011,1010,1001
# Đầu ra sẽ là: 1010

# value = []
# items = [x for x in input("Nhập các số nhị phân: ").split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)
# print(','.join(value))

# EX 17
# Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này) sao cho tất cả
# các chữ số trong số đó là số chẵn.
# In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.

# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0): # this line will check 4 number in str and goin wrong, replace by (int(s[3]) % 2 == 0)
#         values.append(s)
#
# print(",".join(values))

# EX 18
# Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó.
# Giả sử đầu vào sau được cấp cho chương trình: hello world! 123
# Thì đầu ra sẽ là:
# Số chữ cái là: 10
# Số chữ số là: 3

# s = input(" Nhập câu của bạn: ")
# d = {"DIGITS": 0, "LETTERS": 0,  "CHAC": 0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"] += 1
#     elif c.isnumeric():
#         d["CHAC"] += 1
#     elif c.isalpha():
#         d["LETTERS"] += 1.
#     else:
#         pass
# print("Số chữ cái là:", d["LETTERS"])
# print("Số chữ số là:", d["DIGITS"])
# print("Số ki hieu là:", d["CHAC"])

# EX 19
# count uppercase and lowercase

# s = input("Nhập câu của bạn: ")
# d = {"UPPER CASE": 0, "LOWER CASE": 0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"] += 1
#     elif c.islower():
#         d["LOWER CASE"] += 1
#     else:
#         pass
# print("Chữ hoa:", d["UPPER CASE"])
# print("Chữ thường:", d["LOWER CASE"])

# EX 20
# Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng.
# Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234

# a = input("Nhập số a: ")
# n1 = int("%s" % a)
# n2 = int("%s%s" % (a, a))
# n3 = int("%s%s%s" % (a, a, a))
# n4 = int("%s%s%s%s" % (a, a, a, a))
# print("Tổng cần tính là: ", n1+n2+n3+n4)

# EX 21
# Sử dụng một danh sách để lọc các số lẻ từ danh sách được người dùng nhập vào.
# Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9
# odd = lẻ , even = chẵn

# values = input("Nhập dãy số của bạn, cách nhau bởi dấu phẩy: ")
# odd = [x for x in values.split(",") if int(x) % 2 != 0]
# even = [x for x in values.split(",") if int(x) % 2 == 0]
# print(",".join(odd))
# print(",".join(even))

# EX 22
# Viết chương trình tính số tiền thực của một tài
# khoản ngân hàng dựa trên nhật ký giao dịch được nhập vào từ giao diện điều khiển.
# Định dạng nhật ký được hiển thị như sau:
# D 100
# W 200
# (D là tiền gửi, W là tiền rút ra).

# import sys
# netAmount = 0
# while True:
#     s = input("Nhập nhật ký giao dịch: ")
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation == "D":
#         netAmount += amount
#     elif operation == "W":
#         netAmount -= amount
#     else:
#         pass
# print(netAmount)

# EX 23
# nhập một dãy số nguyên, sau đó kiểm tra xem nó có khả đối xứng không?
# Nếu 0, hãy biến đổi nó để được một dãy đối xứng.
#
# def kiem_tra_doi_xung(lst):
#     return lst == lst[::-1]
# def convert_doi_xung(lst):
#     if kiem_tra_doi_xung(lst):
#         return lst
#     else:
#         for i in range(len(lst)//2):
#             if lst[i] != lst[-i-1]:
#                 for j in range(i+1, len(lst)):
#                     if lst[j] == lst[-i-1]:
#                         lst[i], lst[j] = lst[j], lst[i]
#                         break
#         return lst
#
# lst = list(map(int, input("Nhập dãy số nguyên, cách nhau bởi dấu cách: ").split()))
#
# if kiem_tra_doi_xung(lst):
#     print("Dãy số đã đối xứng.")
# else:
#     new_lst = convert_doi_xung(lst)
#     if kiem_tra_doi_xung(new_lst):
#         print("Dãy số đã khả đối xứng và biến đổi thành dãy số đối xứng: ", new_lst)
#     else:
#         print("Dãy số không khả đối xứng.")

# EX 24
# Viết chương trình Python nhập một mảng hai chiều các số thực A (m hàng, n cột) từ bàn phím.
# a. Tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột
# b. Tìm phần tử lớn nhất và phần tử nhỏ nhất của mảng A cùng các chỉ số hàng và cột của 2 phần tử này.
# c. Trong mảng A có bao nhiêu phần tử bằng phần tử lớn nhất.

# using numpy
# import numpy as np
#
# # Nhập mảng A từ bàn phím
# m, n = map(int, input("Nhập số hàng và số cột của mảng A (cách nhau bởi dấu cách): ").split())
# A = np.zeros((m, n))
# for i in range(m):
#     row = list(map(float, input(f"Nhập dòng {i+1} của mảng A, cách nhau bởi dấu cách: ").split()))
#     A[i, :] = row
#
# # Tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột
# max_col = np.amax(A, axis=0)
# min_col = np.amin(A, axis=0)
# print("Giá trị lớn nhất trên mỗi cột:", max_col)
# print("Giá trị nhỏ nhất trên mỗi cột:", min_col)
#
# # Tìm phần tử lớn nhất và phần tử nhỏ nhất của mảng A cùng với chỉ số hàng và cột của 2 phần tử này
# max_val = np.amax(A)
# max_idx = np.unravel_index(np.argmax(A), A.shape)
# min_val = np.amin(A)
# min_idx = np.unravel_index(np.argmin(A), A.shape)
# print("Phần tử lớn nhất của mảng A là", max_val, "ở dòng", max_idx[0]+1, "cột", max_idx[1]+1)
# print("Phần tử nhỏ nhất của mảng A là", min_val, "ở dòng", min_idx[0]+1, "cột", min_idx[1]+1)
#
# # Tính số phần tử bằng phần tử lớn nhất
# count_max = np.count_nonzero(A == max_val)
# print("Số phần tử bằng phần tử lớn nhất là:", count_max)

# not using numpy
# Hàm nhập mảng A từ bàn phím
# def input_array(m, n):
#     A = []
#     for i in range(m):
#         row = list(map(float, input(f"Nhập hàng {i+1}, cách nhau bởi dấu cách: ").split()))
#         A.append(row)
#     return A
# # Hàm tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột của mảng A
# def find_max_min_per_col(A):
#     m, n = len(A), len(A[0])
#     max_per_col = [max([A[i][j] for i in range(m)]) for j in range(n)]
#     min_per_col = [min([A[i][j] for i in range(m)]) for j in range(n)]
#     return max_per_col, min_per_col
# # Hàm tìm phần tử lớn nhất và nhỏ nhất của mảng A cùng các chỉ số hàng và cột
# def find_max_min_index(A):
#     max_val, min_val = A[0][0], A[0][0]
#     max_row, max_col, min_row, min_col = 0, 0, 0, 0
#     m, n = len(A), len(A[0])
#     for i in range(m):
#         for j in range(n):
#             if A[i][j] > max_val:
#                 max_val = A[i][j]
#                 max_row, max_col = i, j
#             if A[i][j] < min_val:
#                 min_val = A[i][j]
#                 min_row, min_col = i, j
#     return max_val, max_row, max_col, min_val, min_row, min_col
# # Hàm đếm số phần tử trong mảng A bằng phần tử lớn nhất
# def count_max_value(A):
#     max_val = max([max(row) for row in A])
#     count = 0
#     for row in A:
#         count += row.count(max_val)
#     return count
# # Nhập mảng A từ bàn phím
# m, n = map(int, input("Nhập số hàng và số cột của mảng A, cách nhau bởi dấu cách: ").split())
# A = input_array(m, n)
# # Tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột của mảng A
# max_per_col, min_per_col = find_max_min_per_col(A)
# print("Giá trị lớn nhất trên mỗi cột: ", max_per_col)
# print("Giá trị nhỏ nhất trên mỗi cột: ", min_per_col)
# # Tìm phần tử lớn nhất và nhỏ nhất của mảng A cùng các chỉ số hàng và cột
# max_val, max_row, max_col, min_val, min_row, min_col = find_max_min_index(A)
# print(f"Phần tử lớn nhất: {max_val}, hàng: {max_row+1}, cột: {max_col+1}")
# print(f"Phần tử nhỏ nhất: {min_val}, hàng: {min_row+1}, cột: {min_col+1}")
# # Đếm số phần tử trong mảng
# count = count_max_value(A)
# print(f"Số phần tử bằng giá trị lớn nhất ({max_val}) trong mảng A: {count}")

# EX 25
# Các tiêu chí kiểm tra mật khẩu bao gồm:
# 1. Ít nhất 1 chữ cái nằm trong [a-z]
# 2. Ít nhất 1 số nằm trong [0-9]
# 3. Ít nhất 1 kí tự nằm trong [A-Z]
# 4. Ít nhất 1 ký tự nằm trong [$ # @]
# 5. Độ dài mật khẩu tối thiểu: 6
# 6. Độ dài mật khẩu tối đa: 12
# Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy và kiểm tra xem chúng có đáp ứng những tiêu chí trên hay không.
# Mật khẩu hợp lệ sẽ được in, mỗi mật khẩu cách nhau bởi dấu phẩy.
# Ví dụ mật khẩu nhập vào chương trình là: ABd1234@1,a F1#,2w3E*,2We3345 Thì đầu ra sẽ là: ABd1234@1

# import re
# value = []
# items = [x for x in input("Nhập mật khẩu: ").split(',')]
# for p in items:
#     if len(p) < 6 or len(p) > 12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]",p):
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("[A-Z]",p):
#         continue
#     elif not re.search("[$#@]",p):
#         continue
#     elif re.search("\s",p):
#         continue
#     else:
#         pass
#     value.append(p)
# print(",".join(value))

# EX 26
# Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, name là string, age và height là number.
# Tuple được nhập vào bởi người dùng. Tiêu chí sắp xếp là:
# Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score. Ưu tiên là tên > tuổi > điểm.
# Nếu đầu vào là:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Thì đầu ra sẽ là:[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

# import operator
# l = []
# while True:
#     s = input()
#     if not s:
#        break
#     l.append(tuple(s.split(",")))
# print(sorted(l, key=operator.itemgetter(0, 1, 2)))

# EX 27
# Xác định một class với generator có thể lặp lại các số nằm trong khoảng 0 và n, và chia hết cho 7
# def putNumbers(n):
#     i = 0
#     while i<n:
#         j=i
#         i=i+1
#         if j%7==0:
#             yield j
# for i in putNumbers (100):
#      print (i)

# EX 28
# Viết chương trình tính tần suất các từ từ input. Output được xuất ra sau khi đã sắp xếp theo bảng chữ cái.
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# freq = {} # frequency of words in text
# line = input()
# for word in line.split():
#     freq[word] = freq.get(word,0)+1
# words = sorted(freq.keys())
# for w in words:
#     print ("%s:%d" % (w,freq[w]))

# EX 29 : Định nghĩa 1 hàm có thể tính tổng hai số.
# def SumFunction(number1, number2): #định nghĩa hàm tính tổng
#     return number1+number2
# print (SumFunction(5,7)) #in tổng 2 số 5 và 7

# EX 30 : Định nghĩa một hàm có thể chuyển số nguyên thành chuỗi và in nó ra giao diện điều khiển
# def printValue(n):
#     print (str(n))
# printValue(3)

# EX 31 : Định nghĩa hàm có thể nhận hai số nguyên trong dạng chuỗi và tính tổng của chúng, sau đó in tổng ra giao diện điều khiển.
# def printValue(s1,s2):
#     print (int(s1)+int(s2))
# printValue("3","4") #Kết quả là 7

# EX 32 : Định nghĩa hàm có thể nhận 2 chuỗi từ input và nối chúng sau đó in ra giao diện điều khiển
# def printValue(s1,s2):
#     print (s1+s2)
# printValue("3","4") #Kết quả là 34

# EX 33 : Định nghĩa một hàm có input là 2 chuỗi và in chuỗi có độ dài lớn hơn trong giao diện điều khiển. Nếu 2 chuỗi có chiều dài như nhau thì in tất cả các chuỗi theo dòng.
# def printValue(s1,s2):
#     len1 = len(s1)
#     len2 = len(s2)
#     if len1>len2:
#         print (s1)
#     elif len2>len1:
#         print (s2)
#     else:
#         print(s1)
#         print (s2)
# printValue("one","three")

# EX 34 : Định nghĩa hàm có thể chấp nhận input là số nguyên và in "Đây là một số chẵn" nếu nó chẵn và in "Đây là một số lẻ" nếu là số lẻ.
# def checkValue(n):
#     if n%2 == 0:
# print ("Đây là một số chẵn")
#     else:
#        print ("Đây là một số lẻ")
# checkValue(7)

# EX 35 : Định nghĩa một hàm có thể in dictionary chứa key là các số từ 1 đến 3 (bao gồm cả hai số) và các giá trị bình phương của chúng.
# def printDict():
#     d=dict()
#     d[1]=1
#     d[2]=2**2
#     d[3]=3**2
#     print(d)
# printDict()

# EX 36 : Định nghĩa một hàm có thể in dictionary chứa các key là số từ 1 đến 20 (bao gồm cả 1 và 20) và các giá trị bình phương của chúng.

# def printDict():
#     d=dict()
#     for i in range(1,21):
#        d[i]=i**2
#     print (d)
# printDict()

# 37 : Định nghĩa một hàm có thể tạo dictionary, chứa các key là số từ 1 đến 20 (bao gồm cả 1 và 20) và các giá trị bình phương của chúng. Hàm chỉ in các giá trị mà thôi.
# Sử dụng dict[key]=value để nhập mục vào dictionary.
# Sử dụng toán từ ** để lấy bình phương của một số.
# Sử dụng range() cho các vòng lặp.
# Sử dụng keys() để di lặp các key trong dictionary. Có thể sử dụng item() để nhận cặp key/value.

# def printDict():
#     d = dict()
#     for i in range(1, 21):
#         d[i] = i**2
#     for (k, v) in d.items():
#         print(v)
# printDict()

# 38 : Định nghĩa một hàm có thể tạo ra một dictionary chứa key là những số từ 1 đến 20 (bao gồm cả 1 và 20) và các giá trị bình phương của key. Hàm chỉ cần in các key.
# def printDict():
#  d=dict()
#  for i in range(1,21):
#     d[i]=i**2
#  for k in d.keys():
#        print (k)
# printDict()

# 39 : Định nghĩa một hàm có thể tạo và in list chứa các giá trị bình phương của các số từ 1 đến 20 (tính cả 1 và 20).
# def printList():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print (li)
# printList()

# 40 : Định nghĩa một hàm có thể tạo list chứa các giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20) và in 5 mục đầu tiên trong list.
# Sử dụng toán tử ** để lấy giá trị bình phương.
# Sử dụng range() cho vòng lặp.
# Sử dụng list.append() để thêm giá trị vào list.
# Sử dụng [n1:n2] để cắt list

# def printList():
#     li = list()
#     for i in range(1,21):
#         li.append(i**2)
#     print(li[:5])
#
# printList()

# EX 41 : Định nghĩa một hàm có thể tạo ra list chứa các giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20), rồi in 5 mục cuối cùng trong list.
# def printList():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print (li[-5:])
# printList()

# EX 42 :  Định nghĩa một hàm có thể tạo list chứa giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20). Sau đó in tất cả các giá trị của list, trừ 5 mục đầu tiên.
# def printList():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print (li[5:])
# printList()

# EX 43 : Định nghĩa 1 hàm có thể tạo và in một tuple chứa các giá trị bình phương của các số từ 1 đến 20 (tính cả 1 và 20).
# def printTuple():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print (tuple(li))
#
# printTuple()

# EX 44 : Với tuple (1,2,3,4,5,6,7,8,9,10) cho trước, viết một chương trình in một nửa số giá trị đầu tiên trong 1 dòng và 1 nửa số giá trị cuối trong 1 dòng.
# tp=(1,2,3,4,5,6,7,8,9,10)
# tp1=tp[:5]
# tp2=tp[5:]
# print (tp1)
# print (tp2)

# 45 : Viết một chương trình để tạo tuple khác, chứa các giá trị là số chẵn trong tuple (1,2,3,4,5,6,7,8,9,10) cho trước.
# tp=(1,2,3,4,5,6,7,8,9,10)
# li=list()
# for i in tp:
#  if tp[-i]%2==0:
#        li.append(tp[i])
#
# tp2=tuple(li)
# print (tp2)

# 46 : Viết một chương trình để tạo ra và in tuple chứa các số chẵn được lấy từ tuple (1,2,3,4,5,6,7,8,9,10).
# tp=(1,2,3,4,5,6,7,8,9,10)
# li=list()
# for i in tp:
#     if tp[i-1]%2==0:
#         li.append(tp[i-1])
#         tp2=tuple(li)
# print (tp2)

# EX 47 : Viết một chương trình Python nhận chuỗi nhập vào bởi người dùng, in "Yes" nếu chuỗi là "yes" hoặc "YES" hoặc "Yes", nếu không in "No".
# s = input ("Nhập chuỗi: ")
# if s == "yes" or s == "YES" or s == "Yes":
#    print ("Yes")
# else:
#     print ("No")

# EX 48 : Viết chương trình Python có thể lọc các số chẵn trong danh sách sử dụng hàm filter. Danh sách là [1,2,3,4,5,6,7,8,9,10].
# li = [1,2,3,4,5,6,7,8,9,10]
# evenNumbers = list(filter (lambda x: x% 2 == 0, li))
# print (evenNumbers)

# 49 : Viết chương trình Python dùng map() để tạo list chứa các giá trị bình phương của các số trong [1,2,3,4,5,6,7,8,9,10].
# li = [1,2,3,4,5,6,7,8,9,10]
# squaredNumbers = list(map (lambda x: x ** 2, li))
# print (squaredNumbers)

# 50 : Viết chương trình Python dùng map() và filter() để tạo list chứa giá trị bình phương của các số chẵn trong [1,2,3,4,5,6,7,8,9,10].
# Dùng map() để tạo list.
# Dùng filter() để lọc thành phần trong list.
# Dùng lambda để định nghĩa hàm chưa biết.

# li = [1,2,3,4,5,6,7,8,9,10]
# squareOfEvenNumbers = list (map (lambda x: x ** 2, filter (lambda x: x% 2 == 0, li)))
# print (squareOfEvenNumbers)

# 51 : Viết chương trình Python dùng filter() để tạo danh sách chứa các số chẵn trong đoạn [1,20].
# evenNumbers = list(filter (lambda x: x% 2 == 0, range (1,21)))
# print (evenNumbers)

# 52 : Viết chương trình Python sử dụng map() để tạo list chứa giá trị bình phương của các số trong đoạn [1,20].
# squaredNumbers = list(map(lambda x: x ** 2, range (1,21)))
# print (squaredNumbers)

# 53 : Định nghĩa một class có tên là Vietnam, với static method là printNationality. Sử dụng @staticmethod để định nghĩa class với static method.
# class Vietnam (object):
#     @staticmethod
#     def printNationality ():
#         print ("Vietnam")
# VietnamVodich = Vietnam ()
# VietnamVodich.printNationality ()
# Vietnam.printNationality ()

# 54 : Định nghĩa một class tên Vietnam và class con của nó là Hanoi. Sử dụng Subclass(ParentClass) để định nghĩa một class con.
# class Vietnam(object):
#     pass
#
# class Hanoi(Vietnam):
#     pass
# # Bài Python 51, Code by Quantrimang.com
# VietnamVodich = Vietnam()
# NguoiHanoi = Hanoi()
# print (VietnamVodich)
# print (NguoiHanoi)

# 55 : Định nghĩa một class có tên là Circle có thể được xây dựng từ bán kính. Circle có một method có thể tính diện tích.
# Sử dụng def methodName(self) để định nghĩa method.

# class Circle(object):
#     def __init__(self, r):
#        self.radius = r
# # Bài Python 52, Code by Quantrimang.com
#     def area(self):
#        return self.radius**2*3.14
#
# aCircle = Circle(2)
# print (aCircle.area())

# 56 : Định nghĩa class có tên là Hinhchunhat được xây dựng bằng chiều dài và chiều rộng. Class Hinhchunhat có method để tính diện tích.
# class Hinhchunhat(object):
#     def __init__(self, l, w):
#        self.dai = l
#        self.rong = w
#     def area(self):
#        return self.dai*self.rong
# aHinhchunhat = Hinhchunhat(10,2)
# print (aHinhchunhat.area())

# 57 : Định nghĩa một class có tên là Shape và class con là Square. Square có hàm init để lấy đối số là chiều dài. Cả 2 class đều có hàm area để in diện tích của hình, diện tích mặc định của Shape là 0.
# class Shape(object):
#     def __init__(self):
#        pass
#
#     def area(self):
#        return 0
# class Square(Shape):
#     def __init__(self, l):
#        Shape.__init__(self)
#        self.length = l
#
#     def area(self):
#        return self.length*self.length
#
# aSquare= Square(3)
# print (aSquare.area())

# 58 :  Đưa ra một RuntimeError exception.
# raise RuntimeError('something wrong')

#or

# class RuntimeError(Exception):
#     def __init__(self, mismatch):
#        Exception.__init__(self, mismatch)
# try:
#     print ("And now, the Vocational Guidance Counsellor Sketch.")
#     raise RuntimeError("Does not have proper hat")
#     print ("This print statement will not be reached.")
# except RuntimeError as problem:
#     print ("Vocation problem: {0}".format(problem))

# 59 : Viết một chương trình chấp nhận chuỗi từ được phân tách bằng khoảng trống và in các từ chỉ gồm chữ số.
# import re
# s = input()
# print (re.findall("\d+",s))

# 60 : Viết chương trình để đọc chuỗi ASCII và chuyển đổi nó sang một chuỗi Unicode được mã hóa bằng UTF-8.

# s = input()
# v = s.encode() # có thể dùng v=s.encode('utf-8')
# print (v)

# 61 :  Viết một chương trình tính 1/2 + 2/3 + 3/4 + ... + n/(n + 1) với một n là số được nhập vào (n> 0).

# n=int(input("Nhập số n >0: "))
# sum=0.0
# for i in range(1,n+1):
#     sum += float(float(i)/(i+1))
# print (sum)

# 62 : Viết chương trình tính: f(n)=f(n-1)+100 khi n>0 và f(0)=1, với n là số được nhập vào (n>0).
# def f(n):
#     if n==0:
#         return 0
#     else:
#         return f(n-1)+100
# n=int(input("Nhập số n>0: "))
# print (f(n))

# 63 : Dãy Fibonacci được tính dựa trên công thức sau:
# f(n)=0 nếu n=0
# f(n)=1 nếu n=1
# f(n)=f(n-1)+f(n-2) nếu n>1
# Hãy viết chương trình tính giá trị của f(n) với n là số được người dùng nhập vào.
# Ví dụ: Nếu n được nhập vào là 7 thì đầu ra của chương trình sẽ là 13.

# def f(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return f(n-1)+f(n-2)
# n=int(input("Nhập số n: "))
# print (f(n))

# 64 : Dãy Fibonacci được tính dựa trên công thức sau:
# f(n)=0 nếu n=0
# f(n)=1 nếu n=1
# f(n)=f(n-1)+f(n-2) nếu n>1
# Hãy viết chương trình sử dụng list comprehension để in dãy Fibonacci dưới dạng tách biệt bằng dấu ",", n được người dùng nhập vào.
# Ví dụ: Nếu n được nhập vào là 7 thì đầu ra của chương trình sẽ là: 0,1,1,2,3,5,8,13
# Chúng ta có thể định nghĩa hàm đệ quy trong Python.
# Sử dụng list comprehension để tạo ra list từ list hiện có.
# Sử dụng string.join() để nối danh sách các chuỗi.

# def f(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return f(n-1)+f(n-2)
# n=int(input("Nhập số n: "))
# values = [str(f(x)) for x in range(0, n+1)]
# print (",".join(values))

# 65 : Viết chương trình sử dụng generator để in số chẵn trong khoảng từ 0 đến n, cách nhau bởi dấu phẩy, n là số được nhập vào.
# Ví dụ nếu n=10 được nhập vào thì đầu ra của chương trình là: 0,2,4,6,8,10

# def EvenGenerator(n):
#     i=0
#     while i<=n:
#         if i%2==0:
#             yield i
#         i+=1
# n=int(input("Nhập n: "))
# values = []
# for i in EvenGenerator(n):
#     values.append(str(i))
# print ("Các số chẵn trong khoảng 0 và n là: ",",".join(values))

# 66 : Viết chương trình sử dụng generator để in số chia hết cho 5 và 7 giữa 0 và n, cách nhau bằng dấu phẩy, n được người dùng nhập vào.
# Ví dụ: Nếu n=100 được nhập vào thì đầu ra của chương trình là: 0,35,70.
# def NumGenerator(n):
#     for i in range(n+1):
#         if i%5==0 and i%7==0:
#             yield i
# n=int(input("Nhập n: "))
# values = []
# for i in NumGenerator(n):
#     values.append(str(i))
#
# print ("Các số chia hết cho 5 và 7 trong khoảng 0 và n là: ",",".join(values))

# 67 : Viết các lệnh assert để xác minh rằng tất cả các số trong list [2,4,6,8] là chẵn.
# li = [2,4,6,8]
# for i in li:
#  assert i%2==0

# 68 : Viết chương trình chấp nhận biểu thức toán học cơ bản do người dùng nhập vào từ bảng điều khiển và in kết quả ước lượng ra ngoài màn hình.

# expression = input("Nhập biểu thức cần tính: ")
# print (eval(expression))
# example : input = 3+5 => output = 8

# 69 : Viết hàm tìm kiếm nhị phân để tìm các item trong một list đã được sắp xếp. Hàm sẽ trả lại chỉ số của phần tử được tìm thấy trong list.

# import math
# def bin_search(li, element):
#     bottom = 0
#     top = len(li)-1
#     index = -1
#     while top>=bottom and index==-1:
#         mid = int(math.floor((top+bottom)/2.0))
#         if li[mid]==element:
#             index = mid
#         elif li[mid]>element:
#             top = mid-1
#         else:
#             bottom = mid+1
#     return index
# li=[2,5,7,9,11,17,222]
# print (bin_search(li,11))
# print (bin_search(li,12))

# 70 : Tạo một số thập phân ngẫu nhiên, có giá trị nằm trong khoảng từ 10 đến 100 bằng cách sử dụng module math của Python.
# import random
# print (random.random()*100)

# 71 : Tạo một số thập phân ngẫu nhiên, có giá trị nằm trong khoảng 5 đến 95, sử dụng module math của Python.
# import random
# print (random.random()*100-5)

#72 : Viết chương trình xuất ra một số chẵn ngẫu nhiên trong khoảng 0 đến 10 (bao gồm cả 0 và 10), sử dụng module random và list comprehension.
# import random
# print (random.choice([i for i in range(11) if i%2==0]))

# 73 : Vui lòng viết chương trình để xuất một số ngẫu nhiên, chia hết cho 5 và 7, từ 0 đến 200 (gồm cả 0 và 200), sử dụng module random và list comprehension.
# import random
# print (random.choice([i for i in range(201) if i%5==0 and i%7==0]))

# 74 : Vui lòng viết chương trình để tạo một list với 5 số ngẫu nhiên từ 100 đến 200.
# import random
# print (random.sample(range(100,201), 5))

# 75 : Viết chương trình tạo ngẫu nhiên list gồm 5 số chẵn nằm trong đoạn [100;200].
# import random
# print (random.sample([i for i in range(100,201) if i%2==0], 5))

# 76 : Viết chương trình để tạo ngẫu nhiên một list gồm 5 số, chia hết cho 5 và 7, nằm trong đoạn [1;1000].
# import random
# print (random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))

# 77 : Viết chương trình để in một số nguyên ngẫu nhiên từ 7 đến 15.
# import random
# print (random.randrange(7,16))

# 78 : Viết chương trình để nén và giải nén string ""hello world!hello world!hello world!hello world!".
# Sử dụng zlib.compress() và zlib.decompress() để nén và giải nén string.

# import zlib
# s = "hello world!hello world!hello world!hello world!"
# t = zlib.compress(s)
# print t
# print zlib.decompress(t)

#or

#import zlib
# s = "hello world!hello world!hello world!hello world!"
# t = zlib.compress(s.encode("utf-8"))
# print (t)
# print (zlib.decompress(t))

# 79 : Bạn hãy viết một chương trình để in thời gian thực thi (running time of execution) phép tính "1+1" 100 lần.
# Sử dụng timeit() để đo thời gian chạy

# from timeit import Timer
# t = Timer("for i in range(100):1+1")
# print (t.timeit())

# 80 : Viết chương trình để trộn và in list [3,6,7,8]. Sử dụng shuffle() để trộn list.
# from random import shuffle
# li = [3,6,7,8]
# shuffle(li)
# print (li)

# 81 : Viết một chương trình để tạo tất cả các câu có chủ ngữ nằm trong ["Anh","Em"], động từ nằm trong ["Chơi","Yêu"] và tân ngữ là ["Bóng đá","Xếp hình"].
# Sử dụng list[index] để lấy phần tử từ list.

# chu_ngu=["Anh","Em"]
# dong_tu=["Chơi","Yêu"]
# tan_ngu=["Bóng đá","Xếp hình"]
# # Code by Quantrimang.com
# for i in range(len(chu_ngu)):
#     for j in range(len(dong_tu)):
#         for k in range(len(tan_ngu)):
#             cau = "%s %s %s." % (chu_ngu[i], dong_tu[j], tan_ngu[k])
#             print (cau)

# 82 : Viết chương trình in list sau khi xóa các số chẵn trong [5,6,77,45,22,12,24].

# li = [5,6,77,45,22,12,24]
# li = [x for x in li if x%2!=0]
# print (li)

# 83 : Sử dụng list comprehension để viết chương trình in list sau khi đã loại bỏ các số chia hết cho 5 và 7 trong [12,24,35,70,88,120,155].
# li = [12,24,35,70,88,120,155]
# li = [i for i in li if i%5!=0 or i%7!=0]
# print (li)

# 84 : Viết chương trình in list sau khi đã xóa số thứ 0, thứ 2, thứ 4, thứ 6 trong [12,24,35,70,88,120,155].
# Sử dụng list comprehension để xóa một loạt phần tử trong list.
# Sử dụng hàm enumerate() để lấy index, value của tuple.

# li = [12,24,35,70,88,120,155]
# a= [x for i,x in enumerate(li)if i%2!=0]
# print (a)

# 85 : Viết chương trình tạo mảng 3D 3*5*8 có mỗi phần tử là 0. Sử dụng list comprehension để tạo mảng.
# array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
# print (array)

# 86 : Viết chương trình in list sau khi đã xóa số ở vị trí thứ 0, thứ 5, thứ 5 trong [12,24,35,70,88,120,155].
# li = [12,24,35,70,88,120,155]
# li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
# print (li)

# 87 : Viết chương trình in list sau khi đã xóa giá trị 24 trong [12,24,35,24,88,120,155].
# li = [12,24,35,24,88,120,155]
# li = [x for x in li if x!=24]
# print (li)

# 88 : Với 2 list cho trước: [1,3,6,78,35,55] và [12,24,35,24,88,120,155], viết chương trình để tạo list có phần tử là giao của 2 list đã cho.
# Sử dụng set() và "&=" để thiết lập điểm giao.

# list1=set([12,3,6,78,35,55,120])
# list2=set([12,24,35,24,88,120,155])
# list1 &= list2
# li=list(list1)
# print (li)

# 89 : Viết chương trình in list từ list [12,24,35,24,88,120,155,88,120,155], sau khi đã xóa hết các giá trị trùng nhau. Sử dụng set() để lưu trữ các giá trị không bị trùng lặp.

# def xoaTrung( li ):
#     list_moi=[]
#     xem = set()
#     for i in li:
#         if i not in xem:
#             xem.add( i )
#             list_moi.append(i)
#     return list_moi
#
# li=[12,12,15,24,35,35,24,88,120,155,88,120,155]
# print ("List sau khi xóa giá trị trùng là:",xoaTrung(li))

# 90 : Định nghĩa class Nguoi và 2 class con của nó: Nam, Nu. Tất cả các class có method "getGender" có thể in "Nam" cho class Nam và "Nữ" cho class Nu.
# Sử dụng Subclass(Parentclass) để định nghĩa 1 class con.

# class Nguoi(object):
#     def getGender(self):
#         return "Unknown"
# class Nam(Nguoi):
#     def getGender(self):
#         return "Nam"
# class Nu(Nguoi):
#     def getGender(self):
#         return "Nữ"
# aNam = Nam()
# aNu= Nu()
# print (aNam.getGender())
# print (aNu.getGender())

# 91 : Viết chương trình đếm và in số ký tự của chuỗi do người dùng nhập vào.
#
# Ví dụ:
#
# Nếu chuỗi nhập vào là quantrimang.com thì đầu ra sẽ là:
#
# q,1
# u,1
# a,2
# n,2
# t,1
# r,1
# i,1
# m,2
# g,1
# .,1
# c,1
# o,1

# Sử dụng dict để lưu trữ các cặp key/value.
# Sử dụng dict.get() để tra cứu key với giá trị mặc định.

# dic = {}
# chuoi=input("Nhập chuỗi cần đếm ký tự: ")
# # Code by Quantrimang.com
# for c in chuoi:
#     dic[c] = dic.get(c,0)+1
# print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))

# 92 : Viết chương trình nhận chuỗi đầu vào từ giao diện điều khiển và in nó theo thứ tự ngược lại.
# Ví dụ nếu chuỗi nhập vào là:
# i love you
# Thì kết quả đầu ra là:
# uoy evol i

# chuoi=input("Nhập chuỗi vào đây: ")
# chuoi = chuoi[::-1]
# print (chuoi)

# 93 : Viết chương trình nhận chuỗi do người dùng nhập vào và in các ký tự có chỉ số chẵn.
# Ví dụ: Nếu chuỗi sau được nhập vào: q1u2a3n4t5r6i7m8a9n4g5.6c7o8m, thì đầu ra sẽ là: quantrimang.com. Sử dụng list[::2] để lặp list cách 2 vị trí.

# chuoi=input("Nhập chuỗi vào đây: ")
# chuoi = chuoi[::2]
# print (chuoi)

# 94 : Viết chương trình in tất cả các hoán vị của [1,2,3]. Sử dụng itertools.permutations() để lấy hết các hoán vị của list.
# import itertools
# print (list(itertools.permutations([1,2,3])))

# 95 : Viết chương trình để giải 1 câu đố cổ của Trung Quốc: Một trang trại thỏ và gà có 35 đầu, 94 chân, hỏi số thỏ và gà là bao nhiêu?

# def giai(dau,chan):
#     klg='Không có dáp án phù hợp!'
#     for i in range(dau+1):
#         j=dau-i
#         if 2*i+4*j==chan:
#             return i,j
#     return klg,klg
# dau=35
# chan=94
# dap_an=giai(dau,chan)
# print (dap_an)