#Làm việc với string
my_string = 'xin chao'
i =1
for x in my_string:
    print('Ky tu thu ' + str(i) + x)
    i+=1

my_string = 'xin chao'
print('Chieu dai cua chuoi la:' + str(len(my_string)))

txt = 'Chuoi ky tu A'
if 'A' in txt:
    print('Co A trong chuoi txt')

#Đầu vào 2 chuỗi: chuỗi 1, chuỗi 2
# Kiểm tra xem chuỗi 1 có nằm trong chuỗi 2 hay k
# gọi 

chuoi1 = input('Xin chao ban')
chuoi2 = input('xin chao')
if chuoi1 in chuoi2:
    print('ok')

#Đầu vào 2 chuỗi: chuỗi 1, chuỗi 2
# Kiểm tra xem chuỗi 1 có nằm trong chuỗi 2 hay k
chuoi1 = input('facebook')
chuoi2 = input('ok')
if chuoi1 not in chuoi2:
    print('Khong chua trong')
else:
    print('chua trong')

#thứ tự các ký tự
chuoi1 = 'xin chao cac ban'
print(chuoi1[-1])

#In hoa
a = 'Hello world'
print(a.upper())

#In thường
a = 'Hello world'
print(a.lower())



