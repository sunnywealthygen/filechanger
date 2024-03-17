file1 = open('thepower.txt', 'r')
Lines = file1.readlines()
count=0
k=''
for line in Lines:
  k=line

file1 = open('thepower.txt', 'w')
file1.write(str(int(k)+1))
file1.close()
