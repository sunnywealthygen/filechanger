file1 = open('thepower.txt', 'r')
Lines = file1.readlines()
count=0
k=''
for line in Lines:
  k=line
print(k)
k=str(int(k)+1)
file2 = open('thepower.txt', 'w')
file2.write(k)
print('version 2')

with open('thepower.txt', 'w') as file_obj:
    file_obj.write("I love programming!\n")
    file_obj.write("I love Python!\n")
