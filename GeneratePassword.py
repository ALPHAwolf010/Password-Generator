import random
alpha=['a','b','c','d','e','f','g','h','i','j','k',
     'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
     'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
     'P','Q','R','S','T','U','V','W','X','Y','Z'];
num=['0','1','2','3','4','5','6','7','8','9'];
special=['!','@','#','$','%','^','&','*'];     

alphab=int(input("No of Alphabet in PassWord : "));
num1=int(input('No of Number in PassWord : '));
spec=int(input("No of Special Characters in PassWord : "));

passWord=[];
for i in range(0,alphab):
    passWord.append(random.choice(alpha));

for i in range(0,num1):
    passWord.append(random.choice(num));
for i in range(0,spec):
    passWord.append(random.choice(special));

# for i in range (0,len(passWord)):
    random.shuffle(passWord);
# passWord=str(passWord);
pass1 ="";
for i in passWord:
   pass1+=i;
print("Your PassWord is Generated : "+pass1);    





