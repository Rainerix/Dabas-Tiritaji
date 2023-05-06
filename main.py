from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from funkcijas import *


GARUMS=370
PLATUMS=500
logs=Tk()
logs.title('Vides saudzetajs')

#sakuma canva
start=Canvas(logs,width=PLATUMS,height=GARUMS,bg='darkblue')
start.pack()
bg= ImageTk.PhotoImage(file="main_menu.png")
start.create_image(0,0,anchor=NW,image=bg)
start.create_text(370,150,text='Zemes tīrītāji',fill='white',font=('Helvetica', 20,'bold'))

#infopoga 
info=Button(start,text ="Info", command=noteikumi, fg='black', bg='#84EE0D')
info.place(x=12, y=330)

#pāreja uz otro canvu
def talak():
  start.pack_forget()
  
  menu.pack()
  skola3.pack(pady=20,padx=20)
  skolas.pack()
  # dato3.pack(pady=20,padx=20,)
label=start.create_text(380,200,text='Start',font=('Bahnschrift Condensed',19,'bold'), fill='lime')
start.tag_bind(label, '<Button-1>', lambda event: talak())

#otra Canva
GARUMS2=335
menu=Canvas(logs,width=PLATUMS,height=GARUMS2,bg='darkblue')
menu.pack_forget()
bg2= ImageTk.PhotoImage(file="menubilde.png")
menu.create_image(0,0,anchor=NW,image=bg2)

#klases poga
def skolas_limenis():
  pudele3.pack(pady=200,padx=580)
  paper3.pack(pady=370,padx=600)
  gruzi3.pack(pady=350,padx=200)  #Normāli nejievieto, nodzēšs labo malu
  
  info.pack_forget()
  menu.pack_forget()
  klase.pack()
  skola3.pack_forget()
  skolas.pack_forget()
  
  
  
skolas= Label(menu, text= "1.Līmenis Skola", font= ('Helvetica 17 bold'))
skola=ImageTk.PhotoImage(file="skolaklase.png")
skola2=Label(image=skola)
skola3=Button(menu, image=skola,command= skolas_limenis, borderwidth=0,bd=5)

#klase
PLATUMS3=600
klase=Canvas(logs,width=PLATUMS3,height=GARUMS,bg="blue")
klase.pack_forget()
bg3= ImageTk.PhotoImage(file="skola.jpg")
klase.create_image(0,0,anchor=NW,image=bg3)
punkti_skola=0
def papirs():
  paper3.pack_forget()
  global punkti_skola  
  punkti_skola+= 1 
  print (punkti_skola) 
paper=ImageTk.PhotoImage(file="paper.png")
paper2=Label(image=paper)
paper3=Button(klase,image=paper,command=papirs,borderwidth=0)



def pudeles():
  pudele3.pack_forget()
  global punkti_skola  
  punkti_skola+= 1 
  print (punkti_skola) 
pudele=ImageTk.PhotoImage(file="pudele.png")
pudele2=Label(image=pudele)
pudele3=Button(klase,image=pudele,command=pudeles,borderwidth=0)


def gruzis():
  gruzi3.pack_forget()
  global punkti_skola  
  punkti_skola+= 1 
  print (punkti_skola) 
gruzi=ImageTk.PhotoImage(file="gruzi.png")
gruzi2=Label(image=gruzi)
gruzi3=Button(klase,image=gruzi,command=gruzis,borderwidth=0)





# #datorklases poga
# GARUMS3=350
# def dator_limenis():
#   menu.pack_forget()
#   dator.pack()
#   dato3.pack_forget()
#   skolass.pack_forget()
# skolass= Label(menu, text= "Skola", font= ('Helvetica 17 bold'))
# dato=ImageTk.PhotoImage(file="datorklase.png")
# dato2=Label(image=dato)
# dato3=Button(menu,image=dato,command=dator_limenis,borderwidth=0,bd=5)

# #datorklase
# dator=Canvas(logs,width=PLATUMS,height=GARUMS3,bg="blue")
# bg4=ImageTk.PhotoImage(file="datorklase1.jpg")
# dator.create_image(0,0,anchor=NW,image=bg4)
