with open('users2.csv') as fp1, open('hobby2.csv') as fp2:
  line1 = fp1.readlines()
  line2 = fp2.readlines()
  #print(line1, line2)
  
  users2_and_hobby2 = dict(zip(line1, line2))
  #print(users2_and_hobby2)

def users2_and_hobby2():
  i = 0
  j = 0
  while i < len(line2):
    if i >= len(line1):
      yield ('1')
      i += 1
      j += 1
      break
    else:
      yield (line1[j], line2[i])
      i += 1
      j += 1
    
for gen in users2_and_hobby2():
    print(gen)
