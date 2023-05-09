from numpy import array
from scipy.linalg import lu,qr,svd
def task(count):
    print("*********TASK {}***********".format(count))


task(1)

# define a square matrix
A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
# LU decomposition
P, L, U = lu(A)
print(P)
print(L)
print(U)
# reconstruct
B = P.dot(L).dot(U)
print(B)

task(2)
print("qr decomposition")
Q,R=qr(A)
print(Q)
print(R)

task(3)
print("SVD")
U, s, V = svd(A)
print(U)
print(s)
print(V)

task(4)
print("applications of SVD:\n"
      "1. Used in google search\n"
      "2. Solves least squared problem\n"
      "3. Image Compression\n"
      "4. Classifications of hand-written digits\n"
      "5. Recommendation Systems\n")