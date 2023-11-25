if 3 > 2:
 print('funciona')

if 5>2:
 print('5 é maior que 2')
else:
 print('5 não é maior que 2') 

name = 'Sonja'
if name == 'Ola':
  print('Olá Ola!')
elif name == "Sonja":
  print('Olá Sonja!')
else:
  print('Olá estranho!') 

volume = 57
if volume < 20:
  print("Esta um pouco baixo")
elif 20 <= volume < 40:
  print('Está bom para musica ambiente')

elif 40 <= volume < 60: 
    print("Perfeito, posso ouvir todos os detalhes")
elif 60 <= volume < 80: 
    print("Ótimo para festas!")
elif 80 <= volume < 100: 
    print("Está muito alto!")
else: 
    print("Meus ouvidos doem! :(")  
def hi():
  print('Ola!')
  print('Tudo bem?')  

hi()

def hi(name):
    if name == 'Ola':
        print('Olá Ola!')
    elif name == 'Sonja':
        print('Olá Sonja!')
    else:
        print('Olá estranho!')

hi('Ola')

def hi(name):
    print('Olá ' + name + '!')

hi("Rachel")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'você']

for name in girls:
   hi(name)
   print('Proxima')

for i in range(1, 6):
    print(i)   