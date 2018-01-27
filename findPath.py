def findPath(listA):
   i = j = 0 
   pCol = None #previous column

   for row in range(i, len(listA)-1):
      for col in range(j, len(listA[row])):
         col = checkVert(row, row+1, listA)
         #check row 0 and 1 
         if(col >= 0 and row == 0):
            pCol = col
            break
         elif(col == -1 and row == 0):
            return False 
         #check remaining rows
         elif(col >= 0 and checkHoriz(row, col, pCol, listA)):
            pCol = col
            break
         else:
            return False
   return True

def checkVert(row, nextRow, listA):
   for i in range(0, len(listA[row])):
      if(listA[row][i] == 1 and listA[nextRow][i] == 1):
         return i
   return -1 
      

def checkHoriz(row, col, prevCol, listA):
   if(col > prevCol):
      start = prevCol
      end = col + 1
   else:
      start = col
      end = prevCol + 1

   for i in range(start, end): 
      if (listA[row][i] == 0):
         return False
   return True

#no path
listA = [[1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1], 
         [0, 1, 0, 0, 1], 
         [1, 1, 1, 0, 1], #breaks here 
         [0, 0, 0, 1, 1]]
#path
listB = [[1, 0, 0, 0, 0],
         [1, 1, 0, 0, 0], 
         [0, 1, 1, 0, 0], 
         [1, 0, 1, 1, 1], 
         [0, 0, 0, 0, 1]]

#horz TEST
print("expect: True; value: %s" % checkHoriz(1, 0, 1, listB))
print("expect: True; value: %s" % checkHoriz(1, 1, 0, listB))
print("expect: True; value: %s" % checkHoriz(1, 0, 0, listB))
print("expect: False; value: %s" % checkHoriz(4, 0, 3, listB))


#vert TEST
print("expect: 0; value: %s" % checkVert(1, 0, listA))
print("expect: -1; value: %s" % checkVert(2, 0, listA))

#find
print("expect: False; value: %s" % findPath(listA)); 
print("expect: True; value; %s" % findPath(listB));
