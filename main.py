from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from time import sleep, time

GARUMS=370
PLATUMS=500
GARUMS3=350
logs=Tk()
logs.title('Vides saudzetajs')

#sakuma canva
start=Canvas(logs,width=PLATUMS,height=GARUMS,bg='darkblue')
start.pack()
bg= ImageTk.PhotoImage(file="main_menu.png")
start.create_image(0,0,anchor=NW,image=bg)
start.create_text(370,150,text='Zemes tīrītāji',fill='white',font=('Helvetica', 20,'bold'))
def noteikumi():
   messagebox.showinfo( "Noteikumi","Laipni lūgti jautrā spēlē kuru sauc ZEMES TĪRĪTĀJI. Spēles galvenais uzdevums ir iet pa līmeņiem un savākt")
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
  pudele3.place(x=480, y=100)
  paper3.place(x=300, y=270)
  gruzi3.place(x=350,y=200)
  kafija3.place(x=200,y=200)
  
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

def līmeņa_beigas():
  klase.create_text(320,160,text='Līmenis pabeigts!',fill='#A8FF4C',font=('Helvetica 30 bold'))
  level2= Button(klase, text ="Doties uz otro līmeni",command=limenisnr2,bg='#A8FF4C')
  level2.place(x=250,y=200)
def papirs():
  paper3.destroy()
  global punkti_skola  
  punkti_skola+= 1 
  print (punkti_skola) 
  if punkti_skola == 4:
    līmeņa_beigas()
# paper=ImageTk.PhotoImage(file="paper.png")
# paper2=Label(image=paper)
# paper3=Button(klase,image=paper,command=papirs,borderwidth=0)

def pudeles():
  pudele3.destroy()
  global punkti_skola  
  punkti_skola+= 1 
  print (punkti_skola) 
  if punkti_skola == 4:
    līmeņa_beigas()

def pudele():
  pudele3.destroy()
  global punkti_skola  
  punkti_skola+= 1 
  print (punkti_skola) 
  if punkti_skola == 4:
    līmeņa_beigas()

def kafijass():
  kafija3.destroy()
  global punkti_skola  
  punkti_skola+= 1 
  print (punkti_skola) 
  if punkti_skola == 4:
    līmeņa_beigas()
    
def gruzis():
  gruzi3.destroy()
  global punkti_skola  
  punkti_skola+= 1 
  if punkti_skola == 4:
    līmeņa_beigas()
  print (punkti_skola) 
gruzi=ImageTk.PhotoImage(file="gruzi.png")
gruzi2=Label(image=gruzi)
gruzi3=Button(klase,image=gruzi,command=gruzis,borderwidth=0)

paper=ImageTk.PhotoImage(file="paper.png")
paper2=Label(image=paper)
paper3=Button(klase,image=paper,command=papirs,borderwidth=0)

pudele=ImageTk.PhotoImage(file="pudele.png")
pudele2=Label(image=pudele)
pudele3=Button(klase,image=pudele,command=pudeles,borderwidth=0)

kafija=ImageTk.PhotoImage(file="kafijas_krūze.png")
kafija2=Label(image=kafija)
kafija3=Button(klase,image=kafija,command=kafijass,borderwidth=0)

# LAIKA_IEROBEŽOJUMS=0
# beigas=time()+LAIKA_IEROBEŽOJUMS
# rezultāts=0
# klase.create_text(20,20,text=str(rezultāts))

# def parādīt_rezultātu(rezultāts):
#   klase.itemconfig(rezultāts_teksts,text=str(rezultāts),foreground="red")

# while beigas<30:
#   parādīt_laiku(int(beigas+time()))
#   parādīt_rezultātu(rezultāts)
#   logs.update()
#   sleep(0.1)

#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________

def limenisnr2():
  menu.pack()
  klase.pack_forget()
  dato3.pack()
  dato_text.pack()



def datoris():
  menu.pack_forget()
  dator.pack()
  dato3.pack_forget()
  cipsi3.place(x=200, y=200)
  burgir3.place(x=50,y=100)
  arbuz3.place(x=425,y=150)
  lode3.place(x=400,y=200)
  
dato_text= Label(menu, text= "2.Limenis Datora Klase", font= ('Helvetica 17 bold'))
dato=ImageTk.PhotoImage(file="datorklase.png")
dato2=Label(image=dato)
dato3=Button(menu,image=dato,command=datoris,borderwidth=0,bd=5)









#datorklase
dator=Canvas(logs,width=PLATUMS,height=GARUMS3,bg="blue")
bg4=ImageTk.PhotoImage(file="datorklase1.jpg")
dator.create_image(0,0,anchor=NW,image=bg4)


punkti_datorklase=0
def cipsis():
  cipsi3.destroy()
  global punkti_datorklase  
  punkti_datorklase+= 1 
  if punkti_datorklase == 4:
    līmeņa2_beigas()
  print (punkti_datorklase) 
cipsi=ImageTk.PhotoImage(file="cipsi.png")
cipsi2=Label(image=cipsi)
cipsi3=Button(dator,image=cipsi,command=cipsis,borderwidth=0)

def burgirr():
  burgir3.destroy()
  global punkti_datorklase  
  punkti_datorklase+= 1 
  if punkti_datorklase == 4:
    līmeņa2_beigas()
  print (punkti_datorklase) 
burgir=ImageTk.PhotoImage(file="burgir.png")
burgir2=Label(image=burgir)
burgir3=Button(dator,image=burgir,command=burgirr,borderwidth=0)

def arbuzz():
  arbuz3.destroy()
  global punkti_datorklase  
  punkti_datorklase+= 1 
  if punkti_datorklase == 4:
    līmeņa2_beigas()
  print (punkti_datorklase) 
arbuz=ImageTk.PhotoImage(file="arbuz.png")
arbuz2=Label(image=arbuz)
arbuz3=Button(dator,image=arbuz,command=arbuzz,borderwidth=0)

def lodee():
  lode3.destroy()
  global punkti_datorklase  
  punkti_datorklase+= 1 
  if punkti_datorklase == 4:
    līmeņa2_beigas()
  print (punkti_datorklase) 
lode=ImageTk.PhotoImage(file="lode.png")
lode2=Label(image=lode)
lode3=Button(dator,image=lode,command=lodee,borderwidth=0)


def līmeņa2_beigas():
  dator.create_text(270,160,text='SPĒLES BEIGAS',fill='#A8FF4C',font=('Helvetica 30 bold'))
  level2= Button(dator, text ="Doties uz otro līmeni",command=limenisnr3,bg='#A8FF4C')
  level2.place(x=190,y=200)


# #__________________________________________________________________________________________________________________________________________________________________________

def limenisnr3():
  menu.pack()
  daba3.pack()
  dator.pack_forget()
  limenitis3.pack()
  dato_text.pack_forget()


def dabass():
  menu.pack_forget()
  daba.pack()
  daba3.pack_forget()

#trešā līmeņa menu
limenitis3= Label(menu, text= "3.Līmenis Daba", font= ('Helvetica 17 bold'))
daba=ImageTk.PhotoImage(file="dabamaza.png")
daba2=Label(image=daba)
daba3=Button(menu, image=daba,command=dabass, borderwidth=0,bd=5)



dabalimenis=Canvas(logs,width=PLATUMS3,height=GARUMS,bg="blue")
dabalimenis.pack_forget()
bgdaba=ImageTk.PhotoImage(file="daba.png")
dabalimenis.create_image(0,0,anchor=NW,image=bg3)
