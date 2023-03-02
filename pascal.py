from math import factorial

def pascal(n):

    print()

    for i in range(n):

        for k in range(n-i+1):
            print(end="   ")

        for k in range(i+1):
            # nCk = n!/((n-k)!*k!)
            print(factorial(i)//(factorial(k)*factorial(i-k)), end="    ")

        print("\n")

if __name__ == '__main__':  

    n = input ("Please input a positive integer value for n ( > 0 ): ")
    try:
        val_n = int(n)
        if val_n > 0:
            print("Input is a positive integer ( > 0 ). Number = ", val_n)
            pascal(val_n)
        else:
            print("Please input a positive integer ( > 0 )")
    except ValueError:
        print()
        print("Please input a positive integer ( > 0 )")
        print()
    
    # if type(type_n is int)
