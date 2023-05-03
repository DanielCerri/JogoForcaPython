desenhoForca = ['''
+---+
|   |
    |
    |
    |
    |
=========''','''

+---+
|   |
O   |
    |
    |
    |
=========''','''

+---+
|   |
O   |
|   |
    |
    |
=========''','''

+---+
|   |
O   |
/|   |
    |
    |
=========''','''

+---+
|   |
O   |
/|\  |
    |
    |
=========''','''

+---+
|   |
O   |
/|\  |
/    |
    |
=========''','''

+---+
|   |
O   |
/|\  |
/ \  |
    |
=========''']

letra=''
palavra_desenho=''  
palavra=""
contador=0
ganhou=False

def PalavraForca():
    global palavra,palavra_desenho
   
    palavra=list(input('Digite a Palavra da forca: '))
    palavra_desenho=['_']*len(palavra)

def Forca():
    global contador,ganhou,palavra_desenho
    while contador<7:
        
        print(desenhoForca[contador])
        letra=input('Digite uma letra:')
        for l in palavra:
            if l==letra:
                palavra_desenho[palavra.index(letra)]=letra
        ganhou = False if '_' in palavra_desenho else True
        if(ganhou): 
            print('Parabens Voce Ganhou!')   
            print(palavra_desenho)
            break  
                  
        print(palavra_desenho)
        contador=contador+1
        
    if(ganhou is False): 
        print('Voce perdeu!')  
        print(palavra)

PalavraForca()         
Forca()    
   

