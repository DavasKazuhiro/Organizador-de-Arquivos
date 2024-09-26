import os
import shutil

pasta = input("Digite o caminho para a pasta a ser organizada: ")

for arquivo in os.listdir(pasta):
    nome, extensao = os.path.splitext(arquivo)
    extensao = extensao[1:]
    print(nome, extensao)

    organizar = f"{pasta}/{extensao}"

    if not os.path.isdir(organizar):
        os.mkdir(organizar)

    shutil.move(f"{pasta}/{arquivo}", f"{organizar}/{arquivo}")

