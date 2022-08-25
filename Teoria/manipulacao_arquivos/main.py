# Programa que manipula arquivos
# 'w' - write - escreve no arquivo
# 'a' - append - escreve no final do arquivo
# 'r' - read - le o arquivo

try:
    arquivo = open('data/dados.txt','a')
    continuar = True
    while continuar:
        time = input('Digite o nome do time(vazio para sair): ')
        # TODA STRING VAZIA É FALSE
        # Entra no loop se a string estiver vazia
        if not time:
            continuar = False
            continue
        arquivo.write(time + '\n')
    arquivo.close()
    s = 9/1
except ZeroDivisionError:
    print('Divisão por zero')
except FileNotFoundError:
    print('Arquivo ou diretório não encontrado')
except:
    print('Erro ao abrir o arquivo')
else:
    print('Arquivo aberto com sucesso')
    