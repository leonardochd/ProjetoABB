from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
# import os

# A4 = (210*mm,297*mm)



# Converte milimetros para pontos
def mm2p(milimetros):
    return milimetros / 0.352777


#pastaApp=os.path.dirname(__file__)

def ger(T_PEP,T_NOMEPROJETO,B_ok_11,B_no_11,B_na_11,B_ok_12,B_no_12,B_na_12,B_ok_13,B_no_13,B_na_13,B_ok_14,B_no_14,B_na_14,B_ok_15,B_no_15,B_na_15,B_ok_16,B_no_16,B_na_16,B_ok_17,B_no_17,B_na_17,B_ok_21, B_no_21,B_na_21,B_ok_22, B_no_22,B_na_22,B_ok_23, B_no_23,B_na_23,B_ok_24, B_no_24,B_na_24,B_ok_25,B_no_25,B_na_25,B_ok_26, B_no_26,B_na_26,B_ok_27, B_no_27,B_na_27 ,B_ok_31,B_no_31,B_na_31,B_ok_32,B_no_32,B_na_32,B_ok_33,B_no_33,B_na_33,B_ok_34,B_no_34,B_na_34,B_ok_35,B_no_35,B_na_35,B_ok_36,B_no_36,B_na_36):

    margem = 15
    m_texto = 15


    cnv = canvas.Canvas("relatorio.pdf", pagesize=A4)


    ## PRIMEIRA PAGINA
    cnv.drawInlineImage("LogoABB.png", mm2p(margem), mm2p(250))

    # TITULO
    cnv.setFont("Helvetica", 14)
    cnv.drawString(mm2p(90),mm2p(277),"ELETRIFICATION DISTRIBUTION SYSTEMS")
    cnv.drawString(mm2p(127),mm2p(269),"DA SOLUTIONS PRODUCTS")

    #
    cnv.setFont("Helvetica", 12)
    cnv.drawString(mm2p(margem),mm2p(251),"RELATÓRIO DE TESTES")
    cnv.drawString(mm2p(margem),mm2p(244),"TEST REPORT")

    cnv.setFont("Helvetica", 8)
    cnv.drawString(mm2p(margem),mm2p(229),"A ABB Brasil certifica que o painel e testado em 100% do lote de acordo com as normas IEC NBR 61439-1:2017.")
    cnv.drawString(mm2p(margem),mm2p(224),"ABB Brazil certifies panel is tested at 100% of the lot in accordance with IEC NBR 61439-1:2017.")


    cnv.drawString(mm2p(margem),mm2p(206),"Considerações para os testes")
    cnv.drawString(mm2p(margem),mm2p(201),"Comments before testing")

    cnv.drawString(mm2p(margem),mm2p(192),"a) Serão testados os dispositivos funcionais de proteção e controle;")
    cnv.drawString(mm2p(margem),mm2p(187),"The typical protection and control funcional devices will be tested;")

    cnv.drawString(mm2p(margem),mm2p(178),"b) Para a configuração dos IEDs, será utilizado o software PMC600 em sua versão mais recente;")
    cnv.drawString(mm2p(margem),mm2p(173),"IEDs configuration will be made using PCM600 software, in its most recent version;")

    cnv.drawString(mm2p(margem),mm2p(164),"c) Todos os procedimentos que terão a necessidade da utilização destes software serão feitos atravéz de um Computador da ADD, que")
    cnv.drawString(mm2p(margem),mm2p(159),"terá disponivel todas as ferramentas acima mencionadas.")
    cnv.drawString(mm2p(margem),mm2p(154),"All the procedures that ned to use those software will be made using an ABB computer with all the tools installed on it.")

    cnv.showPage()

    ######################################### SEGUNDA PAGINA ######################################################################
    cnv.drawImage("logo.png", mm2p(margem), mm2p(270))

    # TITULO
    cnv.setFont("Helvetica", 15)
    cnv.drawString(mm2p(87),mm2p(277),"ELETRIFICATION DISTRIBUTION SYSTEMS")
    cnv.drawString(mm2p(125),mm2p(269),"DA SOLUTIONS PRODUCTS")


    cnv.setFont("Helvetica", 8)
    cnv.drawString(mm2p(15), mm2p(259),"PROJETO / Project")
    cnv.drawString(mm2p(56), mm2p(259),":")
    cnv.drawString(mm2p(60),mm2p(259),T_NOMEPROJETO)
    cnv.drawString(mm2p(15), mm2p(250),"PEP")
    cnv.drawString(mm2p(56), mm2p(250),":")
    cnv.drawString(mm2p(60),mm2p(250),T_PEP)
    cnv.drawString(mm2p(15), mm2p(232),"TESTE REALIZADO EM (TEST PERFORMED ON):")
    cnv.drawString(mm2p(20), mm2p(222),"DATA INÍCIO/ Beginning: ")
    
    cnv.drawString(mm2p(110), mm2p(222),"DATA FIM/ End: ")

    cnv.drawString(mm2p(15), mm2p(194),"TESTE REALIZADO POR (TEST SURVEYED BY):")
    cnv.drawString(mm2p(20), mm2p(179),"Nome (name)")
    cnv.drawString(mm2p(60), mm2p(179),"Empresa (Company)")
    cnv.drawString(mm2p(113), mm2p(179),"Assinatura (Sign)")
    #MONTAGEM DAS GRADES
    cnv.drawString(mm2p(18),mm2p(228),"______________________________________________________________________________________________________")
    cnv.drawString(mm2p(17.5),mm2p(225.5),"|")
    cnv.drawString(mm2p(17.5),mm2p(223),"|")
    cnv.drawString(mm2p(17.5),mm2p(220.5),"|")
    cnv.drawString(mm2p(18),mm2p(220.5),"______________________________________________________________________________________________________")
    cnv.drawString(mm2p(177.8),mm2p(225.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(223),"|")
    cnv.drawString(mm2p(177.8),mm2p(220.5),"|")
    cnv.drawString(mm2p(17.5),mm2p(218),"|")
    cnv.drawString(mm2p(17.5),mm2p(215.5),"|")
    cnv.drawString(mm2p(17.5),mm2p(213),"|")
    cnv.drawString(mm2p(177.8),mm2p(218),"|")
    cnv.drawString(mm2p(177.8),mm2p(215.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(213),"|")
    cnv.drawString(mm2p(18),mm2p(213),"______________________________________________________________________________________________________")
    cnv.drawString(mm2p(107),mm2p(218),"|")
    cnv.drawString(mm2p(107),mm2p(215.5),"|")
    cnv.drawString(mm2p(107),mm2p(213),"|")
    cnv.drawString(mm2p(107),mm2p(225.5),"|")
    cnv.drawString(mm2p(107),mm2p(223),"|")
    cnv.drawString(mm2p(107),mm2p(220.5),"|")
    cnv.drawString(mm2p(18),mm2p(184),"______________________________________________________________________________________________________")
    cnv.drawString(mm2p(17.5),mm2p(181.5),"|")
    cnv.drawString(mm2p(17.5),mm2p(179),"|")
    cnv.drawString(mm2p(17.5),mm2p(176.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(181.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(179),"|")
    cnv.drawString(mm2p(177.8),mm2p(176.5),"|")
    cnv.drawString(mm2p(18),mm2p(176.5),"______________________________________________________________________________________________________")
    cnv.drawString(mm2p(17.5),mm2p(174),"|")
    cnv.drawString(mm2p(17.5),mm2p(171.5),"|")
    cnv.drawString(mm2p(17.5),mm2p(169),"|")
    cnv.drawString(mm2p(17.5),mm2p(166.5),"|")
    cnv.drawString(mm2p(18),mm2p(166.5),"______________________________________________________________________________________________________")
    cnv.drawString(mm2p(177.8),mm2p(174),"|")
    cnv.drawString(mm2p(177.8),mm2p(171.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(169),"|")
    cnv.drawString(mm2p(177.8),mm2p(166.5),"|")
    cnv.drawString(mm2p(18),mm2p(166.5),"______________________________________________________________________________________________________")
    cnv.drawString(mm2p(17.5),mm2p(164),"|")
    cnv.drawString(mm2p(17.5),mm2p(161.5),"|")
    cnv.drawString(mm2p(17.5),mm2p(159),"|")
    cnv.drawString(mm2p(17.5),mm2p(156.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(164),"|")
    cnv.drawString(mm2p(177.8),mm2p(161.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(159),"|")
    cnv.drawString(mm2p(177.8),mm2p(156.5),"|")
    cnv.drawString(mm2p(18),mm2p(156.5),"______________________________________________________________________________________________________")
    cnv.drawString(mm2p(17.5),mm2p(154),"|")
    cnv.drawString(mm2p(17.5),mm2p(151.5),"|")
    cnv.drawString(mm2p(17.5),mm2p(149),"|")
    cnv.drawString(mm2p(17.5),mm2p(146.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(154),"|")
    cnv.drawString(mm2p(177.8),mm2p(151.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(149),"|")
    cnv.drawString(mm2p(177.8),mm2p(146.5),"|")
    cnv.drawString(mm2p(18),mm2p(146.5),"______________________________________________________________________________________________________")
    cnv.drawString(mm2p(17.5),mm2p(144),"|")
    cnv.drawString(mm2p(17.5),mm2p(141.5),"|")
    cnv.drawString(mm2p(17.5),mm2p(139),"|")
    cnv.drawString(mm2p(17.5),mm2p(136.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(144),"|")
    cnv.drawString(mm2p(177.8),mm2p(141.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(139),"|")
    cnv.drawString(mm2p(177.8),mm2p(136.5),"|")
    cnv.drawString(mm2p(18),mm2p(136.5),"______________________________________________________________________________________________________")
    cnv.drawString(mm2p(17.5),mm2p(134),"|")
    cnv.drawString(mm2p(17.5),mm2p(131.5),"|")
    cnv.drawString(mm2p(17.5),mm2p(129),"|")
    cnv.drawString(mm2p(17.5),mm2p(126.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(134),"|")
    cnv.drawString(mm2p(177.8),mm2p(131.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(129),"|")
    cnv.drawString(mm2p(177.8),mm2p(126.5),"|")
    cnv.drawString(mm2p(18),mm2p(126.5),"______________________________________________________________________________________________________")
    cnv.drawString(mm2p(17.5),mm2p(124),"|")
    cnv.drawString(mm2p(17.5),mm2p(121.5),"|")
    cnv.drawString(mm2p(17.5),mm2p(119),"|")
    cnv.drawString(mm2p(17.5),mm2p(116.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(124),"|")
    cnv.drawString(mm2p(177.8),mm2p(121.5),"|")
    cnv.drawString(mm2p(177.8),mm2p(119),"|")
    cnv.drawString(mm2p(177.8),mm2p(116.5),"|")
    cnv.drawString(mm2p(18),mm2p(116.5),"______________________________________________________________________________________________________")
    cnv.drawString(mm2p(58),mm2p(181.5),"|")
    cnv.drawString(mm2p(58),mm2p(179),"|")
    cnv.drawString(mm2p(58),mm2p(176.5),"|")
    cnv.drawString(mm2p(58),mm2p(174),"|")
    cnv.drawString(mm2p(58),mm2p(171.5),"|")
    cnv.drawString(mm2p(58),mm2p(169),"|")
    cnv.drawString(mm2p(58),mm2p(166.5),"|")
    cnv.drawString(mm2p(58),mm2p(164),"|")
    cnv.drawString(mm2p(58),mm2p(161.5),"|")
    cnv.drawString(mm2p(58),mm2p(159),"|")
    cnv.drawString(mm2p(58),mm2p(156.5),"|")
    cnv.drawString(mm2p(58),mm2p(154),"|")
    cnv.drawString(mm2p(58),mm2p(151.5),"|")
    cnv.drawString(mm2p(58),mm2p(149),"|")
    cnv.drawString(mm2p(58),mm2p(146.5),"|")
    cnv.drawString(mm2p(58),mm2p(144),"|")
    cnv.drawString(mm2p(58),mm2p(141.5),"|")
    cnv.drawString(mm2p(58),mm2p(139),"|")
    cnv.drawString(mm2p(58),mm2p(136.5),"|")
    cnv.drawString(mm2p(58),mm2p(134),"|")
    cnv.drawString(mm2p(58),mm2p(131.5),"|")
    cnv.drawString(mm2p(58),mm2p(129),"|")
    cnv.drawString(mm2p(58),mm2p(126.5),"|")
    cnv.drawString(mm2p(58),mm2p(124),"|")
    cnv.drawString(mm2p(58),mm2p(121.5),"|")
    cnv.drawString(mm2p(58),mm2p(119),"|")
    cnv.drawString(mm2p(58),mm2p(116.5),"|")
    cnv.drawString(mm2p(111),mm2p(181.5),"|")
    cnv.drawString(mm2p(111),mm2p(179),"|")
    cnv.drawString(mm2p(111),mm2p(176.5),"|")
    cnv.drawString(mm2p(111),mm2p(174),"|")
    cnv.drawString(mm2p(111),mm2p(171.5),"|")
    cnv.drawString(mm2p(111),mm2p(169),"|")
    cnv.drawString(mm2p(111),mm2p(166.5),"|")
    cnv.drawString(mm2p(111),mm2p(164),"|")
    cnv.drawString(mm2p(111),mm2p(161.5),"|")
    cnv.drawString(mm2p(111),mm2p(159),"|")
    cnv.drawString(mm2p(111),mm2p(156.5),"|")
    cnv.drawString(mm2p(111),mm2p(154),"|")
    cnv.drawString(mm2p(111),mm2p(151.5),"|")
    cnv.drawString(mm2p(111),mm2p(149),"|")
    cnv.drawString(mm2p(111),mm2p(146.5),"|")
    cnv.drawString(mm2p(111),mm2p(144),"|")
    cnv.drawString(mm2p(111),mm2p(141.5),"|")
    cnv.drawString(mm2p(111),mm2p(139),"|")
    cnv.drawString(mm2p(111),mm2p(136.5),"|")
    cnv.drawString(mm2p(111),mm2p(134),"|")
    cnv.drawString(mm2p(111),mm2p(131.5),"|")
    cnv.drawString(mm2p(111),mm2p(129),"|")
    cnv.drawString(mm2p(111),mm2p(126.5),"|")
    cnv.drawString(mm2p(111),mm2p(124),"|")
    cnv.drawString(mm2p(111),mm2p(121.5),"|")
    cnv.drawString(mm2p(111),mm2p(119),"|")
    cnv.drawString(mm2p(111),mm2p(116.5),"|")


    cnv.showPage()

    ######################################### TERCEIRA PAGINA ######################################################################

    # TITULO
    cnv.setFont("Helvetica", 15)
    cnv.drawString(mm2p(85),mm2p(277),"ELETRIFICATION DISTRIBUTION SYSTEMS")
    cnv.drawString(mm2p(125),mm2p(269),"DA SOLUTIONS PRODUCTS")

    #
    cnv.setFont("Helvetica", 10)
    cnv.drawString(mm2p(margem),mm2p(251),"INSPEÇÃO VISUAL E VERIFICAÇÕES DIMENSIONAIS")
    cnv.drawString(mm2p(margem),mm2p(247),"VISUAL AND DIMENSIONAL INSPECTION")


    cnv.setFont("Helvetica",7)
    ## APENAS OS TEXTOS POR ENQUANTO
    cnv.drawString(mm2p(130+10),mm2p(241),"ABB Interno")
    cnv.drawString(mm2p(155+10),mm2p(241),"Teste realizados com o cliente")

    ## Canto direito superior do quadrado 
    cnv.drawString(mm2p(130+10),mm2p(236),"OK")
    cnv.drawString(mm2p(139+10),mm2p(236),"NO")
    cnv.drawString(mm2p(148+10),mm2p(236),"NA")
    cnv.drawString(mm2p(159+10),mm2p(236),"OK")
    cnv.drawString(mm2p(169+10),mm2p(236),"NO")
    cnv.drawString(mm2p(177+10),mm2p(236),"Comment")

    OK = 140
    NO = 149
    NA = 158

    ## Primeira pergunta
    cnv.setFont("Helvetica",7)
    cnv.drawString(mm2p(m_texto),mm2p(222),"Verifique se as unidades são construídas de acordo com as prescrições de compra e de projeto.")
    cnv.drawString(mm2p(m_texto),mm2p(218),"Check that the are built according to the purchasing and design prescriptions.")
   
    if B_ok_11 == True:
        cnv.drawString(mm2p(OK),mm2p(220),"X")

    if B_no_11 == True:
        cnv.drawString(mm2p(NO),mm2p(220),"X")

    if B_na_11 == True:
        cnv.drawString(mm2p(NA),mm2p(220),"X")

    # MONTANDO AS GRADES
    # canto esquerdo
    cnv.drawString(mm2p(14),mm2p(223),"|")
    cnv.drawString(mm2p(14),mm2p(221),"|")
    cnv.drawString(mm2p(14),mm2p(219),"|")
    cnv.drawString(mm2p(14),mm2p(217),"|")
    cnv.drawString(mm2p(14),mm2p(215),"|")
    cnv.drawString(mm2p(14),mm2p(213),"|")
    cnv.drawString(mm2p(14),mm2p(211),"|")
    # canto direito
    cnv.drawString(mm2p(198),mm2p(223),"|")
    cnv.drawString(mm2p(198),mm2p(221),"|")
    cnv.drawString(mm2p(198),mm2p(219),"|")
    cnv.drawString(mm2p(198),mm2p(217),"|")
    cnv.drawString(mm2p(198),mm2p(215),"|")
    cnv.drawString(mm2p(198),mm2p(213),"|")
    cnv.drawString(mm2p(198),mm2p(211),"|")

    cnv.drawString(mm2p(137),mm2p(223),"|")
    cnv.drawString(mm2p(137),mm2p(221),"|")
    cnv.drawString(mm2p(137),mm2p(219),"|")
    cnv.drawString(mm2p(137),mm2p(217),"|")
    cnv.drawString(mm2p(137),mm2p(215),"|")
    cnv.drawString(mm2p(137),mm2p(213),"|")
    cnv.drawString(mm2p(137),mm2p(211),"|")

    cnv.drawString(mm2p(146),mm2p(223),"|")
    cnv.drawString(mm2p(146),mm2p(221),"|")
    cnv.drawString(mm2p(146),mm2p(219),"|")
    cnv.drawString(mm2p(146),mm2p(217),"|")
    cnv.drawString(mm2p(146),mm2p(215),"|")
    cnv.drawString(mm2p(146),mm2p(213),"|")
    cnv.drawString(mm2p(146),mm2p(211),"|")

    cnv.drawString(mm2p(155),mm2p(223),"|")
    cnv.drawString(mm2p(155),mm2p(221),"|")
    cnv.drawString(mm2p(155),mm2p(219),"|")
    cnv.drawString(mm2p(155),mm2p(217),"|")
    cnv.drawString(mm2p(155),mm2p(215),"|")
    cnv.drawString(mm2p(155),mm2p(213),"|")
    cnv.drawString(mm2p(155),mm2p(211),"|")

    cnv.drawString(mm2p(165),mm2p(223),"|")
    cnv.drawString(mm2p(165),mm2p(221),"|")
    cnv.drawString(mm2p(165),mm2p(219),"|")
    cnv.drawString(mm2p(165),mm2p(217),"|")
    cnv.drawString(mm2p(165),mm2p(215),"|")
    cnv.drawString(mm2p(165),mm2p(213),"|")
    cnv.drawString(mm2p(165),mm2p(211),"|")

    cnv.drawString(mm2p(175),mm2p(223),"|")
    cnv.drawString(mm2p(175),mm2p(221),"|")
    cnv.drawString(mm2p(175),mm2p(219),"|")
    cnv.drawString(mm2p(175),mm2p(217),"|")
    cnv.drawString(mm2p(175),mm2p(215),"|")
    cnv.drawString(mm2p(175),mm2p(213),"|")
    cnv.drawString(mm2p(175),mm2p(211),"|")

    cnv.drawString(mm2p(184),mm2p(223),"|")
    cnv.drawString(mm2p(184),mm2p(221),"|")
    cnv.drawString(mm2p(184),mm2p(219),"|")
    cnv.drawString(mm2p(184),mm2p(217),"|")
    cnv.drawString(mm2p(184),mm2p(215),"|")
    cnv.drawString(mm2p(184),mm2p(213),"|")
    cnv.drawString(mm2p(184),mm2p(211),"|")


    cnv.drawString(mm2p(14.5),mm2p(225),"______________________________________________________________________________________________________________________________________")
    cnv.drawString(mm2p(14.5),mm2p(211),"______________________________________________________________________________________________________________________________________")

    ## Segunda pergunta
    cnv.drawString(mm2p(m_texto),mm2p(202),"Verifique a ausência de deformidade e o nivelamento das chaparias.")
    cnv.drawString(mm2p(m_texto),mm2p(198),"Check the absence of deformations and flatness of the sheets.")

    if B_ok_12 == True:
        cnv.drawString(mm2p(OK),mm2p(200),"X")

    if B_no_12 == True:
        cnv.drawString(mm2p(NO),mm2p(200),"X")

    ## INSERINDO AS GRADES
    # canto esquerdo
    cnv.drawString(mm2p(14),mm2p(205),"|")
    cnv.drawString(mm2p(14),mm2p(207),"|")
    cnv.drawString(mm2p(14),mm2p(209),"|")

    cnv.drawString(mm2p(14),mm2p(203),"|")
    cnv.drawString(mm2p(14),mm2p(201),"|")
    cnv.drawString(mm2p(14),mm2p(199),"|")
    cnv.drawString(mm2p(14),mm2p(197),"|")
    cnv.drawString(mm2p(14),mm2p(195),"|")
    cnv.drawString(mm2p(14),mm2p(193),"|")
    cnv.drawString(mm2p(14),mm2p(191),"|")
    # canto direito
    cnv.drawString(mm2p(198),mm2p(205),"|")
    cnv.drawString(mm2p(198),mm2p(207),"|")
    cnv.drawString(mm2p(198),mm2p(209),"|")

    cnv.drawString(mm2p(198),mm2p(203),"|")
    cnv.drawString(mm2p(198),mm2p(201),"|")
    cnv.drawString(mm2p(198),mm2p(199),"|")
    cnv.drawString(mm2p(198),mm2p(197),"|")
    cnv.drawString(mm2p(198),mm2p(195),"|")
    cnv.drawString(mm2p(198),mm2p(193),"|")
    cnv.drawString(mm2p(198),mm2p(191),"|")

    #
    cnv.drawString(mm2p(137),mm2p(205),"|")
    cnv.drawString(mm2p(137),mm2p(207),"|")
    cnv.drawString(mm2p(137),mm2p(209),"|")

    cnv.drawString(mm2p(137),mm2p(203),"|")
    cnv.drawString(mm2p(137),mm2p(201),"|")
    cnv.drawString(mm2p(137),mm2p(199),"|")
    cnv.drawString(mm2p(137),mm2p(197),"|")
    cnv.drawString(mm2p(137),mm2p(195),"|")
    cnv.drawString(mm2p(137),mm2p(193),"|")
    cnv.drawString(mm2p(137),mm2p(191),"|")

    #
    cnv.drawString(mm2p(146),mm2p(205),"|")
    cnv.drawString(mm2p(146),mm2p(207),"|")
    cnv.drawString(mm2p(146),mm2p(209),"|")

    cnv.drawString(mm2p(146),mm2p(203),"|")
    cnv.drawString(mm2p(146),mm2p(201),"|")
    cnv.drawString(mm2p(146),mm2p(199),"|")
    cnv.drawString(mm2p(146),mm2p(197),"|")
    cnv.drawString(mm2p(146),mm2p(195),"|")
    cnv.drawString(mm2p(146),mm2p(193),"|")
    cnv.drawString(mm2p(146),mm2p(191),"|")

    #
    cnv.drawString(mm2p(155),mm2p(205),"|")
    cnv.drawString(mm2p(155),mm2p(207),"|")
    cnv.drawString(mm2p(155),mm2p(209),"|")

    cnv.drawString(mm2p(155),mm2p(203),"|")
    cnv.drawString(mm2p(155),mm2p(201),"|")
    cnv.drawString(mm2p(155),mm2p(199),"|")
    cnv.drawString(mm2p(155),mm2p(197),"|")
    cnv.drawString(mm2p(155),mm2p(195),"|")
    cnv.drawString(mm2p(155),mm2p(193),"|")
    cnv.drawString(mm2p(155),mm2p(191),"|")

    #
    cnv.drawString(mm2p(165),mm2p(205),"|")
    cnv.drawString(mm2p(165),mm2p(207),"|")
    cnv.drawString(mm2p(165),mm2p(209),"|")

    cnv.drawString(mm2p(165),mm2p(203),"|")
    cnv.drawString(mm2p(165),mm2p(201),"|")
    cnv.drawString(mm2p(165),mm2p(199),"|")
    cnv.drawString(mm2p(165),mm2p(197),"|")
    cnv.drawString(mm2p(165),mm2p(195),"|")
    cnv.drawString(mm2p(165),mm2p(193),"|")
    cnv.drawString(mm2p(165),mm2p(191),"|")

    #
    cnv.drawString(mm2p(175),mm2p(205),"|")
    cnv.drawString(mm2p(175),mm2p(207),"|")
    cnv.drawString(mm2p(175),mm2p(209),"|")

    cnv.drawString(mm2p(175),mm2p(203),"|")
    cnv.drawString(mm2p(175),mm2p(201),"|")
    cnv.drawString(mm2p(175),mm2p(199),"|")
    cnv.drawString(mm2p(175),mm2p(197),"|")
    cnv.drawString(mm2p(175),mm2p(195),"|")
    cnv.drawString(mm2p(175),mm2p(193),"|")
    cnv.drawString(mm2p(175),mm2p(191),"|")

    #
    cnv.drawString(mm2p(184),mm2p(205),"|")
    cnv.drawString(mm2p(184),mm2p(207),"|")
    cnv.drawString(mm2p(184),mm2p(209),"|")

    cnv.drawString(mm2p(184),mm2p(203),"|")
    cnv.drawString(mm2p(184),mm2p(201),"|")
    cnv.drawString(mm2p(184),mm2p(199),"|")
    cnv.drawString(mm2p(184),mm2p(197),"|")
    cnv.drawString(mm2p(184),mm2p(195),"|")
    cnv.drawString(mm2p(184),mm2p(193),"|")
    cnv.drawString(mm2p(184),mm2p(191),"|")


    cnv.drawString(mm2p(14.5),mm2p(191),"______________________________________________________________________________________________________________________________________")



    ## TERCEIRA PERGUNTA
    cnv.drawString(mm2p(m_texto),mm2p(182),"Verifique a montagem correta e as conexões de aterramento em todos os componentes.")
    cnv.drawString(mm2p(m_texto),mm2p(178),"Check the correct mounting and earthing connection in all components.")

    if B_ok_13 == True:
        cnv.drawString(mm2p(OK),mm2p(180),"X")

    if B_no_13 == True:
        cnv.drawString(mm2p(NO),mm2p(180),"X")

    if B_na_13 == True:
        cnv.drawString(mm2p(NA),mm2p(180),"X")

    ## INSERINDO AS GRADES
    # canto esquerdo
    cnv.drawString(mm2p(14),mm2p(185),"|")
    cnv.drawString(mm2p(14),mm2p(187),"|")
    cnv.drawString(mm2p(14),mm2p(189),"|")

    cnv.drawString(mm2p(14),mm2p(183),"|")
    cnv.drawString(mm2p(14),mm2p(181),"|")
    cnv.drawString(mm2p(14),mm2p(179),"|")
    cnv.drawString(mm2p(14),mm2p(177),"|")
    cnv.drawString(mm2p(14),mm2p(175),"|")
    cnv.drawString(mm2p(14),mm2p(173),"|")
    cnv.drawString(mm2p(14),mm2p(171),"|")
    # canto direito
    cnv.drawString(mm2p(198),mm2p(185),"|")
    cnv.drawString(mm2p(198),mm2p(187),"|")
    cnv.drawString(mm2p(198),mm2p(189),"|")

    cnv.drawString(mm2p(198),mm2p(183),"|")
    cnv.drawString(mm2p(198),mm2p(181),"|")
    cnv.drawString(mm2p(198),mm2p(179),"|")
    cnv.drawString(mm2p(198),mm2p(177),"|")
    cnv.drawString(mm2p(198),mm2p(175),"|")
    cnv.drawString(mm2p(198),mm2p(173),"|")
    cnv.drawString(mm2p(198),mm2p(171),"|")

    #
    cnv.drawString(mm2p(137),mm2p(185),"|")
    cnv.drawString(mm2p(137),mm2p(187),"|")
    cnv.drawString(mm2p(137),mm2p(189),"|")

    cnv.drawString(mm2p(137),mm2p(183),"|")
    cnv.drawString(mm2p(137),mm2p(181),"|")
    cnv.drawString(mm2p(137),mm2p(179),"|")
    cnv.drawString(mm2p(137),mm2p(177),"|")
    cnv.drawString(mm2p(137),mm2p(175),"|")
    cnv.drawString(mm2p(137),mm2p(173),"|")
    cnv.drawString(mm2p(137),mm2p(171),"|")

    #
    cnv.drawString(mm2p(146),mm2p(185),"|")
    cnv.drawString(mm2p(146),mm2p(187),"|")
    cnv.drawString(mm2p(146),mm2p(189),"|")

    cnv.drawString(mm2p(146),mm2p(183),"|")
    cnv.drawString(mm2p(146),mm2p(181),"|")
    cnv.drawString(mm2p(146),mm2p(179),"|")
    cnv.drawString(mm2p(146),mm2p(177),"|")
    cnv.drawString(mm2p(146),mm2p(175),"|")
    cnv.drawString(mm2p(146),mm2p(173),"|")
    cnv.drawString(mm2p(146),mm2p(171),"|")

    #
    cnv.drawString(mm2p(155),mm2p(185),"|")
    cnv.drawString(mm2p(155),mm2p(187),"|")
    cnv.drawString(mm2p(155),mm2p(189),"|")

    cnv.drawString(mm2p(155),mm2p(183),"|")
    cnv.drawString(mm2p(155),mm2p(181),"|")
    cnv.drawString(mm2p(155),mm2p(179),"|")
    cnv.drawString(mm2p(155),mm2p(177),"|")
    cnv.drawString(mm2p(155),mm2p(175),"|")
    cnv.drawString(mm2p(155),mm2p(173),"|")
    cnv.drawString(mm2p(155),mm2p(171),"|")

    #
    cnv.drawString(mm2p(165),mm2p(185),"|")
    cnv.drawString(mm2p(165),mm2p(187),"|")
    cnv.drawString(mm2p(165),mm2p(189),"|")

    cnv.drawString(mm2p(165),mm2p(183),"|")
    cnv.drawString(mm2p(165),mm2p(181),"|")
    cnv.drawString(mm2p(165),mm2p(179),"|")
    cnv.drawString(mm2p(165),mm2p(177),"|")
    cnv.drawString(mm2p(165),mm2p(175),"|")
    cnv.drawString(mm2p(165),mm2p(173),"|")
    cnv.drawString(mm2p(165),mm2p(171),"|")

    #
    cnv.drawString(mm2p(175),mm2p(185),"|")
    cnv.drawString(mm2p(175),mm2p(187),"|")
    cnv.drawString(mm2p(175),mm2p(189),"|")

    cnv.drawString(mm2p(175),mm2p(183),"|")
    cnv.drawString(mm2p(175),mm2p(181),"|")
    cnv.drawString(mm2p(175),mm2p(179),"|")
    cnv.drawString(mm2p(175),mm2p(177),"|")
    cnv.drawString(mm2p(175),mm2p(175),"|")
    cnv.drawString(mm2p(175),mm2p(173),"|")
    cnv.drawString(mm2p(175),mm2p(171),"|")

    #
    cnv.drawString(mm2p(184),mm2p(185),"|")
    cnv.drawString(mm2p(184),mm2p(187),"|")
    cnv.drawString(mm2p(184),mm2p(189),"|")

    cnv.drawString(mm2p(184),mm2p(183),"|")
    cnv.drawString(mm2p(184),mm2p(181),"|")
    cnv.drawString(mm2p(184),mm2p(179),"|")
    cnv.drawString(mm2p(184),mm2p(177),"|")
    cnv.drawString(mm2p(184),mm2p(175),"|")
    cnv.drawString(mm2p(184),mm2p(173),"|")
    cnv.drawString(mm2p(184),mm2p(171),"|")


    cnv.drawString(mm2p(14.5),mm2p(171),"______________________________________________________________________________________________________________________________________")


    ## Quarta pergunta
    cnv.drawString(mm2p(m_texto),mm2p(162),"Verifique a presença de dutos para a passagem de cabos auxiliares de acordo com os desenhos.")
    cnv.drawString(mm2p(m_texto),mm2p(158),"Check the presence of the ducts for the passage of the auxiliary cables according to the drawings.")

    if B_ok_14 == True:
        cnv.drawString(mm2p(OK),mm2p(160),"X")

    if B_no_14 == True:
        cnv.drawString(mm2p(NO),mm2p(160),"X")

    if B_na_14 == True:
        cnv.drawString(mm2p(NA),mm2p(160),"X")

    ## INSERINDO AS GRADES
    # canto esquerdo
    cnv.drawString(mm2p(14),mm2p(165),"|")
    cnv.drawString(mm2p(14),mm2p(167),"|")
    cnv.drawString(mm2p(14),mm2p(169),"|")

    cnv.drawString(mm2p(14),mm2p(163),"|")
    cnv.drawString(mm2p(14),mm2p(161),"|")
    cnv.drawString(mm2p(14),mm2p(159),"|")
    cnv.drawString(mm2p(14),mm2p(151),"|")
    cnv.drawString(mm2p(14),mm2p(157),"|")
    cnv.drawString(mm2p(14),mm2p(155),"|")
    cnv.drawString(mm2p(14),mm2p(153),"|")
    # canto direito
    cnv.drawString(mm2p(198),mm2p(165),"|")
    cnv.drawString(mm2p(198),mm2p(167),"|")
    cnv.drawString(mm2p(198),mm2p(169),"|")

    cnv.drawString(mm2p(198),mm2p(163),"|")
    cnv.drawString(mm2p(198),mm2p(161),"|")
    cnv.drawString(mm2p(198),mm2p(159),"|")
    cnv.drawString(mm2p(198),mm2p(151),"|")
    cnv.drawString(mm2p(198),mm2p(157),"|")
    cnv.drawString(mm2p(198),mm2p(155),"|")
    cnv.drawString(mm2p(198),mm2p(153),"|")

    #
    cnv.drawString(mm2p(137),mm2p(165),"|")
    cnv.drawString(mm2p(137),mm2p(167),"|")
    cnv.drawString(mm2p(137),mm2p(169),"|")

    cnv.drawString(mm2p(137),mm2p(163),"|")
    cnv.drawString(mm2p(137),mm2p(161),"|")
    cnv.drawString(mm2p(137),mm2p(159),"|")
    cnv.drawString(mm2p(137),mm2p(151),"|")
    cnv.drawString(mm2p(137),mm2p(157),"|")
    cnv.drawString(mm2p(137),mm2p(155),"|")
    cnv.drawString(mm2p(137),mm2p(153),"|")

    #
    cnv.drawString(mm2p(146),mm2p(165),"|")
    cnv.drawString(mm2p(146),mm2p(167),"|")
    cnv.drawString(mm2p(146),mm2p(169),"|")

    cnv.drawString(mm2p(146),mm2p(163),"|")
    cnv.drawString(mm2p(146),mm2p(161),"|")
    cnv.drawString(mm2p(146),mm2p(159),"|")
    cnv.drawString(mm2p(146),mm2p(151),"|")
    cnv.drawString(mm2p(146),mm2p(157),"|")
    cnv.drawString(mm2p(146),mm2p(155),"|")
    cnv.drawString(mm2p(146),mm2p(153),"|")

    #
    cnv.drawString(mm2p(155),mm2p(165),"|")
    cnv.drawString(mm2p(155),mm2p(167),"|")
    cnv.drawString(mm2p(155),mm2p(169),"|")

    cnv.drawString(mm2p(155),mm2p(163),"|")
    cnv.drawString(mm2p(155),mm2p(161),"|")
    cnv.drawString(mm2p(155),mm2p(159),"|")
    cnv.drawString(mm2p(155),mm2p(151),"|")
    cnv.drawString(mm2p(155),mm2p(157),"|")
    cnv.drawString(mm2p(155),mm2p(155),"|")
    cnv.drawString(mm2p(155),mm2p(153),"|")

    #
    cnv.drawString(mm2p(165),mm2p(165),"|")
    cnv.drawString(mm2p(165),mm2p(167),"|")
    cnv.drawString(mm2p(165),mm2p(169),"|")

    cnv.drawString(mm2p(165),mm2p(163),"|")
    cnv.drawString(mm2p(165),mm2p(161),"|")
    cnv.drawString(mm2p(165),mm2p(159),"|")
    cnv.drawString(mm2p(165),mm2p(151),"|")
    cnv.drawString(mm2p(165),mm2p(157),"|")
    cnv.drawString(mm2p(165),mm2p(155),"|")
    cnv.drawString(mm2p(165),mm2p(153),"|")

    #
    cnv.drawString(mm2p(175),mm2p(165),"|")
    cnv.drawString(mm2p(175),mm2p(167),"|")
    cnv.drawString(mm2p(175),mm2p(169),"|")

    cnv.drawString(mm2p(175),mm2p(163),"|")
    cnv.drawString(mm2p(175),mm2p(161),"|")
    cnv.drawString(mm2p(175),mm2p(159),"|")
    cnv.drawString(mm2p(175),mm2p(151),"|")
    cnv.drawString(mm2p(175),mm2p(157),"|")
    cnv.drawString(mm2p(175),mm2p(155),"|")
    cnv.drawString(mm2p(175),mm2p(153),"|")

    #
    cnv.drawString(mm2p(184),mm2p(165),"|")
    cnv.drawString(mm2p(184),mm2p(167),"|")
    cnv.drawString(mm2p(184),mm2p(169),"|")

    cnv.drawString(mm2p(184),mm2p(163),"|")
    cnv.drawString(mm2p(184),mm2p(161),"|")
    cnv.drawString(mm2p(184),mm2p(159),"|")
    cnv.drawString(mm2p(184),mm2p(151),"|")
    cnv.drawString(mm2p(184),mm2p(157),"|")
    cnv.drawString(mm2p(184),mm2p(155),"|")
    cnv.drawString(mm2p(184),mm2p(153),"|")


    cnv.drawString(mm2p(14.5),mm2p(151),"______________________________________________________________________________________________________________________________________")


    # Quinta pergunta
    cnv.drawString(mm2p(m_texto),mm2p(142),"Verifique a disposição correta para passagem dos cabos de alimentação de acordo com os desenhos")
    cnv.drawString(mm2p(m_texto),mm2p(142-4),"de montagem.")
    cnv.drawString(mm2p(m_texto),mm2p(138-4),"Check the correct disposition for the passage of the power cables according to the assembly drawings.")

    if B_ok_15 == True:
        cnv.drawString(mm2p(OK),mm2p(138),"X")

    if B_no_15 == True:
        cnv.drawString(mm2p(NO),mm2p(138),"X")

    if B_na_15 == True:
        cnv.drawString(mm2p(NA),mm2p(138),"X")

    ## INSERINDO AS GRADES
    # canto esquerdo
    cnv.drawString(mm2p(14),mm2p(145),"|")
    cnv.drawString(mm2p(14),mm2p(147),"|")
    cnv.drawString(mm2p(14),mm2p(149),"|")

    cnv.drawString(mm2p(14),mm2p(143),"|")
    cnv.drawString(mm2p(14),mm2p(141),"|")
    cnv.drawString(mm2p(14),mm2p(139),"|")
    cnv.drawString(mm2p(14),mm2p(137),"|")
    cnv.drawString(mm2p(14),mm2p(135),"|")
    cnv.drawString(mm2p(14),mm2p(133),"|")
    cnv.drawString(mm2p(14),mm2p(131),"|")
    cnv.drawString(mm2p(14),mm2p(129),"|")
    cnv.drawString(mm2p(14),mm2p(127),"|")

    # canto direito
    cnv.drawString(mm2p(198),mm2p(145),"|")
    cnv.drawString(mm2p(198),mm2p(147),"|")
    cnv.drawString(mm2p(198),mm2p(149),"|")

    cnv.drawString(mm2p(198),mm2p(143),"|")
    cnv.drawString(mm2p(198),mm2p(141),"|")
    cnv.drawString(mm2p(198),mm2p(139),"|")
    cnv.drawString(mm2p(198),mm2p(137),"|")
    cnv.drawString(mm2p(198),mm2p(135),"|")
    cnv.drawString(mm2p(198),mm2p(133),"|")
    cnv.drawString(mm2p(198),mm2p(131),"|")
    cnv.drawString(mm2p(198),mm2p(129),"|")
    cnv.drawString(mm2p(198),mm2p(127),"|")

    #
    cnv.drawString(mm2p(137),mm2p(145),"|")
    cnv.drawString(mm2p(137),mm2p(147),"|")
    cnv.drawString(mm2p(137),mm2p(149),"|")

    cnv.drawString(mm2p(137),mm2p(143),"|")
    cnv.drawString(mm2p(137),mm2p(141),"|")
    cnv.drawString(mm2p(137),mm2p(139),"|")
    cnv.drawString(mm2p(137),mm2p(137),"|")
    cnv.drawString(mm2p(137),mm2p(135),"|")
    cnv.drawString(mm2p(137),mm2p(133),"|")
    cnv.drawString(mm2p(137),mm2p(131),"|")
    cnv.drawString(mm2p(137),mm2p(129),"|")
    cnv.drawString(mm2p(137),mm2p(127),"|")

    #
    cnv.drawString(mm2p(146),mm2p(145),"|")
    cnv.drawString(mm2p(146),mm2p(147),"|")
    cnv.drawString(mm2p(146),mm2p(149),"|")

    cnv.drawString(mm2p(146),mm2p(143),"|")
    cnv.drawString(mm2p(146),mm2p(141),"|")
    cnv.drawString(mm2p(146),mm2p(139),"|")
    cnv.drawString(mm2p(146),mm2p(137),"|")
    cnv.drawString(mm2p(146),mm2p(135),"|")
    cnv.drawString(mm2p(146),mm2p(133),"|")
    cnv.drawString(mm2p(146),mm2p(131),"|")
    cnv.drawString(mm2p(146),mm2p(129),"|")
    cnv.drawString(mm2p(146),mm2p(127),"|")

    #
    cnv.drawString(mm2p(155),mm2p(145),"|")
    cnv.drawString(mm2p(155),mm2p(147),"|")
    cnv.drawString(mm2p(155),mm2p(149),"|")

    cnv.drawString(mm2p(155),mm2p(143),"|")
    cnv.drawString(mm2p(155),mm2p(141),"|")
    cnv.drawString(mm2p(155),mm2p(139),"|")
    cnv.drawString(mm2p(155),mm2p(137),"|")
    cnv.drawString(mm2p(155),mm2p(135),"|")
    cnv.drawString(mm2p(155),mm2p(133),"|")
    cnv.drawString(mm2p(155),mm2p(131),"|")
    cnv.drawString(mm2p(155),mm2p(129),"|")
    cnv.drawString(mm2p(155),mm2p(127),"|")

    #
    cnv.drawString(mm2p(165),mm2p(145),"|")
    cnv.drawString(mm2p(165),mm2p(147),"|")
    cnv.drawString(mm2p(165),mm2p(149),"|")

    cnv.drawString(mm2p(165),mm2p(143),"|")
    cnv.drawString(mm2p(165),mm2p(141),"|")
    cnv.drawString(mm2p(165),mm2p(139),"|")
    cnv.drawString(mm2p(165),mm2p(137),"|")
    cnv.drawString(mm2p(165),mm2p(135),"|")
    cnv.drawString(mm2p(165),mm2p(133),"|")
    cnv.drawString(mm2p(165),mm2p(131),"|")
    cnv.drawString(mm2p(165),mm2p(129),"|")
    cnv.drawString(mm2p(165),mm2p(127),"|")

    #
    cnv.drawString(mm2p(175),mm2p(145),"|")
    cnv.drawString(mm2p(175),mm2p(147),"|")
    cnv.drawString(mm2p(175),mm2p(149),"|")

    cnv.drawString(mm2p(175),mm2p(143),"|")
    cnv.drawString(mm2p(175),mm2p(141),"|")
    cnv.drawString(mm2p(175),mm2p(139),"|")
    cnv.drawString(mm2p(175),mm2p(137),"|")
    cnv.drawString(mm2p(175),mm2p(135),"|")
    cnv.drawString(mm2p(175),mm2p(133),"|")
    cnv.drawString(mm2p(175),mm2p(131),"|")
    cnv.drawString(mm2p(175),mm2p(129),"|")
    cnv.drawString(mm2p(175),mm2p(127),"|")

    #
    cnv.drawString(mm2p(184),mm2p(145),"|")
    cnv.drawString(mm2p(184),mm2p(147),"|")
    cnv.drawString(mm2p(184),mm2p(149),"|")

    cnv.drawString(mm2p(184),mm2p(143),"|")
    cnv.drawString(mm2p(184),mm2p(141),"|")
    cnv.drawString(mm2p(184),mm2p(139),"|")
    cnv.drawString(mm2p(184),mm2p(137),"|")
    cnv.drawString(mm2p(184),mm2p(135),"|")
    cnv.drawString(mm2p(184),mm2p(133),"|")
    cnv.drawString(mm2p(184),mm2p(131),"|")
    cnv.drawString(mm2p(184),mm2p(129),"|")
    cnv.drawString(mm2p(184),mm2p(127),"|")


    cnv.drawString(mm2p(14.5),mm2p(127),"______________________________________________________________________________________________________________________________________")


    ## Sexta pergunta
    cnv.drawString(mm2p(m_texto),mm2p(114),"Verifique a disposição correta dos equipamentos de acordo com os desenhos do projeto.")
    cnv.drawString(mm2p(m_texto),mm2p(108),"Check the correct disposition of equipments according to the project drawings.")

    if B_ok_16 == True:
        cnv.drawString(mm2p(OK),mm2p(111),"X")

    if B_no_16 == True:
        cnv.drawString(mm2p(NO),mm2p(111),"X")

    if B_na_16 == True:
        cnv.drawString(mm2p(NA),mm2p(111),"X")

    ## INSERINDO AS GRADES
    # canto esquerdo
    cnv.drawString(mm2p(14),mm2p(117),"|")
    cnv.drawString(mm2p(14),mm2p(119),"|")
    cnv.drawString(mm2p(14),mm2p(121),"|")
    cnv.drawString(mm2p(14),mm2p(123),"|")
    cnv.drawString(mm2p(14),mm2p(125),"|")

    cnv.drawString(mm2p(14),mm2p(115),"|")
    cnv.drawString(mm2p(14),mm2p(113),"|")
    cnv.drawString(mm2p(14),mm2p(111),"|")
    cnv.drawString(mm2p(14),mm2p(109),"|")
    cnv.drawString(mm2p(14),mm2p(107),"|")
    cnv.drawString(mm2p(14),mm2p(105),"|")
    cnv.drawString(mm2p(14),mm2p(103),"|")
    # canto direito
    cnv.drawString(mm2p(198),mm2p(117),"|")
    cnv.drawString(mm2p(198),mm2p(119),"|")
    cnv.drawString(mm2p(198),mm2p(121),"|")
    cnv.drawString(mm2p(198),mm2p(123),"|")
    cnv.drawString(mm2p(198),mm2p(125),"|")

    cnv.drawString(mm2p(198),mm2p(115),"|")
    cnv.drawString(mm2p(198),mm2p(113),"|")
    cnv.drawString(mm2p(198),mm2p(111),"|")
    cnv.drawString(mm2p(198),mm2p(109),"|")
    cnv.drawString(mm2p(198),mm2p(107),"|")
    cnv.drawString(mm2p(198),mm2p(105),"|")
    cnv.drawString(mm2p(198),mm2p(103),"|")

    #
    cnv.drawString(mm2p(137),mm2p(117),"|")
    cnv.drawString(mm2p(137),mm2p(119),"|")
    cnv.drawString(mm2p(137),mm2p(121),"|")
    cnv.drawString(mm2p(137),mm2p(123),"|")
    cnv.drawString(mm2p(137),mm2p(125),"|")

    cnv.drawString(mm2p(137),mm2p(115),"|")
    cnv.drawString(mm2p(137),mm2p(113),"|")
    cnv.drawString(mm2p(137),mm2p(111),"|")
    cnv.drawString(mm2p(137),mm2p(109),"|")
    cnv.drawString(mm2p(137),mm2p(107),"|")
    cnv.drawString(mm2p(137),mm2p(105),"|")
    cnv.drawString(mm2p(137),mm2p(103),"|")

    #
    cnv.drawString(mm2p(146),mm2p(117),"|")
    cnv.drawString(mm2p(146),mm2p(119),"|")
    cnv.drawString(mm2p(146),mm2p(121),"|")
    cnv.drawString(mm2p(146),mm2p(123),"|")
    cnv.drawString(mm2p(146),mm2p(125),"|")

    cnv.drawString(mm2p(146),mm2p(115),"|")
    cnv.drawString(mm2p(146),mm2p(113),"|")
    cnv.drawString(mm2p(146),mm2p(111),"|")
    cnv.drawString(mm2p(146),mm2p(109),"|")
    cnv.drawString(mm2p(146),mm2p(107),"|")
    cnv.drawString(mm2p(146),mm2p(105),"|")
    cnv.drawString(mm2p(146),mm2p(103),"|")

    #
    cnv.drawString(mm2p(155),mm2p(117),"|")
    cnv.drawString(mm2p(155),mm2p(119),"|")
    cnv.drawString(mm2p(155),mm2p(121),"|")
    cnv.drawString(mm2p(155),mm2p(123),"|")
    cnv.drawString(mm2p(155),mm2p(125),"|")

    cnv.drawString(mm2p(155),mm2p(115),"|")
    cnv.drawString(mm2p(155),mm2p(113),"|")
    cnv.drawString(mm2p(155),mm2p(111),"|")
    cnv.drawString(mm2p(155),mm2p(109),"|")
    cnv.drawString(mm2p(155),mm2p(107),"|")
    cnv.drawString(mm2p(155),mm2p(105),"|")
    cnv.drawString(mm2p(155),mm2p(103),"|")

    #
    cnv.drawString(mm2p(165),mm2p(117),"|")
    cnv.drawString(mm2p(165),mm2p(119),"|")
    cnv.drawString(mm2p(165),mm2p(121),"|")
    cnv.drawString(mm2p(165),mm2p(123),"|")
    cnv.drawString(mm2p(165),mm2p(125),"|")

    cnv.drawString(mm2p(165),mm2p(115),"|")
    cnv.drawString(mm2p(165),mm2p(113),"|")
    cnv.drawString(mm2p(165),mm2p(111),"|")
    cnv.drawString(mm2p(165),mm2p(109),"|")
    cnv.drawString(mm2p(165),mm2p(107),"|")
    cnv.drawString(mm2p(165),mm2p(105),"|")
    cnv.drawString(mm2p(165),mm2p(103),"|")

    #
    cnv.drawString(mm2p(175),mm2p(117),"|")
    cnv.drawString(mm2p(175),mm2p(119),"|")
    cnv.drawString(mm2p(175),mm2p(121),"|")
    cnv.drawString(mm2p(175),mm2p(123),"|")
    cnv.drawString(mm2p(175),mm2p(125),"|")

    cnv.drawString(mm2p(175),mm2p(115),"|")
    cnv.drawString(mm2p(175),mm2p(113),"|")
    cnv.drawString(mm2p(175),mm2p(111),"|")
    cnv.drawString(mm2p(175),mm2p(109),"|")
    cnv.drawString(mm2p(175),mm2p(107),"|")
    cnv.drawString(mm2p(175),mm2p(105),"|")
    cnv.drawString(mm2p(175),mm2p(103),"|")

    cnv.drawString(mm2p(184),mm2p(117),"|")
    cnv.drawString(mm2p(184),mm2p(119),"|")
    cnv.drawString(mm2p(184),mm2p(121),"|")
    cnv.drawString(mm2p(184),mm2p(123),"|")
    cnv.drawString(mm2p(184),mm2p(125),"|")

    cnv.drawString(mm2p(184),mm2p(115),"|")
    cnv.drawString(mm2p(184),mm2p(113),"|")
    cnv.drawString(mm2p(184),mm2p(111),"|")
    cnv.drawString(mm2p(184),mm2p(109),"|")
    cnv.drawString(mm2p(184),mm2p(107),"|")
    cnv.drawString(mm2p(184),mm2p(105),"|")
    cnv.drawString(mm2p(184),mm2p(103),"|")


    cnv.drawString(mm2p(14.5),mm2p(103),"______________________________________________________________________________________________________________________________________")


    ## Sétima pergunta
    cnv.drawString(mm2p(m_texto),mm2p(94),"Verifique se o equipamento não foi danificado durante a montagem.")
    cnv.drawString(mm2p(m_texto),mm2p(88),"Check that no damage in the apparatus occurred during the assembly.")

    if B_ok_17 == True:
        cnv.drawString(mm2p(OK),mm2p(91),"X")

    if B_no_17 == True:
        cnv.drawString(mm2p(NO),mm2p(91),"X")

    if B_na_17 == True:
        cnv.drawString(mm2p(NA),mm2p(91),"X")

    ## INSERINDO AS GRADES
    # canto esquerdo
    cnv.drawString(mm2p(14),mm2p(97),"|")
    cnv.drawString(mm2p(14),mm2p(99),"|")
    cnv.drawString(mm2p(14),mm2p(101),"|")

    cnv.drawString(mm2p(14),mm2p(95),"|")
    cnv.drawString(mm2p(14),mm2p(93),"|")
    cnv.drawString(mm2p(14),mm2p(91),"|")
    cnv.drawString(mm2p(14),mm2p(89),"|")
    cnv.drawString(mm2p(14),mm2p(87),"|")
    cnv.drawString(mm2p(14),mm2p(85),"|")
    cnv.drawString(mm2p(14),mm2p(83),"|")
    # canto direito
    cnv.drawString(mm2p(198),mm2p(97),"|")
    cnv.drawString(mm2p(198),mm2p(99),"|")
    cnv.drawString(mm2p(198),mm2p(101),"|")

    cnv.drawString(mm2p(198),mm2p(95),"|")
    cnv.drawString(mm2p(198),mm2p(93),"|")
    cnv.drawString(mm2p(198),mm2p(91),"|")
    cnv.drawString(mm2p(198),mm2p(89),"|")
    cnv.drawString(mm2p(198),mm2p(87),"|")
    cnv.drawString(mm2p(198),mm2p(85),"|")
    cnv.drawString(mm2p(198),mm2p(83),"|")

    #
    cnv.drawString(mm2p(137),mm2p(97),"|")
    cnv.drawString(mm2p(137),mm2p(99),"|")
    cnv.drawString(mm2p(137),mm2p(101),"|")

    cnv.drawString(mm2p(137),mm2p(95),"|")
    cnv.drawString(mm2p(137),mm2p(93),"|")
    cnv.drawString(mm2p(137),mm2p(91),"|")
    cnv.drawString(mm2p(137),mm2p(89),"|")
    cnv.drawString(mm2p(137),mm2p(87),"|")
    cnv.drawString(mm2p(137),mm2p(85),"|")
    cnv.drawString(mm2p(137),mm2p(83),"|")

    #
    cnv.drawString(mm2p(146),mm2p(97),"|")
    cnv.drawString(mm2p(146),mm2p(99),"|")
    cnv.drawString(mm2p(146),mm2p(101),"|")

    cnv.drawString(mm2p(146),mm2p(95),"|")
    cnv.drawString(mm2p(146),mm2p(93),"|")
    cnv.drawString(mm2p(146),mm2p(91),"|")
    cnv.drawString(mm2p(146),mm2p(89),"|")
    cnv.drawString(mm2p(146),mm2p(87),"|")
    cnv.drawString(mm2p(146),mm2p(85),"|")
    cnv.drawString(mm2p(146),mm2p(83),"|")

    #
    cnv.drawString(mm2p(155),mm2p(97),"|")
    cnv.drawString(mm2p(155),mm2p(99),"|")
    cnv.drawString(mm2p(155),mm2p(101),"|")

    cnv.drawString(mm2p(155),mm2p(95),"|")
    cnv.drawString(mm2p(155),mm2p(93),"|")
    cnv.drawString(mm2p(155),mm2p(91),"|")
    cnv.drawString(mm2p(155),mm2p(89),"|")
    cnv.drawString(mm2p(155),mm2p(87),"|")
    cnv.drawString(mm2p(155),mm2p(85),"|")
    cnv.drawString(mm2p(155),mm2p(83),"|")

    #
    cnv.drawString(mm2p(165),mm2p(97),"|")
    cnv.drawString(mm2p(165),mm2p(99),"|")
    cnv.drawString(mm2p(165),mm2p(101),"|")

    cnv.drawString(mm2p(165),mm2p(95),"|")
    cnv.drawString(mm2p(165),mm2p(93),"|")
    cnv.drawString(mm2p(165),mm2p(91),"|")
    cnv.drawString(mm2p(165),mm2p(89),"|")
    cnv.drawString(mm2p(165),mm2p(87),"|")
    cnv.drawString(mm2p(165),mm2p(85),"|")
    cnv.drawString(mm2p(165),mm2p(83),"|")

    #
    cnv.drawString(mm2p(175),mm2p(97),"|")
    cnv.drawString(mm2p(175),mm2p(99),"|")
    cnv.drawString(mm2p(175),mm2p(101),"|")

    cnv.drawString(mm2p(175),mm2p(95),"|")
    cnv.drawString(mm2p(175),mm2p(93),"|")
    cnv.drawString(mm2p(175),mm2p(91),"|")
    cnv.drawString(mm2p(175),mm2p(89),"|")
    cnv.drawString(mm2p(175),mm2p(87),"|")
    cnv.drawString(mm2p(175),mm2p(85),"|")
    cnv.drawString(mm2p(175),mm2p(83),"|")

    #
    cnv.drawString(mm2p(184),mm2p(97),"|")
    cnv.drawString(mm2p(184),mm2p(99),"|")
    cnv.drawString(mm2p(184),mm2p(101),"|")

    cnv.drawString(mm2p(184),mm2p(95),"|")
    cnv.drawString(mm2p(184),mm2p(93),"|")
    cnv.drawString(mm2p(184),mm2p(91),"|")
    cnv.drawString(mm2p(184),mm2p(89),"|")
    cnv.drawString(mm2p(184),mm2p(87),"|")
    cnv.drawString(mm2p(184),mm2p(85),"|")
    cnv.drawString(mm2p(184),mm2p(83),"|")


    cnv.drawString(mm2p(14.5),mm2p(83),"______________________________________________________________________________________________________________________________________")

    cnv.drawString(mm2p(14),mm2p(244),"________________________________________________________________________________________________________________________________________")



    cnv.showPage()

    ######################################### QUARTA PAGINA ######################################################################
    cnv.drawImage("logo.png", mm2p(margem), mm2p(270))

    # TITULO
    cnv.setFont("Helvetica", 15)
    cnv.drawString(mm2p(87),mm2p(277),"ELETRIFICATION DISTRIBUTION SYSTEMS")
    cnv.drawString(mm2p(125),mm2p(269),"DA SOLUTIONS PRODUCTS")

    #
    cnv.setFont("Helvetica", 10)
    cnv.drawString(mm2p(margem),mm2p(251),"VERIFICAÇÃO DE CONEXÃO E FUNCIONALIDADE ELÉTRICA")
    cnv.drawString(mm2p(margem),mm2p(247),"CHECK OF THE ELECTRICAL OPERATION AND WIRING")


    cnv.setFont("Helvetica",7)
    ## APENAS OS TEXTOS POR ENQUANTO
    cnv.drawString(mm2p(130+10),mm2p(241),"ABB Interno")
    cnv.drawString(mm2p(155+10),mm2p(241),"Testes realizados com o cliente")

    ## Canto direito superior do quadrado 
    cnv.drawString(mm2p(130+10),mm2p(236),"OK")
    cnv.drawString(mm2p(139+10),mm2p(236),"NO")
    cnv.drawString(mm2p(148+10),mm2p(236),"NA")
    cnv.drawString(mm2p(155+10),mm2p(236),"OK")
    cnv.drawString(mm2p(165+10),mm2p(236),"NO")
    cnv.drawString(mm2p(173+10),mm2p(236),"Comment")

    cnv.drawString(mm2p(14),mm2p(244),"________________________________________________________________________________________________________________________________________")



    ## Primeira pergunta
    cnv.setFont("Helvetica",7)
    cnv.drawString(mm2p(m_texto),mm2p(222),"Verifique se a fiação, anilhas e crachás estão em conformidade com o diagrama funcional.")
    cnv.drawString(mm2p(m_texto),mm2p(218),"Os terminais devem possuir numeração e identificação corretas.")
    cnv.drawString(mm2p(m_texto),mm2p(214),"Check that the wiring and terminals are in compliance with the functional diagram.")
    cnv.drawString(mm2p(m_texto),mm2p(210),"Terminals must have the correct identification and numbering.")

    if B_ok_21 == True:
        cnv.drawString(mm2p(OK),mm2p(216),"X")

    if B_no_21 == True:
        cnv.drawString(mm2p(NO),mm2p(216),"X")

    if B_na_21 == True:
        cnv.drawString(mm2p(NA),mm2p(216),"X")

    ## Segunda pergunta
    cnv.drawString(mm2p(m_texto),mm2p(198),"Verifique se a fiação de interligação está em conformidade com o diagrama.")
    cnv.drawString(mm2p(m_texto),mm2p(194),"A interligação deve possuir identificações e numerações de acordo com o diagrama.")
    cnv.drawString(mm2p(m_texto),mm2p(190),"Check that the interconnection wiring is in compliance with the diagram.")
    cnv.drawString(mm2p(m_texto),mm2p(186),"Interconnection and customer´s terminals must have the identification and numbering according")
    cnv.drawString(mm2p(m_texto),mm2p(182),"to the diagram.")

    if B_ok_22 == True:
        cnv.drawString(mm2p(OK),mm2p(190),"X")

    if B_no_22 == True:
        cnv.drawString(mm2p(NO),mm2p(190),"X")
    
    if B_na_22 == True:
        cnv.drawString(mm2p(NA),mm2p(190),"X")

    ## Terceira pergunta
    cnv.drawString(mm2p(m_texto),mm2p(170),"Verifique a conformidade das funções lógicas de sinalização nos IEDs.")
    cnv.drawString(mm2p(m_texto),mm2p(166),"Check the compliance of the logic functions of signaling in IEDs.")

    if B_ok_23 == True:
        cnv.drawString(mm2p(OK),mm2p(168),"X")

    if B_no_23 == True:
        cnv.drawString(mm2p(NO),mm2p(168),"X")

    if B_na_23 == True:
        cnv.drawString(mm2p(NA),mm2p(168),"X")

    ## Quarta pergunta
    cnv.drawString(mm2p(m_texto),mm2p(154),"Force as saídas digitais no IED e verifique se as mesmos estão comutando corretamente,")
    cnv.drawString(mm2p(m_texto),mm2p(150),"medindo continuidade na régua de borne.")
    cnv.drawString(mm2p(m_texto),mm2p(146),"Force the digitals outputs on the IED and check that they are switching correctly,")
    cnv.drawString(mm2p(m_texto),mm2p(142),"measuring continuity in the terminals.")

    if B_ok_24 == True:
        cnv.drawString(mm2p(OK),mm2p(148),"X")

    if B_no_24 == True:
        cnv.drawString(mm2p(NO),mm2p(148),"X")

    if B_na_24 == True:
        cnv.drawString(mm2p(NA),mm2p(148),"X")

    # Quinta pergunta
    cnv.drawString(mm2p(m_texto),mm2p(130),"Realize os fechamentos corretos dos bornes equivalentes das entradas digitais")
    cnv.drawString(mm2p(m_texto),mm2p(126),"e verifique a correta atuação no IED.")
    cnv.drawString(mm2p(m_texto),mm2p(122),"Perform the correct closings on the equivalent terminals of the digital inputs")
    cnv.drawString(mm2p(m_texto),mm2p(118),"and check the correct performance on the IED.")

    if B_ok_25 == True:
        cnv.drawString(mm2p(OK),mm2p(124),"X")

    if B_no_25 == True:
        cnv.drawString(mm2p(NO),mm2p(124),"X")

    if B_na_25 == True:
        cnv.drawString(mm2p(NA),mm2p(124),"X")


    ## Sexta pergunta
    cnv.drawString(mm2p(m_texto),mm2p(106),"Verifque o correto funcionamento das Entradas/Saídas analógicas.")
    cnv.drawString(mm2p(m_texto),mm2p(102),"Check the correct operation of the analog inputs / outputs.")

    if B_ok_26 == True:
        cnv.drawString(mm2p(OK),mm2p(104),"X")

    if B_no_26 == True:
        cnv.drawString(mm2p(NO),mm2p(104),"X")

    if B_na_26 == True:
        cnv.drawString(mm2p(NA),mm2p(104),"X")

    ## Sétima pergunta
    cnv.drawString(mm2p(m_texto),mm2p(90),"Verifique a correta funcionalidade elétrica dos equipamentos de comunicação.")
    cnv.drawString(mm2p(m_texto),mm2p(86),"Check the correct electrical operation of the communication equipament.")

    if B_ok_27 == True:
        cnv.drawString(mm2p(OK),mm2p(88),"X")

    if B_no_27 == True:
        cnv.drawString(mm2p(NO),mm2p(88),"X")

    if B_na_27 == True:
        cnv.drawString(mm2p(NA),mm2p(88),"X")


    # CONSTRUÇÂO DA TABELA
    cnv.drawString(mm2p(14),mm2p(244),"________________________________________________________________________________________________________________________________________")
    cnv.drawString(mm2p(13.5),mm2p(241.9),"|")
    cnv.drawString(mm2p(13.5),mm2p(240),"|")
    cnv.drawString(mm2p(13.5),mm2p(238),"|")
    cnv.drawString(mm2p(13.5),mm2p(236),"|")
    cnv.drawString(mm2p(13.5),mm2p(234),"|")
    cnv.drawString(mm2p(13.5),mm2p(232),"|")
    cnv.drawString(mm2p(13.5),mm2p(230),"|")
    cnv.drawString(mm2p(13.5),mm2p(228),"|")
    cnv.drawString(mm2p(13.5),mm2p(226),"|")
    cnv.drawString(mm2p(13.5),mm2p(224),"|")
    cnv.drawString(mm2p(13.5),mm2p(222),"|")
    cnv.drawString(mm2p(13.5),mm2p(220),"|")
    cnv.drawString(mm2p(13.5),mm2p(218),"|")
    cnv.drawString(mm2p(13.5),mm2p(216),"|")
    cnv.drawString(mm2p(13.5),mm2p(214),"|")
    cnv.drawString(mm2p(13.5),mm2p(212),"|")
    cnv.drawString(mm2p(13.5),mm2p(210),"|")
    cnv.drawString(mm2p(13.5),mm2p(208),"|")
    cnv.drawString(mm2p(13.5),mm2p(206),"|")
    cnv.drawString(mm2p(13.5),mm2p(204),"|")
    cnv.drawString(mm2p(13.5),mm2p(202),"|")
    cnv.drawString(mm2p(13.5),mm2p(200),"|")
    cnv.drawString(mm2p(13.5),mm2p(198),"|")
    cnv.drawString(mm2p(13.5),mm2p(196),"|")
    cnv.drawString(mm2p(13.5),mm2p(194),"|")
    cnv.drawString(mm2p(13.5),mm2p(192),"|")
    cnv.drawString(mm2p(13.5),mm2p(190),"|")
    cnv.drawString(mm2p(13.5),mm2p(188),"|")
    cnv.drawString(mm2p(13.5),mm2p(186),"|")
    cnv.drawString(mm2p(13.5),mm2p(184),"|")
    cnv.drawString(mm2p(13.5),mm2p(182),"|")
    cnv.drawString(mm2p(13.5),mm2p(180),"|")
    cnv.drawString(mm2p(13.5),mm2p(178),"|")
    cnv.drawString(mm2p(13.5),mm2p(176),"|")
    cnv.drawString(mm2p(13.5),mm2p(174),"|")
    cnv.drawString(mm2p(13.5),mm2p(172),"|")
    cnv.drawString(mm2p(13.5),mm2p(170),"|")
    cnv.drawString(mm2p(13.5),mm2p(168),"|")
    cnv.drawString(mm2p(13.5),mm2p(166),"|")
    cnv.drawString(mm2p(13.5),mm2p(164),"|")
    cnv.drawString(mm2p(13.5),mm2p(162),"|")
    cnv.drawString(mm2p(13.5),mm2p(160),"|")
    cnv.drawString(mm2p(13.5),mm2p(158),"|")
    cnv.drawString(mm2p(13.5),mm2p(156),"|")
    cnv.drawString(mm2p(13.5),mm2p(154),"|")
    cnv.drawString(mm2p(13.5),mm2p(152),"|")
    cnv.drawString(mm2p(13.5),mm2p(150),"|")
    cnv.drawString(mm2p(13.5),mm2p(148),"|")
    cnv.drawString(mm2p(13.5),mm2p(146),"|")
    cnv.drawString(mm2p(13.5),mm2p(144),"|")
    cnv.drawString(mm2p(13.5),mm2p(142),"|")
    cnv.drawString(mm2p(13.5),mm2p(140),"|")
    cnv.drawString(mm2p(13.5),mm2p(138),"|")
    cnv.drawString(mm2p(13.5),mm2p(136),"|")
    cnv.drawString(mm2p(13.5),mm2p(134),"|")
    cnv.drawString(mm2p(13.5),mm2p(132),"|")
    cnv.drawString(mm2p(13.5),mm2p(130),"|")
    cnv.drawString(mm2p(13.5),mm2p(128),"|")
    cnv.drawString(mm2p(13.5),mm2p(126),"|")
    cnv.drawString(mm2p(13.5),mm2p(124),"|")
    cnv.drawString(mm2p(13.5),mm2p(122),"|")
    cnv.drawString(mm2p(13.5),mm2p(120),"|")
    cnv.drawString(mm2p(13.5),mm2p(118),"|")
    cnv.drawString(mm2p(13.5),mm2p(116),"|")
    cnv.drawString(mm2p(13.5),mm2p(114),"|")
    cnv.drawString(mm2p(13.5),mm2p(112),"|")
    cnv.drawString(mm2p(13.5),mm2p(110),"|")
    cnv.drawString(mm2p(13.5),mm2p(108),"|")
    cnv.drawString(mm2p(13.5),mm2p(106),"|")
    cnv.drawString(mm2p(13.5),mm2p(104),"|")
    cnv.drawString(mm2p(13.5),mm2p(102),"|")
    cnv.drawString(mm2p(13.5),mm2p(100),"|")
    cnv.drawString(mm2p(13.5),mm2p(98),"|")
    cnv.drawString(mm2p(13.5),mm2p(96),"|")
    cnv.drawString(mm2p(13.5),mm2p(94),"|")
    cnv.drawString(mm2p(13.5),mm2p(92),"|")
    cnv.drawString(mm2p(13.5),mm2p(90),"|")
    cnv.drawString(mm2p(13.5),mm2p(88),"|")
    cnv.drawString(mm2p(13.5),mm2p(86),"|")
    cnv.drawString(mm2p(13.5),mm2p(84),"|")
    cnv.drawString(mm2p(13.5),mm2p(82),"|")
    cnv.drawString(mm2p(14),mm2p(82),"________________________________________________________________________________________________________________________________________")
    cnv.drawString(mm2p(200.5),mm2p(241.9),"|")
    cnv.drawString(mm2p(200.5),mm2p(240),"|")
    cnv.drawString(mm2p(200.5),mm2p(238),"|")
    cnv.drawString(mm2p(200.5),mm2p(236),"|")
    cnv.drawString(mm2p(200.5),mm2p(234),"|")
    cnv.drawString(mm2p(200.5),mm2p(232),"|")
    cnv.drawString(mm2p(200.5),mm2p(230),"|")
    cnv.drawString(mm2p(200.5),mm2p(228),"|")
    cnv.drawString(mm2p(200.5),mm2p(226),"|")
    cnv.drawString(mm2p(200.5),mm2p(224),"|")
    cnv.drawString(mm2p(200.5),mm2p(222),"|")
    cnv.drawString(mm2p(200.5),mm2p(220),"|")
    cnv.drawString(mm2p(200.5),mm2p(218),"|")
    cnv.drawString(mm2p(200.5),mm2p(216),"|")
    cnv.drawString(mm2p(200.5),mm2p(214),"|")
    cnv.drawString(mm2p(200.5),mm2p(212),"|")
    cnv.drawString(mm2p(200.5),mm2p(210),"|")
    cnv.drawString(mm2p(200.5),mm2p(208),"|")
    cnv.drawString(mm2p(200.5),mm2p(206),"|")
    cnv.drawString(mm2p(200.5),mm2p(204),"|")
    cnv.drawString(mm2p(200.5),mm2p(202),"|")
    cnv.drawString(mm2p(200.5),mm2p(200),"|")
    cnv.drawString(mm2p(200.5),mm2p(198),"|")
    cnv.drawString(mm2p(200.5),mm2p(196),"|")
    cnv.drawString(mm2p(200.5),mm2p(194),"|")
    cnv.drawString(mm2p(200.5),mm2p(192),"|")
    cnv.drawString(mm2p(200.5),mm2p(190),"|")
    cnv.drawString(mm2p(200.5),mm2p(188),"|")
    cnv.drawString(mm2p(200.5),mm2p(186),"|")
    cnv.drawString(mm2p(200.5),mm2p(184),"|")
    cnv.drawString(mm2p(200.5),mm2p(182),"|")
    cnv.drawString(mm2p(200.5),mm2p(180),"|")
    cnv.drawString(mm2p(200.5),mm2p(178),"|")
    cnv.drawString(mm2p(200.5),mm2p(176),"|")
    cnv.drawString(mm2p(200.5),mm2p(174),"|")
    cnv.drawString(mm2p(200.5),mm2p(172),"|")
    cnv.drawString(mm2p(200.5),mm2p(170),"|")
    cnv.drawString(mm2p(200.5),mm2p(168),"|")
    cnv.drawString(mm2p(200.5),mm2p(166),"|")
    cnv.drawString(mm2p(200.5),mm2p(164),"|")
    cnv.drawString(mm2p(200.5),mm2p(162),"|")
    cnv.drawString(mm2p(200.5),mm2p(160),"|")
    cnv.drawString(mm2p(200.5),mm2p(158),"|")
    cnv.drawString(mm2p(200.5),mm2p(156),"|")
    cnv.drawString(mm2p(200.5),mm2p(154),"|")
    cnv.drawString(mm2p(200.5),mm2p(152),"|")
    cnv.drawString(mm2p(200.5),mm2p(150),"|")
    cnv.drawString(mm2p(200.5),mm2p(148),"|")
    cnv.drawString(mm2p(200.5),mm2p(146),"|")
    cnv.drawString(mm2p(200.5),mm2p(144),"|")
    cnv.drawString(mm2p(200.5),mm2p(142),"|")
    cnv.drawString(mm2p(200.5),mm2p(140),"|")
    cnv.drawString(mm2p(200.5),mm2p(138),"|")
    cnv.drawString(mm2p(200.5),mm2p(136),"|")
    cnv.drawString(mm2p(200.5),mm2p(134),"|")
    cnv.drawString(mm2p(200.5),mm2p(132),"|")
    cnv.drawString(mm2p(200.5),mm2p(130),"|")
    cnv.drawString(mm2p(200.5),mm2p(128),"|")
    cnv.drawString(mm2p(200.5),mm2p(126),"|")
    cnv.drawString(mm2p(200.5),mm2p(124),"|")
    cnv.drawString(mm2p(200.5),mm2p(122),"|")
    cnv.drawString(mm2p(200.5),mm2p(120),"|")
    cnv.drawString(mm2p(200.5),mm2p(118),"|")
    cnv.drawString(mm2p(200.5),mm2p(116),"|")
    cnv.drawString(mm2p(200.5),mm2p(114),"|")
    cnv.drawString(mm2p(200.5),mm2p(112),"|")
    cnv.drawString(mm2p(200.5),mm2p(110),"|")
    cnv.drawString(mm2p(200.5),mm2p(108),"|")
    cnv.drawString(mm2p(200.5),mm2p(106),"|")
    cnv.drawString(mm2p(200.5),mm2p(104),"|")
    cnv.drawString(mm2p(200.5),mm2p(102),"|")
    cnv.drawString(mm2p(200.5),mm2p(100),"|")
    cnv.drawString(mm2p(200.5),mm2p(98),"|")
    cnv.drawString(mm2p(200.5),mm2p(96),"|")
    cnv.drawString(mm2p(200.5),mm2p(94),"|")
    cnv.drawString(mm2p(200.5),mm2p(92),"|")
    cnv.drawString(mm2p(200.5),mm2p(90),"|")
    cnv.drawString(mm2p(200.5),mm2p(88),"|")
    cnv.drawString(mm2p(200.5),mm2p(86),"|")
    cnv.drawString(mm2p(200.5),mm2p(84),"|")
    cnv.drawString(mm2p(200.5),mm2p(82),"|")
    cnv.drawString(mm2p(14),mm2p(225),"________________________________________________________________________________________________________________________________________")
    cnv.drawString(mm2p(14),mm2p(201),"________________________________________________________________________________________________________________________________________")
    cnv.drawString(mm2p(14),mm2p(173),"________________________________________________________________________________________________________________________________________")
    cnv.drawString(mm2p(14),mm2p(157),"________________________________________________________________________________________________________________________________________")
    cnv.drawString(mm2p(14),mm2p(133),"________________________________________________________________________________________________________________________________________")
    cnv.drawString(mm2p(14),mm2p(109),"________________________________________________________________________________________________________________________________________")
    cnv.drawString(mm2p(14),mm2p(93),"________________________________________________________________________________________________________________________________________")
    cnv.drawString(mm2p(137),mm2p(222.9),"|")
    cnv.drawString(mm2p(137),mm2p(222),"|")
    cnv.drawString(mm2p(137),mm2p(220),"|")
    cnv.drawString(mm2p(137),mm2p(218),"|")
    cnv.drawString(mm2p(137),mm2p(216),"|")
    cnv.drawString(mm2p(137),mm2p(214),"|")
    cnv.drawString(mm2p(137),mm2p(212),"|")
    cnv.drawString(mm2p(137),mm2p(210),"|")
    cnv.drawString(mm2p(137),mm2p(208),"|")
    cnv.drawString(mm2p(137),mm2p(206),"|")
    cnv.drawString(mm2p(137),mm2p(204),"|")
    cnv.drawString(mm2p(137),mm2p(202),"|")
    cnv.drawString(mm2p(137),mm2p(200),"|")
    cnv.drawString(mm2p(137),mm2p(198),"|")
    cnv.drawString(mm2p(137),mm2p(196),"|")
    cnv.drawString(mm2p(137),mm2p(194),"|")
    cnv.drawString(mm2p(137),mm2p(192),"|")
    cnv.drawString(mm2p(137),mm2p(190),"|")
    cnv.drawString(mm2p(137),mm2p(188),"|")
    cnv.drawString(mm2p(137),mm2p(186),"|")
    cnv.drawString(mm2p(137),mm2p(184),"|")
    cnv.drawString(mm2p(137),mm2p(182),"|")
    cnv.drawString(mm2p(137),mm2p(180),"|")
    cnv.drawString(mm2p(137),mm2p(178),"|")
    cnv.drawString(mm2p(137),mm2p(176),"|")
    cnv.drawString(mm2p(137),mm2p(174),"|")
    cnv.drawString(mm2p(137),mm2p(172),"|")
    cnv.drawString(mm2p(137),mm2p(170),"|")
    cnv.drawString(mm2p(137),mm2p(168),"|")
    cnv.drawString(mm2p(137),mm2p(166),"|")
    cnv.drawString(mm2p(137),mm2p(164),"|")
    cnv.drawString(mm2p(137),mm2p(162),"|")
    cnv.drawString(mm2p(137),mm2p(160),"|")
    cnv.drawString(mm2p(137),mm2p(158),"|")
    cnv.drawString(mm2p(137),mm2p(156),"|")
    cnv.drawString(mm2p(137),mm2p(154),"|")
    cnv.drawString(mm2p(137),mm2p(152),"|")
    cnv.drawString(mm2p(137),mm2p(150),"|")
    cnv.drawString(mm2p(137),mm2p(148),"|")
    cnv.drawString(mm2p(137),mm2p(146),"|")
    cnv.drawString(mm2p(137),mm2p(144),"|")
    cnv.drawString(mm2p(137),mm2p(142),"|")
    cnv.drawString(mm2p(137),mm2p(140),"|")
    cnv.drawString(mm2p(137),mm2p(138),"|")
    cnv.drawString(mm2p(137),mm2p(136),"|")
    cnv.drawString(mm2p(137),mm2p(134),"|")
    cnv.drawString(mm2p(137),mm2p(132),"|")
    cnv.drawString(mm2p(137),mm2p(130),"|")
    cnv.drawString(mm2p(137),mm2p(128),"|")
    cnv.drawString(mm2p(137),mm2p(126),"|")
    cnv.drawString(mm2p(137),mm2p(124),"|")
    cnv.drawString(mm2p(137),mm2p(122),"|")
    cnv.drawString(mm2p(137),mm2p(120),"|")
    cnv.drawString(mm2p(137),mm2p(118),"|")
    cnv.drawString(mm2p(137),mm2p(116),"|")
    cnv.drawString(mm2p(137),mm2p(114),"|")
    cnv.drawString(mm2p(137),mm2p(112),"|")
    cnv.drawString(mm2p(137),mm2p(110),"|")
    cnv.drawString(mm2p(137),mm2p(108),"|")
    cnv.drawString(mm2p(137),mm2p(106),"|")
    cnv.drawString(mm2p(137),mm2p(104),"|")
    cnv.drawString(mm2p(137),mm2p(102),"|")
    cnv.drawString(mm2p(137),mm2p(100),"|")
    cnv.drawString(mm2p(137),mm2p(98),"|")
    cnv.drawString(mm2p(137),mm2p(96),"|")
    cnv.drawString(mm2p(137),mm2p(94),"|")
    cnv.drawString(mm2p(137),mm2p(92),"|")
    cnv.drawString(mm2p(137),mm2p(90),"|")
    cnv.drawString(mm2p(137),mm2p(88),"|")
    cnv.drawString(mm2p(137),mm2p(86),"|")
    cnv.drawString(mm2p(137),mm2p(84),"|")
    cnv.drawString(mm2p(137),mm2p(82),"|")
    cnv.drawString(mm2p(162),mm2p(222.9),"|")
    cnv.drawString(mm2p(162),mm2p(222),"|")
    cnv.drawString(mm2p(162),mm2p(220),"|")
    cnv.drawString(mm2p(162),mm2p(218),"|")
    cnv.drawString(mm2p(162),mm2p(216),"|")
    cnv.drawString(mm2p(162),mm2p(214),"|")
    cnv.drawString(mm2p(162),mm2p(212),"|")
    cnv.drawString(mm2p(162),mm2p(210),"|")
    cnv.drawString(mm2p(162),mm2p(208),"|")
    cnv.drawString(mm2p(162),mm2p(206),"|")
    cnv.drawString(mm2p(162),mm2p(204),"|")
    cnv.drawString(mm2p(162),mm2p(202),"|")
    cnv.drawString(mm2p(162),mm2p(200),"|")
    cnv.drawString(mm2p(162),mm2p(198),"|")
    cnv.drawString(mm2p(162),mm2p(196),"|")
    cnv.drawString(mm2p(162),mm2p(194),"|")
    cnv.drawString(mm2p(162),mm2p(192),"|")
    cnv.drawString(mm2p(162),mm2p(190),"|")
    cnv.drawString(mm2p(162),mm2p(188),"|")
    cnv.drawString(mm2p(162),mm2p(186),"|")
    cnv.drawString(mm2p(162),mm2p(184),"|")
    cnv.drawString(mm2p(162),mm2p(182),"|")
    cnv.drawString(mm2p(162),mm2p(180),"|")
    cnv.drawString(mm2p(162),mm2p(178),"|")
    cnv.drawString(mm2p(162),mm2p(176),"|")
    cnv.drawString(mm2p(162),mm2p(174),"|")
    cnv.drawString(mm2p(162),mm2p(172),"|")
    cnv.drawString(mm2p(162),mm2p(170),"|")
    cnv.drawString(mm2p(162),mm2p(168),"|")
    cnv.drawString(mm2p(162),mm2p(166),"|")
    cnv.drawString(mm2p(162),mm2p(164),"|")
    cnv.drawString(mm2p(162),mm2p(162),"|")
    cnv.drawString(mm2p(162),mm2p(160),"|")
    cnv.drawString(mm2p(162),mm2p(158),"|")
    cnv.drawString(mm2p(162),mm2p(156),"|")
    cnv.drawString(mm2p(162),mm2p(154),"|")
    cnv.drawString(mm2p(162),mm2p(152),"|")
    cnv.drawString(mm2p(162),mm2p(150),"|")
    cnv.drawString(mm2p(162),mm2p(148),"|")
    cnv.drawString(mm2p(162),mm2p(146),"|")
    cnv.drawString(mm2p(162),mm2p(144),"|")
    cnv.drawString(mm2p(162),mm2p(142),"|")
    cnv.drawString(mm2p(162),mm2p(140),"|")
    cnv.drawString(mm2p(162),mm2p(138),"|")
    cnv.drawString(mm2p(162),mm2p(136),"|")
    cnv.drawString(mm2p(162),mm2p(134),"|")
    cnv.drawString(mm2p(162),mm2p(132),"|")
    cnv.drawString(mm2p(162),mm2p(130),"|")
    cnv.drawString(mm2p(162),mm2p(128),"|")
    cnv.drawString(mm2p(162),mm2p(126),"|")
    cnv.drawString(mm2p(162),mm2p(124),"|")
    cnv.drawString(mm2p(162),mm2p(122),"|")
    cnv.drawString(mm2p(162),mm2p(120),"|")
    cnv.drawString(mm2p(162),mm2p(118),"|")
    cnv.drawString(mm2p(162),mm2p(116),"|")
    cnv.drawString(mm2p(162),mm2p(114),"|")
    cnv.drawString(mm2p(162),mm2p(112),"|")
    cnv.drawString(mm2p(162),mm2p(110),"|")
    cnv.drawString(mm2p(162),mm2p(108),"|")
    cnv.drawString(mm2p(162),mm2p(106),"|")
    cnv.drawString(mm2p(162),mm2p(104),"|")
    cnv.drawString(mm2p(162),mm2p(102),"|")
    cnv.drawString(mm2p(162),mm2p(100),"|")
    cnv.drawString(mm2p(162),mm2p(98),"|")
    cnv.drawString(mm2p(162),mm2p(96),"|")
    cnv.drawString(mm2p(162),mm2p(94),"|")
    cnv.drawString(mm2p(162),mm2p(92),"|")
    cnv.drawString(mm2p(162),mm2p(90),"|")
    cnv.drawString(mm2p(162),mm2p(88),"|")
    cnv.drawString(mm2p(162),mm2p(86),"|")
    cnv.drawString(mm2p(162),mm2p(84),"|")
    cnv.drawString(mm2p(162),mm2p(82),"|")
    cnv.drawString(mm2p(146),mm2p(222.9),"|")
    cnv.drawString(mm2p(146),mm2p(222),"|")
    cnv.drawString(mm2p(146),mm2p(220),"|")
    cnv.drawString(mm2p(146),mm2p(218),"|")
    cnv.drawString(mm2p(146),mm2p(216),"|")
    cnv.drawString(mm2p(146),mm2p(214),"|")
    cnv.drawString(mm2p(146),mm2p(212),"|")
    cnv.drawString(mm2p(146),mm2p(210),"|")
    cnv.drawString(mm2p(146),mm2p(208),"|")
    cnv.drawString(mm2p(146),mm2p(206),"|")
    cnv.drawString(mm2p(146),mm2p(204),"|")
    cnv.drawString(mm2p(146),mm2p(202),"|")
    cnv.drawString(mm2p(146),mm2p(200),"|")
    cnv.drawString(mm2p(146),mm2p(198),"|")
    cnv.drawString(mm2p(146),mm2p(196),"|")
    cnv.drawString(mm2p(146),mm2p(194),"|")
    cnv.drawString(mm2p(146),mm2p(192),"|")
    cnv.drawString(mm2p(146),mm2p(190),"|")
    cnv.drawString(mm2p(146),mm2p(188),"|")
    cnv.drawString(mm2p(146),mm2p(186),"|")
    cnv.drawString(mm2p(146),mm2p(184),"|")
    cnv.drawString(mm2p(146),mm2p(182),"|")
    cnv.drawString(mm2p(146),mm2p(180),"|")
    cnv.drawString(mm2p(146),mm2p(178),"|")
    cnv.drawString(mm2p(146),mm2p(176),"|")
    cnv.drawString(mm2p(146),mm2p(174),"|")
    cnv.drawString(mm2p(146),mm2p(172),"|")
    cnv.drawString(mm2p(146),mm2p(170),"|")
    cnv.drawString(mm2p(146),mm2p(168),"|")
    cnv.drawString(mm2p(146),mm2p(166),"|")
    cnv.drawString(mm2p(146),mm2p(164),"|")
    cnv.drawString(mm2p(146),mm2p(162),"|")
    cnv.drawString(mm2p(146),mm2p(160),"|")
    cnv.drawString(mm2p(146),mm2p(158),"|")
    cnv.drawString(mm2p(146),mm2p(156),"|")
    cnv.drawString(mm2p(146),mm2p(154),"|")
    cnv.drawString(mm2p(146),mm2p(152),"|")
    cnv.drawString(mm2p(146),mm2p(150),"|")
    cnv.drawString(mm2p(146),mm2p(148),"|")
    cnv.drawString(mm2p(146),mm2p(146),"|")
    cnv.drawString(mm2p(146),mm2p(144),"|")
    cnv.drawString(mm2p(146),mm2p(142),"|")
    cnv.drawString(mm2p(146),mm2p(140),"|")
    cnv.drawString(mm2p(146),mm2p(138),"|")
    cnv.drawString(mm2p(146),mm2p(136),"|")
    cnv.drawString(mm2p(146),mm2p(134),"|")
    cnv.drawString(mm2p(146),mm2p(132),"|")
    cnv.drawString(mm2p(146),mm2p(130),"|")
    cnv.drawString(mm2p(146),mm2p(128),"|")
    cnv.drawString(mm2p(146),mm2p(126),"|")
    cnv.drawString(mm2p(146),mm2p(124),"|")
    cnv.drawString(mm2p(146),mm2p(122),"|")
    cnv.drawString(mm2p(146),mm2p(120),"|")
    cnv.drawString(mm2p(146),mm2p(118),"|")
    cnv.drawString(mm2p(146),mm2p(116),"|")
    cnv.drawString(mm2p(146),mm2p(114),"|")
    cnv.drawString(mm2p(146),mm2p(112),"|")
    cnv.drawString(mm2p(146),mm2p(110),"|")
    cnv.drawString(mm2p(146),mm2p(108),"|")
    cnv.drawString(mm2p(146),mm2p(106),"|")
    cnv.drawString(mm2p(146),mm2p(104),"|")
    cnv.drawString(mm2p(146),mm2p(102),"|")
    cnv.drawString(mm2p(146),mm2p(100),"|")
    cnv.drawString(mm2p(146),mm2p(98),"|")
    cnv.drawString(mm2p(146),mm2p(96),"|")
    cnv.drawString(mm2p(146),mm2p(94),"|")
    cnv.drawString(mm2p(146),mm2p(92),"|")
    cnv.drawString(mm2p(146),mm2p(90),"|")
    cnv.drawString(mm2p(146),mm2p(88),"|")
    cnv.drawString(mm2p(146),mm2p(86),"|")
    cnv.drawString(mm2p(146),mm2p(84),"|")
    cnv.drawString(mm2p(146),mm2p(82),"|")
    cnv.drawString(mm2p(155),mm2p(222.9),"|")
    cnv.drawString(mm2p(155),mm2p(222),"|")
    cnv.drawString(mm2p(155),mm2p(220),"|")
    cnv.drawString(mm2p(155),mm2p(218),"|")
    cnv.drawString(mm2p(155),mm2p(216),"|")
    cnv.drawString(mm2p(155),mm2p(214),"|")
    cnv.drawString(mm2p(155),mm2p(212),"|")
    cnv.drawString(mm2p(155),mm2p(210),"|")
    cnv.drawString(mm2p(155),mm2p(208),"|")
    cnv.drawString(mm2p(155),mm2p(206),"|")
    cnv.drawString(mm2p(155),mm2p(204),"|")
    cnv.drawString(mm2p(155),mm2p(202),"|")
    cnv.drawString(mm2p(155),mm2p(200),"|")
    cnv.drawString(mm2p(155),mm2p(198),"|")
    cnv.drawString(mm2p(155),mm2p(196),"|")
    cnv.drawString(mm2p(155),mm2p(194),"|")
    cnv.drawString(mm2p(155),mm2p(192),"|")
    cnv.drawString(mm2p(155),mm2p(190),"|")
    cnv.drawString(mm2p(155),mm2p(188),"|")
    cnv.drawString(mm2p(155),mm2p(186),"|")
    cnv.drawString(mm2p(155),mm2p(184),"|")
    cnv.drawString(mm2p(155),mm2p(182),"|")
    cnv.drawString(mm2p(155),mm2p(180),"|")
    cnv.drawString(mm2p(155),mm2p(178),"|")
    cnv.drawString(mm2p(155),mm2p(176),"|")
    cnv.drawString(mm2p(155),mm2p(174),"|")
    cnv.drawString(mm2p(155),mm2p(172),"|")
    cnv.drawString(mm2p(155),mm2p(170),"|")
    cnv.drawString(mm2p(155),mm2p(168),"|")
    cnv.drawString(mm2p(155),mm2p(166),"|")
    cnv.drawString(mm2p(155),mm2p(164),"|")
    cnv.drawString(mm2p(155),mm2p(162),"|")
    cnv.drawString(mm2p(155),mm2p(160),"|")
    cnv.drawString(mm2p(155),mm2p(158),"|")
    cnv.drawString(mm2p(155),mm2p(156),"|")
    cnv.drawString(mm2p(155),mm2p(154),"|")
    cnv.drawString(mm2p(155),mm2p(152),"|")
    cnv.drawString(mm2p(155),mm2p(150),"|")
    cnv.drawString(mm2p(155),mm2p(148),"|")
    cnv.drawString(mm2p(155),mm2p(146),"|")
    cnv.drawString(mm2p(155),mm2p(144),"|")
    cnv.drawString(mm2p(155),mm2p(142),"|")
    cnv.drawString(mm2p(155),mm2p(140),"|")
    cnv.drawString(mm2p(155),mm2p(138),"|")
    cnv.drawString(mm2p(155),mm2p(136),"|")
    cnv.drawString(mm2p(155),mm2p(134),"|")
    cnv.drawString(mm2p(155),mm2p(132),"|")
    cnv.drawString(mm2p(155),mm2p(130),"|")
    cnv.drawString(mm2p(155),mm2p(128),"|")
    cnv.drawString(mm2p(155),mm2p(126),"|")
    cnv.drawString(mm2p(155),mm2p(124),"|")
    cnv.drawString(mm2p(155),mm2p(122),"|")
    cnv.drawString(mm2p(155),mm2p(120),"|")
    cnv.drawString(mm2p(155),mm2p(118),"|")
    cnv.drawString(mm2p(155),mm2p(116),"|")
    cnv.drawString(mm2p(155),mm2p(114),"|")
    cnv.drawString(mm2p(155),mm2p(112),"|")
    cnv.drawString(mm2p(155),mm2p(110),"|")
    cnv.drawString(mm2p(155),mm2p(108),"|")
    cnv.drawString(mm2p(155),mm2p(106),"|")
    cnv.drawString(mm2p(155),mm2p(104),"|")
    cnv.drawString(mm2p(155),mm2p(102),"|")
    cnv.drawString(mm2p(155),mm2p(100),"|")
    cnv.drawString(mm2p(155),mm2p(98),"|")
    cnv.drawString(mm2p(155),mm2p(96),"|")
    cnv.drawString(mm2p(155),mm2p(94),"|")
    cnv.drawString(mm2p(155),mm2p(92),"|")
    cnv.drawString(mm2p(155),mm2p(90),"|")
    cnv.drawString(mm2p(155),mm2p(88),"|")
    cnv.drawString(mm2p(155),mm2p(86),"|")
    cnv.drawString(mm2p(155),mm2p(84),"|")
    cnv.drawString(mm2p(155),mm2p(82),"|")
    cnv.drawString(mm2p(172),mm2p(222.9),"|")
    cnv.drawString(mm2p(172),mm2p(222),"|")
    cnv.drawString(mm2p(172),mm2p(220),"|")
    cnv.drawString(mm2p(172),mm2p(218),"|")
    cnv.drawString(mm2p(172),mm2p(216),"|")
    cnv.drawString(mm2p(172),mm2p(214),"|")
    cnv.drawString(mm2p(172),mm2p(212),"|")
    cnv.drawString(mm2p(172),mm2p(210),"|")
    cnv.drawString(mm2p(172),mm2p(208),"|")
    cnv.drawString(mm2p(172),mm2p(206),"|")
    cnv.drawString(mm2p(172),mm2p(204),"|")
    cnv.drawString(mm2p(172),mm2p(202),"|")
    cnv.drawString(mm2p(172),mm2p(200),"|")
    cnv.drawString(mm2p(172),mm2p(198),"|")
    cnv.drawString(mm2p(172),mm2p(196),"|")
    cnv.drawString(mm2p(172),mm2p(194),"|")
    cnv.drawString(mm2p(172),mm2p(192),"|")
    cnv.drawString(mm2p(172),mm2p(190),"|")
    cnv.drawString(mm2p(172),mm2p(188),"|")
    cnv.drawString(mm2p(172),mm2p(186),"|")
    cnv.drawString(mm2p(172),mm2p(184),"|")
    cnv.drawString(mm2p(172),mm2p(182),"|")
    cnv.drawString(mm2p(172),mm2p(180),"|")
    cnv.drawString(mm2p(172),mm2p(178),"|")
    cnv.drawString(mm2p(172),mm2p(176),"|")
    cnv.drawString(mm2p(172),mm2p(174),"|")
    cnv.drawString(mm2p(172),mm2p(172),"|")
    cnv.drawString(mm2p(172),mm2p(170),"|")
    cnv.drawString(mm2p(172),mm2p(168),"|")
    cnv.drawString(mm2p(172),mm2p(166),"|")
    cnv.drawString(mm2p(172),mm2p(164),"|")
    cnv.drawString(mm2p(172),mm2p(162),"|")
    cnv.drawString(mm2p(172),mm2p(160),"|")
    cnv.drawString(mm2p(172),mm2p(158),"|")
    cnv.drawString(mm2p(172),mm2p(156),"|")
    cnv.drawString(mm2p(172),mm2p(154),"|")
    cnv.drawString(mm2p(172),mm2p(152),"|")
    cnv.drawString(mm2p(172),mm2p(150),"|")
    cnv.drawString(mm2p(172),mm2p(148),"|")
    cnv.drawString(mm2p(172),mm2p(146),"|")
    cnv.drawString(mm2p(172),mm2p(144),"|")
    cnv.drawString(mm2p(172),mm2p(142),"|")
    cnv.drawString(mm2p(172),mm2p(140),"|")
    cnv.drawString(mm2p(172),mm2p(138),"|")
    cnv.drawString(mm2p(172),mm2p(136),"|")
    cnv.drawString(mm2p(172),mm2p(134),"|")
    cnv.drawString(mm2p(172),mm2p(132),"|")
    cnv.drawString(mm2p(172),mm2p(130),"|")
    cnv.drawString(mm2p(172),mm2p(128),"|")
    cnv.drawString(mm2p(172),mm2p(126),"|")
    cnv.drawString(mm2p(172),mm2p(124),"|")
    cnv.drawString(mm2p(172),mm2p(122),"|")
    cnv.drawString(mm2p(172),mm2p(120),"|")
    cnv.drawString(mm2p(172),mm2p(118),"|")
    cnv.drawString(mm2p(172),mm2p(116),"|")
    cnv.drawString(mm2p(172),mm2p(114),"|")
    cnv.drawString(mm2p(172),mm2p(112),"|")
    cnv.drawString(mm2p(172),mm2p(110),"|")
    cnv.drawString(mm2p(172),mm2p(108),"|")
    cnv.drawString(mm2p(172),mm2p(106),"|")
    cnv.drawString(mm2p(172),mm2p(104),"|")
    cnv.drawString(mm2p(172),mm2p(102),"|")
    cnv.drawString(mm2p(172),mm2p(100),"|")
    cnv.drawString(mm2p(172),mm2p(98),"|")
    cnv.drawString(mm2p(172),mm2p(96),"|")
    cnv.drawString(mm2p(172),mm2p(94),"|")
    cnv.drawString(mm2p(172),mm2p(92),"|")
    cnv.drawString(mm2p(172),mm2p(90),"|")
    cnv.drawString(mm2p(172),mm2p(88),"|")
    cnv.drawString(mm2p(172),mm2p(86),"|")
    cnv.drawString(mm2p(172),mm2p(84),"|")
    cnv.drawString(mm2p(172),mm2p(82),"|")
    cnv.drawString(mm2p(180),mm2p(222.9),"|")
    cnv.drawString(mm2p(180),mm2p(222),"|")
    cnv.drawString(mm2p(180),mm2p(220),"|")
    cnv.drawString(mm2p(180),mm2p(218),"|")
    cnv.drawString(mm2p(180),mm2p(216),"|")
    cnv.drawString(mm2p(180),mm2p(214),"|")
    cnv.drawString(mm2p(180),mm2p(212),"|")
    cnv.drawString(mm2p(180),mm2p(210),"|")
    cnv.drawString(mm2p(180),mm2p(208),"|")
    cnv.drawString(mm2p(180),mm2p(206),"|")
    cnv.drawString(mm2p(180),mm2p(204),"|")
    cnv.drawString(mm2p(180),mm2p(202),"|")
    cnv.drawString(mm2p(180),mm2p(200),"|")
    cnv.drawString(mm2p(180),mm2p(198),"|")
    cnv.drawString(mm2p(180),mm2p(196),"|")
    cnv.drawString(mm2p(180),mm2p(194),"|")
    cnv.drawString(mm2p(180),mm2p(192),"|")
    cnv.drawString(mm2p(180),mm2p(190),"|")
    cnv.drawString(mm2p(180),mm2p(188),"|")
    cnv.drawString(mm2p(180),mm2p(186),"|")
    cnv.drawString(mm2p(180),mm2p(184),"|")
    cnv.drawString(mm2p(180),mm2p(182),"|")
    cnv.drawString(mm2p(180),mm2p(180),"|")
    cnv.drawString(mm2p(180),mm2p(178),"|")
    cnv.drawString(mm2p(180),mm2p(176),"|")
    cnv.drawString(mm2p(180),mm2p(174),"|")
    cnv.drawString(mm2p(180),mm2p(172),"|")
    cnv.drawString(mm2p(180),mm2p(170),"|")
    cnv.drawString(mm2p(180),mm2p(168),"|")
    cnv.drawString(mm2p(180),mm2p(166),"|")
    cnv.drawString(mm2p(180),mm2p(164),"|")
    cnv.drawString(mm2p(180),mm2p(162),"|")
    cnv.drawString(mm2p(180),mm2p(160),"|")
    cnv.drawString(mm2p(180),mm2p(158),"|")
    cnv.drawString(mm2p(180),mm2p(156),"|")
    cnv.drawString(mm2p(180),mm2p(154),"|")
    cnv.drawString(mm2p(180),mm2p(152),"|")
    cnv.drawString(mm2p(180),mm2p(150),"|")
    cnv.drawString(mm2p(180),mm2p(148),"|")
    cnv.drawString(mm2p(180),mm2p(146),"|")
    cnv.drawString(mm2p(180),mm2p(144),"|")
    cnv.drawString(mm2p(180),mm2p(142),"|")
    cnv.drawString(mm2p(180),mm2p(140),"|")
    cnv.drawString(mm2p(180),mm2p(138),"|")
    cnv.drawString(mm2p(180),mm2p(136),"|")
    cnv.drawString(mm2p(180),mm2p(134),"|")
    cnv.drawString(mm2p(180),mm2p(132),"|")
    cnv.drawString(mm2p(180),mm2p(130),"|")
    cnv.drawString(mm2p(180),mm2p(128),"|")
    cnv.drawString(mm2p(180),mm2p(126),"|")
    cnv.drawString(mm2p(180),mm2p(124),"|")
    cnv.drawString(mm2p(180),mm2p(122),"|")
    cnv.drawString(mm2p(180),mm2p(120),"|")
    cnv.drawString(mm2p(180),mm2p(118),"|")
    cnv.drawString(mm2p(180),mm2p(116),"|")
    cnv.drawString(mm2p(180),mm2p(114),"|")
    cnv.drawString(mm2p(180),mm2p(112),"|")
    cnv.drawString(mm2p(180),mm2p(110),"|")
    cnv.drawString(mm2p(180),mm2p(108),"|")
    cnv.drawString(mm2p(180),mm2p(106),"|")
    cnv.drawString(mm2p(180),mm2p(104),"|")
    cnv.drawString(mm2p(180),mm2p(102),"|")
    cnv.drawString(mm2p(180),mm2p(100),"|")
    cnv.drawString(mm2p(180),mm2p(98),"|")
    cnv.drawString(mm2p(180),mm2p(96),"|")
    cnv.drawString(mm2p(180),mm2p(94),"|")
    cnv.drawString(mm2p(180),mm2p(92),"|")
    cnv.drawString(mm2p(180),mm2p(90),"|")
    cnv.drawString(mm2p(180),mm2p(88),"|")
    cnv.drawString(mm2p(180),mm2p(86),"|")
    cnv.drawString(mm2p(180),mm2p(84),"|")
    cnv.drawString(mm2p(180),mm2p(82),"|")


    cnv.showPage()



    ######################################### QUINTA PAGINA ######################################################################

    # TITULO
    cnv.setFont("Helvetica", 15)
    cnv.drawString(mm2p(87),mm2p(277),"ELETRIFICATION DISTRIBUTION SYSTEMS")
    cnv.drawString(mm2p(125),mm2p(269),"DA SOLUTIONS PRODUCTS")

    #
    cnv.setFont("Helvetica", 10)
    cnv.drawString(mm2p(margem),mm2p(251),"INSPEÇÃO VISUAL E VERIFICAÇÕES DIMENSIONAIS")
    cnv.drawString(mm2p(margem),mm2p(247),"VISUAL AND DIMENSIONAL INSPECTION")


    cnv.setFont("Helvetica",7)
    ## APENAS OS TEXTOS POR ENQUANTO
    cnv.drawString(mm2p(130+10),mm2p(241),"ABB Interno")
    cnv.drawString(mm2p(155+10),mm2p(241),"Teste realizados com o cliente")

    ## Canto direito superior do quadrado 
    cnv.drawString(mm2p(130+10),mm2p(236),"OK")
    cnv.drawString(mm2p(139+10),mm2p(236),"NO")
    cnv.drawString(mm2p(148+10),mm2p(236),"NA")
    cnv.drawString(mm2p(155+10),mm2p(236),"OK")
    cnv.drawString(mm2p(165+10),mm2p(236),"NO")
    cnv.drawString(mm2p(173+10),mm2p(236),"Comment")


    ## Primeira pergunta
    cnv.setFont("Helvetica",7)
    cnv.drawString(mm2p(m_texto),mm2p(222),"TESTES DE COMANDO.")
    cnv.drawString(mm2p(m_texto),mm2p(218),"control testing.")

    
    ## Segunda pergunta
    cnv.drawString(mm2p(m_texto),mm2p(202),"Realizar comando de abertura no frontal do IED.")
    cnv.drawString(mm2p(m_texto),mm2p(198),"Perform open command at the IED's Local HMI.")

    if B_ok_31 == True:
        cnv.drawString(mm2p(OK),mm2p(200),"X")

    if B_no_31 == True:
        cnv.drawString(mm2p(NO),mm2p(200),"X")

    if B_na_31 == True:
        cnv.drawString(mm2p(NA),mm2p(200),"X")
    
    ## Terceira pergunta
    cnv.drawString(mm2p(m_texto),mm2p(182),"Realizar comando de fechamento no frontal do IED.")
    cnv.drawString(mm2p(m_texto),mm2p(178),"Perform close command at the IED's Local HMI.")

    if B_ok_32 == True:
        cnv.drawString(mm2p(OK),mm2p(180),"X")

    if B_no_32 == True:
        cnv.drawString(mm2p(NO),mm2p(180),"X")

    if B_na_32 == True:
        cnv.drawString(mm2p(NA),mm2p(180),"X")

    ## Quarta pergunta
    cnv.drawString(mm2p(m_texto),mm2p(162),"TESTE DE FALHA DO IED (IRF).")
    cnv.drawString(mm2p(m_texto),mm2p(158),"IED internal fault testing.")

    # Quinta pergunta
    cnv.drawString(mm2p(m_texto),mm2p(142),"Forçar a atuação do contato de saída de falha interna do IED. Cortar a corrente continua dos IEDS")
    cnv.drawString(mm2p(m_texto),mm2p(138),"e depois retornar.")
    cnv.drawString(mm2p(m_texto),mm2p(134),"Verificar e registrar o comportamento do sistema, as sinalizações e alarmes pertinentes bem como")
    cnv.drawString(mm2p(m_texto),mm2p(130),"o registro de eventos.")
    cnv.drawString(mm2p(m_texto),mm2p(126),"Force the operation of IED's IRF contact. Unplug the auxiliary voltage and plug it back.")
    cnv.drawString(mm2p(m_texto),mm2p(122),"Check and record the system behavior, signaling, alarms and avents.")

    if B_ok_33 == True:
        cnv.drawString(mm2p(OK),mm2p(132),"X")

    if B_no_33 == True:
        cnv.drawString(mm2p(NO),mm2p(132),"X")

    if B_na_33 == True:
        cnv.drawString(mm2p(NA),mm2p(132),"X")

    ## Sexta pergunta
    cnv.drawString(mm2p(m_texto),mm2p(106),"TESTE DAS FUNÇÕES DE CORRENTE E TENSÃO.")
    cnv.drawString(mm2p(m_texto),mm2p(102),"CURRENT AND VOLTAGE FUNCTIONS TESTING.")

    ## Sétima pergunta
    cnv.drawString(mm2p(m_texto),mm2p(86),"Realizar a medição de correntes de fase no frontal do IED.")
    cnv.drawString(mm2p(m_texto),mm2p(82),"Perfom phase current measurement at the IED's Local HMI.")

    if B_ok_34 == True:
        cnv.drawString(mm2p(OK),mm2p(84),"X")

    if B_no_34 == True:
        cnv.drawString(mm2p(NO),mm2p(84),"X")

    if B_na_34 == True:
        cnv.drawString(mm2p(NA),mm2p(84),"X")

    ## Oitáva pergunta
    cnv.drawString(mm2p(m_texto),mm2p(66),"Realizar a medição de tensões no frontal do IED.")
    cnv.drawString(mm2p(m_texto),mm2p(62),"Perfom voltage measurement at the IED's Local HMI.")

    if B_ok_35 == True:
        cnv.drawString(mm2p(OK),mm2p(64),"X")

    if B_no_35 == True:
        cnv.drawString(mm2p(NO),mm2p(64),"X")

    if B_na_35 == True:
        cnv.drawString(mm2p(NA),mm2p(64),"X")

    ## Nona pergunta
    cnv.drawString(mm2p(m_texto),mm2p(46),"Injetar tensão, variando até os valores ajustados para subtensão e sobretensão")
    cnv.drawString(mm2p(m_texto),mm2p(42),"e observar atuação no IED.")
    cnv.drawString(mm2p(m_texto),mm2p(38),"Inject voltage, raging until the adjusted values for under overvoltage")
    cnv.drawString(mm2p(m_texto),mm2p(34),"and check the IED operation.")

    if B_ok_36 == True:
        cnv.drawString(mm2p(OK),mm2p(40),"X")

    if B_no_36 == True:
        cnv.drawString(mm2p(NO),mm2p(40),"X")

    if B_na_36 == True:
        cnv.drawString(mm2p(NA),mm2p(40),"X")

    # 
    # canto esquerdo

    cnv.drawString(mm2p(14),mm2p(223),"|")
    cnv.drawString(mm2p(14),mm2p(221),"|")
    cnv.drawString(mm2p(14),mm2p(219),"|")
    cnv.drawString(mm2p(14),mm2p(217),"|")
    cnv.drawString(mm2p(14),mm2p(215),"|")
    cnv.drawString(mm2p(14),mm2p(213),"|")
    cnv.drawString(mm2p(14),mm2p(211),"|")
    # canto direito
    cnv.drawString(mm2p(198),mm2p(223),"|")
    cnv.drawString(mm2p(198),mm2p(221),"|")
    cnv.drawString(mm2p(198),mm2p(219),"|")
    cnv.drawString(mm2p(198),mm2p(217),"|")
    cnv.drawString(mm2p(198),mm2p(215),"|")
    cnv.drawString(mm2p(198),mm2p(213),"|")
    cnv.drawString(mm2p(198),mm2p(211),"|")

    cnv.drawString(mm2p(137),mm2p(223),"|")
    cnv.drawString(mm2p(137),mm2p(221),"|")
    cnv.drawString(mm2p(137),mm2p(219),"|")
    cnv.drawString(mm2p(137),mm2p(217),"|")
    cnv.drawString(mm2p(137),mm2p(215),"|")
    cnv.drawString(mm2p(137),mm2p(213),"|")
    cnv.drawString(mm2p(137),mm2p(211),"|")

    cnv.drawString(mm2p(146),mm2p(223),"|")
    cnv.drawString(mm2p(146),mm2p(221),"|")
    cnv.drawString(mm2p(146),mm2p(219),"|")
    cnv.drawString(mm2p(146),mm2p(217),"|")
    cnv.drawString(mm2p(146),mm2p(215),"|")
    cnv.drawString(mm2p(146),mm2p(213),"|")
    cnv.drawString(mm2p(146),mm2p(211),"|")

    cnv.drawString(mm2p(155),mm2p(223),"|")
    cnv.drawString(mm2p(155),mm2p(221),"|")
    cnv.drawString(mm2p(155),mm2p(219),"|")
    cnv.drawString(mm2p(155),mm2p(217),"|")
    cnv.drawString(mm2p(155),mm2p(215),"|")
    cnv.drawString(mm2p(155),mm2p(213),"|")
    cnv.drawString(mm2p(155),mm2p(211),"|")

    cnv.drawString(mm2p(165),mm2p(223),"|")
    cnv.drawString(mm2p(165),mm2p(221),"|")
    cnv.drawString(mm2p(165),mm2p(219),"|")
    cnv.drawString(mm2p(165),mm2p(217),"|")
    cnv.drawString(mm2p(165),mm2p(215),"|")
    cnv.drawString(mm2p(165),mm2p(213),"|")
    cnv.drawString(mm2p(165),mm2p(211),"|")

    cnv.drawString(mm2p(175),mm2p(223),"|")
    cnv.drawString(mm2p(175),mm2p(221),"|")
    cnv.drawString(mm2p(175),mm2p(219),"|")
    cnv.drawString(mm2p(175),mm2p(217),"|")
    cnv.drawString(mm2p(175),mm2p(215),"|")
    cnv.drawString(mm2p(175),mm2p(213),"|")
    cnv.drawString(mm2p(175),mm2p(211),"|")

    cnv.drawString(mm2p(184),mm2p(223),"|")
    cnv.drawString(mm2p(184),mm2p(221),"|")
    cnv.drawString(mm2p(184),mm2p(219),"|")
    cnv.drawString(mm2p(184),mm2p(217),"|")
    cnv.drawString(mm2p(184),mm2p(215),"|")
    cnv.drawString(mm2p(184),mm2p(213),"|")
    cnv.drawString(mm2p(184),mm2p(211),"|")


    cnv.drawString(mm2p(14.5),mm2p(225),"______________________________________________________________________________________________________________________________________")
    cnv.drawString(mm2p(14.5),mm2p(211),"______________________________________________________________________________________________________________________________________")

    ## INSERINDO AS GRADES
    # canto esquerdo
    cnv.drawString(mm2p(14),mm2p(205),"|")
    cnv.drawString(mm2p(14),mm2p(207),"|")
    cnv.drawString(mm2p(14),mm2p(209),"|")

    cnv.drawString(mm2p(14),mm2p(203),"|")
    cnv.drawString(mm2p(14),mm2p(201),"|")
    cnv.drawString(mm2p(14),mm2p(199),"|")
    cnv.drawString(mm2p(14),mm2p(197),"|")
    cnv.drawString(mm2p(14),mm2p(195),"|")
    cnv.drawString(mm2p(14),mm2p(193),"|")
    cnv.drawString(mm2p(14),mm2p(191),"|")
    # canto direito
    cnv.drawString(mm2p(198),mm2p(205),"|")
    cnv.drawString(mm2p(198),mm2p(207),"|")
    cnv.drawString(mm2p(198),mm2p(209),"|")

    cnv.drawString(mm2p(198),mm2p(203),"|")
    cnv.drawString(mm2p(198),mm2p(201),"|")
    cnv.drawString(mm2p(198),mm2p(199),"|")
    cnv.drawString(mm2p(198),mm2p(197),"|")
    cnv.drawString(mm2p(198),mm2p(195),"|")
    cnv.drawString(mm2p(198),mm2p(193),"|")
    cnv.drawString(mm2p(198),mm2p(191),"|")

    #
    cnv.drawString(mm2p(137),mm2p(205),"|")
    cnv.drawString(mm2p(137),mm2p(207),"|")
    cnv.drawString(mm2p(137),mm2p(209),"|")

    cnv.drawString(mm2p(137),mm2p(203),"|")
    cnv.drawString(mm2p(137),mm2p(201),"|")
    cnv.drawString(mm2p(137),mm2p(199),"|")
    cnv.drawString(mm2p(137),mm2p(197),"|")
    cnv.drawString(mm2p(137),mm2p(195),"|")
    cnv.drawString(mm2p(137),mm2p(193),"|")
    cnv.drawString(mm2p(137),mm2p(191),"|")

    #
    cnv.drawString(mm2p(146),mm2p(205),"|")
    cnv.drawString(mm2p(146),mm2p(207),"|")
    cnv.drawString(mm2p(146),mm2p(209),"|")

    cnv.drawString(mm2p(146),mm2p(203),"|")
    cnv.drawString(mm2p(146),mm2p(201),"|")
    cnv.drawString(mm2p(146),mm2p(199),"|")
    cnv.drawString(mm2p(146),mm2p(197),"|")
    cnv.drawString(mm2p(146),mm2p(195),"|")
    cnv.drawString(mm2p(146),mm2p(193),"|")
    cnv.drawString(mm2p(146),mm2p(191),"|")

    #
    cnv.drawString(mm2p(155),mm2p(205),"|")
    cnv.drawString(mm2p(155),mm2p(207),"|")
    cnv.drawString(mm2p(155),mm2p(209),"|")

    cnv.drawString(mm2p(155),mm2p(203),"|")
    cnv.drawString(mm2p(155),mm2p(201),"|")
    cnv.drawString(mm2p(155),mm2p(199),"|")
    cnv.drawString(mm2p(155),mm2p(197),"|")
    cnv.drawString(mm2p(155),mm2p(195),"|")
    cnv.drawString(mm2p(155),mm2p(193),"|")
    cnv.drawString(mm2p(155),mm2p(191),"|")

    #
    cnv.drawString(mm2p(165),mm2p(205),"|")
    cnv.drawString(mm2p(165),mm2p(207),"|")
    cnv.drawString(mm2p(165),mm2p(209),"|")

    cnv.drawString(mm2p(165),mm2p(203),"|")
    cnv.drawString(mm2p(165),mm2p(201),"|")
    cnv.drawString(mm2p(165),mm2p(199),"|")
    cnv.drawString(mm2p(165),mm2p(197),"|")
    cnv.drawString(mm2p(165),mm2p(195),"|")
    cnv.drawString(mm2p(165),mm2p(193),"|")
    cnv.drawString(mm2p(165),mm2p(191),"|")

    #
    cnv.drawString(mm2p(175),mm2p(205),"|")
    cnv.drawString(mm2p(175),mm2p(207),"|")
    cnv.drawString(mm2p(175),mm2p(209),"|")

    cnv.drawString(mm2p(175),mm2p(203),"|")
    cnv.drawString(mm2p(175),mm2p(201),"|")
    cnv.drawString(mm2p(175),mm2p(199),"|")
    cnv.drawString(mm2p(175),mm2p(197),"|")
    cnv.drawString(mm2p(175),mm2p(195),"|")
    cnv.drawString(mm2p(175),mm2p(193),"|")
    cnv.drawString(mm2p(175),mm2p(191),"|")

    #
    cnv.drawString(mm2p(184),mm2p(205),"|")
    cnv.drawString(mm2p(184),mm2p(207),"|")
    cnv.drawString(mm2p(184),mm2p(209),"|")

    cnv.drawString(mm2p(184),mm2p(203),"|")
    cnv.drawString(mm2p(184),mm2p(201),"|")
    cnv.drawString(mm2p(184),mm2p(199),"|")
    cnv.drawString(mm2p(184),mm2p(197),"|")
    cnv.drawString(mm2p(184),mm2p(195),"|")
    cnv.drawString(mm2p(184),mm2p(193),"|")
    cnv.drawString(mm2p(184),mm2p(191),"|")

    ## INSERINDO AS GRADES
    # canto esquerdo
    cnv.drawString(mm2p(14),mm2p(185),"|")
    cnv.drawString(mm2p(14),mm2p(187),"|")
    cnv.drawString(mm2p(14),mm2p(189),"|")

    cnv.drawString(mm2p(14),mm2p(183),"|")
    cnv.drawString(mm2p(14),mm2p(181),"|")
    cnv.drawString(mm2p(14),mm2p(179),"|")
    cnv.drawString(mm2p(14),mm2p(177),"|")
    cnv.drawString(mm2p(14),mm2p(175),"|")
    cnv.drawString(mm2p(14),mm2p(173),"|")
    cnv.drawString(mm2p(14),mm2p(171),"|")
    # canto direito
    cnv.drawString(mm2p(198),mm2p(185),"|")
    cnv.drawString(mm2p(198),mm2p(187),"|")
    cnv.drawString(mm2p(198),mm2p(189),"|")

    cnv.drawString(mm2p(198),mm2p(183),"|")
    cnv.drawString(mm2p(198),mm2p(181),"|")
    cnv.drawString(mm2p(198),mm2p(179),"|")
    cnv.drawString(mm2p(198),mm2p(177),"|")
    cnv.drawString(mm2p(198),mm2p(175),"|")
    cnv.drawString(mm2p(198),mm2p(173),"|")
    cnv.drawString(mm2p(198),mm2p(171),"|")

    #
    cnv.drawString(mm2p(137),mm2p(185),"|")
    cnv.drawString(mm2p(137),mm2p(187),"|")
    cnv.drawString(mm2p(137),mm2p(189),"|")

    cnv.drawString(mm2p(137),mm2p(183),"|")
    cnv.drawString(mm2p(137),mm2p(181),"|")
    cnv.drawString(mm2p(137),mm2p(179),"|")
    cnv.drawString(mm2p(137),mm2p(177),"|")
    cnv.drawString(mm2p(137),mm2p(175),"|")
    cnv.drawString(mm2p(137),mm2p(173),"|")
    cnv.drawString(mm2p(137),mm2p(171),"|")

    #
    cnv.drawString(mm2p(146),mm2p(185),"|")
    cnv.drawString(mm2p(146),mm2p(187),"|")
    cnv.drawString(mm2p(146),mm2p(189),"|")

    cnv.drawString(mm2p(146),mm2p(183),"|")
    cnv.drawString(mm2p(146),mm2p(181),"|")
    cnv.drawString(mm2p(146),mm2p(179),"|")
    cnv.drawString(mm2p(146),mm2p(177),"|")
    cnv.drawString(mm2p(146),mm2p(175),"|")
    cnv.drawString(mm2p(146),mm2p(173),"|")
    cnv.drawString(mm2p(146),mm2p(171),"|")

    #
    cnv.drawString(mm2p(155),mm2p(185),"|")
    cnv.drawString(mm2p(155),mm2p(187),"|")
    cnv.drawString(mm2p(155),mm2p(189),"|")

    cnv.drawString(mm2p(155),mm2p(183),"|")
    cnv.drawString(mm2p(155),mm2p(181),"|")
    cnv.drawString(mm2p(155),mm2p(179),"|")
    cnv.drawString(mm2p(155),mm2p(177),"|")
    cnv.drawString(mm2p(155),mm2p(175),"|")
    cnv.drawString(mm2p(155),mm2p(173),"|")
    cnv.drawString(mm2p(155),mm2p(171),"|")

    #
    cnv.drawString(mm2p(165),mm2p(185),"|")
    cnv.drawString(mm2p(165),mm2p(187),"|")
    cnv.drawString(mm2p(165),mm2p(189),"|")

    cnv.drawString(mm2p(165),mm2p(183),"|")
    cnv.drawString(mm2p(165),mm2p(181),"|")
    cnv.drawString(mm2p(165),mm2p(179),"|")
    cnv.drawString(mm2p(165),mm2p(177),"|")
    cnv.drawString(mm2p(165),mm2p(175),"|")
    cnv.drawString(mm2p(165),mm2p(173),"|")
    cnv.drawString(mm2p(165),mm2p(171),"|")

    #
    cnv.drawString(mm2p(175),mm2p(185),"|")
    cnv.drawString(mm2p(175),mm2p(187),"|")
    cnv.drawString(mm2p(175),mm2p(189),"|")

    cnv.drawString(mm2p(175),mm2p(183),"|")
    cnv.drawString(mm2p(175),mm2p(181),"|")
    cnv.drawString(mm2p(175),mm2p(179),"|")
    cnv.drawString(mm2p(175),mm2p(177),"|")
    cnv.drawString(mm2p(175),mm2p(175),"|")
    cnv.drawString(mm2p(175),mm2p(173),"|")
    cnv.drawString(mm2p(175),mm2p(171),"|")

    #
    cnv.drawString(mm2p(184),mm2p(185),"|")
    cnv.drawString(mm2p(184),mm2p(187),"|")
    cnv.drawString(mm2p(184),mm2p(189),"|")

    cnv.drawString(mm2p(184),mm2p(183),"|")
    cnv.drawString(mm2p(184),mm2p(181),"|")
    cnv.drawString(mm2p(184),mm2p(179),"|")
    cnv.drawString(mm2p(184),mm2p(177),"|")
    cnv.drawString(mm2p(184),mm2p(175),"|")
    cnv.drawString(mm2p(184),mm2p(173),"|")
    cnv.drawString(mm2p(184),mm2p(171),"|")


    cnv.drawString(mm2p(14.5),mm2p(171),"______________________________________________________________________________________________________________________________________")

    ## INSERINDO AS GRADES
    # canto esquerdo
    cnv.drawString(mm2p(14),mm2p(165),"|")
    cnv.drawString(mm2p(14),mm2p(167),"|")
    cnv.drawString(mm2p(14),mm2p(169),"|")

    cnv.drawString(mm2p(14),mm2p(163),"|")
    cnv.drawString(mm2p(14),mm2p(161),"|")
    cnv.drawString(mm2p(14),mm2p(159),"|")
    cnv.drawString(mm2p(14),mm2p(151),"|")
    cnv.drawString(mm2p(14),mm2p(157),"|")
    cnv.drawString(mm2p(14),mm2p(155),"|")
    cnv.drawString(mm2p(14),mm2p(153),"|")
    # canto direito
    cnv.drawString(mm2p(198),mm2p(165),"|")
    cnv.drawString(mm2p(198),mm2p(167),"|")
    cnv.drawString(mm2p(198),mm2p(169),"|")

    cnv.drawString(mm2p(198),mm2p(163),"|")
    cnv.drawString(mm2p(198),mm2p(161),"|")
    cnv.drawString(mm2p(198),mm2p(159),"|")
    cnv.drawString(mm2p(198),mm2p(151),"|")
    cnv.drawString(mm2p(198),mm2p(157),"|")
    cnv.drawString(mm2p(198),mm2p(155),"|")
    cnv.drawString(mm2p(198),mm2p(153),"|")

    #
    cnv.drawString(mm2p(137),mm2p(165),"|")
    cnv.drawString(mm2p(137),mm2p(167),"|")
    cnv.drawString(mm2p(137),mm2p(169),"|")

    cnv.drawString(mm2p(137),mm2p(163),"|")
    cnv.drawString(mm2p(137),mm2p(161),"|")
    cnv.drawString(mm2p(137),mm2p(159),"|")
    cnv.drawString(mm2p(137),mm2p(151),"|")
    cnv.drawString(mm2p(137),mm2p(157),"|")
    cnv.drawString(mm2p(137),mm2p(155),"|")
    cnv.drawString(mm2p(137),mm2p(153),"|")

    #
    cnv.drawString(mm2p(146),mm2p(165),"|")
    cnv.drawString(mm2p(146),mm2p(167),"|")
    cnv.drawString(mm2p(146),mm2p(169),"|")

    cnv.drawString(mm2p(146),mm2p(163),"|")
    cnv.drawString(mm2p(146),mm2p(161),"|")
    cnv.drawString(mm2p(146),mm2p(159),"|")
    cnv.drawString(mm2p(146),mm2p(151),"|")
    cnv.drawString(mm2p(146),mm2p(157),"|")
    cnv.drawString(mm2p(146),mm2p(155),"|")
    cnv.drawString(mm2p(146),mm2p(153),"|")

    #
    cnv.drawString(mm2p(155),mm2p(165),"|")
    cnv.drawString(mm2p(155),mm2p(167),"|")
    cnv.drawString(mm2p(155),mm2p(169),"|")

    cnv.drawString(mm2p(155),mm2p(163),"|")
    cnv.drawString(mm2p(155),mm2p(161),"|")
    cnv.drawString(mm2p(155),mm2p(159),"|")
    cnv.drawString(mm2p(155),mm2p(151),"|")
    cnv.drawString(mm2p(155),mm2p(157),"|")
    cnv.drawString(mm2p(155),mm2p(155),"|")
    cnv.drawString(mm2p(155),mm2p(153),"|")

    #
    cnv.drawString(mm2p(165),mm2p(165),"|")
    cnv.drawString(mm2p(165),mm2p(167),"|")
    cnv.drawString(mm2p(165),mm2p(169),"|")

    cnv.drawString(mm2p(165),mm2p(163),"|")
    cnv.drawString(mm2p(165),mm2p(161),"|")
    cnv.drawString(mm2p(165),mm2p(159),"|")
    cnv.drawString(mm2p(165),mm2p(151),"|")
    cnv.drawString(mm2p(165),mm2p(157),"|")
    cnv.drawString(mm2p(165),mm2p(155),"|")
    cnv.drawString(mm2p(165),mm2p(153),"|")

    #
    cnv.drawString(mm2p(175),mm2p(165),"|")
    cnv.drawString(mm2p(175),mm2p(167),"|")
    cnv.drawString(mm2p(175),mm2p(169),"|")

    cnv.drawString(mm2p(175),mm2p(163),"|")
    cnv.drawString(mm2p(175),mm2p(161),"|")
    cnv.drawString(mm2p(175),mm2p(159),"|")
    cnv.drawString(mm2p(175),mm2p(151),"|")
    cnv.drawString(mm2p(175),mm2p(157),"|")
    cnv.drawString(mm2p(175),mm2p(155),"|")
    cnv.drawString(mm2p(175),mm2p(153),"|")

    #
    cnv.drawString(mm2p(184),mm2p(165),"|")
    cnv.drawString(mm2p(184),mm2p(167),"|")
    cnv.drawString(mm2p(184),mm2p(169),"|")

    cnv.drawString(mm2p(184),mm2p(163),"|")
    cnv.drawString(mm2p(184),mm2p(161),"|")
    cnv.drawString(mm2p(184),mm2p(159),"|")
    cnv.drawString(mm2p(184),mm2p(151),"|")
    cnv.drawString(mm2p(184),mm2p(157),"|")
    cnv.drawString(mm2p(184),mm2p(155),"|")
    cnv.drawString(mm2p(184),mm2p(153),"|")


    cnv.drawString(mm2p(14.5),mm2p(151),"______________________________________________________________________________________________________________________________________")

    cnv.drawString(mm2p(14.5),mm2p(191),"______________________________________________________________________________________________________________________________________")

    ## INSERINDO AS GRADES
    # canto esquerdo
    cnv.drawString(mm2p(14),mm2p(145),"|")
    cnv.drawString(mm2p(14),mm2p(147),"|")
    cnv.drawString(mm2p(14),mm2p(149),"|")

    cnv.drawString(mm2p(14),mm2p(143),"|")
    cnv.drawString(mm2p(14),mm2p(141),"|")
    cnv.drawString(mm2p(14),mm2p(139),"|")
    cnv.drawString(mm2p(14),mm2p(137),"|")
    cnv.drawString(mm2p(14),mm2p(135),"|")
    cnv.drawString(mm2p(14),mm2p(133),"|")
    cnv.drawString(mm2p(14),mm2p(131),"|")
    cnv.drawString(mm2p(14),mm2p(129),"|")
    cnv.drawString(mm2p(14),mm2p(127),"|")

    # canto direito
    cnv.drawString(mm2p(198),mm2p(145),"|")
    cnv.drawString(mm2p(198),mm2p(147),"|")
    cnv.drawString(mm2p(198),mm2p(149),"|")

    cnv.drawString(mm2p(198),mm2p(143),"|")
    cnv.drawString(mm2p(198),mm2p(141),"|")
    cnv.drawString(mm2p(198),mm2p(139),"|")
    cnv.drawString(mm2p(198),mm2p(137),"|")
    cnv.drawString(mm2p(198),mm2p(135),"|")
    cnv.drawString(mm2p(198),mm2p(133),"|")
    cnv.drawString(mm2p(198),mm2p(131),"|")
    cnv.drawString(mm2p(198),mm2p(129),"|")
    cnv.drawString(mm2p(198),mm2p(127),"|")

    #
    cnv.drawString(mm2p(137),mm2p(145),"|")
    cnv.drawString(mm2p(137),mm2p(147),"|")
    cnv.drawString(mm2p(137),mm2p(149),"|")

    cnv.drawString(mm2p(137),mm2p(143),"|")
    cnv.drawString(mm2p(137),mm2p(141),"|")
    cnv.drawString(mm2p(137),mm2p(139),"|")
    cnv.drawString(mm2p(137),mm2p(137),"|")
    cnv.drawString(mm2p(137),mm2p(135),"|")
    cnv.drawString(mm2p(137),mm2p(133),"|")
    cnv.drawString(mm2p(137),mm2p(131),"|")
    cnv.drawString(mm2p(137),mm2p(129),"|")
    cnv.drawString(mm2p(137),mm2p(127),"|")

    #
    cnv.drawString(mm2p(146),mm2p(145),"|")
    cnv.drawString(mm2p(146),mm2p(147),"|")
    cnv.drawString(mm2p(146),mm2p(149),"|")

    cnv.drawString(mm2p(146),mm2p(143),"|")
    cnv.drawString(mm2p(146),mm2p(141),"|")
    cnv.drawString(mm2p(146),mm2p(139),"|")
    cnv.drawString(mm2p(146),mm2p(137),"|")
    cnv.drawString(mm2p(146),mm2p(135),"|")
    cnv.drawString(mm2p(146),mm2p(133),"|")
    cnv.drawString(mm2p(146),mm2p(131),"|")
    cnv.drawString(mm2p(146),mm2p(129),"|")
    cnv.drawString(mm2p(146),mm2p(127),"|")

    #
    cnv.drawString(mm2p(155),mm2p(145),"|")
    cnv.drawString(mm2p(155),mm2p(147),"|")
    cnv.drawString(mm2p(155),mm2p(149),"|")

    cnv.drawString(mm2p(155),mm2p(143),"|")
    cnv.drawString(mm2p(155),mm2p(141),"|")
    cnv.drawString(mm2p(155),mm2p(139),"|")
    cnv.drawString(mm2p(155),mm2p(137),"|")
    cnv.drawString(mm2p(155),mm2p(135),"|")
    cnv.drawString(mm2p(155),mm2p(133),"|")
    cnv.drawString(mm2p(155),mm2p(131),"|")
    cnv.drawString(mm2p(155),mm2p(129),"|")
    cnv.drawString(mm2p(155),mm2p(127),"|")

    #
    cnv.drawString(mm2p(165),mm2p(145),"|")
    cnv.drawString(mm2p(165),mm2p(147),"|")
    cnv.drawString(mm2p(165),mm2p(149),"|")

    cnv.drawString(mm2p(165),mm2p(143),"|")
    cnv.drawString(mm2p(165),mm2p(141),"|")
    cnv.drawString(mm2p(165),mm2p(139),"|")
    cnv.drawString(mm2p(165),mm2p(137),"|")
    cnv.drawString(mm2p(165),mm2p(135),"|")
    cnv.drawString(mm2p(165),mm2p(133),"|")
    cnv.drawString(mm2p(165),mm2p(131),"|")
    cnv.drawString(mm2p(165),mm2p(129),"|")
    cnv.drawString(mm2p(165),mm2p(127),"|")

    #
    cnv.drawString(mm2p(175),mm2p(145),"|")
    cnv.drawString(mm2p(175),mm2p(147),"|")
    cnv.drawString(mm2p(175),mm2p(149),"|")

    cnv.drawString(mm2p(175),mm2p(143),"|")
    cnv.drawString(mm2p(175),mm2p(141),"|")
    cnv.drawString(mm2p(175),mm2p(139),"|")
    cnv.drawString(mm2p(175),mm2p(137),"|")
    cnv.drawString(mm2p(175),mm2p(135),"|")
    cnv.drawString(mm2p(175),mm2p(133),"|")
    cnv.drawString(mm2p(175),mm2p(131),"|")
    cnv.drawString(mm2p(175),mm2p(129),"|")
    cnv.drawString(mm2p(175),mm2p(127),"|")

    #
    cnv.drawString(mm2p(184),mm2p(145),"|")
    cnv.drawString(mm2p(184),mm2p(147),"|")
    cnv.drawString(mm2p(184),mm2p(149),"|")

    cnv.drawString(mm2p(184),mm2p(143),"|")
    cnv.drawString(mm2p(184),mm2p(141),"|")
    cnv.drawString(mm2p(184),mm2p(139),"|")
    cnv.drawString(mm2p(184),mm2p(137),"|")
    cnv.drawString(mm2p(184),mm2p(135),"|")
    cnv.drawString(mm2p(184),mm2p(133),"|")
    cnv.drawString(mm2p(184),mm2p(131),"|")
    cnv.drawString(mm2p(184),mm2p(129),"|")
    cnv.drawString(mm2p(184),mm2p(127),"|")


    cnv.drawString(mm2p(14.5),mm2p(115),"______________________________________________________________________________________________________________________________________")

    ## INSERINDO AS GRADES
    # canto esquerdo
    cnv.drawString(mm2p(14),mm2p(117),"|")
    cnv.drawString(mm2p(14),mm2p(119),"|")
    cnv.drawString(mm2p(14),mm2p(121),"|")
    cnv.drawString(mm2p(14),mm2p(123),"|")
    cnv.drawString(mm2p(14),mm2p(125),"|")

    cnv.drawString(mm2p(14),mm2p(115),"|")
    cnv.drawString(mm2p(14),mm2p(113),"|")
    cnv.drawString(mm2p(14),mm2p(111),"|")
    cnv.drawString(mm2p(14),mm2p(109),"|")
    cnv.drawString(mm2p(14),mm2p(107),"|")
    cnv.drawString(mm2p(14),mm2p(105),"|")
    cnv.drawString(mm2p(14),mm2p(103),"|")
    # canto direito
    cnv.drawString(mm2p(198),mm2p(117),"|")
    cnv.drawString(mm2p(198),mm2p(119),"|")
    cnv.drawString(mm2p(198),mm2p(121),"|")
    cnv.drawString(mm2p(198),mm2p(123),"|")
    cnv.drawString(mm2p(198),mm2p(125),"|")

    cnv.drawString(mm2p(198),mm2p(115),"|")
    cnv.drawString(mm2p(198),mm2p(113),"|")
    cnv.drawString(mm2p(198),mm2p(111),"|")
    cnv.drawString(mm2p(198),mm2p(109),"|")
    cnv.drawString(mm2p(198),mm2p(107),"|")
    cnv.drawString(mm2p(198),mm2p(105),"|")
    cnv.drawString(mm2p(198),mm2p(103),"|")

    #
    cnv.drawString(mm2p(137),mm2p(117),"|")
    cnv.drawString(mm2p(137),mm2p(119),"|")
    cnv.drawString(mm2p(137),mm2p(121),"|")
    cnv.drawString(mm2p(137),mm2p(123),"|")
    cnv.drawString(mm2p(137),mm2p(125),"|")

    cnv.drawString(mm2p(137),mm2p(115),"|")
    cnv.drawString(mm2p(137),mm2p(113),"|")
    cnv.drawString(mm2p(137),mm2p(111),"|")
    cnv.drawString(mm2p(137),mm2p(109),"|")
    cnv.drawString(mm2p(137),mm2p(107),"|")
    cnv.drawString(mm2p(137),mm2p(105),"|")
    cnv.drawString(mm2p(137),mm2p(103),"|")

    #
    cnv.drawString(mm2p(146),mm2p(117),"|")
    cnv.drawString(mm2p(146),mm2p(119),"|")
    cnv.drawString(mm2p(146),mm2p(121),"|")
    cnv.drawString(mm2p(146),mm2p(123),"|")
    cnv.drawString(mm2p(146),mm2p(125),"|")

    cnv.drawString(mm2p(146),mm2p(115),"|")
    cnv.drawString(mm2p(146),mm2p(113),"|")
    cnv.drawString(mm2p(146),mm2p(111),"|")
    cnv.drawString(mm2p(146),mm2p(109),"|")
    cnv.drawString(mm2p(146),mm2p(107),"|")
    cnv.drawString(mm2p(146),mm2p(105),"|")
    cnv.drawString(mm2p(146),mm2p(103),"|")

    #
    cnv.drawString(mm2p(155),mm2p(117),"|")
    cnv.drawString(mm2p(155),mm2p(119),"|")
    cnv.drawString(mm2p(155),mm2p(121),"|")
    cnv.drawString(mm2p(155),mm2p(123),"|")
    cnv.drawString(mm2p(155),mm2p(125),"|")

    cnv.drawString(mm2p(155),mm2p(115),"|")
    cnv.drawString(mm2p(155),mm2p(113),"|")
    cnv.drawString(mm2p(155),mm2p(111),"|")
    cnv.drawString(mm2p(155),mm2p(109),"|")
    cnv.drawString(mm2p(155),mm2p(107),"|")
    cnv.drawString(mm2p(155),mm2p(105),"|")
    cnv.drawString(mm2p(155),mm2p(103),"|")

    #
    cnv.drawString(mm2p(165),mm2p(117),"|")
    cnv.drawString(mm2p(165),mm2p(119),"|")
    cnv.drawString(mm2p(165),mm2p(121),"|")
    cnv.drawString(mm2p(165),mm2p(123),"|")
    cnv.drawString(mm2p(165),mm2p(125),"|")

    cnv.drawString(mm2p(165),mm2p(115),"|")
    cnv.drawString(mm2p(165),mm2p(113),"|")
    cnv.drawString(mm2p(165),mm2p(111),"|")
    cnv.drawString(mm2p(165),mm2p(109),"|")
    cnv.drawString(mm2p(165),mm2p(107),"|")
    cnv.drawString(mm2p(165),mm2p(105),"|")
    cnv.drawString(mm2p(165),mm2p(103),"|")

    #
    cnv.drawString(mm2p(175),mm2p(117),"|")
    cnv.drawString(mm2p(175),mm2p(119),"|")
    cnv.drawString(mm2p(175),mm2p(121),"|")
    cnv.drawString(mm2p(175),mm2p(123),"|")
    cnv.drawString(mm2p(175),mm2p(125),"|")

    cnv.drawString(mm2p(175),mm2p(115),"|")
    cnv.drawString(mm2p(175),mm2p(113),"|")
    cnv.drawString(mm2p(175),mm2p(111),"|")
    cnv.drawString(mm2p(175),mm2p(109),"|")
    cnv.drawString(mm2p(175),mm2p(107),"|")
    cnv.drawString(mm2p(175),mm2p(105),"|")
    cnv.drawString(mm2p(175),mm2p(103),"|")

    cnv.drawString(mm2p(184),mm2p(117),"|")
    cnv.drawString(mm2p(184),mm2p(119),"|")
    cnv.drawString(mm2p(184),mm2p(121),"|")
    cnv.drawString(mm2p(184),mm2p(123),"|")
    cnv.drawString(mm2p(184),mm2p(125),"|")

    cnv.drawString(mm2p(184),mm2p(115),"|")
    cnv.drawString(mm2p(184),mm2p(113),"|")
    cnv.drawString(mm2p(184),mm2p(111),"|")
    cnv.drawString(mm2p(184),mm2p(109),"|")
    cnv.drawString(mm2p(184),mm2p(107),"|")
    cnv.drawString(mm2p(184),mm2p(105),"|")
    cnv.drawString(mm2p(184),mm2p(103),"|")


    cnv.drawString(mm2p(14.5),mm2p(97),"______________________________________________________________________________________________________________________________________")

    ## INSERINDO AS GRADES
    # canto esquerdo
    cnv.drawString(mm2p(14),mm2p(97),"|")
    cnv.drawString(mm2p(14),mm2p(99),"|")
    cnv.drawString(mm2p(14),mm2p(101),"|")

    cnv.drawString(mm2p(14),mm2p(95),"|")
    cnv.drawString(mm2p(14),mm2p(93),"|")
    cnv.drawString(mm2p(14),mm2p(91),"|")
    cnv.drawString(mm2p(14),mm2p(89),"|")
    cnv.drawString(mm2p(14),mm2p(87),"|")
    cnv.drawString(mm2p(14),mm2p(85),"|")
    cnv.drawString(mm2p(14),mm2p(83),"|")
    # canto direito
    cnv.drawString(mm2p(198),mm2p(97),"|")
    cnv.drawString(mm2p(198),mm2p(99),"|")
    cnv.drawString(mm2p(198),mm2p(101),"|")

    cnv.drawString(mm2p(198),mm2p(95),"|")
    cnv.drawString(mm2p(198),mm2p(93),"|")
    cnv.drawString(mm2p(198),mm2p(91),"|")
    cnv.drawString(mm2p(198),mm2p(89),"|")
    cnv.drawString(mm2p(198),mm2p(87),"|")
    cnv.drawString(mm2p(198),mm2p(85),"|")
    cnv.drawString(mm2p(198),mm2p(83),"|")

    #
    cnv.drawString(mm2p(137),mm2p(97),"|")
    cnv.drawString(mm2p(137),mm2p(99),"|")
    cnv.drawString(mm2p(137),mm2p(101),"|")

    cnv.drawString(mm2p(137),mm2p(95),"|")
    cnv.drawString(mm2p(137),mm2p(93),"|")
    cnv.drawString(mm2p(137),mm2p(91),"|")
    cnv.drawString(mm2p(137),mm2p(89),"|")
    cnv.drawString(mm2p(137),mm2p(87),"|")
    cnv.drawString(mm2p(137),mm2p(85),"|")
    cnv.drawString(mm2p(137),mm2p(83),"|")

    #
    cnv.drawString(mm2p(146),mm2p(97),"|")
    cnv.drawString(mm2p(146),mm2p(99),"|")
    cnv.drawString(mm2p(146),mm2p(101),"|")

    cnv.drawString(mm2p(146),mm2p(95),"|")
    cnv.drawString(mm2p(146),mm2p(93),"|")
    cnv.drawString(mm2p(146),mm2p(91),"|")
    cnv.drawString(mm2p(146),mm2p(89),"|")
    cnv.drawString(mm2p(146),mm2p(87),"|")
    cnv.drawString(mm2p(146),mm2p(85),"|")
    cnv.drawString(mm2p(146),mm2p(83),"|")

    #
    cnv.drawString(mm2p(155),mm2p(97),"|")
    cnv.drawString(mm2p(155),mm2p(99),"|")
    cnv.drawString(mm2p(155),mm2p(101),"|")

    cnv.drawString(mm2p(155),mm2p(95),"|")
    cnv.drawString(mm2p(155),mm2p(93),"|")
    cnv.drawString(mm2p(155),mm2p(91),"|")
    cnv.drawString(mm2p(155),mm2p(89),"|")
    cnv.drawString(mm2p(155),mm2p(87),"|")
    cnv.drawString(mm2p(155),mm2p(85),"|")
    cnv.drawString(mm2p(155),mm2p(83),"|")

    #
    cnv.drawString(mm2p(165),mm2p(97),"|")
    cnv.drawString(mm2p(165),mm2p(99),"|")
    cnv.drawString(mm2p(165),mm2p(101),"|")

    cnv.drawString(mm2p(165),mm2p(95),"|")
    cnv.drawString(mm2p(165),mm2p(93),"|")
    cnv.drawString(mm2p(165),mm2p(91),"|")
    cnv.drawString(mm2p(165),mm2p(89),"|")
    cnv.drawString(mm2p(165),mm2p(87),"|")
    cnv.drawString(mm2p(165),mm2p(85),"|")
    cnv.drawString(mm2p(165),mm2p(83),"|")

    #
    cnv.drawString(mm2p(175),mm2p(97),"|")
    cnv.drawString(mm2p(175),mm2p(99),"|")
    cnv.drawString(mm2p(175),mm2p(101),"|")

    cnv.drawString(mm2p(175),mm2p(95),"|")
    cnv.drawString(mm2p(175),mm2p(93),"|")
    cnv.drawString(mm2p(175),mm2p(91),"|")
    cnv.drawString(mm2p(175),mm2p(89),"|")
    cnv.drawString(mm2p(175),mm2p(87),"|")
    cnv.drawString(mm2p(175),mm2p(85),"|")
    cnv.drawString(mm2p(175),mm2p(83),"|")

    #
    cnv.drawString(mm2p(184),mm2p(97),"|")
    cnv.drawString(mm2p(184),mm2p(99),"|")
    cnv.drawString(mm2p(184),mm2p(101),"|")

    cnv.drawString(mm2p(184),mm2p(95),"|")
    cnv.drawString(mm2p(184),mm2p(93),"|")
    cnv.drawString(mm2p(184),mm2p(91),"|")
    cnv.drawString(mm2p(184),mm2p(89),"|")
    cnv.drawString(mm2p(184),mm2p(87),"|")
    cnv.drawString(mm2p(184),mm2p(85),"|")
    cnv.drawString(mm2p(184),mm2p(83),"|")

    cnv.drawString(mm2p(14),mm2p(81),"|")
    cnv.drawString(mm2p(14),mm2p(79),"|")
    cnv.drawString(mm2p(14),mm2p(77),"|")
    cnv.drawString(mm2p(14),mm2p(75),"|")
    cnv.drawString(mm2p(14),mm2p(73),"|")

    cnv.drawString(mm2p(137),mm2p(81),"|")
    cnv.drawString(mm2p(137),mm2p(79),"|")
    cnv.drawString(mm2p(137),mm2p(77),"|")
    cnv.drawString(mm2p(137),mm2p(75),"|")
    cnv.drawString(mm2p(137),mm2p(73),"|")

    cnv.drawString(mm2p(146),mm2p(81),"|")
    cnv.drawString(mm2p(146),mm2p(79),"|")
    cnv.drawString(mm2p(146),mm2p(77),"|")
    cnv.drawString(mm2p(146),mm2p(75),"|")
    cnv.drawString(mm2p(146),mm2p(73),"|")

    cnv.drawString(mm2p(155),mm2p(81),"|")
    cnv.drawString(mm2p(155),mm2p(79),"|")
    cnv.drawString(mm2p(155),mm2p(77),"|")
    cnv.drawString(mm2p(155),mm2p(75),"|")
    cnv.drawString(mm2p(155),mm2p(73),"|")

    cnv.drawString(mm2p(165),mm2p(81),"|")
    cnv.drawString(mm2p(165),mm2p(79),"|")
    cnv.drawString(mm2p(165),mm2p(77),"|")
    cnv.drawString(mm2p(165),mm2p(75),"|")
    cnv.drawString(mm2p(165),mm2p(73),"|")

    cnv.drawString(mm2p(175),mm2p(81),"|")
    cnv.drawString(mm2p(175),mm2p(79),"|")
    cnv.drawString(mm2p(175),mm2p(77),"|")
    cnv.drawString(mm2p(175),mm2p(75),"|")
    cnv.drawString(mm2p(175),mm2p(73),"|")

    cnv.drawString(mm2p(184),mm2p(81),"|")
    cnv.drawString(mm2p(184),mm2p(79),"|")
    cnv.drawString(mm2p(184),mm2p(77),"|")
    cnv.drawString(mm2p(184),mm2p(75),"|")
    cnv.drawString(mm2p(184),mm2p(73),"|")

    cnv.drawString(mm2p(198),mm2p(81),"|")
    cnv.drawString(mm2p(198),mm2p(79),"|")
    cnv.drawString(mm2p(198),mm2p(77),"|")
    cnv.drawString(mm2p(198),mm2p(75),"|")
    cnv.drawString(mm2p(198),mm2p(73),"|")


    cnv.drawString(mm2p(14.5),mm2p(73),"______________________________________________________________________________________________________________________________________")

    cnv.drawString(mm2p(14),mm2p(73),"|")
    cnv.drawString(mm2p(14),mm2p(71),"|")
    cnv.drawString(mm2p(14),mm2p(69),"|")
    cnv.drawString(mm2p(14),mm2p(67),"|")
    cnv.drawString(mm2p(14),mm2p(65),"|")
    cnv.drawString(mm2p(14),mm2p(63),"|")
    cnv.drawString(mm2p(14),mm2p(61),"|")
    cnv.drawString(mm2p(14),mm2p(59),"|")
    cnv.drawString(mm2p(14),mm2p(57),"|")

    # canto direito
    cnv.drawString(mm2p(198),mm2p(73),"|")
    cnv.drawString(mm2p(198),mm2p(71),"|")
    cnv.drawString(mm2p(198),mm2p(69),"|")
    cnv.drawString(mm2p(198),mm2p(67),"|")
    cnv.drawString(mm2p(198),mm2p(65),"|")

    cnv.drawString(mm2p(198),mm2p(63),"|")
    cnv.drawString(mm2p(198),mm2p(61),"|")
    cnv.drawString(mm2p(198),mm2p(59),"|")
    cnv.drawString(mm2p(198),mm2p(57),"|")

    #
    cnv.drawString(mm2p(137),mm2p(73),"|")
    cnv.drawString(mm2p(137),mm2p(71),"|")
    cnv.drawString(mm2p(137),mm2p(69),"|")
    cnv.drawString(mm2p(137),mm2p(67),"|")
    cnv.drawString(mm2p(137),mm2p(65),"|")
    cnv.drawString(mm2p(137),mm2p(63),"|")
    cnv.drawString(mm2p(137),mm2p(61),"|")
    cnv.drawString(mm2p(137),mm2p(59),"|")
    cnv.drawString(mm2p(137),mm2p(57),"|")

    #
    cnv.drawString(mm2p(146),mm2p(73),"|")
    cnv.drawString(mm2p(146),mm2p(71),"|")
    cnv.drawString(mm2p(146),mm2p(69),"|")
    cnv.drawString(mm2p(146),mm2p(67),"|")
    cnv.drawString(mm2p(146),mm2p(65),"|")

    cnv.drawString(mm2p(146),mm2p(63),"|")
    cnv.drawString(mm2p(146),mm2p(61),"|")
    cnv.drawString(mm2p(146),mm2p(59),"|")
    cnv.drawString(mm2p(146),mm2p(57),"|")

    #
    cnv.drawString(mm2p(155),mm2p(73),"|")
    cnv.drawString(mm2p(155),mm2p(71),"|")
    cnv.drawString(mm2p(155),mm2p(69),"|")
    cnv.drawString(mm2p(155),mm2p(67),"|")
    cnv.drawString(mm2p(155),mm2p(65),"|")

    cnv.drawString(mm2p(155),mm2p(63),"|")
    cnv.drawString(mm2p(155),mm2p(61),"|")
    cnv.drawString(mm2p(155),mm2p(59),"|")
    cnv.drawString(mm2p(155),mm2p(57),"|")

    #
    cnv.drawString(mm2p(165),mm2p(73),"|")
    cnv.drawString(mm2p(165),mm2p(71),"|")
    cnv.drawString(mm2p(165),mm2p(69),"|")
    cnv.drawString(mm2p(165),mm2p(67),"|")
    cnv.drawString(mm2p(165),mm2p(65),"|")
    cnv.drawString(mm2p(165),mm2p(63),"|")
    cnv.drawString(mm2p(165),mm2p(61),"|")
    cnv.drawString(mm2p(165),mm2p(59),"|")
    cnv.drawString(mm2p(165),mm2p(57),"|")

    #
    cnv.drawString(mm2p(175),mm2p(73),"|")
    cnv.drawString(mm2p(175),mm2p(71),"|")
    cnv.drawString(mm2p(175),mm2p(69),"|")
    cnv.drawString(mm2p(175),mm2p(67),"|")
    cnv.drawString(mm2p(175),mm2p(65),"|")
    cnv.drawString(mm2p(175),mm2p(63),"|")
    cnv.drawString(mm2p(175),mm2p(61),"|")
    cnv.drawString(mm2p(175),mm2p(59),"|")
    cnv.drawString(mm2p(175),mm2p(57),"|")

    cnv.drawString(mm2p(184),mm2p(73),"|")
    cnv.drawString(mm2p(184),mm2p(71),"|")
    cnv.drawString(mm2p(184),mm2p(69),"|")
    cnv.drawString(mm2p(184),mm2p(67),"|")
    cnv.drawString(mm2p(184),mm2p(65),"|")
    cnv.drawString(mm2p(184),mm2p(63),"|")
    cnv.drawString(mm2p(184),mm2p(61),"|")
    cnv.drawString(mm2p(184),mm2p(59),"|")
    cnv.drawString(mm2p(184),mm2p(57),"|")

    cnv.drawString(mm2p(14.5),mm2p(57),"______________________________________________________________________________________________________________________________________")

    cnv.drawString(mm2p(14),mm2p(57),"|")
    cnv.drawString(mm2p(14),mm2p(55),"|")
    cnv.drawString(mm2p(14),mm2p(53),"|")
    cnv.drawString(mm2p(14),mm2p(51),"|")
    cnv.drawString(mm2p(14),mm2p(49),"|")
    cnv.drawString(mm2p(14),mm2p(47),"|")
    cnv.drawString(mm2p(14),mm2p(45),"|")
    cnv.drawString(mm2p(14),mm2p(43),"|")
    cnv.drawString(mm2p(14),mm2p(41),"|")
    cnv.drawString(mm2p(14),mm2p(39),"|")
    cnv.drawString(mm2p(14),mm2p(37),"|")
    cnv.drawString(mm2p(14),mm2p(35),"|")
    cnv.drawString(mm2p(14),mm2p(33),"|")
    cnv.drawString(mm2p(14),mm2p(31),"|")
    cnv.drawString(mm2p(14),mm2p(29),"|")
    cnv.drawString(mm2p(14),mm2p(27),"|")
    cnv.drawString(mm2p(14),mm2p(25),"|")

    # canto direito
    cnv.drawString(mm2p(198),mm2p(57),"|")
    cnv.drawString(mm2p(198),mm2p(55),"|")
    cnv.drawString(mm2p(198),mm2p(53),"|")
    cnv.drawString(mm2p(198),mm2p(51),"|")
    cnv.drawString(mm2p(198),mm2p(49),"|")
    cnv.drawString(mm2p(198),mm2p(47),"|")
    cnv.drawString(mm2p(198),mm2p(45),"|")
    cnv.drawString(mm2p(198),mm2p(43),"|")
    cnv.drawString(mm2p(198),mm2p(41),"|")
    cnv.drawString(mm2p(198),mm2p(39),"|")
    cnv.drawString(mm2p(198),mm2p(37),"|")
    cnv.drawString(mm2p(198),mm2p(35),"|")
    cnv.drawString(mm2p(198),mm2p(33),"|")
    cnv.drawString(mm2p(198),mm2p(31),"|")
    cnv.drawString(mm2p(198),mm2p(29),"|")
    cnv.drawString(mm2p(198),mm2p(27),"|")
    cnv.drawString(mm2p(198),mm2p(25),"|")
    #
    cnv.drawString(mm2p(137),mm2p(57),"|")
    cnv.drawString(mm2p(137),mm2p(55),"|")
    cnv.drawString(mm2p(137),mm2p(53),"|")
    cnv.drawString(mm2p(137),mm2p(51),"|")
    cnv.drawString(mm2p(137),mm2p(49),"|")
    cnv.drawString(mm2p(137),mm2p(47),"|")
    cnv.drawString(mm2p(137),mm2p(45),"|")
    cnv.drawString(mm2p(137),mm2p(43),"|")
    cnv.drawString(mm2p(137),mm2p(41),"|")
    cnv.drawString(mm2p(137),mm2p(39),"|")
    cnv.drawString(mm2p(137),mm2p(37),"|")
    cnv.drawString(mm2p(137),mm2p(35),"|")
    cnv.drawString(mm2p(137),mm2p(33),"|")
    cnv.drawString(mm2p(137),mm2p(31),"|")
    cnv.drawString(mm2p(137),mm2p(29),"|")
    cnv.drawString(mm2p(137),mm2p(27),"|")
    cnv.drawString(mm2p(137),mm2p(25),"|")

    #
    cnv.drawString(mm2p(146),mm2p(57),"|")
    cnv.drawString(mm2p(146),mm2p(55),"|")
    cnv.drawString(mm2p(146),mm2p(53),"|")
    cnv.drawString(mm2p(146),mm2p(51),"|")
    cnv.drawString(mm2p(146),mm2p(49),"|")
    cnv.drawString(mm2p(146),mm2p(47),"|")
    cnv.drawString(mm2p(146),mm2p(45),"|")
    cnv.drawString(mm2p(146),mm2p(43),"|")
    cnv.drawString(mm2p(146),mm2p(41),"|")
    cnv.drawString(mm2p(146),mm2p(39),"|")
    cnv.drawString(mm2p(146),mm2p(37),"|")
    cnv.drawString(mm2p(146),mm2p(35),"|")
    cnv.drawString(mm2p(146),mm2p(33),"|")
    cnv.drawString(mm2p(146),mm2p(31),"|")
    cnv.drawString(mm2p(146),mm2p(29),"|")
    cnv.drawString(mm2p(146),mm2p(27),"|")
    cnv.drawString(mm2p(146),mm2p(25),"|")

    #
    cnv.drawString(mm2p(155),mm2p(57),"|")
    cnv.drawString(mm2p(155),mm2p(55),"|")
    cnv.drawString(mm2p(155),mm2p(53),"|")
    cnv.drawString(mm2p(155),mm2p(51),"|")
    cnv.drawString(mm2p(155),mm2p(49),"|")
    cnv.drawString(mm2p(155),mm2p(47),"|")
    cnv.drawString(mm2p(155),mm2p(45),"|")
    cnv.drawString(mm2p(155),mm2p(43),"|")
    cnv.drawString(mm2p(155),mm2p(41),"|")
    cnv.drawString(mm2p(155),mm2p(39),"|")
    cnv.drawString(mm2p(155),mm2p(37),"|")
    cnv.drawString(mm2p(155),mm2p(35),"|")
    cnv.drawString(mm2p(155),mm2p(33),"|")
    cnv.drawString(mm2p(155),mm2p(31),"|")
    cnv.drawString(mm2p(155),mm2p(29),"|")
    cnv.drawString(mm2p(155),mm2p(27),"|")
    cnv.drawString(mm2p(155),mm2p(25),"|")

    #
    cnv.drawString(mm2p(165),mm2p(57),"|")
    cnv.drawString(mm2p(165),mm2p(55),"|")
    cnv.drawString(mm2p(165),mm2p(53),"|")
    cnv.drawString(mm2p(165),mm2p(51),"|")
    cnv.drawString(mm2p(165),mm2p(49),"|")
    cnv.drawString(mm2p(165),mm2p(47),"|")
    cnv.drawString(mm2p(165),mm2p(45),"|")
    cnv.drawString(mm2p(165),mm2p(43),"|")
    cnv.drawString(mm2p(165),mm2p(41),"|")
    cnv.drawString(mm2p(165),mm2p(39),"|")
    cnv.drawString(mm2p(165),mm2p(37),"|")
    cnv.drawString(mm2p(165),mm2p(35),"|")
    cnv.drawString(mm2p(165),mm2p(33),"|")
    cnv.drawString(mm2p(165),mm2p(31),"|")
    cnv.drawString(mm2p(165),mm2p(29),"|")
    cnv.drawString(mm2p(165),mm2p(27),"|")
    cnv.drawString(mm2p(165),mm2p(25),"|")

    #

    cnv.drawString(mm2p(175),mm2p(57),"|")
    cnv.drawString(mm2p(175),mm2p(55),"|")
    cnv.drawString(mm2p(175),mm2p(53),"|")
    cnv.drawString(mm2p(175),mm2p(51),"|")
    cnv.drawString(mm2p(175),mm2p(49),"|")
    cnv.drawString(mm2p(175),mm2p(47),"|")
    cnv.drawString(mm2p(175),mm2p(45),"|")
    cnv.drawString(mm2p(175),mm2p(43),"|")
    cnv.drawString(mm2p(175),mm2p(41),"|")
    cnv.drawString(mm2p(175),mm2p(39),"|")
    cnv.drawString(mm2p(175),mm2p(37),"|")
    cnv.drawString(mm2p(175),mm2p(35),"|")
    cnv.drawString(mm2p(175),mm2p(33),"|")
    cnv.drawString(mm2p(175),mm2p(31),"|")
    cnv.drawString(mm2p(175),mm2p(29),"|")
    cnv.drawString(mm2p(175),mm2p(27),"|")
    cnv.drawString(mm2p(175),mm2p(25),"|")

    #

    cnv.drawString(mm2p(184),mm2p(57),"|")
    cnv.drawString(mm2p(184),mm2p(55),"|")
    cnv.drawString(mm2p(184),mm2p(53),"|")
    cnv.drawString(mm2p(184),mm2p(51),"|")
    cnv.drawString(mm2p(184),mm2p(49),"|")
    cnv.drawString(mm2p(184),mm2p(47),"|")
    cnv.drawString(mm2p(184),mm2p(45),"|")
    cnv.drawString(mm2p(184),mm2p(43),"|")
    cnv.drawString(mm2p(184),mm2p(41),"|")
    cnv.drawString(mm2p(184),mm2p(39),"|")
    cnv.drawString(mm2p(184),mm2p(37),"|")
    cnv.drawString(mm2p(184),mm2p(35),"|")
    cnv.drawString(mm2p(184),mm2p(33),"|")
    cnv.drawString(mm2p(184),mm2p(31),"|")
    cnv.drawString(mm2p(184),mm2p(29),"|")
    cnv.drawString(mm2p(184),mm2p(27),"|")
    cnv.drawString(mm2p(184),mm2p(25),"|")

    cnv.drawString(mm2p(14.5),mm2p(25),"______________________________________________________________________________________________________________________________________")


    cnv.save()
