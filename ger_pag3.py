from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


# A4 = (210*mm,297*mm)



# Converte milimetros para pontos
def mm2p(milimetros):
    return milimetros / 0.352777


margem = 15

cnv = canvas.Canvas("relatorio.pdf", pagesize=A4)

cnv.drawImage("logo.png", mm2p(margem), mm2p(270))

# TITULO
cnv.setFont("Helvetica", 15)
cnv.drawString(mm2p(85),mm2p(277),"ELETRIFICATION DISTRIBUITION SYSTEMS")
cnv.drawString(mm2p(125),mm2p(269),"DA SOLUTIONS PRODUCTS")

#
cnv.setFont("Helvetica", 10)
cnv.drawString(mm2p(margem),mm2p(251),"INSPEÇÃO VISUAL E VERIFICAÇÕES DIMENSIONAIS")
cnv.drawString(mm2p(margem),mm2p(247),"VISUAL AND DIMENSIONAL INSPECTION")


cnv.setFont("Helvetica",7)
## APENAS OS TEXTOS POR ENQUANTO
cnv.drawString(mm2p(130+20),mm2p(241),"ABB Interno")
cnv.drawString(mm2p(155+20),mm2p(241),"Teste realizados com o cliente")

## Canto direito superior do quadrado 
cnv.drawString(mm2p(130+20),mm2p(236),"OK")
cnv.drawString(mm2p(139+20),mm2p(236),"NO")
cnv.drawString(mm2p(148+20),mm2p(236),"NA")
cnv.drawString(mm2p(159+20),mm2p(236),"OK")
cnv.drawString(mm2p(169+20),mm2p(236),"NO")
cnv.drawString(mm2p(177+20),mm2p(236),"Comment")

m_texto = 20

## Primeira pergunta
cnv.setFont("Helvetica",7)
cnv.drawString(mm2p(m_texto),mm2p(222),"Verifique se as unidades são construídas de acordo com as prescrições de compra e de projeto.")
cnv.drawString(mm2p(m_texto),mm2p(218),"Check that the are built according to the purchasing and design prescriptions.")

## Segunda pergunta
cnv.drawString(mm2p(m_texto),mm2p(202),"Verifique a ausência de deformidade e o nivelamento das chaparias.")
cnv.drawString(mm2p(m_texto),mm2p(198),"Check the absence of deformations and flatness of the sheets.")

## Terceira pergunta
cnv.drawString(mm2p(m_texto),mm2p(182),"Verifique a montagem correta e as conexões de aterramento em todos os componentes.")
cnv.drawString(mm2p(m_texto),mm2p(178),"Check the correct mounting and earthing connection in all components.")

## Quarta pergunta
cnv.drawString(mm2p(m_texto),mm2p(162),"Verifique a presença de dutos para a passagem de cabos auxiliares de acordo com os desenhos.")
cnv.drawString(mm2p(m_texto),mm2p(158),"Check the presence of the ducts for the passage of the auxiliary cables according to the drawings.")

# Quarta pergunta
cnv.drawString(mm2p(m_texto),mm2p(142),"Verifique a disposição correta para passagem dos cabos de alimentação de acordo com os desenhos de montagem.")
cnv.drawString(mm2p(m_texto),mm2p(138),"Check the correct disposition for the passage of the power cables according to the assembly drawings.")

## Terceira pergunta
cnv.drawString(mm2p(m_texto),mm2p(118),"Verifique a disposição correta dos equipamentos de acordo com os desenhos do projeto.")
cnv.drawString(mm2p(m_texto),mm2p(112),"Check the correct disposition of equipments according to the project drawings.")

## Terceira pergunta
cnv.drawString(mm2p(m_texto),mm2p(98),"Verifique se o equipamento não foi danificado durante a montagem.")
cnv.drawString(mm2p(m_texto),mm2p(92),"Check that no damage in the apparatus occurred during the assembly.")


cnv.save()