from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from time import sleep, time

GARUMS=370
PLATUMS=497
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
menu=Canvas(logs,width=PLATUMS,height=GARUMS,bg='darkblue')
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
  level2= Button(dator, text ="Doties uz trešo līmeni",command=limenisnr3,bg='#A8FF4C')
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
  daba3.pack_forget()
  dabalimenis.pack()
  puppie3.place(x=430,y=270)
  ugun3.place(x=60,y=140)
  saslik3.place(x=10,y=310)
  cig3.place(x=380,y=320)

#trešā līmeņa menu
limenitis3= Label(menu, text= "3.Līmenis Daba", font= ('Helvetica 17 bold'))
daba=ImageTk.PhotoImage(file="dabamaza123.png")
daba2=Label(image=daba)
daba3=Button(menu, image=daba,command=dabass, borderwidth=0,bd=5)


#daba
dabalimenis=Canvas(logs,width=PLATUMS3,height=GARUMS,bg="blue")
dabalimenis.pack_forget()
bgdaba=ImageTk.PhotoImage(file="daba123.png")
dabalimenis.create_image(0,0,anchor=NW,image=bgdaba)
punkti_daba=0

def swamppuppie():
  puppie3.destroy()
  global punkti_daba  
  punkti_daba+= 1 
  if punkti_daba == 4:
    līmeņa3_beigas()
  print (punkti_daba) 
puppie=ImageTk.PhotoImage(file="swamppuppie (1).png")
puppie2=Label(image=puppie)
puppie3=Button(dabalimenis,image=puppie,command=swamppuppie,borderwidth=0)


def campfire():
  ugun3.destroy()
  global punkti_daba  
  punkti_daba+= 1 
  if punkti_daba == 4:
    līmeņa3_beigas()
  print (punkti_daba) 
ugun=ImageTk.PhotoImage(file="campfire.png")
ugun2=Label(image=ugun)
ugun3=Button(dabalimenis,image=ugun,command=campfire,borderwidth=0)

def sasliks():
  saslik3.destroy()
  global punkti_daba  
  punkti_daba+= 1 
  if punkti_daba == 4:
    līmeņa3_beigas()
  print (punkti_daba) 
saslik=ImageTk.PhotoImage(file="saslik.png")
saslik2=Label(image=saslik)
saslik3=Button(dabalimenis,image=saslik,command=sasliks,borderwidth=0)

def cigarete():
  cig3.destroy()
  global punkti_daba  
  punkti_daba+= 1 
  if punkti_daba == 4:
    līmeņa3_beigas()
  print (punkti_daba) 
cig=ImageTk.PhotoImage(file="cig.png")
cig2=Label(image=cig)
cig3=Button(dabalimenis,image=cig,command=cigarete,borderwidth=0)

def līmeņa3_beigas():
  dabalimenis.create_text(270,160,text='SPĒLES BEIGAS',fill='#A8FF4C',font=('Helvetica 30 bold'))
  level2= Button(dabalimenis, text ="Doties uz ceturo līmeni",command=limenisnr4,bg='#A8FF4C')
  level2.place(x=210,y=200)
# _______________________________________________________________________________________________________________________________________________________________________________


def limenisnr4():
  menu.pack()
  dabalimenis.pack_forget()
  street3.pack()
  limenitis3.pack_forget()
  limenitis4.pack()

def iela1():
  menu.pack_forget()
  iela.pack()
  jenots3.place(x=259,y=249)
  stikls3.place(x=50,y=239)
  grafiti3.place(x=390,y=100)
  siers3.place(x=550,y=190)
  # limenitis4.pack()

iela=Canvas(logs,width=PLATUMS3,height=GARUMS,bg="blue")
iela.pack_forget()
bgiela=ImageTk.PhotoImage(file="street.png")
iela.create_image(0,0,anchor=NW,image=bgiela)
punkti_iela=0

limenitis4= Label(menu, text= "4.Līmenis Iela", font= ('Helvetica 17 bold'))
street=ImageTk.PhotoImage(file="iela.png")
street2=Label(image=street)
street3=Button(menu, image=street,command=iela1, borderwidth=0,bd=5)


def jenotinss():
  jenots3.destroy()
  global punkti_iela  
  punkti_iela+= 1 
  if punkti_iela == 4:
    līmeņa4_beigas()
  print (punkti_iela) 
jenots=ImageTk.PhotoImage(file="jenots.png")
jenots2=Label(image=jenots)
jenots3=Button(iela,image=jenots,command=jenotinss,borderwidth=0)


def stiklins():
  stikls3.destroy()
  global punkti_iela  
  punkti_iela+= 1 
  if punkti_iela == 4:
    līmeņa4_beigas()
  print (punkti_iela) 
stikls=ImageTk.PhotoImage(file="stikls.png")
stikls2=Label(image=stikls)
stikls3=Button(iela,image=stikls,command=stiklins,borderwidth=0)

def grafitiss():
  grafiti3.destroy()
  global punkti_iela  
  punkti_iela+= 1 
  if punkti_iela == 4:
    līmeņa4_beigas()
  print (punkti_iela) 
grafiti=ImageTk.PhotoImage(file="grafiti.png")
greafiti2=Label(image=grafiti)
grafiti3=Button(iela,image=grafiti,command=grafitiss,borderwidth=0)

def sierini():
  siers3.destroy()
  global punkti_iela  
  punkti_iela+= 1 
  if punkti_iela == 4:
    līmeņa4_beigas()
  print (punkti_iela) 
siers=ImageTk.PhotoImage(file="siers.png")
siers2=Label(image=siers)
siers3=Button(iela,image=siers,command=sierini,borderwidth=0)

def līmeņa4_beigas():
  iela.create_text(270,160,text='SPĒLES BEIGAS',fill='#A8FF4C',font=('Helvetica 30 bold'))
  level5= Button(iela, text ="Doties uz piekto līmeni",command=limenisnr5atpakal,bg='#A8FF4C')
  level5.place(x=210,y=200)

def limenisnr5atpakal():
  menu.pack()
  kojas3.pack()
  limenitis5.pack()
  iela.pack_forget()
  limenitis4.pack_forget()
  street3.pack_forget()
  # ________________________________________________________________________________________________________________________________________________________________

def limenisnr5():
  menu.pack_forget()
  kojas3.pack_forget()
  kojaslimenis.pack()
  cigarete3.place(x=450,y=220)
  

  
limenitis5= Label(menu, text= "5.Līmenis VTkojas", font= ('Helvetica 17 bold'))
kojas=ImageTk.PhotoImage(file="VT.png")
kojas2=Label(image=kojas)
kojas3=Button(menu, image=kojas,command=limenisnr5, borderwidth=0,bd=5)


kojaslimenis=Canvas(logs,width=PLATUMS3,height=GARUMS,bg="blue")
kojaslimenis.pack_forget()
bgkojas=ImageTk.PhotoImage(file="VTliela.png")
kojaslimenis.create_image(0,0,anchor=NW,image=bgkojas)


punkti_kojas=0

def cigarins():
  cigarete3.destroy()
  global punkti_kojas  
  punkti_kojas+= 1 
  if punkti_kojas == 4:
    līmeņa4_beigas()
  print (punkti_kojas) 
cigarete=ImageTk.PhotoImage(file="cigarete.png")
cigarete2=Label(image=cigarete)
cigarete3=Button(kojaslimenis,image=cigarete,command=cigarins,borderwidth=0)