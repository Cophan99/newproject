def xuatChuoi():
    string1 = "{} {} {}".format('Geeks','For','Life')
    print('Chuoi o thu tu mac dinh')
    print(string1)
    #chuoi o thu sap xep 
    string1 = "{1} {0} {2}".format('Geeks','For','Life')
    print('\n Chuoi o thu tu sap xep')
    print(string1)
    #sap theo tu khoa
    string1 = "{l} {f} {g}".format(g='Geeks',f='For',l='Life')
    print('\n Chuoi o thu tu sap xep theo ky tu')
    print(string1)
if __name__ == "__main__":
    xuatChuoi()
