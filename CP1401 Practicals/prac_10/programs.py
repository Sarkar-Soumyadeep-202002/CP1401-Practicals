# # 1. Reading a string from a file
in_file=open('name.txt','r')
text=in_file.read().strip()
in_file.close()
print(text)

# 2. Write Numbers to a file

out_file=open('range.txt','w')
for number in range(0,101):
    if number%2!=0:
         print(number,file=out_file)
out_file.close()

out_file=open('range.txt','w')
for number in range(0,101,10):
     print(number,file=out_file)
out_file.close()

out_file=open('range.txt','w')
for number in range(20,0,-1):
    if number%2!=0:
         print(number,file=out_file)
out_file.close()

# # 3. Greater-Than Counter
file_name='recentrain.txt'
in_file=open(file_name,'r')
print(f'Filename: {file_name}')
threshold=float(input('Threshold: '))
count=0
number_of_elements=0
for line in in_file:
    number_of_elements+=1
    number=float(line)
    if number>threshold:
        count+=1
percentage=(count/number_of_elements)*100
print('Processing...')
print(f'{count} out of {number_of_elements} ({percentage}%) values in recentrain.txt are greater than {threshold}')













