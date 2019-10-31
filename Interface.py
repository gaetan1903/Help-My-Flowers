from tkinter import *
from tkinter.font import Font
import time, serial, threading
import smtplib
from email.mime.text import MIMEText
import playsound 

lum_captor  = 0
hum_captor = 0

class Info(threading.Thread):
    	def __init__(self):
		threading.Thread.__init__(self)
		self.ser = serial.Serial('COM8', 9600)

    	def run(self):
        	while True:
			global lum_captor
			global hum_captor
			self.value = str(self.ser.readline()).split("'")[1].split("\\")[0].split('_')
			hum_captor = self.value[0]
			lum_captor = self.value[1]


class Interface(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.root = Tk()
		self.root.geometry("1366x768+0+0")
		self.root.title('Help my flowers')
		self.root.config(bg='gray')
		for x in range(1,8):
			y = f"self.logos{x} = PhotoImage(file='{x}.png')"
			exec(y)
		self.img = PhotoImage(file='WallDecor.png')
		self.danger = PhotoImage(file="danger.png")

		self.perfectI = PhotoImage(file='parfait.png')
		self.ensoleilI = PhotoImage(file ='ensoleil.png')
		self.arroserI = PhotoImage(file='arroser.png')
		self.alertI = PhotoImage(file = 'danger.png')
		self.arroserx = PhotoImage(file='arroserX.png')
		self.perfect0 = PhotoImage(file='parfait0.png')
		self.lummin = 1015
		self.hummax = 560
		self.hummin = 160
		self.danger = PhotoImage(file='danger.png')
		
		self.font1 = Font( family="Sans-serif", size=40, weight="normal")
		self.font2 = Font( family="Sans-serif", size=12, weight="normal")
		self.font3 = Font( family="Sans-serif", size=15, weight="normal")
		self.font4 = Font( family="Sans-serif", size=20)

		self.soleil = PhotoImage(file='jour.png')
		self.lune  = PhotoImage(file='nuit.png')
		
		global hum_captor
		global lum_captor
		
		self.background_image=PhotoImage(file="green.png")
		self.background_label = Label(self.root, image=self.background_image)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

		self.HumText = PhotoImage(file = "LUM.png")		
		self.canHum= Canvas(self.root, width = 270, height = 40, highlightthickness = 0)
		self.canHum.place(relx = 0.42, rely = 0.13)
		self.canHum_text = self.canHum.create_image(135, 55, image = self.HumText)
		
		self.LumText = PhotoImage(file = "HUM.png")		
		self.canLum= Canvas(self.root, width = 260, height = 40, highlightthickness = 0)
		self.canLum.place(relx = 0.73, rely = 0.13)
		self.canLum_text = self.canLum.create_image(130, 20, image = self.LumText)

	def run(self):
		while True:
			self.verifie()
			self.valhum.config(text = hum_captor)
			self.valhum.update()

			self.valum.config(text = lum_captor)
			self.valum.update()

			time.sleep(2)

	def mail(self):
		try:
			message = MIMEText('Votre plante est train de mourir si vous ne reagissez pas')
			message['Subject'] = 'Danger plante'

			message['From'] = 'gaetan.jonathan.bakary@esti.mg'
			message['To'] = 'karin.soanarindra.stelanony@esti.mg'

			server = smtplib.SMTP('smtp.gmail.com:587')
			server.starttls()
			server.login('gaetan.jonathan.bakary@esti.mg','**************')
			server.send_message(message)
			server.quit()
		except:
			pass

	def menuTop(self):
		""" fonction permettant de mettre les menus en haut de la fenetre """
		self.menubutton = Menu(self.root)

		self.sous_menubutton_1 = Menu(self.menubutton, tearoff =  0)
		self.sous_menubutton_2 = Menu(self.menubutton, tearoff =  0)
		self.sous_menubutton_3 = Menu(self.menubutton, tearoff =  0)
		self.sous_menubutton_4 = Menu(self.menubutton, tearoff =  0)

		self.menubutton.add_cascade(label ='Fichier', menu = self.sous_menubutton_1)
		self.sous_menubutton_1.add_command(label = "Nouvelle Fenetre")
		self.sous_menubutton_1.add_command(label = "Quitter", command = self.root.quit)

		self.menubutton.add_cascade(label ='Options', menu = self.sous_menubutton_2)
		self.sous_menubutton_2.add_command(label = "Paramètre Utilisateur")
		self.sous_menubutton_2.add_command(label = "Configurer les valeurs seuil")

		self.menubutton.add_cascade(label ='Aide', menu = self.sous_menubutton_3)
		self.sous_menubutton_3.add_command(label = "Documentation")
		self.sous_menubutton_3.add_command(label = "License & Conditions d'utilisation")
		self.sous_menubutton_3.add_command(label = "Reporter un bug")

		self.menubutton.add_cascade(label ='A propos', menu = self.sous_menubutton_4)
		self.sous_menubutton_4.add_command(label = "A propos du Projet")
		self.sous_menubutton_4.add_command(label = "A propos Developpeurs")
		self.sous_menubutton_4.add_command(label = "Faire un Don")

		self.root.config(menu=self.menubutton)


	def chrono(self):
		self.heure = StringVar()
		self.heure.set(time.strftime('%H:%M:%S'))
		self.root.after(100, self.chrono)
		
		self.temps = Label(self.root, textvariable = self.heure, bg="#2ebc4f", font = self.font3)	
		self.temps.place(relx=0.01, rely=0.008)
		
	
	def labela(self):
	
		
		self.valum= Label(self.root, text="Lux", font=self.font4, fg="#2ebc4f", bg="white")
		self.valum.place(relx=0.495, rely=0.20)

		
		self.valhum= Label(self.root, text="%", font=self.font4, fg="#2ebc4f", bg="white")
		self.valhum.place(relx=0.82, rely=0.20)

		"""
		self.Explication= Label(self.root, text="La fleur va mourir si vous ne faites rien. Donc,  arrosez-la maintenant et mettez la dans un endroit lumineux", font=self.font2, bg="black",fg="white")
		self.Explication.place(relx=0.15, rely=0.75)
		
		self.uniteL= Label(self.root, text=f"{self.nbrLum} Lx" , font=self.font4, bg="#000000" , fg="white")
		self.uniteL.place(relx=0.22, rely=0.3)

		self.uniteH= Label(self.root, text=f"{self.nbrHum} %" , font=self.font4, bg="#000000", fg="white" )
		self.uniteH.place(relx=0.63, rely=0.3)
		"""
	
	def image(self):
		"""
		self.can1 = Canvas(self.root , width = 300 ,  height = 260, bg="white")
		self.can1.place(relx=0.36,rely=0.27)
		self.can1_image = self.can1.create_image(150, 132, image = self.logos7)
		"""
		self.can2 = Canvas(self.root , width = 1370, height = 60, bg="#2ebc4f", bd = 0, highlightthickness = 0)
		self.can2.place(relx=-0.00001,rely=0)
		#self.can2_image = self.can2.create_image(640, 17, image = self.img)
		self.can2.create_text(650, 30, text = 'Help My Flower', fill = "white", font = self.font3)

	
	def corps(self):
		self.canG = Canvas(self.root, width = 500, height = 700, bd = 4, highlightthickness = 1, bg='white')
		self.canG.place(relx = 0, rely = 0.045)

		self.canG_fleur = self.canG.create_image(235, 250, image = self.logos7)
		self.soleil0 = self.soleil.subsample(3,3)
		self.lune = self.lune.subsample(4,4)
		self.canG_temps = self.canG.create_image(60, 100, image = self.soleil0)
		
		self.canL1= Canvas(self.root, width=350, height = 225)
		self.canL1_image = self.canL1.create_image(175, 112.5, image = self.perfectI)
		self.canL1.place(relx = 0.4, rely=0.4)
		
		self.canL2 = Canvas(self.root, width = 350, height = 225)
		self.canL2_image = self.canL2.create_image(175, 112.5, image = self.perfectI)	
		self.canL2.place(relx = 0.71, rely=0.4)
		
		self.alert = Canvas(self.root , width = 100, height = 75)
		self.alert_image = self.alert.create_image(50, 37.5, image = self.perfect0)
		self.alert.place(relx =0.65, rely = 0.8)
		
		self.infotext = Text(self.root, width = 50, height = 5)
		self.infotext.place(relx = 0.035, rely = 0.7)	

		
	def verifie(self):
		self.valueHum = int(hum_captor)
		self.valueLum = int(lum_captor)

		if (self.hummin <= self.valueHum <= self.hummax):

			if (self.hummin + 70 <= self.valueHum <= self.hummax - 70):

				if (self.valueLum < self.lummin): #  plante parfaite 
					#  image 7
					 self.canG.itemconfig(self.canG_fleur, image=self.logos7)
					 self.canL1.itemconfig(self.canL1_image, image = self.perfectI)
					 self.canL2.itemconfig(self.canL2_image, image = self.perfectI)
					 self.alert.itemconfig(self.alert_image, image = self.perfect0)
					 self.infotext.delete('1.0', '3.0')
					 self.infotext.insert('1.0', 'La plante est parfaitement en bonne etat')


				else:  # presque parfaite
					# image 4
					self.canG.itemconfig(self.canG_fleur, image=self.logos4)
					self.canL1.itemconfig(self.canL1_image, image = self.ensoleilI)
					self.canL2.itemconfig(self.canL2_image, image = self.perfectI)
					self.alert.itemconfig(self.alert_image, image = self.danger)
					self.infotext.delete('1.0', '3.0')
					self.infotext.insert('1.0', 'La plante manque de lumiere')
	

			else:
				if (self.valueLum < self.lummin):  #  presque parfaite
					# image 4 
					self.canG.itemconfig(self.canG_fleur, image=self.logos4)
					self.canL1.itemconfig(self.canL1_image, image = self.perfectI)
					self.canL2.itemconfig(self.canL2_image, image = self.arroserI)
					self.alert.itemconfig(self.alert_image, image = self.danger)
					self.infotext.delete('1.0', '3.0')
					self.infotext.insert('1.0', "La plante manque d'humidite")
					

				else:  #  pourris
					#  image 1 
					self.canG.itemconfig(self.canG_fleur, image=self.logos1)
					self.canL1.itemconfig(self.canL1_image, image = self.ensoleilI)
					self.canL2.itemconfig(self.canL2_image, image = self.arroserI)
					self.alert.itemconfig(self.alert_image, image = self.danger)
					self.infotext.delete('1.0', '3.0')
					self.infotext.insert('1.0', "La plante manque d'humidite et de soleil")
					try:
						playsound.playsound('boom.wav')
					except:
						pass
					self.mail()
					
					

		else:  #  perdue d avance 
			if (self.valueLum < self.lummin):  # presque parfaite
				# image 3 
				self.canG.itemconfig(self.canG_fleur, image=self.logos3)
				self.canL1.itemconfig(self.canL1_image, image = self.perfectI)
				self.canL2.itemconfig(self.canL2_image, image = self.arroserI)
				self.alert.itemconfig(self.alert_image, image = self.danger)
				self.infotext.delete('1.0', '3.0')
				self.infotext.insert('1.0', "La plante manque d'humidite")
				if (self.valueHum >= self.hummax):
						self.canL2.itemconfig(self.canL2_image, image = self.arroserx)
						self.infotext.delete('1.0', '3.0')
						self.infotext.insert('1.0', "La plante est trop humide")

			else: # pourris
				#  image 1 
				self.canG.itemconfig(self.canG_fleur, image=self.logos1)
				self.canL1.itemconfig(self.canL1_image, image = self.ensoleilI)
				self.canL2.itemconfig(self.canL2_image, image = self.arroserI)
				self.alert.itemconfig(self.alert_image, image = self.danger)
				self.infotext.delete('1.0', '3.0')
				self.infotext.insert('1.0', "La plante manque d'humidite et de soleil")
				try:
						playsound.playsound('boom.wav')
				except:
						pass
				self.mail() 
				if (self.valueHum >= self.hummax):
						self.canL2.itemconfig(self.canL2_image, image = self.arroserx)
						self.infotext.delete('1.0', '3.0')
						self.infotext.insert('1.0', "La plante est trop humide")


	       
	def __final__(self):
		self.root.mainloop()


if __name__ =='__main__':
	arduino = Info()
	arduino.start()
	fen = Interface()
	fen.menuTop()
	fen.corps()
	fen.labela()
	fen.image()
	fen.chrono()
	fen.start()
	fen.__final__()