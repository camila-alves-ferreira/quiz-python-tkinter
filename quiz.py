# Quiz "O Explorador do Universo" usando Tkinter
from tkinter import *
from tkinter import messagebox as mb
import json
from PIL import Image, ImageTk

class Quiz:
	def __init__(self):
		self.q_no=0
		self.display_questao()
		self.opt_selected=IntVar()
		self.opts=self.radio_buttons()
		self.display_opcao()
		self.botoes()
		self.tamanho=len(questao)
		self.correto=0
		self.display_imagem()

	def display_result(self):
		# Calcula a resposta certa
		errado_count = self.tamanho - self.correto
		correto = f'Certas: {self.correto}'
		errado = f'Erradas: {errado_count}'
		# Calcula a porcentagem de acertos
		score = int(self.correto / self.tamanho * 100)
		resultado = f'Pontuação: {score}%'		
		mb.showinfo('Resultado', f'{resultado}\n{correto}\n{errado}')


	# Checagem da resposta
	def check_ans(self, q_no):
		if self.opt_selected.get() == resposta[q_no]:
			return True

	def next_btn(self):		
		if self.check_ans(self.q_no):
			self.correto += 1		
		self.q_no += 1
		
		if self.q_no==self.tamanho:			
			self.display_result()
			gui.destroy()
		else:
			self.display_questao()
			self.display_opcao()


	# Botões de "Próximo" e "Sair"
	def botoes(self):
		next_button = Button(gui, text='Próximo',command=self.next_btn,
		width=9,bg='#c47712',fg='#e4e5f0',font=('Courrier New',16,'bold'), borderwidth=7)
		next_button.place(x=355,y=450)
		quit_button = Button(gui, text='Sair', command=gui.destroy,
		width=5,bg='#cf4f36', fg='#e4e5f0',font=('Courrier New',16,' bold'), borderwidth=7)
		quit_button.place(x=730,y=40)

	def display_opcao(self):
		val=0
		self.opt_selected.set(0)
		for option in opçao[self.q_no]:
			self.opts[val]['text']=option
			val+=1

	def display_questao(self):
		q_no = Label(gui, text=questao[self.q_no], width=55, bg='#23507d', fg='#16c7a3',
		font=('Courrier New' ,16, 'bold'), anchor= 'c' )
		q_no.place(x=50, y=200)

	# Botões de opção
	def radio_buttons(self):
		q_list = []
		y_pos = 250
		while len(q_list) < 4:
			radio_btn = Radiobutton(gui,text=' ',variable=self.opt_selected,
			value = len(q_list)+1, bg='#23507d', fg ='#16c7a3',font = ('Courrier New',14, 'bold'), height=1,
            width=21)
			q_list.append(radio_btn)
			radio_btn.place(x = 290, y = y_pos)
			y_pos += 40
		return q_list

	# Imagem do Jogo
	def display_imagem(self):
		imagem = Image.open('/home/camila/Estudos/Python/quiz-python/AP2/logo.png')
		imagem = ImageTk.PhotoImage(imagem)
		panel = Label(gui, image = imagem, anchor = CENTER, border = 0)
		panel.image = imagem
		panel.grid(row=0, column=0, padx=(260,0))

# Cria uma janela GUI
gui = Tk()

gui.geometry('900x550')
gui.title('QUIZ')
gui['background'] = '#23507d'
gui.resizable(width=False, height=False)


# Arquivo JSON
with open('data.json') as file:
	data = json.load(file)

questao = (data['questao'])
opçao = (data['opçao'])
resposta = (data['resposta'])

quiz = Quiz()

# Inicialização do GUI
gui.mainloop()

