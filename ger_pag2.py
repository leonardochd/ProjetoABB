from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

#Transformar pontos em milímetros
def p2mm(mm):
    return mm/0.352777 


pastaApp=os.path.dirname(__file__)

def criarPDF():
    try:
        cnv=canvas.Canvas(pastaApp+"\\relatorio1.pdf",pagesize=A4) #folha A4 297x210 mm
        cnv.drawImage(pastaApp+"\\logo.png",p2mm(15),p2mm(270),p2mm(46),p2mm(17.5))
        cnv.drawString(p2mm(85),p2mm(277),"ELETRIFICATION DISTRIBUTION SYSTEMS")
        cnv.drawString(p2mm(125),p2mm(269),"DA SOLUTIONS PRODUCTS")
        cnv.drawString(p2mm(15), p2mm(259),"PROJETO / Project")
        cnv.drawString(p2mm(56), p2mm(259),":")
        cnv.drawString(p2mm(15), p2mm(250),"PEP")
        cnv.drawString(p2mm(56), p2mm(250),":")
        cnv.drawString(p2mm(15), p2mm(232),"TESTE REALIZADO EM (TEST PERFORMED ON):")
        cnv.drawString(p2mm(20), p2mm(222),"DATA INÍCIO/ Beginning")
        cnv.drawString(p2mm(110), p2mm(222),"DATA FIM/ End")
        cnv.drawString(p2mm(15), p2mm(194),"TESTE REALIZADO POR (TEST SURVEYED BY):")
        cnv.drawString(p2mm(20), p2mm(179),"Nome (name)")
        cnv.drawString(p2mm(60), p2mm(179),"Empresa (Company)")
        cnv.drawString(p2mm(113), p2mm(179),"Assinatura (Sign)")
        cnv.save()
    except:
        messagebox.showinfo(title="ERRO",message="Erro ao criar o arquivo PDF")
        return
    messagebox.showinfo(title="PDF",message="PDF criado com sucesso!")

app=Tk()
app.title("Relatorio")
app.geometry("600x450")

btn_criarPDF=Button(app,text="Criar PDF",command=criarPDF)
btn_criarPDF.pack(side="left",padx=10)

app.mainloop()