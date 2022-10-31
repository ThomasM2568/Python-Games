from tkinter import*
from PIL import Image, ImageTk
from tkinter.messagebox import*
from random import*
from copy import deepcopy
import time
import pygame

nbcle=0
gene=0
deplacements=0
fenetre1=Tk()

pygame.mixer.init()

def quitter(event):
    fenetre.destroy()
    pygame.mixer.music.stop()

def deppos(direct):
    global nbcle
    if direct=="bas":
        if lines[posy+1][posx]=='0' or int(lines[posy+1][posx])>= 3:
            return('True')
        if lines[posy+1][posx]=='2' and nbcle>0:
            nbcle-=1
            return('True')
    if direct=="haut":
        if lines[posy-1][posx]=='0' or int(lines[posy-1][posx])>= 3:
            return('True')
        if lines[posy-1][posx]=='2'and nbcle>0:
            nbcle-=1
            return('True')
    if direct=="droite":
        if lines[posy][posx+1]=='0' or int(lines[posy][posx+1])>= 3:
            return('True')
        if lines[posy][posx+1]=='2'and nbcle>0:
            nbcle-=1
            return('True')
    if direct=="gauche":
        if lines[posy][posx-1]=='0' or int(lines[posy][posx-1])>= 3:
            return('True')
        if lines[posy][posx-1]=='2'and nbcle>0:
            nbcle-=1
            return('True')


ind = -1
def update(delay=250):
    global ind
    ind += 1
    if ind == 4: ind = 0
    portailphoto.configure(format="gif -index " + str(ind))
    fenetre.after(delay, update)

def case():
    global nbcle,player,brouillarddefinitif,fenetre,labelobjectif,labelcle,labelcommande,labeltouches,labelmiscellaneous
    canvas.delete(player)
    if brouillard.get()==1:
        canvas.delete(ALL)
        affichage_labavecbrouill()
    if lines[posy][posx]=='3':
        lines[posy][posx]='0'
        nbcle+=1
        labelobjectif=Label(fenetre,text=('Trouves la sortie !'), font=(15),fg='red')
        labelobjectif.grid_forget()
        labelobjectif.grid(row=1,column=2)
        labelcle=Label(fenetre,text=('Nombre de clés:',nbcle))
        labelcle.grid_forget()
        labelcle.grid(row=2,column=2)
        labelcommande=Label(fenetre,text=('Commandes: '))
        labelcommande.grid_forget()
        labelcommande.grid(row=3,column=2)
        labeltouches=Label(fenetre,text=('-Déplacements: touches fléchées '))
        labeltouches.grid_forget()
        labeltouches.grid(row=4,column=2)
        labelmiscellaneous=Label(fenetre,text=('-Quitter le jeu: escape '))
        labelmiscellaneous.grid_forget()
        labelmiscellaneous.grid(row=5,column=2)
        canvas.create_image((posx)*13,(posy)*13,anchor=NW,image=solphoto)
        player=canvas.create_image(posx*13+1,posy*13+1,anchor=NW,image=joueurphoto)
    elif lines[posy][posx]=='2':
        canvas.create_image((posx)*13,(posy)*13,anchor=NW,image=porteouvphoto)
        player=canvas.create_image(posx*13+1,posy*13+1,anchor=NW,image=joueurphoto)
        labelobjectif=Label(fenetre,text=('Trouves la sortie !'), font=(15),fg='red')
        labelobjectif.grid_forget()
        labelobjectif.grid(row=1,column=2)
        labelcle=Label(fenetre,text=('Nombre de clés:',nbcle))
        labelcle.grid_forget()
        labelcle.grid(row=2,column=2)
        labelcommande=Label(fenetre,text=('Commandes: '))
        labelcommande.grid_forget()
        labelcommande.grid(row=3,column=2)
        labeltouches=Label(fenetre,text=('-Déplacements: touches fléchées '))
        labeltouches.grid_forget()
        labeltouches.grid(row=4,column=2)
        labelmiscellaneous=Label(fenetre,text=('-Quitter le jeu: escape '))
        labelmiscellaneous.grid_forget()
        labelmiscellaneous.grid(row=5,column=2)
        lines[posy][posx]='5'
    elif lines[posy][posx]=='4':
        player=canvas.create_image(posx*13+1,posy*13+1,anchor=NW,image=joueurphoto)
        showinfo("Gagné !!!",(deplacements+1,"déplacements"))
        fenetre.destroy()
    else:
        player=canvas.create_image(posx*13+1,posy*13+1,anchor=NW,image=joueurphoto)

def droite(event):
    global posx,posy,fenetre,player,deplacements
    if deppos("droite")=='True':
        posx+=1
        canvas.delete(player)
        case()
        deplacements+=1
def gauche(event):
    global posx,posy,fenetre,player,deplacements
    if deppos("gauche")=='True':
        posx-=1
        canvas.delete(player)
        case()
        deplacements+=1
