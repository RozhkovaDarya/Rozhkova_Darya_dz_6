with open('bakery.csv', 'a', encoding='utf-8') as file:
  file.write('50,2\n')

print(open('bakery.csv').read())


with open('bakery.csv') as file:
    lines = file.readlines()
lines = ''.join(lines[1:3])
print(lines)

print('\n')
#########
import sys

sale = input()
original_stdout = sys.stdout 

with open('bakery.csv', 'a', encoding='utf-8') as f:
    sys.stdout = f 
    print(sale)
    sys.stdout = original_stdout