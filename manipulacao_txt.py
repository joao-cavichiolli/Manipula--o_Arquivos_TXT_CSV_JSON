## Vamos abrir um arquivo TXT 

arq1 = open('arquivos/arquivo.txt','r')

# Windows \ # linux /

### Ler o arquivo TXT

print(arq1.read())


## Voltar o cursor ao inicio

arq1.seek(0,0)

print(arq1.read())

## Fechar o arquivo

arq1.close()



## Usar um arquivo em modo gravação

arq2 = open('arquivos/arquivo.txt',"w+")

## Gravar

arq2.write("Tem novo conteudi\n")
arq2.write("Gravei outra linha\n")

arq2.seek(0,0)
print(arq2.read())

# Fechar o arquivos
arq2.close()

## Abrir uma nova manipulacao de alteração de arquivo

arq3 = open('arquivos/arquivo.txt','a+')

arq3.write("Novo conteudo sem apagar o antigo\n")

arq3.seek(0,0)

print(arq3.read())

arq3.close()


### Gerenciador de contexto de arquivos

with open("arquivos/arquivo1.txt",'w+') as f:
    f.write('Primeira linha\n')
    f.write('Segunda linha\n')
    f.seek(0,0)
    grava = str(f.read())
    f.seek(0,0)
    print(f.read())

## Gravar informações em um 2 arquivos
    
with open('arquivos/arquivo2.txt','w+') as f2:
    f2.write(grava)
    f2.seek(0,0)
    print(f2.read())