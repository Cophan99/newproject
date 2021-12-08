def xuLyChuoi():
    items = [x for x in input('Nhap vao mot chuoi').split(',')]
    print('truoc khi sap xep \r\n')
    for a in items:
        print(a)
    items.sort()
    print('sau khi sap xep \r\n')
    for a in items:
        print(a)
    print(','.join(items))

if __name__=="__main__":
    xuLyChuoi()
