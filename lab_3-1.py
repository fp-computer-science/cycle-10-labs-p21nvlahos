# Author: NV 12/7/2020

'''
def sum_to(n):
    total = 0
    for i in range(n+1):
        total += i
        return total
        
num = input("Enter an integer: ")

result = sum_to(int(num))
print(result)
'''

def sum_to(n):
    total = 0
    iteration = 1
    while iteration < n+1:
        total += iteration
        iteration += 1
    return total

num = input("Enter an integer: ")

result = sum_to(int(num))
print(result)