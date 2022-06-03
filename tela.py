import PySimpleGUI as sg



# Definindo as fontes
subsecao = ("Helvetica", 11, "bold")
ing = ("Helvetica", 9, "italic")
port = ("Helvetica", 10)


################################################################## AREA DE TESTES #########################################################################
# Definindo objetos para as perguntas


#include os arquivos txt para ter as perguntas, cada arquivo é uma aba do relatório
with open("pagina1.txt", "r") as tf:
    lines1 = tf.read().split(';')

#with open("pagina2.txt", "r") as tf:
#    lines2 = tf.read().split(',')

#with open("pagina3.txt", "r") as tf:
#    lines3 = tf.read().split(',')

#for line in lines:
#    print(line)

# len() = retorna no numero de elementos da lista
# range() = retorna uma lista de indices de 0 a n-1



###########################################################################################################################################################

class TelaPython:
    def __init__ (self):
### Definindo as fontes para colocar no text ####
        #Layout

        layout_1 = [
            [sg.Text('ELETRIFICATION DISTRIBUTION SYSTEMS DA SOLUTIONS PRODUCTS\nRELATÓRIO DE TESTES')],
            [sg.Text('Projeto / Project:',size=(12,0)),sg.Input(size=(100,0),key='projeto')],
            [sg.Text('PEP:',size=(12,0)),sg.Input(size=(50,0),key='pep')],
            [sg.Text('DATA ÍNICIO:',size=(12,0)),sg.Input(size=(10,0),key='inicio')],
            [sg.Text('DATA FIM:',size=(12,0)),sg.Input(size=(10,0),key='fim')],


            ###################################### 1 - INSPEÇÃO VISUAL E VERIFICAÇÕES DIMENSIONAIS   ###################################################
            #[sg.Text('1-INSPEÇÃO VISUAL E VERIFICAÇÕES DIMENSIONAIS', font=subsecao)],
            [sg.Text(text=list(lines1)[0], font=subsecao)],
            #[sg.Text('1.1 As unidades são construídas de acordo com as precrições de compra e de projeto', font=port)],
            [sg.Text(text=list(lines1)[1], font=port)],
            #[sg.Text(' Check that units are built according to the purchasing and design prescriptions', font=ing)],
            [sg.Text(text=list(lines1)[2], font=ing)],
            [sg.Radio('OK','prescricoes',key='okPrescricoes'),sg.Radio('NO','prescricoes',key='noPrescricoes'),sg.Radio('NA','prescricoes',key='naPrescricoes')],
            #[sg.Text('1.2 Verifique a ausência de deformidades e o nivelamento das chaparias', font=port)],
            [sg.Text(text=list(lines1)[3], font=port)],
            #[sg.Text(' Check the absence of deformations and flatness of the sheets', font=ing)],
            [sg.Text(text=list(lines1)[4], font=ing)],
            [sg.Radio('OK','chaparias',key='okChaparias'),sg.Radio('NO','chaparias',key='noChaparias'),sg.Radio('NA','chaparias',key='naChaparias')],
            #[sg.Text('1.3 Verifique a montagem correta e as conexões de aterramento em todos os componentes', font=port)],
            [sg.Text(text=list(lines1)[5], font=port)],
            #[sg.Text(' Check the correct counting and earthing connection in all components', font=ing)],
            [sg.Text(text=list(lines1)[6], font=ing)],
            [sg.Radio('OK','montagem',key='okMontagem'),sg.Radio('NO','montagem',key='noMontagem'),sg.Radio('NA','montagem',key='naMontagem')],
            #[sg.Text('1.4 Presença de dutos para passagem de cabos auxiliares de acordo com os desenhos', font=port)],
            [sg.Text(text=list(lines1)[7], font=port)],
            #[sg.Text(' Check the presence of the ducts for the passage of the auxiliary cables according to the drawings', font=ing)],
            [sg.Text(text=list(lines1)[8], font=ing)],
            [sg.Radio('OK','dutos',key='okDutos'),sg.Radio('NO','dutos',key='noDutos'),sg.Radio('NA','dutos',key='naDutos')],
            #[sg.Text('1.5 Disposição correta para passagem dos cabos de alimentação de acordo com os desenhos de montagem', font=port)],
            [sg.Text(text=list(lines1)[9], font=port)],
            #[sg.Text(' Check the correct disposition for the passage of the power cables according to the assembly drawings', font=ing)],
            [sg.Text(text=list(lines1)[10], font=ing)],
            [sg.Radio('OK','cabos',key='okCabos'),sg.Radio('NO','cabos',key='noCabos'),sg.Radio('NA','cabos',key='naCabos')],
            #[sg.Text('1.6 Verifique a disposição correta dos equipamentos de acordo com os desenhos do projeto', font=port)],
            [sg.Text(text=list(lines1)[11], font=port)],
            #[sg.Text(' Check the correct disposition of equipments according to the project drawings', font=ing)],
            [sg.Text(text=list(lines1)[12], font=ing)],
            [sg.Radio('OK','equipamentos',key='okEquipamentos'),sg.Radio('NO','equipamentos',key='noEquipamentos'),sg.Radio('NA','equipamentos',key='naEquipamentos')],
            #[sg.Text('1.7 Verifique se o equipamento não foi danificado durante a montagem', font=port)],
            [sg.Text(text=list(lines1)[13], font=port)],
            #[sg.Text(' Check that no damage in the apparatus occurred during the assembly', font=ing)],
            [sg.Text(text=list(lines1)[14], font=ing)],
            [sg.Radio('OK','danificado',key='okDanificado'),sg.Radio('NO','danificado',key='noDanificado'),sg.Radio('NA','danificado',key='naDanificado')],

            ###################################### 2 - VERIFICAÇÃO DE CONEXÃO E FUNCIONALIDADE ELÉTRICA   ###################################################
            #[sg.Text('2-VERIFICAÇÃO DE CONEXÃO E FUNCIONALIDADE ELÉTRICA', font=subsecao)],
            #[sg.Text('2.1 Verifique se a fiação, anilhas e crachás estão em conformidade com o diagrama funcional. Os terminais devem possuir numeração e identificação corretas.', font=port)],
            #[sg.Radio('OK','numeracao',key='okNumeracao'),sg.Radio('NO','numeracao',key='noNumeracao'),sg.Radio('NA','numeracao',key='naNumeracao')],
            #[sg.Text('2.2 Verifique a ausência de deformidades e o nivelamento das chaparias.', font=port)],
            #[sg.Radio('OK','chaparia',key='okChaparia'),sg.Radio('NO','chaparia',key='noChaparia'),sg.Radio('NA','chaparia',key='naChaparia')],
            #[sg.Text('2.3 Verifique a montagem correta e as conexões de aterramento em todos os componentes.', font=port)],
            #[sg.Radio('OK','aterramento',key='okAterramento'),sg.Radio('NO','aterramento',key='noAterramento'),sg.Radio('NA','aterramento',key='naAterramento')],
            #[sg.Text('2.4 Verifique se a inserção e extração dos disjuntores são impedidas quando estes fechados; a inserção e extração somente são permitidas quando o disjuntor estiver na posição aberta', font=port)],
            #[sg.Radio('OK','disjuntores',key='okDisjuntores'),sg.Radio('NO','disjuntores',key='noDisjuntores'),sg.Radio('NA','disjuntores',key='naDisjuntores')],
            
            #### ------ Botão de Confirmação ------- ####
            #[sg.Button('Enviar dados',size=(10,0))]
        ]


        ################## INSERINDO ABAS NA JANELA #################3######3

        tab_group = [
            [sg.TabGroup(
                [[sg.Tab('ABA1', layout_1, title_color='Red', tooltip='ABA1', element_justification='left'),]]
            )]
        ]



        #Janela
        #janela = sg.Window("CARTÃO DE INSPEÇÃO / Inspection card").layout(layout)
        janela = sg.Window('CARTÃO DE INSPEÇÃO / Inspection card', tab_group)
        #Extrair dados
        self.button, self.values = janela.Read()

        #Integração com o Banco de Dados

        #Manipulação dos Dados para geração do PDF
        
        
    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()