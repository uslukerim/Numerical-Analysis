import math

def seriform(a):                     #Bu fonksiyon ile seri formulü tanımlanmıştır
    liste=[]
    for i in range(0,a+1):
        islem=(math.pow(-1,i)/(1+i))
        liste+=[islem]
    #print(liste)
    return islem
#************************************************************************************
def delta():        #Bu fonksiyon Euler Transformasyonu Yöntemi
    d1=[]           #   ile kalanı bulmak için oluşturulmuştur
    d2=[]
    d3=[]
    d4=[]
    ist=15
    k=4
    for j in range(10,ist):
        fark=abs(seriform(j))- abs(seriform(j+1))
        d1+=[-round(fark,6)]
    for j in range(0,k) :
        fark=d1[j]-d1[j+1]
        d2+=[-round(fark,6)]
    for j in range(0,k-1):
        fark=d2[j]-d2[j+1]
        d3+=[-round(fark,6)]
    for j in range(0,k-2):
        fark=d3[j]-d3[j+1]
        d4+=[-round(fark,6)]
    R=(1/2)*seriform(10)-(1/4)*d1[0]+(1/8)*d2[0]-(1/16)*d3[0]+(1/32)*d4[0]
    return round(R,6)
#***************************************************************************************
def S(b):   #Bu fonksiyon Serinin ilk b teriminin toplamını verir
    llist=[]
    for i in range(0,b):
        llist+=[seriform(i)]
    total=sum(llist)
    return total
#***************************************************************************************
def Tort():     #Bu fonksiyon Tekralanan Ortalamalar Yöntemi kullanlarak
    a1 = []     #serinin genel toplamı bulunur
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a6 = []
    for i in range(11,16):
        ort=(S(i)+S(i+1))/2
        a1+=[ort]
    for j in range(0,4):
        ort=(a1[j]+a1[j+1])/2
        a2+=[ort]
    for i in range(0,3):
        ort=(a2[i]+a2[i+1])/2
        a3+=[ort]
    for i in range(0, 2):
        ort = (a3[i] + a3[i + 1]) / 2
        a4 += [ort]
    for i in range(0, 1):
        ort = (a4[i] + a4[i + 1]) / 2
        a5 += [round(ort,6)]
    return a5[0]
#***************************************************************************************
def mainn():
    while True:
        print("\n\n\nLÜTFEN SEÇİMİNİZİ YAPINIZ\n"
              "1-->Tekralanan Ortalamalar Yöntemi kullanlarak genel ortalama hesabı\n"
              "2-->Euler Transformasyonu Yöntemi ile Kalanın bulunması ve genel Ortalamanın hasabı")
        a=int(input())
        if(a==1):
            print("Genel Ortalama:",Tort())
        elif(a==2):
            genelTop=delta()+S(10)
            print("Kalan:",delta(),"\nGenel Ortalama:",round(genelTop,6))

mainn()

