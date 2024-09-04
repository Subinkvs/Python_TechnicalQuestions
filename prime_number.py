# def find_primenumber(num):
#     for i in range(2, (num//2)+ 1):
#         if num % i != 0:
#             print("Prime number")
#             break
#     else:
#         print("Not a Prime number")

# num = 5
# find_primenumber(num)

# def is_prime(num):
    
#     for i in range(2, (num//2) + 1):
#         if num % i == 0:
#             return False
#     return True

# def filter_primenumber(lst):
    
#     return set([j for j in lst if is_prime(j)])

# lst = [1, 3, 5, 6, 7, 8, 9, 3, 5]
# print(filter_primenumber(lst))


def is_prime(num): 
    if num <= 1:
        return False
    
    for i in range(2, (num//2) + 1):
        if num % i == 0:
            return False
    return True

def replace_primenumber(lst):
    for index, value in enumerate(lst):
        if is_prime(value):
            lst[index] = 0
    return lst
            
lst = [1, 3, 5, 6, 8, 9]
print(replace_primenumber(lst))