myfile = open("myfile.txt");
print(myfile.read())
print(myfile.read())
myfile.seek(0)
print(myfile.read())
print(myfile.readlines())  # grab a list where each element replresent a line


# another method


with open('myfile.txt') as myfile:
    contents = myfile.read()

print(contents,"\n")

#modes
#r read only
#r+ read and write
#w+ write + read  but overwrites   

#a append
with open('myfile.txt',mode='a') as myfile:
    myfile.write(" bye")

with open('myfile.txt') as myfile:
    contents1 = myfile.read()

print(contents1,"\n")


#w write only (overwrites)
# with open('myfile.txt',mode='w') as myfile:
#     myfile.write("bye")


# with open('myfile.txt') as myfile:
#     contents2 = myfile.read()

# print(contents2,"\n")



# read + write
with open('myfile.txt',mode='r+') as myfile:
    myfile.read()
    myfile.write(" sam")
   
with open('myfile.txt') as myfile:
    contents2 = myfile.read()

print(contents2,"\n")  
 