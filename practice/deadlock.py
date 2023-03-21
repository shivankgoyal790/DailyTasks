import threading
from threading import Lock

f1 = open("file1.txt" , "w")
f2 = open("file2.txt" , "w")

lock1 = Lock()
lock2 = Lock()

def thread1():
    lock1.acquire()
    f1.write("hi")
    lock2.acquire()
    f2.write("bye")
    lock2.release()
    lock1.release()

def thread2():
    lock2.acquire()
    f2.write("hi")
    lock1.acquire()
    f1.write("bye")
    lock1.release()
    lock2.release()

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t1.start()
t2.start()

# from threading import Lock
# f1 = open("file1.txt" , "w")
# lock = Lock()
# lock.acquire()
# f1.write("shivank")
# f1.close()

# f2 = open("file2.txt" , "w")
# f2.write("samarth")
# f2.close()


# f3 = open("file3.txt" , "w")
# f3.write("adarsh")
# f3.close()

# # with open("file1.txt",'r+') as myfile:
# #     myfile.seek(6)
# #     myfile.write("h")
# #     myfile.seek(0)
# #     print(myfile.read())


# def createdeadlock2():   
#     f1 = open("file1.txt",'r')
#     print(f1.read())
#     lock.acquire()
#     createdeadlock1()

# def createdeadlock1():
#     f1 = open("file1.txt",'w')
#     f1.write("hi there")

# # def createdeadlock3():
# #    f1 = open("file1.txt",'w')
# #    f1.write('w')


# createdeadlock2()
# # asyncio.run(createdeadlock3()).sleep
# # asyncio.run(createdeadlock1())
# # asyncio.run(createdeadlock2())


