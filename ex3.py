"""

De bai: Tim so nguyen to thu k voi k nhap tu ban phim.

"""

print("Chuong trinh tim so nguyen to thu k")
try:
    k = int(input("Ban can tim so nguyen to thu bao nhieu? "))
except:
    print("Nhap so nguyen thu K, Ban vui long kiem tra lai dinh dang")
#Ham try/except de kiem tra xem gia tri k nhap vao co phai gia tri so hay ko?
#Neu no la so thuc thi ham int() tu dong ep kieu de no thanh so nguyen
#Con thieu sot la chua kiem tra dieu kien k duong hay am.

n=0
m=1
while(n<k):
        if k==1:
            n=1
        while(m>0):
            for i in range(2,int(m/2+1)):
                if(m%i)==0:
                    break
            else:
                n+=1

            if n>k :
                print("so nguyen to thu %s la %s" %(k,m))
                break
            m+=1

