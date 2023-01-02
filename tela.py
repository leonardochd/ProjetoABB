# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

from re import A
import PySimpleGUI as sg
# import win32com.client 
import sqlite3
import ger_pdf as pdf
#import sqlite3 import Error


# Definindo as fontes
subsecao = ("Helvetica", 11, "bold")
ing = ("Helvetica", 9, "italic")
port = ("Helvetica", 10)


################################################################## AREA DE TESTES #########################################################################
#include os arquivos txt para ter as perguntas, cada arquivo é uma aba do relatório
with open("pagina1.txt", "r") as tf:
    lines1 = tf.read().split(';')

with open("pagina2.txt", "r") as tf:
    lines2 = tf.read().split(';')

with open("pagina3.txt", "r") as tf:
    lines3 = tf.read().split(';')

with open("pagina4.txt", "r") as tf:
  	lines4 = tf.read().split(';')

###########################################################################################################################################################

class TelaPython:
    def __init__ (self): # Função Construtora
### Definindo as fontes para colocar no text ####
        #Layout
        layout_0 = [
            [sg.Text('ELETRIFICATION DISTRIBUTION SYSTEMS DA SOLUTIONS PRODUCTS\nRELATÓRIO DE TESTES')],
            [sg.Text('Projeto / Project:',size=(12,0)),sg.Input(size=(100,0),key='projeto')],
            [sg.Text('PEP:',size=(12,0)),sg.Input(size=(50,0),key='pep')],
            [sg.Text('DATA ÍNICIO:',size=(12,0)),sg.Input(size=(10,0),key='inicio')],
            [sg.Text('DATA FIM:',size=(12,0)),sg.Input(size=(10,0),key='fim')],
        ]

        layout_1 = [
            ###################################### 1 - INSPEÇÃO VISUAL E VERIFICAÇÕES DIMENSIONAIS   ###################################################
            #[sg.Text('1-INSPEÇÃO VISUAL E VERIFICAÇÕES DIMENSIONAIS', font=subsecao)],
            [sg.Text(text=list(lines1)[0], font=subsecao)],
            [sg.Text(text=list(lines1)[1], font=port)],
            [sg.Text(text=list(lines1)[2], font=ing)],
            [sg.Radio('OK','1.1',key='ok_1.1'),sg.Radio('NO','1.1',key='no_1.1'),sg.Radio('NA','1.1',key='na_1.1')],
            [sg.Text(text=list(lines1)[3], font=port)],
            [sg.Text(text=list(lines1)[4], font=ing)],
            [sg.Radio('OK','1.2',key='ok_1.2'),sg.Radio('NO','1.2',key='no_1.2'),sg.Radio('NA','1.2',key='na_1.2')],
            [sg.Text(text=list(lines1)[5], font=port)],
            [sg.Text(text=list(lines1)[6], font=ing)],
            [sg.Radio('OK','1.3',key='ok_1.3'),sg.Radio('NO','1.3',key='no_1.3'),sg.Radio('NA','1.3',key='na_1.3')],
            [sg.Text(text=list(lines1)[7], font=port)],
            [sg.Text(text=list(lines1)[8], font=ing)],
            [sg.Radio('OK','1.4',key='ok_1.4'),sg.Radio('NO','1.4',key='no_1.4'),sg.Radio('NA','1.4',key='na_1.4')],
            [sg.Text(text=list(lines1)[9], font=port)],
            [sg.Text(text=list(lines1)[10], font=ing)],
            [sg.Radio('OK','1.5',key='ok_1.5'),sg.Radio('NO','1.5',key='no_1.5'),sg.Radio('NA','1.5',key='na_1.5')],
            [sg.Text(text=list(lines1)[11], font=port)],
            [sg.Text(text=list(lines1)[12], font=ing)],
            [sg.Radio('OK','1.6',key='ok_1.6'),sg.Radio('NO','1.6',key='no_1.6'),sg.Radio('NA','1.6',key='na_1.6')],
            [sg.Text(text=list(lines1)[13], font=port)],
            [sg.Text(text=list(lines1)[14], font=ing)],
            [sg.Radio('OK','1.7',key='ok_1.7'),sg.Radio('NO','1.7',key='no_1.7'),sg.Radio('NA','1.7',key='na_1.7')],
        ]

        layout_2 = [
            ######################################       SEGUNDA ABA DE PERGUNTAS        ###################################################
            [sg.Text(text=list(lines2)[0], font=subsecao)],
            [sg.Text(text=list(lines2)[1], font=port)],
            [sg.Text(text=list(lines2)[2], font=ing)],
            [sg.Radio('OK','2.1',key='ok_2.1'),sg.Radio('NO','2.1',key='no_2.1'),sg.Radio('NA','2.1',key='na_2.1')],
            [sg.Text(text=list(lines2)[3], font=port)],
            [sg.Text(text=list(lines2)[4], font=ing)],
            [sg.Radio('OK','2.2',key='ok_2.2'),sg.Radio('NO','2.2',key='no_2.2'),sg.Radio('NA','2.2',key='na_2.2')],
            [sg.Text(text=list(lines2)[5], font=port)],
            [sg.Text(text=list(lines2)[6], font=ing)],
            [sg.Radio('OK','2.3',key='ok_2.3'),sg.Radio('NO','2.3',key='no_2.3'),sg.Radio('NA','2.3',key='na_2.3')],
            [sg.Text(text=list(lines2)[7], font=port)],
            [sg.Text(text=list(lines2)[8], font=ing)],
            [sg.Radio('OK','2.4',key='ok_2.4'),sg.Radio('NO','2.4',key='no_2.4'),sg.Radio('NA','2.4',key='na_2.4')],
            [sg.Text(text=list(lines2)[9], font=port)],
            [sg.Text(text=list(lines2)[10], font=ing)],
            [sg.Radio('OK','2.5',key='ok_2.5'),sg.Radio('NO','2.5',key='no_2.5'),sg.Radio('NA','2.5',key='na_2.5')],
            [sg.Text(text=list(lines2)[11], font=port)],
            [sg.Text(text=list(lines2)[12], font=ing)],
            [sg.Radio('OK','2.6',key='ok_2.6'),sg.Radio('NO','2.6',key='no_2.6'),sg.Radio('NA','2.6',key='na_2.6')],
            [sg.Text(text=list(lines2)[13], font=port)],
            [sg.Text(text=list(lines2)[14], font=ing)],
            [sg.Radio('OK','2.7',key='ok_2.7'),sg.Radio('NO','2.7',key='no_2.7'),sg.Radio('NA','2.7',key='na_2.7')],
        ]

        layout_3 = [
            ######################################        TERCEIRA ABA DE PERGUNTAS       ###################################################
            [sg.Text(text=list(lines3)[0], font=subsecao)],
            [sg.Text(text=list(lines3)[1], font=port)],
            [sg.Text(text=list(lines3)[2], font=ing)],
            [sg.Radio('OK','3.1',key='ok_3.1'),sg.Radio('NO','3.1',key='no_3.1'),sg.Radio('NA','3.1',key='na_3.1')],
            [sg.Text(text=list(lines3)[3], font=port)],
            [sg.Text(text=list(lines3)[4], font=ing)],
            [sg.Radio('OK','3.2',key='ok_3.2'),sg.Radio('NO','3.2',key='no_3.2'),sg.Radio('NA','3.2',key='na_3.2')],
            [sg.Text(text=list(lines3)[5], font=port)],
            [sg.Text(text=list(lines3)[6], font=ing)],
            [sg.Radio('OK','3.3',key='ok_3.3'),sg.Radio('NO','3.3',key='no_3.3'),sg.Radio('NA','3.3',key='na_3.3')],
            [sg.Text(text=list(lines3)[7], font=port)],
            [sg.Text(text=list(lines3)[8], font=ing)],
            [sg.Radio('OK','3.4',key='ok_3.4'),sg.Radio('NO','3.4',key='no_3.4'),sg.Radio('NA','3.4',key='na_3.4')],
            [sg.Text(text=list(lines3)[9], font=port)],
            [sg.Text(text=list(lines3)[10], font=ing)],
            [sg.Radio('OK','3.5',key='ok_3.5'),sg.Radio('NO','3.5',key='no_3.5'),sg.Radio('NA','3.5',key='na_3.5')],
            [sg.Text(text=list(lines3)[11], font=port)],
            [sg.Text(text=list(lines3)[12], font=ing)],
            [sg.Radio('OK','3.6',key='ok_3.6'),sg.Radio('NO','3.6',key='no_3.6'),sg.Radio('NA','3.6',key='na_3.6')],
        ]

        layout_4 = [
            [sg.Text(text=list(lines4)[0])],
            [sg.Text(text=list(lines4)[1],size=(12,0)),sg.Input(size=(100,0),key='instrumento1')],
            [sg.Text(text=list(lines4)[2],size=(12,0)),sg.Input(size=(100,0),key='registro1')],
            [sg.Text(text=list(lines4)[3],size=(12,0)),sg.Input(size=(100,0),key='validade1')],
            [sg.Text(text=list(lines4)[1],size=(12,0)),sg.Input(size=(100,0),key='instrumento2')],
            [sg.Text(text=list(lines4)[2],size=(12,0)),sg.Input(size=(100,0),key='registro2')],
            [sg.Text(text=list(lines4)[3],size=(12,0)),sg.Input(size=(100,0),key='validade2')],
            [sg.Text(text=list(lines4)[1],size=(12,0)),sg.Input(size=(100,0),key='instrumento3')],
            [sg.Text(text=list(lines4)[2],size=(12,0)),sg.Input(size=(100,0),key='registro3')],
            [sg.Text(text=list(lines4)[3],size=(12,0)),sg.Input(size=(100,0),key='validade3')],
            [sg.Text(text=list(lines4)[1],size=(12,0)),sg.Input(size=(100,0),key='instrumento4')],
            [sg.Text(text=list(lines4)[2],size=(12,0)),sg.Input(size=(100,0),key='registro4')],
            [sg.Text(text=list(lines4)[3],size=(12,0)),sg.Input(size=(100,0),key='validade4')],
            [sg.Text(text=list(lines4)[1],size=(12,0)),sg.Input(size=(100,0),key='instrumento5')],
            [sg.Text(text=list(lines4)[2],size=(12,0)),sg.Input(size=(100,0),key='registro5')],
            [sg.Text(text=list(lines4)[3],size=(12,0)),sg.Input(size=(100,0),key='validade5')],
            [sg.Text(text=list(lines4)[1],size=(12,0)),sg.Input(size=(100,0),key='instrumento6')],
            [sg.Text(text=list(lines4)[2],size=(12,0)),sg.Input(size=(100,0),key='registro6')],
            [sg.Text(text=list(lines4)[3],size=(12,0)),sg.Input(size=(100,0),key='validade6')],
            [sg.Text(text=list(lines4)[1],size=(12,0)),sg.Input(size=(100,0),key='instrumento7')],
            [sg.Text(text=list(lines4)[2],size=(12,0)),sg.Input(size=(100,0),key='registro7')],
            [sg.Text(text=list(lines4)[3],size=(12,0)),sg.Input(size=(100,0),key='validade7')],
        ]

        layout_5 = [ 
          [sg.Text('COMENTÁRIOS DOS TESTES / TESTING COMMENTS')],
          [sg.Text('Liberado sem pendências'),sg.Radio('Liberado','5.1',key='ok_5.1')],
          [sg.Text('Liberado com as pendências listadas abaixo: '),sg.Radio('Pendente','5.1',key='pendencia_5.1'),sg.Input(size=(200,0),key='pendencia')],
          [sg.Text('Reprovados pelos motivos mostrados abaixo: '),sg.Radio('Reprovado','5.1',key='no_5.1'),sg.Input(size=(200,0),key='reprovado')]
        ]

        ################## INSERINDO ABAS NA JANELA #################3######3
        tab_group = [
            [sg.TabGroup(
                [[
                    sg.Tab('ABA0', layout_0, title_color='Red', tooltip='ABA0', element_justification='left'),
                    sg.Tab('ABA1', layout_1, title_color='Red', tooltip='ABA1', element_justification='left'),
                    sg.Tab('ABA2', layout_2, title_color='Red', tooltip='ABA2', element_justification='left'),
                    sg.Tab('ABA3', layout_3, title_color='Red', tooltip='ABA3', element_justification='left'),
                    sg.Tab('ABA4', layout_4, title_color='Red', tooltip='ABA4', element_justification='left'),
                    sg.Tab('ABA5', layout_5, title_color='Red', tooltip='ABA5', element_justification='left'),
                ],
                [sg.Button('Fechar')]]
            )]
        ]

        #Janela
        #janela = sg.Window("CARTÃO DE INSPEÇÃO / Inspection card").layout(layout)
        janela = sg.Window('CARTÃO DE INSPEÇÃO / Inspection card', tab_group)
        #Extrair dados
        self.button, self.values = janela.Read()
        #Manipulação dos Dados para geração do PDF
        
        
    def Iniciar(self):
        # Transferindo as variaveis para serem armazenadas no Banco de Dados
        T_NOMEPROJETO = self.values['projeto'].capitalize()
        T_PEP = self.values['pep'].capitalize()
        B_ok_11 = self.values['ok_1.1']
        B_no_11 = self.values['no_1.1']
        B_na_11 = self.values['na_1.1']
        B_ok_12 = self.values['ok_1.2']
        B_no_12 = self.values['no_1.2']
        B_na_12 = self.values['na_1.2']
        B_ok_13 = self.values['ok_1.3']
        B_no_13 = self.values['no_1.3']
        B_na_13 = self.values['na_1.3']
        B_ok_14 = self.values['ok_1.4']
        B_no_14 = self.values['no_1.4']
        B_na_14 = self.values['na_1.4']
        B_ok_15 = self.values['ok_1.5']
        B_no_15 = self.values['no_1.5']
        B_na_15 = self.values['na_1.5']
        B_ok_16 = self.values['ok_1.6']
        B_no_16 = self.values['no_1.6']
        B_na_16 = self.values['na_1.6']
        B_ok_17 = self.values['ok_1.7']
        B_no_17 = self.values['no_1.7']
        B_na_17 = self.values['na_1.7']
        B_ok_21 = self.values['ok_2.1']
        B_no_21 = self.values['no_2.1']
        B_na_21 = self.values['na_2.1']
        B_ok_22 = self.values['ok_2.2']
        B_no_22 = self.values['no_2.2']
        B_na_22 = self.values['na_2.2']
        B_ok_23 = self.values['ok_2.3']
        B_no_23 = self.values['no_2.3']
        B_na_23 = self.values['na_2.3']
        B_ok_24 = self.values['ok_2.4']
        B_no_24 = self.values['no_2.4']
        B_na_24 = self.values['na_2.4']
        B_ok_25 = self.values['ok_2.5']
        B_no_25 = self.values['no_2.5']
        B_na_25 = self.values['na_2.5']
        B_ok_26 = self.values['ok_2.6']
        B_no_26 = self.values['no_2.6']
        B_na_26 = self.values['na_2.6']
        B_ok_27 = self.values['ok_2.7']
        B_no_27 = self.values['no_2.7']
        B_na_27 = self.values['na_2.7']
        B_ok_31 = self.values['ok_2.1']
        B_no_31 = self.values['no_3.1']
        B_na_31 = self.values['na_3.1']
        B_ok_32 = self.values['ok_3.2']
        B_no_32 = self.values['no_3.2']
        B_na_32 = self.values['na_3.2']
        B_ok_33 = self.values['ok_3.3']
        B_no_33 = self.values['no_3.3']
        B_na_33 = self.values['na_3.3']
        B_ok_34 = self.values['ok_3.4']
        B_no_34 = self.values['no_3.4']
        B_na_34 = self.values['na_3.4']
        B_ok_35 = self.values['ok_3.5']
        B_no_35 = self.values['no_3.5']
        B_na_35 = self.values['na_3.5']
        B_ok_36 = self.values['ok_3.6']
        B_no_36 = self.values['no_3.6']
        B_na_36 = self.values['na_3.6']
        T_INSTRUMENTO1 = self.values['instrumento1']
        T_INSTRUMENTO2 = self.values['instrumento2']
        T_INSTRUMENTO3 = self.values['instrumento3']
        T_INSTRUMENTO4 = self.values['instrumento4']
        T_INSTRUMENTO5 = self.values['instrumento5']
        T_INSTRUMENTO6 = self.values['instrumento6']
        T_INSTRUMENTO7 = self.values['instrumento7']
        T_REGISTRO1 = self.values['registro1']
        T_REGISTRO2 = self.values['registro2']
        T_REGISTRO3 = self.values['registro3']
        T_REGISTRO4 = self.values['registro4']
        T_REGISTRO5 = self.values['registro5']
        T_REGISTRO6 = self.values['registro6']
        T_REGISTRO7 = self.values['registro7']
        T_VALIDADE1 = self.values['validade1']
        T_VALIDADE2 = self.values['validade2']
        T_VALIDADE3 = self.values['validade3']
        T_VALIDADE4 = self.values['validade4']
        T_VALIDADE5 = self.values['validade5']
        T_VALIDADE6 = self.values['validade6']
        T_VALIDADE7 = self.values['validade7']


        ################################### BANCO DE DADOS #######################################################
        ############ Criando, manipulando e salvando as informações dentro do banco de dados    ##################
        dbase = sqlite3.connect("projeto.db")
        c = dbase.cursor()
        dbase.commit()

        ### Criando o Banco de Dados ###
        dbase.execute(''' CREATE TABLE IF NOT EXISTS tb_relatorio(
            T_PEP   VARCHAR(30) PRIMARY KEY NOT NULL,
            T_NOMEPROJETO VARCHAR(50),
            B_ok_11		BOOLEAN,
            B_no_11		BOOLEAN,
            B_na_11		BOOLEAN,
            B_ok_12		BOOLEAN,
            B_no_12		BOOLEAN,
            B_na_12		BOOLEAN,
            B_ok_13		BOOLEAN,
            B_no_13		BOOLEAN,
            B_na_13		BOOLEAN,
            B_ok_14		BOOLEAN,
            B_no_14		BOOLEAN,
            B_na_14		BOOLEAN,
            B_ok_15		BOOLEAN,
            B_no_15		BOOLEAN,
            B_na_15		BOOLEAN,
            B_ok_16		BOOLEAN,
            B_no_16		BOOLEAN,
            B_na_16		BOOLEAN,
            B_ok_17		BOOLEAN,
            B_no_17		BOOLEAN,
            B_na_17		BOOLEAN,
            B_ok_21		BOOLEAN, 
            B_no_21		BOOLEAN,
            B_na_21		BOOLEAN,
            B_ok_22		BOOLEAN, 
            B_no_22		BOOLEAN,
            B_na_22		BOOLEAN,
            B_ok_23		BOOLEAN, 
            B_no_23		BOOLEAN,
            B_na_23		BOOLEAN,
            B_ok_24		BOOLEAN, 
            B_no_24		BOOLEAN,
            B_na_24		BOOLEAN,
            B_ok_25		BOOLEAN,
            B_no_25		BOOLEAN,
            B_na_25		BOOLEAN,
            B_ok_26		BOOLEAN, 
            B_no_26		BOOLEAN,
            B_na_26		BOOLEAN,
            B_ok_27		BOOLEAN, 
            B_no_27		BOOLEAN,
            B_na_27 	BOOLEAN,
            B_ok_31		BOOLEAN,
            B_no_31		BOOLEAN,
            B_na_31		BOOLEAN,
            B_ok_32		BOOLEAN,
            B_no_32		BOOLEAN,
            B_na_32		BOOLEAN,
            B_ok_33		BOOLEAN,
            B_no_33		BOOLEAN,
            B_na_33		BOOLEAN,
            B_ok_34		BOOLEAN,
            B_no_34		BOOLEAN,
            B_na_34		BOOLEAN,
            B_ok_35		BOOLEAN,
            B_no_35		BOOLEAN,
            B_na_35		BOOLEAN,
            B_ok_36		BOOLEAN,
            B_no_36		BOOLEAN,
            B_na_36		BOOLEAN,
            T_INSTRUMENTO1		VARCHAR(20),
            T_INSTRUMENTO2		VARCHAR(20),
            T_INSTRUMENTO3		VARCHAR(20),
            T_INSTRUMENTO4		VARCHAR(20),
            T_INSTRUMENTO5		VARCHAR(20),
            T_INSTRUMENTO6		VARCHAR(20),
            T_INSTRUMENTO7		VARCHAR(20),
      	    T_REGISTRO1				VARCHAR(20),
            T_REGISTRO2				VARCHAR(20),
            T_REGISTRO3				VARCHAR(20),
            T_REGISTRO4				VARCHAR(20),
            T_REGISTRO5				VARCHAR(20),
            T_REGISTRO6				VARCHAR(20),
            T_REGISTRO7				VARCHAR(20),
            T_VALIDADE1				VARCHAR(20),
            T_VALIDADE2				VARCHAR(20),
            T_VALIDADE3				VARCHAR(20),
            T_VALIDADE4				VARCHAR(20),
            T_VALIDADE5				VARCHAR(20),
            T_VALIDADE6				VARCHAR(20),
            T_VALIDADE7				VARCHAR(20))''')

        # Aplica as mudanças no banco de dados
        dbase.commit()