def haut(event):
    global posx,posy,fenetre,player,deplacements
    if deppos("haut")=='True':
        posy-=1
        canvas.delete(player)
        case()
        deplacements+=1
def bas(event):
    global posx,posy,fenetre,player,deplacements
    if deppos("bas")=='True':
        posy+=1
        canvas.delete(player)
        case()
        deplacements+=1

def generalea():
    global x,lines,liste
    liste=[]
    x=int(taillelab.get())

    def est_constructible(x,y,liste) :
        if liste[y][x]=='1' :
            return(False)
        compteur=0
        direction=0
        if liste[y][x-1]=='1' :
            compteur+=1
            direction=1
        if liste[y][x+1]=='1' :
            compteur+=1
            direction=2
        if liste[y-1][x]=='1' :
            compteur+=1
            direction=3
        if liste[y+1][x]=='1' :
            compteur+=1
            direction=4
        if compteur==1 :
            if direction==2 :
                if liste[y-1][x-1]=='0' and liste[y+1][x-1]=='0' :
                    return(True)
            if direction==1 :
                if liste[y-1][x+1]=='0' and liste[y+1][x+1]=='0' :
                    return(True)
            if direction==4 :
                if liste[y-1][x-1]=='0' and liste[y-1][x+1]=='0' :
                    return(True)
            if direction==3 :
                if liste[y+1][x-1]=='0' and liste[y+1][x+1]=='0' :
                    return(True)
        return(False)

    def init0():
        for i in range (x+1):
            liste.append([])
            for j in range (x+1):
                if i==x-1  and j==x-1 :
                    liste[i].append('4')
                elif i==x//2 and j==x//2:
                    liste[i].append('1')
                elif i==x or i==0 or j==x or j==0:
                    liste[i].append('1')
                else:
                    liste[i].append('0')

    def constructible():
        global x, constructib,listeconstr
        listeconstr=[]
        for k in range (1,x):
            for l in range (1,x):
                if est_constructible(k,l,liste)==True:
                    listeconstr.append((l,k))
        return (listeconstr)
    constructib=1
    init0()
    constructible()
    while  len(constructible())>0 :
            num1=randint(0,len(listeconstr)-1)
            liste[listeconstr[num1][0]][listeconstr[num1][1]]='1'
            constructible()
    lines=liste

portailphoto = PhotoImage(file="portail.gif")
sol=Image.open("sol.png")
solphoto=ImageTk.PhotoImage(sol)
murphoto=ImageTk.PhotoImage(Image.open("mur.png"))
solcle=Image.open("sol+cle.png")
solclephoto=ImageTk.PhotoImage(solcle)
porte=Image.open("porte.png")
portephoto=ImageTk.PhotoImage(porte)
porteouv=Image.open("portopen.png")
porteouvphoto=ImageTk.PhotoImage(porteouv)
joueur=Image.open("joueur.png")
joueurphoto=ImageTk.PhotoImage(joueur)
canvas2=Canvas(fenetre1,width=40*13,height=30*13)
canvas2.grid(row=0,column=0,rowspan=9,columnspan=4)
for i in range (40):
    for j in range(30):
        canvas2.create_image(i*13,j*13,anchor=NW,image=murphoto)


