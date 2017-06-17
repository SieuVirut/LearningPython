"""
De bai: Nhap ten, tuoi cua 2 nguoi dang yeu nhau, xem ho co hop nhau hay ko?

"""

#!/usr/bin/python3

print("Day la chuong trinh du doan xem 2 nguoi co hop nhau ko ")



a=input("Nhap ten nguoi yeu cua ban ")
b=int(input("Nam sinh cua %s " %a))
c=input("Con ten cua ban la :")
d=int(input("%s sinh nam nao ?" %c))

print("Sau day la thong tin ban nhap vao:")
print("Ten cua nguoi ay la %s va %s sinh nam %d " %(a,a,b))
print("Ten cua ban la %s va %s sinh nam %r" %(c,c,d))
print("Con day la ket qua cua chuong trinh du doan")

if (b-d)%4==0 : #tinh theo tam hop
    print("Tuoi cua 2 ban la tam hop !")
    if (b-d)**2>64 : #tuong duong tri tuyet doi <8,chenh nhau ko qua 8 tuoi
        print("Nhung 2 ban phu hop lam bo va con hon :p. ")
    else:
        print("%s a.Troi sinh 1 cap %s va %s roi. 2 ban that qua hop nhau  ." %(c,c,a))
    print("Ban thay co dung ko? ")
else:
    print("%s a. That su thi 2 ban ko hop nhau lam dau.Nhung dung buon nhe." %c)

