# Exercício 1 - Criar perfil
with open("perfil.txt","w") as arquivo:
    arquivo.write("Nome: Murilo\n")
    arquivo.write("Idade: 16 anos\n")
    arquivo.write("Comida preferida: Paçoca\n")

# Exercício 2 - Ler perfil
with open("perfil.txt","r") as arquivo:
    conteudo_do_perfil = arquivo.read()
print("--- Conteúdo do Perfil ---")
print(conteudo_do_perfil)

# Exercício 3 - Diário Simples
print("\n--- Diário ---")
sentimento = input("Como você está se sentindo hoje? ")
with open("diario.txt","a") as arquivo:
    arquivo.write(sentimento + "\n")
print("Anotação salva!")

# Exercício 4 - Lista de Tarefas
print("\n--- Lista de Tarefas ---")
print("1 = Adicionar uma tarefa")
print("2 = Listar todas as tarefas")
opcao = input("Escolha uma opção |1 ou 2|: ")

if opcao == "1":
    tarefa = input("Digite a tarefa: ")
    with open("tarefa.txt","a") as arquivo:
        arquivo.write(tarefa + "\n")
    print("Tarefa adicionada!")

elif opcao == "2":
    with open("tarefa.txt","r") as arquivo:
        tarefas = arquivo.readlines()
    print("\nSuas tarefas:")
    for tarefa in tarefas:
        print("-", tarefa.strip())

else:
    print("Opção inválida! Escolha |1 ou 2|")

# Exercício 5 - Contador de Linhas
print("\n--- Contador de Linhas ---")
nome = input("Digite o nome de um arquivo para contar as linhas |ex: perfil.txt|: ")
with open(nome,"r") as arquivo:
    linhas = arquivo.readlines()
quantidade = len(linhas)
print(f"O arquivo '{nome}' tem {quantidade} linhas")

# Exercício 6 - Copiador de Arquivos
print("\n--- Copiador de Arquivos ---")
original = input("Digite o nome do arquivo que será copiado |ex: tarefa.txt|: ")
copia = input("Digite o nome do novo arquivo |ex: copia.txt|: ")
with open(original,"r") as orig:
    conteudo = orig.read()
with open(copia,"w") as copi:
    copi.write(conteudo)
print(f"Arquivo '{original}' copiado com sucesso para '{copia}'!")

# Exercício 7 - Tabuada
print("\n--- Tabuada ---")
numero = int(input("Digite um número para ver a tabuada: "))
with open("tabuada.txt","w") as arquivo:
    for i in range(1, 11):
        resultado = numero * i
        linha = f"{numero} x {i} = {resultado}\n"
        arquivo.write(linha)
print(f"A tabuada do número {numero} foi salva no arquivo 'tabuada.txt'")

# Exercício 8 - Calculadora de Média
print("\n--- Calculadora de Média ---")
with open("notas.txt","w") as arquivo:
    arquivo.write("8.5\n")
    arquivo.write("9.0\n")
    arquivo.write("7.5\n")
    arquivo.write("10.0\n")
    arquivo.write("6.0\n")

with open("notas.txt","r") as arquivo:
    linhas = arquivo.readlines()
notas = [float(linha.strip()) for linha in linhas]
media = sum(notas) / len(notas)
print(f"A média das notas é: {media:.2f}")

# Exercício 9 - Buscador de Palavras
print("\n--- Buscador de Palavras ---")
nome_arquivo = input("Digite o nome do arquivo |ex: tarefa.txt|: ")
palavra = input("Digite a palavra que deseja buscar: ")
with open(nome_arquivo,"r") as arquivo:
    conteudo = arquivo.read()
quantidade = conteudo.lower().count(palavra.lower())
print(f"A palavra '{palavra}' aparece {quantidade} vezes no arquivo '{nome_arquivo}'")

# Desafio 10 - Agenda de Contatos
print("\n--- Agenda de Contatos ---")
with open("agenda.csv","w") as arquivo:
    arquivo.write("Caio,12345-6789\n")
    arquivo.write("André,98765-4321\n")
    arquivo.write("Márcio,24682-4286\n")
    arquivo.write("Henrique,13579-7531\n")
    arquivo.write("Fernando,01000-1101\n")

print("1 = Adicionar contato")
print("2 = Listar contatos")
print("3 = Buscar contato")
opcao = input("Escolha uma opção: ")

if opcao == "1":
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    with open("agenda.csv","a") as arquivo:
        arquivo.write(f"{nome},{telefone}\n")
    print(f"Contato '{nome}' adicionado com sucesso!")

elif opcao == "2":
    with open("agenda.csv","r") as arquivo:
        linhas = arquivo.readlines()
    print("\nContatos cadastrados:")
    for linha in linhas:
        nome, telefone = linha.strip().split(",")
        print(f" - {nome} | {telefone}")

elif opcao == "3":
    busca = input("Digite o nome do contato para buscar: ").lower()
    with open("agenda.csv","r") as arquivo:
        linhas = arquivo.readlines()

    contador = 0
    for linha in linhas:
        nome, telefone = linha.strip().split(",")
        if busca in nome.lower():
            print(f" - {nome} | {telefone}")
            contador += 1
        
    if contador == 0:
        print(f"Nenhum contato com o nome '{busca}' encontrado.")

else:
    print("Opção inválida! Escolha |1, 2 ou 3|")
