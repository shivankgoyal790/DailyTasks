
#strings
x = "hello world"
print("hello" + " world")
mystring = "abcdefgh"   #strings are immutable
print(mystring[-2:-1])
print(mystring[:])
print(mystring[::])
print(mystring[::-1])
print(mystring[1:5:2])  # for jumping the characters
print(mystring.upper())
print(x.split())
print("\n\n\n\n\n")



# string formatting 

print("{1} {2} {0}".format('shivank','name','is'))
y = 100/777
print("The result is {r:1.3f}".format(r=y),"\n")  # 1 is the width or the white space addded before result
print(f"The result is {y:2.3f}","\n")  # another method using format string literals
print('the result is %0.5f' %(y),"\n")
print("\n\n\n\n\n")


# lists 

mylist = ["sunday" , "monday" , "tuesday"];
mylist.append("wednesday");
print(mylist,"\n")
mylist.pop(1);
print(mylist,"\n")
newlist = [1,2,3,4,10,5,8,7]
newlist.sort()    # more methods are reverse
print("the sorted list is " , newlist,"\n")
print(' '.join(mylist))


# dictionaries


# when to use a dictionary ?
# Dictionary are unordered and cannot be sorted also dictionaries have key value pair so if you want to retrive the values quickly by not focussing on the indexes use dict
# cannot be indexed or sliced

mydict = {0:"sunday" , 1 : 'monday' ,2 : "tuesday"}
mydict[3] = "wednesday"
print(mydict,"\n")
print(mydict.values(),"\n")
print(mydict.items(),"\n")
print(mydict.keys(),"\n")



# tuples


#tuples are immutable 
#so tuples are useful when we work around oops and did not want items to be changed

t = (3,2,1)
print(t.count(1),"\n")
print(t.index(3),"\n")
print("\n\n\n\n")



#sets

myset = set()
myset.add(1)
myset.add(2)
myset.add(2)
print(myset,"\n")
mylist1 = [12,12,123,124]
print(set(mylist1),'\n')
print("\n\n\n\n")


#keyword agrs and args

def func(*args):
    print("my name is {}".format(args[1]))

func('shivank' , "goyal")



def myfunc(**kargs):
    print("my name is {} and hobby is {}".format(kargs['name'],kargs['hobby']))

myfunc(name="shivank",hobby="swimming")


