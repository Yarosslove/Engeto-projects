print("everything everything")
print("okay!")



#from typing import Any

print('Welcome in Text Analyzer')
print('=' * 40)
print ('Author: Jaroslav Prejza')
print('=' * 40)
credentials = {'bob': '123','ann': 'pass123','mike': 'password123','liz': 'pass123'}

username = input('Please enter username: ')
print()
password = input('Please enter password: ')
print()
print('=' * 40)

if username not in credentials:
    print('No user found')
    exit()
elif credentials[username] != password:
    print('Permission denied')
    exit()
else:
    print('Permission allowed ')
    print()
print('OUR TEXTS:') #????


text_1 = ('''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''')


text_2 = ('''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''')

text_3 = ('''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''')


choice = int(input('We have 3 texts to analyze, please choose 1, 2 or 3: '))
print()

if choice not numeric:
    print('Only numbers please')   
elif choice not in ('1','2','3'):
    print('No such number')
else:
    choice = int(choice)

print()

print('statistics:')
print()

if choice is 1:
    text = text_1
    print(text_1)
elif choice is 2:
    text = text_2
    print(text_2)
elif choice is 3:
    text = text_3
    print(text_3)
else:
    print ('Invalid choice')

word_list = text
word_list = word_list.split()



#word_list.split()

# capitals
capitals = 0
uppers = 0
lowers = 0       
numerics = 0              
i = 0
       
for i in word_list:
    if i in word_list.istitle():
        capitals += 1
    if i in word_list.isupper():
        uppers += 1
    if i in word_list.islower():
        lowers += 1
    if i in word_list.isnumeric():
        numerics += 1
       


#SUM!!!!
digits = word_list.isnumeric()
digits = sum(str(digits))


print ('There are ' + str(capitals) + ' capitals, 
print ('There are ' + str(uppers) + ' uppercases, ' 
print ('There are ' + str(lowers) + ' lowercases, ' 
print ('There are ' + str(numerics) + ' numbers' 
#print ('Sum of digits is ' + int(digits))

print()
print('=' * 40)
print()

print('1' + ' - ' + str(capitals) + capitals * ' *' )
print('2' + ' - ' + str(uppers) + uppers * ' *' )
print('3' + ' - ' + str(lowers) + lowers * ' *' )
print('4' + ' - ' + str(numerics) + numerics * ' *' )

