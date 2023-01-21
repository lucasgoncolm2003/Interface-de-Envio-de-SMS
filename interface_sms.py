# Importação de Biblioteca Tkinter
from tkinter import *
from tkinter import ttk
from twilio.rest import Client
# Importação do Pacote Pillow

# Variáveis de Cores
cor1 = "#3b3b3b"
cor2 = "#1C1C1C"

# Criação de Janela
window = Tk()
window.title('')
window.geometry('500x340')
window.configure(bg=cor1)
num2 = []
account_sid = 'Digite aqui sua Account Sid'
auth_token = 'Digite aqui seu Authentication Token'
client = Client(account_sid, auth_token)
# Envio de SMS
def enviar_sms(numero2, mes):
	message = client.messages \
    .create(body= mes, from_= "Digite aqui seu Número de Telefone da Twilio", to=numero2)

def btn_limpar():
	mensagem.delete("1.0",END)
	contato.delete(0,END)

def btn_envio():
	num2.append(contato.get())
	for i in num2:
		msg = mensagem.get("1.0",END)
		mensagem.delete("1.0",END)
		contato.delete(0,END)
		r = enviar_sms(i,msg)
		print("Messagem para " + i + " ...")
		print("Mensagem Enviada com Sucesso")
		print("======================")
	num2.clear()

# Frames para a Janela
frame_cima = Frame(window, width=500, height=80, bg=cor2, pady=0, padx=3, relief='flat')
frame_cima.place(x=2, y=2)
frame_esquerda = Frame(window, width=500, height=260, bg=cor2, pady=0, padx=3, relief='flat')
frame_esquerda.place(x=2, y=84)

# Estilo de Interface
style = ttk.Style(window)
style.theme_use("clam")

# Labels para Frame de Cima
label_nome = Label(frame_cima, text="Interface de Envio de SMS", width=33,
	height=1, padx=0, relief='flat', anchor='center', font=('Ivy 15 bold'), 
	bg=cor2, foreground='white')
label_nome.place(x=50, y=25)

label_ctt = Label(frame_esquerda, text="Contato:",
	height=1, padx=3, relief='groove', anchor='center', font=('Ivy 10 bold'), 
	bg=cor2, foreground='white')
label_ctt.place(x=50, y=20)
contato = ttk.Entry(frame_esquerda, width=26, justify=('left'), font=('Ivy 10 bold'))
contato.place(x=140, y=20)

label_msg = Label(frame_esquerda, text="Mensagem:",
	height=1, padx=3, relief='groove', anchor='center', font=('Ivy 10 bold'), 
	bg=cor2, foreground='white')
label_msg.place(x=50, y=70)
mensagem = Text(frame_esquerda, width=25, height=6, font=('Ivy 10 bold'))
mensagem.place(x=150, y=70)

envio = Button(frame_esquerda, text="Enviar SMS", width=9, height=1, padx=1,
	relief='raised', overrelief='ridge', anchor='nw', font=('Ivy 12 bold'), 
	bg='white', foreground='black', command=btn_envio)
envio.place(x = 120, y = 200)
limpar = Button(frame_esquerda, text="Limpar Dados", width=11, height=1, padx=1,
	relief='raised', overrelief='ridge', anchor='nw', font=('Ivy 12 bold'), 
	bg='white', foreground='black', command=btn_limpar)
limpar.place(x = 240, y = 200)

# Execução da Interface
window.mainloop()