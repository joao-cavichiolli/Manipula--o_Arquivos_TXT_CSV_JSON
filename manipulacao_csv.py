### Importar o modulo csv 

import csv

## Criar um arquivo csv com as funções writer e writerow

with open('arquivos/nomes.csv','w+',newline="",encoding='utf-8') as fcsv:
    escreve = csv.writer(fcsv,delimiter=',')
    escreve.writerow(('Nome',"Sobrenome","Idade"))
    escreve.writerow(('João',"Ricardo","39"))
    escreve.writerow(('Juca',"Souza","34"))
    escreve.writerow(('Alberto',"Cunha","12"))
    fcsv.seek(0)

## LEr o arquivo CSV criado
    

with open('arquivos/nomes.csv','r') as fcsv:
    ler = csv.reader(fcsv)
    lista1 = list(ler)
    print(lista1)

    for c in lista1:
        print(c)

## Transformar a saida em dicionario com o metodo dictreader

with open('arquivos/nomes.csv','r') as fcsv2:
    ler_dic = csv.DictReader(fcsv2)

    # iterar os valores

    for d in ler_dic:
        print(d["Nome"])