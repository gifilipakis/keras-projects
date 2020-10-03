import random

with open('C:/Users/Giovanna/Documents/TCC/keras-projects/conteudos.csv', encoding="utf8") as myfile:
    conteudos = myfile.read().split('\n')
print(conteudos)
# classes=['Péssima','Ruim','Regular','Boa','Ótima']
classes=['Boa','Ruim']
for i in range(100):
    random.shuffle(conteudos)
    with open('C:/Users/Giovanna/Documents/TCC/keras-projects/dados-iniciais3.csv', "a") as myfile:
        myfile.write(classes[random.randint(0,2)]  + ",")
        for i in conteudos[:-1]:
            myfile.write(i + ',')
        myfile.write(conteudos[len(conteudos)-1] + "\n")
    myfile.close() 