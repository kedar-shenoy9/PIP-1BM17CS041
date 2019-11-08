from tkinter import *

class Application(Frame):
	
	def __init__(self, master):	
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		#for the check boxes
		self.superManLikes = BooleanVar()
		self.andhadhunLikes = BooleanVar()
		self.kirikLikes = BooleanVar()

		#for language
		self.lang = StringVar()
		
		Label(self, text = "Select the language :").grid(row = 0, column = 0, sticky = W)
		
		#radio button for language
		self.eng = Radiobutton(self, text = "English", variable = self.lang, value = "English")
		self.eng.grid(row = 1, column = 0, sticky = W)

		self.hin = Radiobutton(self, text = "Hindi", variable = self.lang, value = "Hindi")
		self.hin.grid(row = 2, column = 0, sticky = W)

		self.kan = Radiobutton(self, text = "Kannada", variable = self.lang, value = "Kannada")
		self.eng.grid(row = 3, column = 0, sticky = W)

		#check box for movies
		Label(self, text = "Select the Movie :").grid(row = 4, column = 0, sticky = W)

		self.superMan = Checkbutton(self, text = "Super man 3", variable = self.superManLikes)
		self.superMan.grid(row = 5, column = 0, sticky = W)
		
		self.andhadhun = Checkbutton(self, text = "Andhadhun", variable = self.andhadhunLikes)
		self.andhadhun.grid(row = 6, column = 0, sticky = W)

		self.kirik = Checkbutton(self, text = "Kirik Party", variable = self.kirikLikes)
		self.kirik.grid(row = 7, column = 0, sticky = W)

		#drop down for number of seats
		Label(self, text = "Select the number of seats :").grid(row = 8, column = 0, sticky = W)
		self.seats = ['1','2','3','4','5']
		self.seatVar = StringVar()
		self.seatVar.set(self.seats[0])
		self.drop = OptionMenu(self, self.seatVar, *self.seats)
		self.drop.grid(row = 8, column = 1, sticky = W)

		#submit button
		self.but = Button(self, text = "Submit", command = self.submit)
		self.but.grid(row = 9, column = 0, sticky = W)

		#text box for displaying the message
		self.messageBox = Entry(self)
		self.messageBox.grid(row = 10, column = 0, sticky = W)

	def submit(self):
		movieLang = self.lang.get()
		if movieLang.strip() == "":
			self.messageBox.delete(0, END)
			self.messageBox.insert(0, "Error")
		
		elif not self.superManLikes.get() and not self.andhadhunLikes.get() and not self.kirikLikes.get():
			self.messageBox.delete(0, END)
			self.messageBox.insert(0, "Error")

		else:
			self.messageBox.delete(0, END)
			self.messageBox.insert(0, "Success")


if __name__ == "__main__":
	root = Tk()
	root.title("Movie ticket booking ")
	root.geometry("300x300")
	app = Application(root)
	root.mainloop()