# Função escreve os valores das variaveis #
        c.execute(""" INSERT OR IGNORE INTO tb_relatorio(T_PEP,
            T_NOMEPROJETO,
            B_ok_11,
            B_no_11,
            B_na_11,
            B_ok_12,
            B_no_12,
            B_na_12,
            B_ok_13,
            B_no_13,
            B_na_13,
            B_ok_14,
            B_no_14,
            B_na_14,
            B_ok_15,
            B_no_15,
            B_na_15,
            B_ok_16,
            B_no_16,
            B_na_16,
            B_ok_17,
            B_no_17,
            B_na_17,
            B_ok_21, 
            B_no_21,
            B_na_21,
            B_ok_22, 
            B_no_22,
            B_na_22,
            B_ok_23, 
            B_no_23,
            B_na_23,
            B_ok_24, 
            B_no_24,
            B_na_24,
            B_ok_25,
            B_no_25,
            B_na_25,
            B_ok_26, 
            B_no_26,
            B_na_26,
            B_ok_27, 
            B_no_27,
            B_na_27,
            B_ok_31,
            B_no_31,
            B_na_31,
            B_ok_32,
            B_no_32,
            B_na_32,
            B_ok_33,
            B_no_33,
            B_na_33,
            B_ok_34,
            B_no_34,
            B_na_34,
            B_ok_35,
            B_no_35,
            B_na_35,
            B_ok_36,
            B_no_36,
            B_na_36,
            T_INSTRUMENTO1,
            T_INSTRUMENTO2,
            T_INSTRUMENTO3,
            T_INSTRUMENTO4,
            T_INSTRUMENTO5,
            T_INSTRUMENTO6,
            T_INSTRUMENTO7,
      	    T_REGISTRO1,
            T_REGISTRO2,
            T_REGISTRO3,
            T_REGISTRO4,
            T_REGISTRO5,
            T_REGISTRO6,
            T_REGISTRO7,
            T_VALIDADE1,
            T_VALIDADE2,
            T_VALIDADE3,
            T_VALIDADE4,
            T_VALIDADE5,
            T_VALIDADE6,
            T_VALIDADE7) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )""", (T_PEP,T_NOMEPROJETO,B_ok_11,B_no_11,B_na_11,B_ok_12,B_no_12,B_na_12,B_ok_13,B_no_13,B_na_13,B_ok_14,B_no_14,B_na_14,B_ok_15,B_no_15,B_na_15,B_ok_16,B_no_16,B_na_16,B_ok_17,B_no_17,B_na_17,B_ok_21, B_no_21,B_na_21,B_ok_22, B_no_22,B_na_22,B_ok_23, B_no_23,B_na_23,B_ok_24, B_no_24,B_na_24,B_ok_25,B_no_25,B_na_25,B_ok_26, B_no_26,B_na_26,B_ok_27, B_no_27,B_na_27 ,B_ok_31,B_no_31,B_na_31,B_ok_32,B_no_32,B_na_32,B_ok_33,B_no_33,B_na_33,B_ok_34,B_no_34,B_na_34,B_ok_35,B_no_35,B_na_35,B_ok_36,B_no_36,B_na_36,T_INSTRUMENTO1,T_INSTRUMENTO2,T_INSTRUMENTO3,T_INSTRUMENTO4,T_INSTRUMENTO5,T_INSTRUMENTO6,T_INSTRUMENTO7,T_REGISTRO1,T_REGISTRO2,T_REGISTRO3,T_REGISTRO4,T_REGISTRO5,T_REGISTRO6,T_REGISTRO7,T_VALIDADE1,T_VALIDADE2,T_VALIDADE3,T_VALIDADE4,T_VALIDADE5,T_VALIDADE6,T_VALIDADE7))
        dbase.commit()

        # CONSULTANDO E INSERINDO OS VALORES DO BANCO DE DADOS PARA O GERADOR DO PDF
        
        pdf.ger(T_PEP,T_NOMEPROJETO,B_ok_11,B_no_11,B_na_11,B_ok_12,B_no_12,B_na_12,B_ok_13,B_no_13,B_na_13,B_ok_14,B_no_14,B_na_14,B_ok_15,B_no_15,B_na_15,B_ok_16,B_no_16,B_na_16,B_ok_17,B_no_17,B_na_17,B_ok_21, B_no_21,B_na_21,B_ok_22, B_no_22,B_na_22,B_ok_23, B_no_23,B_na_23,B_ok_24, B_no_24,B_na_24,B_ok_25,B_no_25,B_na_25,B_ok_26, B_no_26,B_na_26,B_ok_27, B_no_27,B_na_27 ,B_ok_31,B_no_31,B_na_31,B_ok_32,B_no_32,B_na_32,B_ok_33,B_no_33,B_na_33,B_ok_34,B_no_34,B_na_34,B_ok_35,B_no_35,B_na_35,B_ok_36,B_no_36,B_na_36)

        # Imprime no final os valores salvos no banco de dados
        print(self.values)

tela = TelaPython()
tela.Iniciar()

