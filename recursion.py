# non tail recursion 
# direct recusrion

# find the factorial of n numbers
def fact(n):
    if n <= 1:
        return n
    return n * fact(n-1)

# find the sum of n natural numbers
def sum_natural(n):
    if n <= 1:
        return n

    return n + sum_natural(n-1)

# indirect recusion
# find the sum of n natural numbers
def sum_one(n):
    if n <= 1:
        return n

    return n + sum_two(n-1)

def sum_two(n):
    if n <= 1:
        return n
    
    return n + sum_one(n-1)

# print n numbers using direct recursion
def print_num(n):
    if n <= 0:
        return n
    print(n)
    print_num(n-1)
    print(n)


# def pyramid(n, i=1):
#     if i >= n:
#         return i
    
#     print(" * " * i)
#     return pyramid(n, i+1)





if __name__ == "__main__":
    input_val = int(input("Enter the value :"))
    # print("the factorial of ",input_val," is :" ,fact(input_val))
    # print("the sum of ",input_val," natural number is :" ,sum_natural(input_val))
    # print("the sum of ",input_val," natural number(s) are :" ,sum_one(input_val))
    # print("pyramid is" ,pyramid(input_val))
    print(print_num(input_val))