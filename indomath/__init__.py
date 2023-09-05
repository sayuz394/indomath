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