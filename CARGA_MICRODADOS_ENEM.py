import mysql.connector as ms
import pandas as pd
import csv

def row2(value): 
    match value:     
         case '1':     
             return "Menor de 17 anos"     
         case '2':     
             return "17 anos"     
         case '3':     
             return "18 anos"     
         case '4':     
             return "19 anos"     
         case '5':     
             return "20 anos"     
         case '6':     
             return "21 anos"     
         case '7':     
             return "22 anos"     
         case '8':     
             return "23 anos"     
         case '9':     
             return "24 anos"     
         case '10':     
             return "25 anos"     
         case '11':     
             return "Entre 26 e 30 anos"     
         case '12':     
             return "Entre 31 e 35 anos"     
         case '13':     
             return "Entre 36 e 40 anos"     
         case '14':     
             return "Entre 41 e 45 anos"     
         case '15':     
             return "Entre 46 e 50 anos"     
         case '16':     
             return "Entre 51 e 55 anos"     
         case '17':     
             return "Entre 56 e 60 anos"     
         case '18':     
             return "Entre 61 e 65 anos"     
         case '19':     
             return "Entre 66 e 70 anos"     
         case '20':     
             return "Maior de 70 anos"     
         case _:     
             return None 

def row3(value): 
    match value:     
         case 'M':     
             return "Masculino"     
         case 'F':     
             return "Feminino"
         case _:     
             return None 
             
def row4(value): 
    match value:
         case '0':
             return "Não informado"
         case '1':     
             return "Solteiro(a)"     
         case '2':     
             return "Casado(a)/Mora com companheiro(a)"     
         case '3':     
             return "Divorciado(a)/Desquitado(a)/Separado(a)"     
         case '4':     
             return "Viúvo(a)"     
         case _:     
             return None 
             
def row5(value): 
    match value:
         case '0':
             return "Não declarado"
         case '1':     
             return "Branca"     
         case '2':     
             return "Preta"     
         case '3':     
             return "Parda"     
         case '4':     
             return "Amarela"     
         case '5':     
             return "Indígena "     
         case _:     
             return None 
             
def row6(value): 
    match value:
         case '0':
             return "Não informado"
         case '1':     
             return "Brasileiro(a)"     
         case '2':     
             return "Brasileiro(a) Naturalizado(a)"     
         case '3':     
             return "Estrangeiro(a)"     
         case '4':     
             return "Brasileiro(a) Nato(a), nascido(a) no exterior"     
         case _:     
             return None 
             
def row7(value): 
    match value:
         case '1':     
             return "Já concluí o Ensino Médio"     
         case '2':     
             return "Estou cursando e concluirei o Ensino Médio em 2020"     
         case '3':     
             return "Estou cursando e concluirei o Ensino Médio após 2020"     
         case '4':     
             return "Não concluí e não estou cursando o Ensino Médio"     
         case _:     
             return None 
             
def row8(value): 
    match value:     
         case '0':     
             return "Não informado"     
         case '1':     
             return "2019"     
         case '2':     
             return "2018"     
         case '3':     
             return "2017"     
         case '4':     
             return "2016"     
         case '5':     
             return "2015"     
         case '6':     
             return "2014"     
         case '7':     
             return "2013"     
         case '8':     
             return "2012"     
         case '9':     
             return "2011"     
         case '10':     
             return "2010"     
         case '11':     
             return "2009"     
         case '12':     
             return "2008"     
         case '13':     
             return "2007"     
         case '14':     
             return "Antes de 2007"     
         case _:     
             return None 

def row9(value): 
    match value:
         case '1':     
             return "Não Respondeu"     
         case '2':     
             return "Pública"     
         case '3':     
             return "Privada"     
         case '4':     
             return "Exterior"     
         case _:     
             return None 
             
def row10(value): 
    match value:
         case '1':     
             return "Ensino Regular"     
         case '2':     
             return "Educação Especial - Modalidade Substitutiva"     
         case '3':     
             return "Educação de Jovens e Adultos"     
         case _:     
             return None 

def row11(value): 
    match value:     
         case '0':     
             return "Não"     
         case '1':     
             return "Sim"  
         case _:     
             return None 
             
def row16(value): 
    match value:
         case '1':     
             return "Federal"     
         case '2':     
             return "Estadual"     
         case '3':     
             return "Municipal"     
         case '4':     
             return "Privada"     
         case _:     
             return None 
             
def row17(value): 
    match value:
         case '1':     
             return "Urbana"     
         case '2':     
             return "Rural"     
         case _:     
             return None 
             
def row18(value): 
    match value:
         case '1':     
             return "Em atividade"     
         case '2':     
             return "Paralisada"     
         case '3':     
             return "Extinta"     
         case '4':     
             return "Escola extinta em anos anteriores."     
         case _:     
             return None 
             
def row2326(value): 
    match value:     
         case '0':     
             return "Faltou à prova"     
         case '1':     
             return "Presente na prova"  
         case '2':     
             return "Eliminado na prova"     
         case _:     
             return None 
             
