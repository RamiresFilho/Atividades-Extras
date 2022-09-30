file = open('file.txt', 'r')
nome = file.readlines()
idade = file.readlines()
file.close()

nome.append(str(input("Digite seu nome: ")))
idade.append(int(input("Digite sua idade: "))) 

print('O nome digitado foi: ', nome, ',idade', idade, 'anos')

file = open('file.txt', 'w')
nome = file.writelines()
idade = file.writelines()
file.close()

