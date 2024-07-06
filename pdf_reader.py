import PyPDF2
import pandas as pd
import os 

#script_dir = os.path.dirname(__file__)
#files = os.listdir(script_dir)
folder_path = "/work/"
list_files = os.listdir(folder_path)

pdf_files = [f for f in list_files if f.endswith('.pdf')]

matricula = []
consumo = []
referencia = [] 
emissao = []
valor_total = [] 
vencimento = []
dias = []

for file in pdf_files:
    pdf_reader = PyPDF2.PdfReader(file)
    page = pdf_reader.pages[0]
    
    text = page.extract_text().split("\n")
    text
    
       
    index = []
    for i, x in enumerate(text):
        if x == "AGÊNCIA: RUA CORONEL MOREIRA CESAR 157":
            index.append(i)
    #text[index[0]]

    index = [ i+1 for i, x in enumerate(text) if x == "AGÊNCIA: RUA CORONEL MOREIRA CESAR 157"]
    #index
    #text[index[0]]

    lista_valor = []
    lista_valor.append(text[index[0]])
    lista_valor

    lista_flag = lista_valor[0].split(" ")

    vencimento.append(lista_flag[0])
    valor_total.append(lista_flag[1])

    index_infos = [ i+1 for i, x in enumerate(text) if x == "Segunda Via"]

    lista_infos = [] 
    lista_infos.append(text[index_infos[0]])
    lista_infos

    lista_flag2 = lista_infos[0].split(" ")
    #Matricula, Ref, Emissao, Via, Roteirização/fatura

    matricula.append(lista_flag2[0])
    referencia.append(lista_flag2[1])
    emissao.append(lista_flag2[2])

    #print(index_infos)
    matricula_value = lista_flag2[0]

    if matricula_value == '102117192-9':
        index_infos2 = [ i+9 for i, x in enumerate(text) if x == "Segunda Via"]
    else:
        index_infos2 = [ i+10 for i, x in enumerate(text) if x == "Segunda Via"]
    lista_infos2 = [] 
    lista_infos2.append(text[index_infos2[0]])
    lista_flag3 = lista_infos2[0].split(" ")
    consumo.append(lista_flag3[1])
    dias.append(lista_flag3[3])
    #print(lista_infos2)

    df = pd.DataFrame({ 'Matricula':matricula,
                    'Referencia':referencia, 
                    'Vencimento':vencimento,
                    'Emissao':emissao, 
                    'Valor Total':valor_total,  
                    'Consumo':consumo,
                    'Dias':dias
                    })

df.to_excel('data_final.xlsx',index = False)