def row2730(value): 
    match value:     
         case '597' | '567' | '577' | '587':     
             return "Azul"     
         case '598' | '568' | '578' | '588':     
             return "Amarela"     
         case '599' | '590':     
             return "Cinza"     
         case '600' | '570' | '579' | '589':     
             return "Rosa"     
         case '601' | '571' | '581' | '591':     
             return "Rosa - Ampliada"     
         case '602' | '572' | '582' | '592':     
             return "Rosa - Superampliada"     
         case '604' | '574' | '584' | '594':     
             return "Laranja - Adaptada Ledor"     
         case '605' | '575' | '585' | '595':     
             return "Verde - Videoprova - Libras"     
         case '677' | '647' | '657' | '667':     
             return "Azul (Reaplicação)"     
         case '678' | '648' | '658' | '668':     
             return "Amarela (Reaplicação)"     
         case '679' | '670':     
             return "Cinza (Reaplicação)"     
         case '680' | '650' | '659' | '669':     
             return "Rosa (Reaplicação)"     
         case '684' | '654' | '664' | '674':     
             return "Laranja - Adaptada Ledor (Reaplicação)"     
         case '699' | '687' | '691' | '695':     
             return "Azul (Digital)"     
         case '700' | '688' | '692' | '696':     
             return "Amarela (Digital)"     
         case '701' | '690' | '694' | '697':     
             return "Rosa (Digital)"     
         case '702' | '698':     
             return "Cinza (Digital)"     
         case '569' | '580':     
             return "Branca"     
         case '649' | '660':     
             return "Branca (Reaplicação)"     
         case '689' | '693':     
             return "Branca (Digital)"     
         case _:     
             return None 

def row39(value): 
    match value:     
         case '0':     
             return "Inglês"     
         case '1':     
             return "Espanhol"  
         case _:     
             return None 
             
def row44(value): 
    match value:     
         case '1':     
             return "Sem problemas"     
         case '2':     
             return "Anulada"     
         case '3':     
             return "Cópia Texto Motivador"     
         case '4':     
             return "Em Branco"     
         case '6':     
             return "Fuga ao tema"     
         case '6':     
             return "Não atendimento ao tipo textual"     
         case '8':     
             return "Texto insuficiente"     
         case '9':     
             return "Parte desconectada"     
         case _:     
             return None 
             
def row5152(value): 
    match value:     
         case 'A':     
             return "Nunca estudou."     
         case 'B':     
             return "Não completou a 4ª série/5º ano do Ensino Fundamental."     
         case 'C':     
             return "Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental."     
         case 'D':     
             return "Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio."     
         case 'E':     
             return "Completou o Ensino Médio, mas não completou a Faculdade."     
         case 'F':     
             return "Completou a Faculdade, mas não completou a Pós-graduação."     
         case 'G':     
             return "Completou a Pós-graduação."     
         case 'H':     
             return "Não sei."     
         case _:     
             return None 
             
def row5354(value): 
    match value:     
         case 'A':     
             return "Grupo 1"     
         case 'B':     
             return "Grupo 2"     
         case 'C':     
             return "Grupo 3"     
         case 'D':     
             return "Grupo 4"     
         case 'E':     
             return "Grupo 5"     
         case 'F':     
             return "Não sei"     
         case _:     
             return None 
             
def row56(value): 
    match value:     
         case 'A':     
             return "Nenhuma Renda"     
         case 'B':     
             return "Até R$ 1.045,00"     
         case 'C':     
             return "De R$ 1.045,01 até R$ 1.567,50"     
         case 'D':     
             return "De R$ 1.567,51 até R$ 2.090,00"     
         case 'E':     
             return "De R$ 2.090,01 até R$ 2.612,50"     
         case 'F':     
             return "De R$ 2.612,51 até R$ 3.135,00"     
         case 'G':     
             return "De R$ 3.135,01 até R$ 4.180,00"     
         case 'H':     
             return "De R$ 4.180,01 até R$ 5.225,00"     
         case 'I':     
             return "De R$ 5.225,01 até R$ 6.270,00"     
         case 'J':     
             return "De R$ 6.270,01 até R$ 7.315,00"     
         case 'K':     
             return "De R$ 7.315,01 até R$ 8.360,00"     
         case 'L':     
             return "De R$ 8.360,01 até R$ 9.405,00"     
         case 'M':     
             return "De R$ 9.405,01 até R$ 10.450,00"     
         case 'N':     
             return "De R$ 10.450,01 até R$ 12.540,00"     
         case 'O':     
             return "De R$ 12.540,01 até R$ 15.675,00"     
         case 'P':     
             return "De R$ 15.675,01 até R$ 20.900,00"     
         case 'Q':     
             return "Acima de R$ 20.900,00"     
         case _:     
             return None 
             
def row57(value): 
    match value:     
         case 'A':     
             return "Não"     
         case 'B':     
             return "Sim, um ou dois dias por semana."     
         case 'C':     
             return "Sim, três ou quatro dias por semana."     
         case 'D':     
             return "Sim, pelo menos cinco dias por semana."     
         case _:     
             return None 
             
