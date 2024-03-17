file1 = open('thepower.txt', 'r')
Lines = file1.readlines()
count=0
k=''
for line in Lines:
  k=line
file1.close()
print(k)
k=str(int(k)+1)
file2 = open('thepower.txt', 'w')
file2.write(k)
print('version 5')
print(k)
file2.close()
file2.write(k)

with open('thepower.txt', 'w') as file_obj:
    file_obj.write("I love programming!\n")
    file_obj.write("I love Python!\n")
file_obj.close()
with open('thepower.txt', 'r') as file_obj:
    print(file_obj.readlines())
file_obj.close()
with open('thepower.txt', 'r') as file_obj:
    print(file_obj.readlines())
file_obj.close()

