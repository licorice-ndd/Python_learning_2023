# how to use str in py : str = represent for string byte convert int to string

# retake fall Hoalac 2022
# Q1
# an ordered number is a number in which the digits in the number appear in the ascending order. For example 12345 is an ordered number but 14235 is not.
# write a program that will accept an positive integeral number then print out "true" if the number is an ordered number, otherwise print out "false"
# if the user enters anything other than a positive integeral number put out an appropriate message and ignore the number. for example
# Enter an intergeral number : -1234
# please enter an positive intergeral number
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

file = input("Enter file: ")
f = open(file, "r")
line = f.readline()
print('The content of the file:',line)
A = line.split(' ')
list_null=[]
for i in A:
    list_null.append(int(i))
def Average(lst):
    return sum(lst) / len(lst)
average = Average(list_null)
print('Avg =',average)
                
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