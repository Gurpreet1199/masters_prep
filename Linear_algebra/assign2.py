from numpy import array
from numpy.linalg import inv
def task(count):
    print("*********TASK {}***********".format(count))


task(1)
A= array([[1,2,3],[4,5,6]])
print(A)

task(2)
A= array([[1,2,3],[4,5,6]])
B= array([[4,5,6],[1,2,3]])
C= A+B
print(C)

task(3)
A = array([[1, 2], [3, 4], [5, 6]])
print(A)
B = array([[1, 2], [3, 4]])
print(B)
C = A.dot(B)
print(C)

task(4)
print("A/B is not possible but A*Binv may be possible if Binv exists Adj(B)/Det(B)\n"
      "Adj(B) = [Minor(B)].T")

task(5)
print("Transpose")
print(A.T)

task(6)
A=[[1,2],[3,4]]
B=inv(A)
print(A)
print(B)

task(7)
print("Square Matrix - [A]nxn\n"
      "Symetric Matrix is a swaure matrix - Aij=Aji\n"
      "Triangular Matrix is a square matrix - Aij==0 j<i (upper Triangular) and vice-versa for Lower Triangular\n"
      "Diagonal is sqaure mat where Aij=0 if i!=j else Aij!=0\n")





