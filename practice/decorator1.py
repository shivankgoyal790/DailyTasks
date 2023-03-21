# import random 


# def mygen(low,high,n):
#     for x in range(n):
#         yield random.randint(low,high)
# for x in mygen(1,10,3):
#     print(x)

# def new_decorator(original_func):
#     def func():
#         print("before original function")
#         original_func();
#         print("after original function")
#     return func

# # if i want to decorator

# # method 1
# # function1(originalfunc)

# # #method 2

# @new_decorator
# def originalfunc():
#     print("adarsh")

# originalfunc()

# print(range(0,10))



# def cubes(n):
#     for x in range(n):
#         yield x*x*x

# for x in cubes(10):
#     print(x);