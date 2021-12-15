def caulenhif():
    try:  
       a = int(input('nhap a= '))
       b = int(input('nhap b= '))

       if a==b:
           print("đúng")
       else: 
           print("sai") 
       print('hoan thanh')
    except:
        print('Loi nhap du lieu')


if __name__ == "__main__":
    caulenhif()
