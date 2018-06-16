import numpy
import  sys
import  os

'''os.system("touch data.txt")
a=input("enter  the matrix  in list form  ")
m1=np.array(a)
print(m1.shape())
print(m1)
#np.savetxt('data.txt',m1,delimiter=',')
#m2=np.genfromtxt('data.txt',)'''

print ("Enter the Matrix Row & Column")
row=int(input("No. of rows : "))
column=int(input("No. of columns : "))
element=int(input("Enter matrix element : "))
matrix=numpy.full((row,column),element)
file=open('matrix.txt',mode ='a')
for item in matrix:
	file.write("%s\n" % item)
file.close()
print("possible shapes  ")
x1=matrix.reshape(column,row)
print (x1)
print("File reading")
file=open('matrix.txt',mode ='r')
print(file.read())
file.close()