def generation():
    global canvas,fenetre,gene,posx,posy,deplacements,nbcle,lines,labelobjectif,labelcle,labelcommande,labeltouches,labelmiscellaneous
    deplacements=0
    fenetre=Toplevel(fenetre1)

    posx=1
    posy=1
    fenetre.focus_set()
    x=taillelab.get()
    if aleatoire.get()==0:
        generalea()
    else:
        lines=[]
        aouvrir=str("Labyrinthe"+str(aleatoire.get())+".txt")
        fichier=open(aouvrir,"r")
        caractereslus=fichier.readlines()
        fichier.close()
        for n in range(len(caractereslus)):
            lines.append([])
            for m in range(len(caractereslus[1])-1):
                lines[n].append(caractereslus[n][m])
    canvas=Canvas(fenetre,width=13*len(lines[1]),height=13*len(lines))
    player=canvas.create_image(posx*13+1,posy*13+1,anchor=NW,image=joueurphoto)
    canvas.grid(row=1,column=1,rowspan=len(lines)//2)
    labelobjectif=Label(fenetre,text=('Trouves la sortie !'), font=(15),fg='red')
    labelobjectif.grid(row=1,column=2)
    labelcle=Label(fenetre,text=('Nombre de clés:',nbcle))
    labelcle.grid(row=2,column=2)
    labelcommande=Label(fenetre,text=('Commandes: '))
    labelcommande.grid(row=3,column=2)
    labeltouches=Label(fenetre,text=('-Déplacements: touches fléchées '))
    labeltouches.grid(row=4,column=2)
    labelmiscellaneous=Label(fenetre,text=('-Quitter le jeu: escape '))
    labelmiscellaneous.grid(row=5,column=2)
    if brouillard.get()==0 :
        affichage_labsansbrouill()
    else:
        affichage_labavecbrouill()
    for x in range(10):
        pygame.mixer.music.load("song.wav")
        pygame.mixer.music.play()
    fenetre.bind('<Right>', droite)
    fenetre.bind('<Left>', gauche)
    fenetre.bind('<Down>', bas)
    fenetre.bind('<Up>', haut)
    fenetre.bind('<Escape>',quitter)
    fenetre.title("My Little Laby")
    fenetre.iconbitmap("logo.ico")
    update()
    fenetre.mainloop()

def affichage_labsansbrouill():
    global canvas, player, posx,posy,lines
    for i in range (len (lines)):
        for j in range (len(lines[0])):
            if lines[i][j]=='0':
                        canvas.create_image(j*13,i*13,anchor=NW,image=solphoto )
            elif lines[i][j]=='1':
                        canvas.create_image(j*13,i*13,anchor=NW,image=murphoto)
            elif lines[i][j]=='2':
                        canvas.create_image(j*13,i*13,anchor=NW,image=portephoto)
            elif lines[i][j]=='3':
                        canvas.create_image(j*13,i*13, anchor=NW,image=solclephoto)
            elif lines[i][j]=='5':
                        canvas.create_image(j*13,i*13, anchor=NW,image=porteouvphoto)
            else:
                        canvas.create_image(j*13,i*13, anchor=NW,image=portailphoto)
    player=canvas.create_image(posx*13+1,posy*13+1,anchor=NW,image=joueurphoto)

def affichage_labavecbrouill():
    global canvas,player, posx,posy
    for i in range (len (lines)):
        for j in range (len(lines[0])):
            if (posy-2)<=i<=(posy+2):
                if (posx-2)<=j<=(posx+2):
                    if lines[i][j]=='0':
                        canvas.create_image(j*13,i*13,anchor=NW,image=solphoto )
                    elif lines[i][j]=='1':
                        canvas.create_image(j*13,i*13,anchor=NW,image=murphoto)
                    elif lines[i][j]=='2':
                        canvas.create_image(j*13,i*13,anchor=NW,image=portephoto)
                    elif lines[i][j]=='3':
                        canvas.create_image(j*13,i*13, anchor=NW,image=solclephoto)
                    elif lines[i][j]=='5':
                        canvas.create_image(j*13,i*13, anchor=NW,image=porteouvphoto)
                    else:
                        canvas.create_image(j*13,i*13, anchor=NW,image=portailphoto)
    player=canvas.create_image(posx*13+1,posy*13+1,anchor=NW,image=joueurphoto)
brouillard=IntVar()
brouillard.set(0)

generer=Button(fenetre1,text='Générer',command=generation,bg='#CC0000')
generer.grid(row=1,column=1,rowspan=6)

brouillardlabel=Label(fenetre1,text='brouillard ?',bg='#AAAAAA')
brouillardlabel.grid(row=1,column=2,rowspan=2)
on=Radiobutton(fenetre1,text="On",variable=brouillard,value= 1,bg='#AAAAAA')
on.grid(row=1,column=3)
off=Radiobutton(fenetre1,text="Off",variable=brouillard,value= 0,bg='#AAAAAA')
off.grid(row=2,column=3)



aleatoire=IntVar()
aleatoire.set(0)
labelalea=Label(fenetre1,text='Générer aléatoirement ou labyrinthe préconçu ?',bg='#AAAAAA')
labelalea.grid(row=3,column=2,rowspan=1)
al=Radiobutton(fenetre1,text="Aléatoire",variable=aleatoire,value=0,bg='#AAAAAA')
al.grid(row=3,column=3)
lab1=Radiobutton(fenetre1,text="15x15",variable=aleatoire,value=1,bg='#AAAAAA')
lab1.grid(row=5,column=3)
lab2=Radiobutton(fenetre1,text="20x10",variable=aleatoire,value=2,bg='#AAAAAA')
lab2.grid(row=6,column=3)
lab3=Radiobutton(fenetre1,text="30x30",variable=aleatoire,value=3,bg='#AAAAAA')
lab3.grid(row=7,column=3)
lab4=Radiobutton(fenetre1,text="13x54",variable=aleatoire,value=4,bg='#AAAAAA')
lab4.grid(row=8,column=3)

labeltaille=Label(fenetre1,text='Entrer la taille du labyrinthe(si généré aléatoirement):',bg='#AAAAAA')
labeltaille.grid(row=4,column=2)
taillelab=Entry(fenetre1,bg='bisque')
taillelab.grid(row=4,column=3)

fenetre1.title("Bienvenue dans le labyrinthe, veuillez selectionner un niveau")
fenetre1.mainloop()
