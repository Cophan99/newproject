def toantubangoi():
    try:
        a = int(input('nhap a= '))
        b = int(input('nhap b= '))
        c = int(input('nhap c= '))
        
        if a>b and a>c:
            print('max=' + str(a))
        elif a>b and a<c:
            print('min=' + str(b))
    except:
        print('loi du lieu')
    

    
if __name__ == "__main__":
    toantubangoi()

