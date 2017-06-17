"""
De bai: In ra tat ca cac so nguyen to trong pham vi nhap vao

"""

print("Chuong trinh liet ke cac so nguyen to trong pham vi tu 0 den : ")
n=int(input())
d=0
for i in range(1,n):
    if i<=2 :
        print("so %s la so nguyen to. " %i)
        d+=1
    else:
        for j in range(2,int(i/2+1)):
            if i%j==0 :
                break
        else:
            print("so %s la so nguyen to. "%i)
            d+=1
print("co tat ca %s so nguyen to trong pham vi tu 0 den %s" %(d,n))