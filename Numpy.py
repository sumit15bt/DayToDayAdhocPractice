#!/usr/bin/python3
import numpy

print ("Enter the Matrix Row & Column")
matrix_row=int(input("No. of rows : "))
matrix_column=int(input("No. of columns : "))
matrix_element=int(input("Enter matrix element : "))
matrix=numpy.full((matrix_row,matrix_column),matrix_element)
print (matrix)
createfile=open('matrix.txt',mode ='a')
for item in matrix:
  createfile.write("%s\n" % item)
