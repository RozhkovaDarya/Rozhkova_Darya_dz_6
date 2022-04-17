with open('users.csv') as fp1, open('hobby.csv') as fp2:
  line1 = fp1.readlines()
  line2 = fp2.readlines()
  #print(line1, line2)
  
  users_and_hobby = dict(zip(line1, line2))
  #print(users_and_hobby)

  
def users_and_hobby():
  i = 0
  j = 0
  while j < len(line1):
    if j >= len(line2):
      yield (line1[j], None)
      i += 1
      j += 1
      break
    else:
      yield (line1[j], line2[i])
      i += 1
      j += 1
    
for gen in users_and_hobby():
  print(gen)