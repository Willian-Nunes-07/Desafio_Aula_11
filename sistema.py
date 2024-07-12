# 12.DESAFIO MATPLOT LIB, PANDAS, NUMPY
# Neste desafio, você irá criar um sistema que lê dados de um arquivo CSV, processa esses dados usando NumPy e Pandas, e gera gráficos com Matplotlib. Siga o passo a passo abaixo para completar a tarefa.


# Passo 1: Instalação das Bibliotecas
# Antes de começar, você precisa instalar as bibliotecas necessárias. Abra o terminal ou prompt de comando e execute os seguintes comandos:

# Passo 2: Preparação dos Dados
# Crie um arquivo CSV chamado dados.csv com o seguinte conteúdo:

# Passo 3: Criação do Sistema
# Agora, vamos criar o script Python que realizará as seguintes tarefas:
# Ler o arquivo CSV usando Pandas.
# Processar os dados usando NumPy.
# Gerar gráficos usando Matplotlib.
# Exibir a interface gráfica com Tkinter.
# Crie 5 botões 
# Em cada botão precisa mostrar um tipo de grafico
# Mostre a estatistica também


# dados.csv

# vendas,vendedor
# 1000,'CARLOS'
# 2000, 'FERNANDO'
# 3000,'MARIA'
# 50000,'MARTA'
# 9000,'ELOYSA'
# 7000,'CARMEM'
# 8000,'PABLO'



# Passo 4: Executar o Sistema
# Salve o script acima em um arquivo Python, por exemplo, sistema.py. Execute o script no terminal ou prompt de comando:

# Explicação do Sistema
# Ler o Arquivo CSV: Usamos pandas.read_csv para ler os dados do arquivo CSV.
# Processar os Dados: Extraímos os dados das colunas 'ano' e 'vendas' e os convertemos em arrays NumPy.
# Gerar Gráficos: Criamos um gráfico de linha com Matplotlib, adicionamos rótulos e título, e exibimos o gráfico na interface Tkinter.
# Interface Gráfica: Criamos uma interface simples com Tkinter que inclui um botão para gerar o gráfico.

# Desafio Extra

# Deixe executável em sua máquina 
# Crie um repositório no GIt Hub
# Suba o projeto 
# Insira o link  abaixo:
    
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

#Importação de dados:
dados = pd.read_csv("dados1.csv")
vendas = dados["vendas"].to_list()
vendedores = dados["vendedor"].to_list()

# Calculos Matematicos:
maior = np.max(vendas)
print("\nMaior:\n",maior)

menor = np.min(vendas)
print("\nMenor:\n",menor)

media = np.mean(vendas)
print("\nMedia:\n",f'{media:.2f}')

mediana = np.median(vendas)
print("\nMediana:\n",f'{mediana:.2f}')

desvio = np.std(vendas)
print("\nDesvio Padrão:\n",f'{desvio:.2f}')

#Interface:

janela = tk.Tk()

janela.title("Desafio Aula 11")

text = tk.Label(janela,text = "Graficos e Informações",) #Titulo
text2 = tk.Label(janela,text= "Escolha uma das opções abaixo:")
text.grid(row=0,column=0,columnspan=5)
text2.grid(row=1,column=0,columnspan=5)


#Graficos:
def pizza():
    fig = Figure(figsize=(8, 4), dpi=100)
    fig, grafico = plt.subplots()
    grafico.pie(vendas,labels=vendedores, autopct="%.1f%%")
    # grafico.set_xlabel("Vendas")
    # grafico.set_ylabel("Vendedores")
    canvas = FigureCanvasTkAgg(fig, master=janela)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=3,column=0,columnspan=5)
    
def barras():
    fig = Figure(figsize=(8, 4), dpi=100)
    fig, grafico = plt.subplots()
    grafico.bar(vendedores,vendas)
    grafico.set_ylabel("Vendas")
    grafico.set_xlabel("Vendedores")
    canvas = FigureCanvasTkAgg(fig, master=janela)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=3,column=0,columnspan=5)
    
def disp():
    fig = Figure(figsize=(8, 4), dpi=100)
    fig, grafico = plt.subplots()
    grafico.scatter(vendedores,vendas)
    grafico.set_ylabel("Vendas")
    grafico.set_xlabel("Vendedores")
    canvas = FigureCanvasTkAgg(fig, master=janela)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=3,column=0,columnspan=5)
    
def linha():
    fig = Figure(figsize=(8, 4), dpi=100)
    fig, grafico = plt.subplots()
    grafico.plot(vendedores,vendas)
    grafico.set_ylabel("Vendas")
    grafico.set_xlabel("Vendedores")
    canvas = FigureCanvasTkAgg(fig, master=janela)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=3,column=0,columnspan=5)

def info():
    info = tk.Label(janela,text= "Info:")
    info.config(text= f"""
        Maior Venda:{maior}
        Menor Venda:{menor}
        Media de Vendas:{media:.2f}
        Mediana de Vendas:{mediana}
        Desvio Padrão:{desvio:.2f}
            """ ,justify="left") 
    info.grid(row=2,column=0,columnspan=5)
    
#Botões:
btn1 = tk.Button(janela,text="Grafico de Barra", command=barras) # Executa o comando
btn2 = tk.Button(janela,text="Grafico de Linha", command=linha) # Executa o comando
btn3 = tk.Button(janela,text="Grafico de Disperção", command=disp) # Executa o comando
btn4 = tk.Button(janela,text="Grafico de Pizza", command=pizza) # Executa o comando
btn5 = tk.Button(janela,text="Informações estatisticas", command=info) # Executa o comando


btn1.grid(column=0,row=4,padx=5)
btn2.grid(column=1,row=4,padx=5)
btn3.grid(column=2,row=4,padx=5)
btn4.grid(column=3,row=4,padx=5)
btn5.grid(column=4,row=4,padx=5)

        

janela.mainloop()

