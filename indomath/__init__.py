
phi = 22/7

def kali(*args):
    result = 1
    for i in args:
        result *= i
    print(result)
def tambah(*args):
    result = 0
    for i in args:
        result += i
    print(result)
def bagi(*args):
    if not args:
        print("No arguments provided. Division result undefined.")
        return None
    
    result = args[0]  
    for i in args[1:]:  
        result /= i
    print(result)
def akar(a):
    print(pow(a ,1/2))
def kurang(*args):
    result = 0
    for i in args:
        result -= i
    print(result)
def pangkat(a,b):
    z = pow(a,b)
    print(z)
def terbesar(*args):
    print(max(args))
def terkecil(*args):
    print(min(args))
# geometri
def luas_segitiga(a,t):
    result = 1/2 * a * t
    print(result)
def keliling_segitiga(a,b,c):
    print(a+b+c)
def luas_persegi_panjang(p,l):
    result = p * l 
    print(result)
def keliling_persegi_panjang(p,l):
    print(2 * (p+l))
def luas_persegi(a):
    print(a * a)
def keliling_persegi(s):
    print(4 * s)
def luas_jajar_genjang(a,t):
    print(a * t)
def keliling_jajar_genjang(a,b,c,d):
    print(a + b + c + d)
def luas_lingkaran(r):
    print(phi * r * r)
def keliling_lingkaran(r,d):
    print(2*phi*r)
def keliling_trapesium(a,b,c,d):
    print(a + b + c + d)
def luas_trapesium(a,b,t):
    print(1/2 * (a+b) * t)
def luas_layang(x,y):
    print(1/2*x*y)
def keliling_layang(a,b,c,d):
    print(a + b + c + d)
def luas_belah_ketupat(x,y):
    print(1/2 * x * y)
def keliling_belah_ketupat(a,b,c,d):
    print(a + b + c + d)

def pitagoras(a,b):
    d = pow(a,2) + pow(b,2)
    c = pow(d,1/2)
    print(c)
# matriks

def matriks2x2_kali(a,b,c,d,e,f,g,h):
    h1 = a * e + c * f
    h2 = b * e + d * f
    h3 =  a * g + a * h
    h4 = b * g  + d * h
    print(h1,h3)
    print(h2,h4)
def matriks2x2_tambah(a,b,c,d,e,f,g,h):
    print(a + e,c + g)
    print(b + d,d + h)
def matriks2x2_kurang(a,b,c,d,e,f,g,h):
    print(a - e,c - g)
    print(b - d,d - h)
def matriks2x2_skalar(a,b,c,d,nilai):
    print(nilai * a,nilai * c)
    print(nilai * b,nilai * c)
def matriks2x2_adjoint(a,b,c,d):
    print(d,c * -1)
    print(b * -1,a)
def matriks2x2_determinan(a,b,c,d):
    print(a * d - b * c)
