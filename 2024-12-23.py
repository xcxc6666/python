# def factorial(x):
#     ans = 1
#     for i in range(1, x + 1):
#         ans *= i
#     return ans    
# ans = 0
# for i in range(1, 11):
#     ans += factorial(i)
# print(ans)    


# def gcd(a,b):
#     c = min(a,b)
#     for i in range(c,0,-1):
#         if a%i==0 and b%i==0:
#             return i
# ans = gcd(7,21)
# print(ans)        



# def lcm(a,b):
#     c = max(a,b)
#     while True:
#         if c%a==0 and c%b==0:
#             return c
#         c+=1

# ans = lcm(9,6)
# print(ans)



# def is_prime(x):
#     if x<2:
#         return False
#     for i in range(2,x):
#         if x%i==0:
#             return False
#     return True
# print(is_prime(6))


# def Area(a,b,c):
#     if a+b>c and a+c>b and b+c>a:
#         s = (a+b+c)/2
#         area = (s*(s-a)*(s-b)*(s-c))**0.5
#         return area
#     else:
#         return "Invalid Triangle"
# print(Area(3,5,9))    


import math
print(math.pi)
