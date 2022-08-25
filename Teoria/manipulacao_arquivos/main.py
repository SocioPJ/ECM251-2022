# Programa que manipula arquivos
# 'w' - write - escreve no arquivo
# 'a' - append - escreve no final do arquivo
# 'r' - read - le o arquivo


arquivo = open('dados.txt','a')
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