def row58(value): 
    match value:     
         case 'A':     
             return "Não"     
         case 'B':     
             return "Sim, um."     
         case 'C':     
             return "Sim, dois."     
         case 'D':     
             return "Sim, três."     
         case 'E':     
             return "Sim, quatro ou mais."     
         case _:     
             return None 
             
def row61(value): 
    match value:     
         case 'A':     
             return "Não"     
         case 'B':     
             return "Sim, uma."     
         case 'C':     
             return "Sim, duas."     
         case 'D':     
             return "Sim, três."     
         case 'E':     
             return "Sim, quatro ou mais."     
         case _:     
             return None 
             
def row68(value): 
    match value:     
         case 'A':     
             return "Não"     
         case 'B':     
             return "Sim"     
         case _:     
             return None 
             
def lerCSV():
    dados = pd.read_csv(csv_file_path, sep=";")
    dados.head()
    print(dados)

def getconn():
    conn = ms.connect(host="localhost", database="prova", port=3306, user="root", password="root")
    return conn

def InsCSVtoMS():
    conn = getconn()
    #print(conn.get_server_info())
    
#    with open("C:\\Users\\claud\\Documents\\PULSE\\DADOS\\TESTE_PYTHON.csv", encoding='utf-8') as arq_csv:
    with open("C:\\Users\\claud\\Documents\\PULSE\\DADOS\\MICRODADOS_ENEM_2020_SH.csv") as arq_csv:
        dados_csv = csv.reader(arq_csv, delimiter=";")
        dadosTOms = []
        for row in dados_csv:
            for i in range(0,76):
                if (row[i] == ''):
                    row[i] = None
            else:
                row[2] = row2(row[2]) #FAIXA ETÁRIA
                row[3] = row3(row[3]) #SEXO
                row[4] = row4(row[4]) #ESTADO CIVIL
                row[5] = row5(row[5]) #COR/RAÇA
                row[6] = row6(row[6]) #NACIONALIDADE
                row[7] = row7(row[7]) #CONCLUSÃO ENSINO MÉDIO
                row[8] = row8(row[8]) #ANO CONCLUSÃO ENSINO MÉDIO
                row[9] = row9(row[9]) #TIPO ESCOLA
                row[10] = row10(row[10]) #TIPO ENSINO
                row[11] = row11(row[11]) #IN_TREINEIRO
                row[16] = row16(row[16]) #DEP. ADM
                row[17] = row17(row[17]) #LOCALIZAÇÃO ESCOLA
                row[18] = row18(row[18]) #SIT.ESCOLA
                row[23] = row2326(row[23]) #PRESENÇA CN
                row[24] = row2326(row[24]) #PRESENÇA CH
                row[25] = row2326(row[25]) #PRESENÇA LC
                row[26] = row2326(row[26]) #PRESENÇA MT
                row[27] = row2730(row[27]) #COR CIÊNCIAS
                row[28] = row2730(row[28]) #COR HUMANAS
                row[29] = row2730(row[29]) #COR LINGUAGENS
                row[30] = row2730(row[30]) #COR MATEMÁTICA
                row[39] = row39(row[39]) #LÍNGUA
                row[44] = row44(row[44]) #STATUS REDAÇÃO
                row[51] = row5152(row[51]) #Q001
                row[52] = row5152(row[52]) #Q002
                row[53] = row5354(row[53]) #Q003
                row[54] = row5354(row[54]) #Q004
                row[56] = row56(row[56]) #Q006
                row[57] = row57(row[57]) #Q007
                row[58] = row58(row[58]) #Q008
                row[59] = row58(row[59]) #Q009
                row[60] = row58(row[60]) #Q010
                row[61] = row61(row[61]) #Q011
                row[62] = row61(row[62]) #Q012
                row[63] = row58(row[63]) #Q013
                row[64] = row61(row[64]) #Q014
                row[65] = row61(row[65]) #Q015
                row[66] = row58(row[66]) #Q016
                row[67] = row61(row[67]) #Q017
                row[68] = row68(row[68]) #Q018
                row[69] = row61(row[69]) #Q019
                row[70] = row68(row[70]) #Q020
                row[71] = row68(row[71]) #Q021
                row[72] = row58(row[72]) #Q022
                row[73] = row68(row[73]) #Q023
                row[74] = row58(row[74]) #Q024
                row[75] = row68(row[75]) #Q025
                
            dadosTOms.append((row[0],  row[1],  row[2],  row[3],  row[4],  row[5],  row[6],  row[7],  row[8],  row[9],
                              row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19],
                              row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29],
                              row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39],
                              row[40], row[41], row[42], row[43], row[44], row[45], row[46], row[47], row[48], row[49],
                              row[50], row[51], row[52], row[53], row[54], row[55], row[56], row[57], row[58], row[59],
                              row[60], row[61], row[62], row[63], row[64], row[65], row[66], row[67], row[68], row[69],
                              row[70], row[71], row[72], row[73], row[74], row[75]))
            #print(dadosTOms)
            sql_com = "INSERT INTO prova.microdados_2020 values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            #print(sql_com)
            cur = conn.cursor()
            cur.executemany(sql_com, dadosTOms)
            dadosTOms = []
            conn.commit()
        cur.close()

if __name__ == '__main__':
    InsCSVtoMS()