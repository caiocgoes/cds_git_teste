import test

def sum(a, b):
    a = int(input("Numero 1:"))
    b = int(input("Numero 2:"))
    return a,b
def main():
    n1,n2 = sum()
    print(n1+n2)
def div():
    n1,n2 = sum()
    print(n1/n2)
def mult():
    n1,n2 = sum()
    print(n1*n2)
if __name__ == "__main__":
    main()
    