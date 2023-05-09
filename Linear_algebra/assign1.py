from numpy import array
def task(count):
    print("*********TASK {}***********".format(count))
def palindrome(s):
    return s==s[::-1]
def Npalindrome(n):
    tmp=n
    rev=0;
    while tmp!=0:
        rev=10*rev + tmp%10
        tmp=tmp//10
    return rev==n
task(1)
v = array([1, 2, 3])
print(v)

task(2)
a = array([1, 2, 3])
print(a)
b = array([1, 2, 3])
print(b)
c = a * b
print(c)

task(3)
print(a+b)
print(a-b)
print(a//b)

task(4)
print("vector can be of 1D,2D,3D .. it shows a direction ..it can be scaled ... \n"
      "eg : v = i+j+k is a 3d vector \n"
      "|v| = sqrt(3)\n")
print("scaler is a constant quantity and have no direction eg : 1, 2 etc ")

task(5)
s = "viviv"
print(palindrome(s))

task(6)
n=-1
print(Npalindrome(abs(n)))

task(7)
print("string is a consecutive sequence of characters eg: \"hello\" , \"gurpreet\ etc")