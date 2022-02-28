char = input('Inserisci un carattere: ')
num = int(input('Inserisci un intero: '))

if num > 0 :
    print('L\'intero inserito è maggiore di 0')
else:
    num = int(input('Inserisci un intero maggiore di 0: '))
    
for i in range(num):
    print(char * num)
