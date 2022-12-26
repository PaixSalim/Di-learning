phrase=input('Entrer un mots de 10 caractères : ')
i=len(phrase)
if i < 10 :
    print('chaîne pas assez longue')
elif i >10:
    print('chaîne trop longue')

print('le premier caractère est :',phrase[0], ' le dernier est ',phrase[i-1])
word=""
for j in phrase:
    word=word+j
    print(word) 
  
    

    

   
    
 
