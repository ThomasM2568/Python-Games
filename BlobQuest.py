from tkinter import*
from PIL import Image, ImageTk
#PENSER QU'ON PEUT METTRE DES GIFS POUR L'EAU

from tkinter.messagebox import *
import tkinter.font as font
import tkinter as tk

#--Import
import sqlite3
from random import *
import time
attaque=0

#--Class--
class Guerrier :
    def __init__(self):
        self.HP=5
        self.ATK=3
        self.LVL=1
        self.XP=0
        global conn
        conn.commit()
        cursor = conn.cursor()
        v=self.LVL
        print(v)
        for name in ("1"):
            cursor.execute("SELECT rowid FROM saves WHERE id = ?", (name,))
            data=cursor.fetchall()
            if len(data)==0:
                text=str(self.LVL)+","+str(self.XP)+","+str(self.HP)+","+str(self.ATK)
                commande="INSERT INTO SAVES (id,classe,lvl,xp,hp,atk) \
                VALUES (1, 'Guerrier',"+str(text)+")"
                conn.execute(commande);
                print('Le joueur avec ID %s a été ajouté à la table'%name)
            else:
                print('Le joueur avec ID %s est déjà dans la table %s'%(name,','.join(map(str, next(zip(*data))))))
                self.__chargersauvegarde__()



        conn.commit()

        #conn.close()


    def __progression__(self,EXP):
        self.XP+=EXP
        self.__lvlup__()
        return("XP =",self.XP)

    def __lvlup__(self):
        if self.XP>=10:
            self.XP-=10
            self.LVL+=1
            self.ATK+=1
            self.HP+=3
            self.__lvlup__()
        return("XP =",self.XP,"LVL =",self.LVL,"HP =",self.HP,"ATK =",self.ATK)

    def __stats__(self):
        return("XP =",self.XP,"LVL =",self.LVL,"HP =",self.HP,"ATK =",self.ATK)

    def __sauvegarde__(self):
        global conn
        #sqlite3.connect("projet.db")
        text="UPDATE saves SET xp="+str(self.XP)+" WHERE id=1"
        text2="UPDATE saves SET lvl="+str(self.LVL)+" WHERE id=1"
        text3="UPDATE saves SET hp="+str(self.HP)+" WHERE id=1"
        text4="UPDATE saves SET atk="+str(self.ATK)+" WHERE id=1"
        conn.execute(text)
        conn.execute(text2)
        conn.execute(text3)
        conn.execute(text4)
        conn.commit()

    def __chargersauvegarde__(self):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM saves WHERE id = ?", (1, ))
        user1 = cursor.fetchone()

        conn.commit()
        return(user1,"Voici les infos de la sauvegarde")


    def __degatsinfliges__(self,mob):
        print(mob.HP)
        if mob.posactuellex==posX+1 and mob.posactuelley==posY and mob.HP>0 or mob.posactuellex==posX+1 and mob.posactuelley==posY+1 and mob.HP>0 or mob.posactuellex==posX and mob.posactuelley==posY+1 and mob.HP>0 or mob.posactuellex==posX-1 and mob.posactuelley==posY+1 and mob.HP>0 or mob.posactuellex==posX-1 and mob.posactuelley==posY and mob.HP>0 or mob.posactuellex==posX-1 and mob.posactuelley==posY-1 and mob.HP>0 or mob.posactuellex==posX and mob.posactuelley==posY-1 and mob.HP>0 or mob.posactuellex==posX+1 and mob.posactuelley==posY-1 and mob.HP>0:
            mob.HP-=self.ATK
            if mob.HP<=0:
                self.__progression__(mob.XP)
                self.HP+=1
        return(mob.ATK," dégats pris par le mob")



class Archer :
    def __init__(self):
        self.HP=3
        self.ATK=5
        self.LVL=1
        self.XP=0
        global conn
        conn.commit()
        cursor = conn.cursor()
        v=self.LVL
        print(v)
        for name in ("2"):
            cursor.execute("SELECT rowid FROM saves WHERE id = ?", (name,))
            data=cursor.fetchall()
            if len(data)==0:
                text=str(self.LVL)+","+str(self.XP)+","+str(self.HP)+","+str(self.ATK)
                commande="INSERT INTO SAVES (id,classe,lvl,xp,hp,atk) \
                VALUES (2, 'Archer',"+str(text)+")"
                conn.execute(commande);
                print('Le joueur avec ID %s a été ajouté à la table'%name)
            else:
                print('Le joueur avec ID %s est déjà dans la table %s'%(name,','.join(map(str, next(zip(*data))))))
                self.__chargersauvegarde__()

    def __progression__(self,EXP):
        self.XP+=EXP
        self.__lvlup__()
        return("XP =",self.XP)

    def __lvlup__(self):
        if self.XP>=10:
            self.XP-=10
            self.LVL+=1
            self.ATK+=2
            self.HP+=1
            self.__lvlup__()
        return("XP =",self.XP,"LVL =",self.LVL,"HP =",self.HP,"ATK =",self.ATK)

    def __stats__(self):
        return("XP =",self.XP,"LVL =",self.LVL,"HP =",self.HP,"ATK =",self.ATK)

    def __sauvegarde__(self):
        global conn
        #sqlite3.connect("projet.db")
        text="UPDATE saves SET xp="+str(self.XP)+" WHERE id=2"
        text2="UPDATE saves SET lvl="+str(self.LVL)+" WHERE id=2"
        text3="UPDATE saves SET hp="+str(self.HP)+" WHERE id=2"
        text4="UPDATE saves SET atk="+str(self.ATK)+" WHERE id=2"
        conn.execute(text)
        conn.execute(text2)
        conn.execute(text3)
        conn.execute(text4)
        conn.commit()

    def __chargersauvegarde__(self):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM saves WHERE id = ?", (2, ))
        user1 = cursor.fetchone()

        conn.commit()
        return(user1,"Voici les infos de la sauvegarde")


    def __degatsinfliges__(self,mob):
        if mob.posactuellex==posX+1 and mob.posactuelley==posY and mob.HP>0 or mob.posactuellex==posX+1 and mob.posactuelley==posY+1 and mob.HP>0 or mob.posactuellex==posX and mob.posactuelley==posY+1 and mob.HP>0 or mob.posactuellex==posX-1 and mob.posactuelley==posY+1 and mob.HP>0 or mob.posactuellex==posX-1 and mob.posactuelley==posY and mob.HP>0 or mob.posactuellex==posX-1 and mob.posactuelley==posY-1 and mob.HP>0 or mob.posactuellex==posX and mob.posactuelley==posY-1 and mob.HP>0 or mob.posactuellex==posX+1 and mob.posactuelley==posY-1 and mob.HP>0:
            mob.HP-=self.ATK
            if mob.HP<=0:
                print("Oui")
                self.__progression__(mob.XP)
                self.HP+=1
        return(mob.ATK," dégats pris par le mob")



class Mage :
    def __init__(self):
        self.HP=4
        self.ATK=4
        self.LVL=1
        self.XP=0
        global conn
        conn.commit()
        cursor = conn.cursor()
        v=self.LVL
        print(v)
        for name in ("3"):
            cursor.execute("SELECT rowid FROM saves WHERE id = ?", (name,))
            data=cursor.fetchall()
            if len(data)==0:
                text=str(self.LVL)+","+str(self.XP)+","+str(self.HP)+","+str(self.ATK)
                commande="INSERT INTO SAVES (id,classe,lvl,xp,hp,atk) \
                VALUES (3, 'Mage',"+str(text)+")"
                conn.execute(commande);
                print('Le joueur avec ID %s a été ajouté à la table'%name)
            else:
                print('Le joueur avec ID %s est déjà dans la table %s'%(name,','.join(map(str, next(zip(*data))))))
                self.__chargersauvegarde__()

    def __progression__(self,EXP):
        self.XP+=EXP
        self.__lvlup__()
        return("XP =",self.XP)

    def __lvlup__(self):
        if self.XP>=10:
            self.XP-=10
            self.LVL+=1
            self.ATK+=1
            self.HP+=2
            self.__lvlup__()
        return("XP =",self.XP,"LVL =",self.LVL,"HP =",self.HP,"ATK =",self.ATK)

    def __stats__(self):
        return("XP =",self.XP,"LVL =",self.LVL,"HP =",self.HP,"ATK =",self.ATK)

    def __sauvegarde__(self):
        global conn
        #sqlite3.connect("projet.db")
        text="UPDATE saves SET xp="+str(self.XP)+" WHERE id=3"
        text2="UPDATE saves SET lvl="+str(self.LVL)+" WHERE id=3"
        text3="UPDATE saves SET hp="+str(self.HP)+" WHERE id=3"
        text4="UPDATE saves SET atk="+str(self.ATK)+" WHERE id=3"
        conn.execute(text)
        conn.execute(text2)
        conn.execute(text3)
        conn.execute(text4)
        conn.commit()

    def __chargersauvegarde__(self):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM saves WHERE id = ?", (3, ))
        user1 = cursor.fetchone()

        conn.commit()
        return(user1,"Voici les infos de la sauvegarde")


    def __degatsinfliges__(self,mob):
        if mob.posactuellex==posX+1 and mob.posactuelley==posY and mob.HP>0 or mob.posactuellex==posX+1 and mob.posactuelley==posY+1 and mob.HP>0 or mob.posactuellex==posX and mob.posactuelley==posY+1 and mob.HP>0 or mob.posactuellex==posX-1 and mob.posactuelley==posY+1 and mob.HP>0 or mob.posactuellex==posX-1 and mob.posactuelley==posY and mob.HP>0 or mob.posactuellex==posX-1 and mob.posactuelley==posY-1 and mob.HP>0 or mob.posactuellex==posX and mob.posactuelley==posY-1 and mob.HP>0 or mob.posactuellex==posX+1 and mob.posactuelley==posY-1 and mob.HP>0:
            mob.HP-=self.ATK
            if mob.HP<=0:
                print("Oui")
                self.__progression__(mob.XP)
                self.HP+=1
        return(mob.ATK," dégats pris par le mob")

class troll:
    def __init__(self, posactuellex, posactuelley):
        self.HP=119
        self.ATK=3
        self.LVL=1
        self.XP=666
        self.posactuellex=posactuellex
        self.posactuelley=posactuelley
        global conn
        conn.commit()
        cursor = conn.cursor()
        v=self.LVL
        print(v)
        for name in ("4"):
            cursor.execute("SELECT rowid FROM saves WHERE id = ?", (name,))
            data=cursor.fetchall()
            if len(data)==0:
                text=str(self.LVL)+","+str(self.XP)+","+str(self.HP)+","+str(self.ATK)
                commande="INSERT INTO SAVES (id,classe,lvl,xp,hp,atk) \
                VALUES (4, 'Mob',"+str(text)+")"
                conn.execute(commande);
                print('Le joueur avec ID %s a été ajouté à la table'%name)
            else:
                print('Le joueur avec ID %s est déjà dans la table %s'%(name,','.join(map(str, next(zip(*data))))))

    def __deplacement__(self):
        self.nombre1=randint(-1,1)
        self.nombre2=randint(0,1)

        if self.nombre2==0:
            if self.nombre1==-1:
                self.posactuellex=self.nombre1+self.posactuellex
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuellex+=1
            if self.nombre1==1:
                self.posactuellex=self.nombre1+self.posactuellex
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuellex-=1
        if self.nombre2==1:
            if self.nombre1==-1:
                self.posactuelley=self.nombre1+self.posactuelley
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuelley+=1
            if self.nombre1==1:
                self.posactuelley=self.nombre1+self.posactuelley
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuelley-=1
        return(self.posactuellex,self.posactuelley)


    def __degatsinfliges__(self,mob):
        mob.HP-=self.ATK
        return(mob.ATK," dégats pris par le joueur")


class blobb:
    def __init__(self, posactuellex, posactuelley):
        self.HP=9
        self.ATK=1
        self.LVL=1
        self.XP=4
        self.posactuellex=posactuellex#posdumobX
        self.posactuelley=posactuelley#posdemobY
        global conn
        conn.commit()
        cursor = conn.cursor()
        v=self.LVL
        print(v)
        for name in ("5"):
            cursor.execute("SELECT rowid FROM saves WHERE id = ?", (name,))
            data=cursor.fetchall()
            if len(data)==0:
                text=str(self.LVL)+","+str(self.XP)+","+str(self.HP)+","+str(self.ATK)
                commande="INSERT INTO SAVES (id,classe,lvl,xp,hp,atk) \
                VALUES (5, 'Mob1',"+str(text)+")"
                conn.execute(commande);
                print('Le joueur avec ID %s a été ajouté à la table'%name)
            else:
                print('Le joueur avec ID %s est déjà dans la table %s'%(name,','.join(map(str, next(zip(*data))))))

    def __deplacement__(self):
        self.nombre1=randint(-1,1)
        self.nombre2=randint(0,1)

        if self.nombre2==0:
            if self.nombre1==-1:
                self.posactuellex=self.nombre1+self.posactuellex
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuellex+=1
            if self.nombre1==1:
                self.posactuellex=self.nombre1+self.posactuellex
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuellex-=1
        if self.nombre2==1:
            if self.nombre1==-1:
                self.posactuelley=self.nombre1+self.posactuelley
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuelley+=1
            if self.nombre1==1:
                self.posactuelley=self.nombre1+self.posactuelley
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuelley-=1
        return(self.posactuellex,self.posactuelley)


    def __degatsinfliges__(self,mob):
        mob.HP-=self.ATK
        return(mob.ATK," dégats pris par le mob")

class blobo:
    def __init__(self, posactuellex, posactuelley):
        self.HP=15
        self.ATK=1
        self.LVL=1
        self.XP=4
        self.posactuellex=posactuellex#posdumobX
        self.posactuelley=posactuelley#posdemobY
        global conn
        conn.commit()
        cursor = conn.cursor()
        v=self.LVL
        print(v)
        for name in ("6"):
            cursor.execute("SELECT rowid FROM saves WHERE id = ?", (name,))
            data=cursor.fetchall()
            if len(data)==0:
                text=str(self.LVL)+","+str(self.XP)+","+str(self.HP)+","+str(self.ATK)
                commande="INSERT INTO SAVES (id,classe,lvl,xp,hp,atk) \
                VALUES (6, 'Mob2',"+str(text)+")"
                conn.execute(commande);
                print('Le joueur avec ID %s a été ajouté à la table'%name)
            else:
                print('Le joueur avec ID %s est déjà dans la table %s'%(name,','.join(map(str, next(zip(*data))))))

    def __deplacement__(self):
        self.nombre1=randint(-1,1)
        self.nombre2=randint(0,1)

        if self.nombre2==0:
            if self.nombre1==-1:
                self.posactuellex=self.nombre1+self.posactuellex
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuellex+=1
            if self.nombre1==1:
                self.posactuellex=self.nombre1+self.posactuellex
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuellex-=1
        if self.nombre2==1:
            if self.nombre1==-1:
                self.posactuelley=self.nombre1+self.posactuelley
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuelley+=1
            if self.nombre1==1:
                self.posactuelley=self.nombre1+self.posactuelley
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuelley-=1
        return(self.posactuellex,self.posactuelley)


    def __degatsinfliges__(self,mob):
        mob.HP-=self.ATK

class blobv:
    def __init__(self, posactuellex, posactuelley):
        self.HP=30
        self.ATK=2
        self.LVL=1
        self.XP=4
        self.posactuellex=posactuellex#posdumobX
        self.posactuelley=posactuelley#posdemobY
        global conn
        conn.commit()
        cursor = conn.cursor()
        v=self.LVL
        print(v)
        for name in ("7"):
            cursor.execute("SELECT rowid FROM saves WHERE id = ?", (name,))
            data=cursor.fetchall()
            if len(data)==0:
                text=str(self.LVL)+","+str(self.XP)+","+str(self.HP)+","+str(self.ATK)
                commande="INSERT INTO SAVES (id,classe,lvl,xp,hp,atk) \
                VALUES (7, 'Mob3',"+str(text)+")"
                conn.execute(commande);
                print('Le joueur avec ID %s a été ajouté à la table'%name)
            else:
                print('Le joueur avec ID %s est déjà dans la table %s'%(name,','.join(map(str, next(zip(*data))))))

    def __deplacement__(self):
        self.nombre1=randint(-1,1)
        self.nombre2=randint(0,1)

        if self.nombre2==0:
            if self.nombre1==-1:
                self.posactuellex=self.nombre1+self.posactuellex
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuellex+=1
            if self.nombre1==1:
                self.posactuellex=self.nombre1+self.posactuellex
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuellex-=1
        if self.nombre2==1:
            if self.nombre1==-1:
                self.posactuelley=self.nombre1+self.posactuelley
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuelley+=1
            if self.nombre1==1:
                self.posactuelley=self.nombre1+self.posactuelley
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuelley-=1
        return(self.posactuellex,self.posactuelley)


    def __degatsinfliges__(self,mob):
        mob.HP-=self.ATK

class blobj:
    def __init__(self, posactuellex, posactuelley):
        self.HP=20
        self.ATK=3
        self.LVL=1
        self.XP=4
        self.posactuellex=posactuellex#posdumobX
        self.posactuelley=posactuelley#posdemobY
        global conn
        conn.commit()
        cursor = conn.cursor()
        v=self.LVL
        print(v)
        for name in ("8"):
            cursor.execute("SELECT rowid FROM saves WHERE id = ?", (name,))
            data=cursor.fetchall()
            if len(data)==0:
                text=str(self.LVL)+","+str(self.XP)+","+str(self.HP)+","+str(self.ATK)
                commande="INSERT INTO SAVES (id,classe,lvl,xp,hp,atk) \
                VALUES (8, 'Mob4',"+str(text)+")"
                conn.execute(commande);
                print('Le joueur avec ID %s a été ajouté à la table'%name)
            else:
                print('Le joueur avec ID %s est déjà dans la table %s'%(name,','.join(map(str, next(zip(*data))))))

    def __deplacement__(self):
        self.nombre1=randint(-1,1)
        self.nombre2=randint(0,1)

        if self.nombre2==0:
            if self.nombre1==-1:
                self.posactuellex=self.nombre1+self.posactuellex
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuellex+=1
            if self.nombre1==1:
                self.posactuellex=self.nombre1+self.posactuellex
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuellex-=1
        if self.nombre2==1:
            if self.nombre1==-1:
                self.posactuelley=self.nombre1+self.posactuelley
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuelley+=1
            if self.nombre1==1:
                self.posactuelley=self.nombre1+self.posactuelley
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuelley-=1
        return(self.posactuellex,self.posactuelley)


    def __degatsinfliges__(self,mob):
        mob.HP-=self.ATK


class blobve:
    def __init__(self, posactuellex, posactuelley):
        self.HP=35
        self.ATK=3
        self.LVL=1
        self.XP=4
        self.posactuellex=posactuellex#posdumobX
        self.posactuelley=posactuelley#posdemobY
        global conn
        conn.commit()
        cursor = conn.cursor()
        v=self.LVL
        print(v)
        for name in ("9"):
            cursor.execute("SELECT rowid FROM saves WHERE id = ?", (name,))
            data=cursor.fetchall()
            if len(data)==0:
                text=str(self.LVL)+","+str(self.XP)+","+str(self.HP)+","+str(self.ATK)
                commande="INSERT INTO SAVES (id,classe,lvl,xp,hp,atk) \
                VALUES (9, 'Mob5',"+str(text)+")"
                conn.execute(commande);
                print('Le joueur avec ID %s a été ajouté à la table'%name)
            else:
                print('Le joueur avec ID %s est déjà dans la table %s'%(name,','.join(map(str, next(zip(*data))))))

    def __deplacement__(self):
        self.nombre1=randint(-1,1)
        self.nombre2=randint(0,1)

        if self.nombre2==0:
            if self.nombre1==-1:
                self.posactuellex=self.nombre1+self.posactuellex
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuellex+=1
            if self.nombre1==1:
                self.posactuellex=self.nombre1+self.posactuellex
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuellex-=1
        if self.nombre2==1:
            if self.nombre1==-1:
                self.posactuelley=self.nombre1+self.posactuelley
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuelley+=1
            if self.nombre1==1:
                self.posactuelley=self.nombre1+self.posactuelley
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuelley-=1
        return(self.posactuellex,self.posactuelley)


    def __degatsinfliges__(self,mob):
        mob.HP-=self.ATK

class blobm:
    def __init__(self, posactuellex, posactuelley):
        self.HP=42
        self.ATK=2
        self.LVL=1
        self.XP=4
        self.posactuellex=posactuellex#posdumobX
        self.posactuelley=posactuelley#posdemobY
        global conn
        conn.commit()
        cursor = conn.cursor()
        v=self.LVL
        print(v)
        for name in ("0"):
            cursor.execute("SELECT rowid FROM saves WHERE id = ?", (name,))
            data=cursor.fetchall()
            if len(data)==0:
                text=str(self.LVL)+","+str(self.XP)+","+str(self.HP)+","+str(self.ATK)
                commande="INSERT INTO SAVES (id,classe,lvl,xp,hp,atk) \
                VALUES (0, 'Mob6',"+str(text)+")"
                conn.execute(commande);
                print('Le joueur avec ID %s a été ajouté à la table'%name)
            else:
                print('Le joueur avec ID %s est déjà dans la table %s'%(name,','.join(map(str, next(zip(*data))))))

    def __deplacement__(self):
        self.nombre1=randint(-1,1)
        self.nombre2=randint(0,1)

        if self.nombre2==0:
            if self.nombre1==-1:
                self.posactuellex=self.nombre1+self.posactuellex
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuellex+=1
            if self.nombre1==1:
                self.posactuellex=self.nombre1+self.posactuellex
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuellex-=1
        if self.nombre2==1:
            if self.nombre1==-1:
                self.posactuelley=self.nombre1+self.posactuelley
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuelley+=1
            if self.nombre1==1:
                self.posactuelley=self.nombre1+self.posactuelley
                if monde[self.posactuellex][self.posactuelley]=='0' or monde[self.posactuellex][self.posactuelley]=='M' or monde[self.posactuellex][self.posactuelley]=='N' or monde[self.posactuellex][self.posactuelley]=='5' or monde[self.posactuellex][self.posactuelley]=='6' or monde[self.posactuellex][self.posactuelley]=='A' or monde[self.posactuellex][self.posactuelley]=='7' or monde[self.posactuellex][self.posactuelley]=='8' or monde[self.posactuellex][self.posactuelley]=='9' or monde[self.posactuellex][self.posactuelley]=='T' or monde[self.posactuellex][self.posactuelley]=='Z' or monde[self.posactuellex][self.posactuelley]=='K':
                    self.posactuelley-=1
        return(self.posactuellex,self.posactuelley)


    def __degatsinfliges__(self,mob):
        mob.HP-=self.ATK

#-----
def createtable():

    global conn
    conn = sqlite3.connect('projet.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS saves(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         classe TEXT,
         lvl INTERGER,
         xp INTERGER,
         hp INTERGER,
         atk INTERGER
    )
    """)
    return("Done")



print(createtable())

Kylian=troll(201,33)
blobby=blobb(7,27)
blobby1=blobb(16,51)
blobby2=blobb(62,17)
blobby3=blobo(28,14)
blobby4=blobo(23,45)
blobby5=blobb(49,40)
blobby6=blobj(97,40)
blobby7=blobv(109,27)
blobby8=blobv(116,49)
blobby9=blobj(128,17)
blobby10=blobve(133,40)
blobby11=blobve(149,26)
blobby12=blobm(175,24)
blobby13=blobm(174,41)
blobby14=blobm(183,43)
blobby15=blobm(191,23)

def fullscreen():
    window.attributes('-fullscreen',1)

def start_go():
    global perso, pingouin, JL, joueur
    print(pingouin)
    joueur = varsource.get()
    print(joueur)
    if pingouin!=1:
        if joueur==0:
            showerror("Error", "Merci de choisir une classe")
        if joueur==1:
            tk.Button(window, text="Lancer", command=window.destroy).pack()
            perso=2
            pingouin=1
        if joueur==2:
            tk.Button(window, text="Lancer", command=window.destroy).pack()
            perso=3
            pingouin=1
        if joueur==3:
            tk.Button(window, text="Lancer", command=window.destroy).pack()
            perso=1
            pingouin=1

color="black"
window= Tk()
window.title("Blob Quest")
window.iconbitmap("logo.ico")
height=window.winfo_screenheight()
width=window.winfo_screenwidth()
window.minsize(height,width)
window.config(background=color)
window.state('zoomed')

varsource=IntVar()
pingouin=0

choix_1 = Radiobutton(window, text="Guerrier", variable=varsource, font=("Helvetica", 15),indicatoron=0,value=1)
choix_2 = Radiobutton(window, text="Mage", variable=varsource, font=("Helvetica", 15),indicatoron=0,value=2)
choix_3 = Radiobutton(window, text="Lancier", variable=varsource, font=("Helvetica", 15),indicatoron=0,value=3)

choix_1.place(y=height/2,x=(width/2)-220)
choix_2.place(y=height/2,x=width/2)
choix_3.place(y=height/2,x=(width/2)+205)

tk.Button(window, text="Préparation", command=start_go).pack()

window.mainloop()

JL=Guerrier()
JP=Mage()
JK=Archer()


world_map=Tk()
world_map.title("Blob Quest")
world_map.iconbitmap("logo.ico")
fichier=open("map_PROJET_RPG","r")

water=Image.open("water.png")
photowater = ImageTk.PhotoImage(water)

sand=Image.open("sand.png")
photosand = ImageTk.PhotoImage(sand)

blob=Image.open("blob.png")
photoblob = ImageTk.PhotoImage(blob)

blob1=Image.open("blob1.png")
photoblob1 = ImageTk.PhotoImage(blob1)

blob2=Image.open("blob2.png")
photoblob2 = ImageTk.PhotoImage(blob2)

blob3=Image.open("blob3.png")
photoblob3 = ImageTk.PhotoImage(blob3)

blob4=Image.open("blob4.png")
photoblob4 = ImageTk.PhotoImage(blob4)

blob5=Image.open("blob5.png")
photoblob5 = ImageTk.PhotoImage(blob5)

grass=Image.open("grass.png")
photograss = ImageTk.PhotoImage(grass)

troll=Image.open("troll.png")
phototroll = ImageTk.PhotoImage(troll)

magesf=Image.open("magesf.png")
photomagesf = ImageTk.PhotoImage(magesf)

osa=Image.open("osa.png")
photoosa = ImageTk.PhotoImage(osa)

iop=Image.open("iop.png")
photoiop = ImageTk.PhotoImage(iop)

sol=Image.open("wood.png")
photosol = ImageTk.PhotoImage(sol)

mur=Image.open("brick.png")
photomur = ImageTk.PhotoImage(mur)

caillou=Image.open("stone.png")
photocaillou = ImageTk.PhotoImage(caillou)

pont=Image.open("bridge.png")
photopont = ImageTk.PhotoImage(pont)

door=Image.open("door.png")
photodoor = ImageTk.PhotoImage(door)

pantin=Image.open("pantin.png")
photopantin = ImageTk.PhotoImage(pantin)

pantinchamp=Image.open("pantinchamp.png")
photopantinchamp = ImageTk.PhotoImage(pantinchamp)

torche=Image.open("torche.png")
phototorche = ImageTk.PhotoImage(torche)

panneau=Image.open("panneau.png")
photopanneau = ImageTk.PhotoImage(panneau)

panneau2=Image.open("panneau2.png")
photopanneau2 = ImageTk.PhotoImage(panneau2)

feu=Image.open("feu.png")
photofeu = ImageTk.PhotoImage(feu)

epee=Image.open("epee.png")
photoepee = ImageTk.PhotoImage(epee)

lance=Image.open("lance.png")
photolance = ImageTk.PhotoImage(lance)

mort=Image.open("mort.png")
photomort = ImageTk.PhotoImage(mort)


tree7=Image.open("tree7.png")
phototree7 = ImageTk.PhotoImage(tree7)
treeA=Image.open("treeA.png")
phototreeA = ImageTk.PhotoImage(treeA)
tree8=Image.open("tree8.png")
phototree8 = ImageTk.PhotoImage(tree8)
tree9=Image.open("tree9.png")
phototree9 = ImageTk.PhotoImage(tree9)

champ=Image.open("champ.png")
photochamp = ImageTk.PhotoImage(champ)

road=Image.open("road.png")
photoroad = ImageTk.PhotoImage(road)

"""eau=canevas.create_image(i*16,j*16,anchor=NW,image=photowater)"""
ligne=fichier.readlines()
K=[]


bouton_quitter = Button(world_map, text = "Quitter", command = world_map.destroy)
bouton_quitter.pack()
Largeur = 5000
Hauteur = 5000
canevas = Canvas(world_map, width = Largeur, height =Hauteur, bg ='white')
canevas.pack(padx =5, pady =5)
posX=13
posY=11
posx=25
posy=13
r=20
mapi=1

def création(txt):
    monde=[]
    for i in txt:
        ligne=[]
        for j in i:
            if j=='0' or j=='1' or j=='2' or j=='3'or j=='J' or j=='P' or j=='M' or j=='N' or j=='4' or j=='5' or j=='6' or j=='7' or j=='A' or j=='8' or j=='9' or j=='F' or j=='R' or j=='T' or j=='Z' or j=='K':
                ligne.append(j)
        monde.append(ligne)
    return(monde)



w=1

def case(monde) :
    global posX, posY,mapi, w, posx, posy
    if posX==79 and posY==43 or posX==79 and posY==44 or posX==79 and posY==45 or posX==79 and posY==46:
        mapi=2
        canevas.place(x=-1200,y=-150)
        w=2
    if posX==78 and posY==43 or posX==78 and posY==44 or posX==78 and posY==45 or posX==78 and posY==46:
        mapi=1
        canevas.place(x=0,y=-150)# IMPORTANT
    if posX>=158:
        mapi=3
        canevas.place(x=-2400,y=-150)
        w=3
    if posX<158 and mapi==3:
        mapi=2
        canevas.place(x=-1200,y=-150)
        w=2
    if mapi==1:
        canevas.place(x=0,y=-150)# IMPORTANT
    if posX>216:
        w=3


    for i in range(posX-8,posX+9):
        for j in range(posY-8,posY+9):
            if blobby.HP>0:
                canevas.create_image(blobby.posactuellex*16,blobby.posactuelley*16,anchor=NW,image=photoblob)
            if blobby1.HP>0:
                canevas.create_image(blobby1.posactuellex*16,blobby1.posactuelley*16,anchor=NW,image=photoblob)
            if blobby2.HP>0:
                canevas.create_image(blobby2.posactuellex*16,blobby2.posactuelley*16,anchor=NW,image=photoblob)
            if blobby3.HP>0:
                canevas.create_image(blobby3.posactuellex*16,blobby3.posactuelley*16,anchor=NW,image=photoblob2)
            if blobby4.HP>0:
                canevas.create_image(blobby4.posactuellex*16,blobby4.posactuelley*16,anchor=NW,image=photoblob2)
            if blobby5.HP>0:
                canevas.create_image(blobby5.posactuellex*16,blobby5.posactuelley*16,anchor=NW,image=photoblob2)
            if blobby6.HP>0:
                canevas.create_image(blobby6.posactuellex*16,blobby6.posactuelley*16,anchor=NW,image=photoblob4)
            if blobby7.HP>0:
                canevas.create_image(blobby7.posactuellex*16,blobby7.posactuelley*16,anchor=NW,image=photoblob1)
            if blobby8.HP>0:
                canevas.create_image(blobby8.posactuellex*16,blobby8.posactuelley*16,anchor=NW,image=photoblob1)
            if blobby9.HP>0:
                canevas.create_image(blobby9.posactuellex*16,blobby9.posactuelley*16,anchor=NW,image=photoblob4)
            if blobby10.HP>0:
                canevas.create_image(blobby10.posactuellex*16,blobby10.posactuelley*16,anchor=NW,image=photoblob3)
            if blobby11.HP>0:
                canevas.create_image(blobby11.posactuellex*16,blobby11.posactuelley*16,anchor=NW,image=photoblob3)
            if blobby12.HP>0:
                canevas.create_image(blobby12.posactuellex*16,blobby12.posactuelley*16,anchor=NW,image=photoblob5)
            if blobby13.HP>0:
                canevas.create_image(blobby13.posactuellex*16,blobby13.posactuelley*16,anchor=NW,image=photoblob5)
            if blobby14.HP>0:
                canevas.create_image(blobby14.posactuellex*16,blobby14.posactuelley*16,anchor=NW,image=photoblob5)
            if blobby15.HP>0:
                canevas.create_image(blobby15.posactuellex*16,blobby15.posactuelley*16,anchor=NW,image=photoblob5)
            if Kylian.HP>0:
                canevas.create_image(Kylian.posactuellex*16,Kylian.posactuelley*16,anchor=NW,image=phototroll)
            if perso==3:
                canevas.create_image(posX*16,posY*16,anchor=NW,image=photomagesf)
            elif perso==1:
                canevas.create_image(posX*16,posY*16,anchor=NW,image=photoosa)
            elif perso==2:
                canevas.create_image(posX*16,posY*16,anchor=NW,image=photoiop)
            if (monde[i][j])=='0':#eau
                canevas.create_image(i*16,j*16,anchor=NW,image=photowater)
            elif (monde[i][j])=='1':#sol de maison
                canevas.create_image(i*16,j*16,anchor=NW,image=photosol)
            elif (monde[i][j])=='2':#pont
                canevas.create_image(i*16,j*16,anchor=NW,image=photopont)
            elif (monde[i][j])=='3':#herbe
                canevas.create_image(i*16,j*16,anchor=NW,image=photograss)
            elif (monde[i][j])=='4':#sable
                canevas.create_image(i*16,j*16,anchor=NW,image=photosand)
            elif (monde[i][j])=='5':#mur
                canevas.create_image(i*16,j*16,anchor=NW,image=photomur)
            elif (monde[i][j])=='6':#caillou
                canevas.create_image(i*16,j*16,anchor=NW,image=photocaillou)
            elif (monde[i][j])=='7':#arbrebasgauche
                canevas.create_image(i*16,j*16,anchor=NW,image=phototree7)
            elif (monde[i][j])=='A':#arbrebasdroite
                canevas.create_image(i*16,j*16,anchor=NW,image=phototreeA)
            elif (monde[i][j])=='8':#arbrehautgauche
                canevas.create_image(i*16,j*16,anchor=NW,image=phototree8)
            elif (monde[i][j])=='9':#arbrehautdroite
                canevas.create_image(i*16,j*16,anchor=NW,image=phototree9)
            elif (monde[i][j])=='P':#porte
                canevas.create_image(i*16,j*16,anchor=NW,image=photodoor)
            elif (monde[i][j])=='M':#pantin
                canevas.create_image(i*16,j*16,anchor=NW,image=photopantin)
            elif (monde[i][j])=='N':#pantinchamp
                canevas.create_image(i*16,j*16,anchor=NW,image=photopantinchamp)
            elif (monde[i][j])=='F':#champ
                canevas.create_image(i*16,j*16,anchor=NW,image=photochamp)
            elif (monde[i][j])=='R':#chemin
                canevas.create_image(i*16,j*16,anchor=NW,image=photoroad)
            elif (monde[i][j])=='T':#torche
                canevas.create_image(i*16,j*16,anchor=NW,image=phototorche)
            elif (monde[i][j])=='Z':#panneau
                canevas.create_image(i*16,j*16,anchor=NW,image=photopanneau)
            elif (monde[i][j])=='K':#panneau2
                canevas.create_image(i*16,j*16,anchor=NW,image=photopanneau2)


def casefullmap(monde) :
    global posX, posY,mapi, w, posx, posy

    if posX==79 and posY==43 or posX==79 and posY==44 or posX==79 and posY==45 or posX==79 and posY==46:
        mapi=2
        canevas.place(x=-1200,y=-150)
        w=1
    if posX>=158 and mapi==2:
        mapi=3
        canevas.place(x=-2400,y=-150)
        w=2
    if mapi==1:
        mapi=1
        canevas.place(x=0,y=-150)# IMPORTANT

    if posX>216:
        w=3

    print(posX,posY)
    for i in range(len(monde)):#79,43 ,79,44 ,79,45 ,79,46
        for j in range(len(monde[i])):
            if blobby.HP>0:
                canevas.create_image(blobby.posactuellex*16,blobby.posactuelley*16,anchor=NW,image=photoblob)
            if blobby1.HP>0:
                canevas.create_image(blobby1.posactuellex*16,blobby1.posactuelley*16,anchor=NW,image=photoblob)
            if blobby2.HP>0:
                canevas.create_image(blobby2.posactuellex*16,blobby2.posactuelley*16,anchor=NW,image=photoblob)
            if blobby3.HP>0:
                canevas.create_image(blobby3.posactuellex*16,blobby3.posactuelley*16,anchor=NW,image=photoblob2)
            if blobby4.HP>0:
                canevas.create_image(blobby4.posactuellex*16,blobby4.posactuelley*16,anchor=NW,image=photoblob2)
            if blobby5.HP>0:
                canevas.create_image(blobby5.posactuellex*16,blobby5.posactuelley*16,anchor=NW,image=photoblob2)
            if blobby6.HP>0:
                canevas.create_image(blobby6.posactuellex*16,blobby6.posactuelley*16,anchor=NW,image=photoblob4)
            if blobby7.HP>0:
                canevas.create_image(blobby7.posactuellex*16,blobby7.posactuelley*16,anchor=NW,image=photoblob1)
            if blobby8.HP>0:
                canevas.create_image(blobby8.posactuellex*16,blobby8.posactuelley*16,anchor=NW,image=photoblob1)
            if blobby9.HP>0:
                canevas.create_image(blobby9.posactuellex*16,blobby9.posactuelley*16,anchor=NW,image=photoblob4)
            if blobby10.HP>0:
                canevas.create_image(blobby10.posactuellex*16,blobby10.posactuelley*16,anchor=NW,image=photoblob3)
            if blobby11.HP>0:
                canevas.create_image(blobby11.posactuellex*16,blobby11.posactuelley*16,anchor=NW,image=photoblob3)
            if blobby12.HP>0:
                canevas.create_image(blobby12.posactuellex*16,blobby12.posactuelley*16,anchor=NW,image=photoblob5)
            if blobby13.HP>0:
                canevas.create_image(blobby13.posactuellex*16,blobby13.posactuelley*16,anchor=NW,image=photoblob5)
            if blobby14.HP>0:
                canevas.create_image(blobby14.posactuellex*16,blobby14.posactuelley*16,anchor=NW,image=photoblob5)
            if blobby15.HP>0:
                canevas.create_image(blobby15.posactuellex*16,blobby15.posactuelley*16,anchor=NW,image=photoblob2)
            if Kylian.HP>0:
                canevas.create_image(Kylian.posactuellex*16,Kylian.posactuelley*16,anchor=NW,image=phototroll)
            if perso==3:
                canevas.create_image(posX*16,posY*16,anchor=NW,image=photomagesf)
            elif perso==1:
                canevas.create_image(posX*16,posY*16,anchor=NW,image=photoosa)
            elif perso==2:
                canevas.create_image(posX*16,posY*16,anchor=NW,image=photoiop)
            if (monde[i][j])=='0':#eau
                canevas.create_image(i*16,j*16,anchor=NW,image=photowater)
            elif (monde[i][j])=='1':#sol de maison
                canevas.create_image(i*16,j*16,anchor=NW,image=photosol)
            elif (monde[i][j])=='2':#pont
                canevas.create_image(i*16,j*16,anchor=NW,image=photopont)
            elif (monde[i][j])=='3':#herbe
                canevas.create_image(i*16,j*16,anchor=NW,image=photograss)
            elif (monde[i][j])=='4':#sable
                canevas.create_image(i*16,j*16,anchor=NW,image=photosand)
            elif (monde[i][j])=='5':#mur
                canevas.create_image(i*16,j*16,anchor=NW,image=photomur)
            elif (monde[i][j])=='6':#caillou
                canevas.create_image(i*16,j*16,anchor=NW,image=photocaillou)
            elif (monde[i][j])=='7':#arbrebasgauche
                canevas.create_image(i*16,j*16,anchor=NW,image=phototree7)
            elif (monde[i][j])=='A':#arbrebasdroite
                canevas.create_image(i*16,j*16,anchor=NW,image=phototreeA)
            elif (monde[i][j])=='8':#arbrehautgauche
                canevas.create_image(i*16,j*16,anchor=NW,image=phototree8)
            elif (monde[i][j])=='9':#arbrehautdroite
                canevas.create_image(i*16,j*16,anchor=NW,image=phototree9)
            elif (monde[i][j])=='P':#porte
                canevas.create_image(i*16,j*16,anchor=NW,image=photodoor)
            elif (monde[i][j])=='M':#pantin
                canevas.create_image(i*16,j*16,anchor=NW,image=photopantin)
            elif (monde[i][j])=='N':#pantinchamp
                canevas.create_image(i*16,j*16,anchor=NW,image=photopantinchamp)
            elif (monde[i][j])=='F':#champ
                canevas.create_image(i*16,j*16,anchor=NW,image=photochamp)
            elif (monde[i][j])=='R':#chemin
                canevas.create_image(i*16,j*16,anchor=NW,image=photoroad)
            elif (monde[i][j])=='T':#torche
                canevas.create_image(i*16,j*16,anchor=NW,image=phototorche)
            elif (monde[i][j])=='Z':#panneau
                canevas.create_image(i*16,j*16,anchor=NW,image=photopanneau)
            elif (monde[i][j])=='K':#panneau2
                canevas.create_image(i*16,j*16,anchor=NW,image=photopanneau2)


def deplacement(event):
        global posX, posY, w, attaque
        touche = event.keysym
        if touche == "m":
            canevas.delete(ALL)
            casefullmap(monde)

        if touche == "Up":
            attaque=0
            posY -=1
            canevas.delete(ALL)
            if monde[posX][posY]=='0' or monde[posX][posY]=='M' or monde[posX][posY]=='N' or monde[posX][posY]=='5' or monde[posX][posY]=='6' or monde[posX][posY]=='A' or monde[posX][posY]=='7' or monde[posX][posY]=='8' or monde[posX][posY]=='9' or monde[posX][posY]=='T' or monde[posX][posY]=='Z' or monde[posX][posY]=='K':
                if monde[posX][posY]=='Z' and w==1 or monde[posX][posY]=='Z' and w==2:
                    showinfo("Panneau", "# Bienvenue dans BLOB Quest, le principe est simple, nettoyer le monde des villains bloby ! Pour y arriver vous aurez plusieurs touches : les flèches pour les déplacements, s pour sauvegarder, i pour voir ses stats, a pour attaquer, m pour afficher la carte en entière(non recommandé pour le gameplay et peut entraîner un léger crash). Le jeu se divise en 3 cartes où les monstres deviendront de plus en plus fort, dans l'ordre des monstres du plus faible au plus puissant : bleu,orange,violet,jaune,vert,métal,??? . Les gains d'expérience sont fixés à : zone 1 : 5 / zone 2 : 4 / zone 3 : 3. Le système de combat se repose sur un système de temps réel donc à chaque déplacement ou action les ennemis bougeront aussi et vous attaqueront si ils arrivent à atteindre votre case(corps à corps) , Bonne chance et Bon voyage (:")
                if monde[posX][posY]=='K' and w==2:
                    showinfo("Panneau", "Intentional game design :)")
                if monde[posX][posY]=='K' and w==3:
                    showinfo("Panneau", "Danger, ne pas aller plus loin.")
                if monde[posX][posY]=='Z' and w==3:
                    showinfo("Panneau", "t'as nettoyé les blobs Gg wp.")
                    world_map.destroy()
                posY+=1
            blobby.__deplacement__()
            blobby1.__deplacement__()
            blobby2.__deplacement__()
            blobby3.__deplacement__()
            blobby4.__deplacement__()
            blobby5.__deplacement__()
            blobby6.__deplacement__()
            blobby7.__deplacement__()
            blobby8.__deplacement__()
            blobby9.__deplacement__()
            blobby10.__deplacement__()
            blobby11.__deplacement__()
            blobby12.__deplacement__()
            blobby13.__deplacement__()
            blobby14.__deplacement__()
            blobby15.__deplacement__()
            Kylian.__deplacement__()
            if joueur==1:
                    if blobby.posactuellex==posX and blobby.posactuelley==posY and blobby.HP>0:
                        blobby.__degatsinfliges__(JL)
                    if blobby1.posactuellex==posX and blobby1.posactuelley==posY and blobby1.HP>0:
                        blobby1.__degatsinfliges__(JL)
                    if blobby2.posactuellex==posX and blobby2.posactuelley==posY and blobby2.HP>0:
                        blobby2.__degatsinfliges__(JL)
                    if blobby3.posactuellex==posX and blobby3.posactuelley==posY and blobby3.HP>0:
                        blobby3.__degatsinfliges__(JL)
                    if blobby4.posactuellex==posX and blobby4.posactuelley==posY and blobby4.HP>0:
                        blobby4.__degatsinfliges__(JL)
                    if blobby5.posactuellex==posX and blobby5.posactuelley==posY and blobby5.HP>0:
                        blobby5.__degatsinfliges__(JL)
                    if blobby6.posactuellex==posX and blobby6.posactuelley==posY and blobby6.HP>0:
                        blobby6.__degatsinfliges__(JL)
                    if blobby7.posactuellex==posX and blobby7.posactuelley==posY and blobby7.HP>0:
                        blobby7.__degatsinfliges__(JL)
                    if blobby8.posactuellex==posX and blobby8.posactuelley==posY and blobby8.HP>0:
                        blobby8.__degatsinfliges__(JL)
                    if blobby9.posactuellex==posX and blobby9.posactuelley==posY and blobby9.HP>0:
                        blobby9.__degatsinfliges__(JL)
                    if blobby10.posactuellex==posX and blobby10.posactuelley==posY and blobby10.HP>0:
                        blobby10.__degatsinfliges__(JL)
                    if blobby11.posactuellex==posX and blobby11.posactuelley==posY and blobby11.HP>0:
                        blobby11.__degatsinfliges__(JL)
                    if blobby12.posactuellex==posX and blobby12.posactuelley==posY and blobby12.HP>0:
                        blobby12.__degatsinfliges__(JL)
                    if blobby13.posactuellex==posX and blobby13.posactuelley==posY and blobby13.HP>0:
                        blobby13.__degatsinfliges__(JL)
                    if blobby14.posactuellex==posX and blobby14.posactuelley==posY and blobby14.HP>0:
                        blobby14.__degatsinfliges__(JL)
                    if blobby15.posactuellex==posX and blobby15.posactuelley==posY and blobby15.HP>0:
                        blobby15.__degatsinfliges__(JL)
                    if Kylian.posactuellex==posX and Kylian.posactuelley==posY and Kylian.HP>0:
                        Kylian.__degatsinfliges__(JL)
                    if JL.HP<=0:
                        showwarning("", "Vous avez perdu !")
                        world_map.destroy()
            elif joueur==2:
                    if blobby.posactuellex==posX and blobby.posactuelley==posY and blobby.HP>0:
                        blobby.__degatsinfliges__(JP)
                    if blobby1.posactuellex==posX and blobby1.posactuelley==posY and blobby1.HP>0:
                        blobby1.__degatsinfliges__(JP)
                    if blobby2.posactuellex==posX and blobby2.posactuelley==posY and blobby2.HP>0:
                        blobby2.__degatsinfliges__(JP)
                    if blobby3.posactuellex==posX and blobby3.posactuelley==posY and blobby3.HP>0:
                        blobby3.__degatsinfliges__(JP)
                    if blobby4.posactuellex==posX and blobby4.posactuelley==posY and blobby4.HP>0:
                        blobby4.__degatsinfliges__(JP)
                    if blobby5.posactuellex==posX and blobby5.posactuelley==posY and blobby5.HP>0:
                        blobby5.__degatsinfliges__(JP)
                    if blobby6.posactuellex==posX and blobby6.posactuelley==posY and blobby6.HP>0:
                        blobby6.__degatsinfliges__(JP)
                    if blobby7.posactuellex==posX and blobby7.posactuelley==posY and blobby7.HP>0:
                        blobby7.__degatsinfliges__(JP)
                    if blobby8.posactuellex==posX and blobby8.posactuelley==posY and blobby8.HP>0:
                        blobby8.__degatsinfliges__(JP)
                    if blobby9.posactuellex==posX and blobby9.posactuelley==posY and blobby9.HP>0:
                        blobby9.__degatsinfliges__(JP)
                    if blobby10.posactuellex==posX and blobby10.posactuelley==posY and blobby10.HP>0:
                        blobby10.__degatsinfliges__(JP)
                    if blobby11.posactuellex==posX and blobby11.posactuelley==posY and blobby11.HP>0:
                        blobby11.__degatsinfliges__(JP)
                    if blobby12.posactuellex==posX and blobby12.posactuelley==posY and blobby12.HP>0:
                        blobby12.__degatsinfliges__(JP)
                    if blobby13.posactuellex==posX and blobby13.posactuelley==posY and blobby13.HP>0:
                        blobby13.__degatsinfliges__(JP)
                    if blobby14.posactuellex==posX and blobby14.posactuelley==posY and blobby14.HP>0:
                        blobby14.__degatsinfliges__(JP)
                    if blobby15.posactuellex==posX and blobby15.posactuelley==posY and blobby15.HP>0:
                        blobby15.__degatsinfliges__(JP)
                    if Kylian.posactuellex==posX and Kylian.posactuelley==posY and Kylian.HP>0:
                        Kylian.__degatsinfliges__(JP)
                    if JP.HP<=0:
                        showwarning("", "Vous avez perdu !")
                        world_map.destroy()
            else:
                    if blobby.posactuellex==posX and blobby.posactuelley==posY and blobby.HP>0:
                        blobby.__degatsinfliges__(JK)
                    if blobby1.posactuellex==posX and blobby1.posactuelley==posY and blobby1.HP>0:
                        blobby1.__degatsinfliges__(JK)
                    if blobby2.posactuellex==posX and blobby2.posactuelley==posY and blobby2.HP>0:
                        blobby2.__degatsinfliges__(JK)
                    if blobby3.posactuellex==posX and blobby3.posactuelley==posY and blobby3.HP>0:
                        blobby3.__degatsinfliges__(JK)
                    if blobby4.posactuellex==posX and blobby4.posactuelley==posY and blobby4.HP>0:
                        blobby4.__degatsinfliges__(JK)
                    if blobby5.posactuellex==posX and blobby5.posactuelley==posY and blobby5.HP>0:
                        blobby5.__degatsinfliges__(JK)
                    if blobby6.posactuellex==posX and blobby6.posactuelley==posY and blobby6.HP>0:
                        blobby6.__degatsinfliges__(JK)
                    if blobby7.posactuellex==posX and blobby7.posactuelley==posY and blobby7.HP>0:
                        blobby7.__degatsinfliges__(JK)
                    if blobby8.posactuellex==posX and blobby8.posactuelley==posY and blobby8.HP>0:
                        blobby8.__degatsinfliges__(JK)
                    if blobby9.posactuellex==posX and blobby9.posactuelley==posY and blobby9.HP>0:
                        blobby9.__degatsinfliges__(JK)
                    if blobby10.posactuellex==posX and blobby10.posactuelley==posY and blobby10.HP>0:
                        blobby10.__degatsinfliges__(JK)
                    if blobby11.posactuellex==posX and blobby11.posactuelley==posY and blobby11.HP>0:
                        blobby11.__degatsinfliges__(JK)
                    if blobby12.posactuellex==posX and blobby12.posactuelley==posY and blobby12.HP>0:
                        blobby12.__degatsinfliges__(JK)
                    if blobby13.posactuellex==posX and blobby13.posactuelley==posY and blobby13.HP>0:
                        blobby13.__degatsinfliges__(JK)
                    if blobby14.posactuellex==posX and blobby14.posactuelley==posY and blobby14.HP>0:
                        blobby14.__degatsinfliges__(JK)
                    if blobby15.posactuellex==posX and blobby15.posactuelley==posY and blobby15.HP>0:
                        blobby15.__degatsinfliges__(JK)
                    if Kylian.posactuellex==posX and Kylian.posactuelley==posY and Kylian.HP>0:
                        Kylian.__degatsinfliges__(JK)
                    if JK.HP<=0:
                        showwarning("", "Vous avez perdu !")
                        world_map.destroy()
            case(monde)


        elif touche == "Down":
            attaque=0
            posY +=1
            canevas.delete(ALL)
            if monde[posX][posY]=='0' or monde[posX][posY]=='M' or monde[posX][posY]=='N' or monde[posX][posY]=='5' or monde[posX][posY]=='6' or monde[posX][posY]=='A' or monde[posX][posY]=='7' or monde[posX][posY]=='8' or monde[posX][posY]=='9' or monde[posX][posY]=='T' or monde[posX][posY]=='Z' or monde[posX][posY]=='K':
                if monde[posX][posY]=='Z' and w==1 or monde[posX][posY]=='Z' and w==2:
                    showinfo("Panneau", "# Bienvenue dans BLOB Quest, le principe est simple, nettoyer le monde des villains bloby ! Pour y arriver vous aurez plusieurs touches : les flèches pour les déplacements, s pour sauvegarder, i pour voir ses stats, a pour attaquer, m pour afficher la carte en entière(non recommandé pour le gameplay et peut entraîner un léger crash). Le jeu se divise en 3 cartes où les monstres deviendront de plus en plus fort, dans l'ordre des monstres du plus faible au plus puissant : bleu,orange,violet,jaune,vert,métal,??? . Les gains d'expérience sont fixés à : zone 1 : 5 / zone 2 : 4 / zone 3 : 3. Le système de combat se repose sur un système de temps réel donc à chaque déplacement ou action les ennemis bougeront aussi et vous attaqueront si ils arrivent à atteindre votre case(corps à corps) , Bonne chance et Bon voyage (:")
                if monde[posX][posY]=='K' and w==2:
                    showinfo("Panneau", "Intentional game design :)")
                if monde[posX][posY]=='K' and w==3:
                    showinfo("Panneau", "Danger, ne pas aller plus loin.")
                if monde[posX][posY]=='Z' and w==3:
                    showinfo("Panneau", "t'as nettoyé les blobs Gg wp.")
                    world_map.destroy()
                posY-=1
            blobby.__deplacement__()
            blobby1.__deplacement__()
            blobby2.__deplacement__()
            blobby3.__deplacement__()
            blobby4.__deplacement__()
            blobby5.__deplacement__()
            blobby6.__deplacement__()
            blobby7.__deplacement__()
            blobby8.__deplacement__()
            blobby9.__deplacement__()
            blobby10.__deplacement__()
            blobby11.__deplacement__()
            blobby12.__deplacement__()
            blobby13.__deplacement__()
            blobby14.__deplacement__()
            blobby15.__deplacement__()
            Kylian.__deplacement__()
            if joueur==1:
                    if blobby.posactuellex==posX and blobby.posactuelley==posY and blobby.HP>0:
                        blobby.__degatsinfliges__(JL)
                    if blobby1.posactuellex==posX and blobby1.posactuelley==posY and blobby1.HP>0:
                        blobby1.__degatsinfliges__(JL)
                    if blobby2.posactuellex==posX and blobby2.posactuelley==posY and blobby2.HP>0:
                        blobby2.__degatsinfliges__(JL)
                    if blobby3.posactuellex==posX and blobby3.posactuelley==posY and blobby3.HP>0:
                        blobby3.__degatsinfliges__(JL)
                    if blobby4.posactuellex==posX and blobby4.posactuelley==posY and blobby4.HP>0:
                        blobby4.__degatsinfliges__(JL)
                    if blobby5.posactuellex==posX and blobby5.posactuelley==posY and blobby5.HP>0:
                        blobby5.__degatsinfliges__(JL)
                    if blobby6.posactuellex==posX and blobby6.posactuelley==posY and blobby6.HP>0:
                        blobby6.__degatsinfliges__(JL)
                    if blobby7.posactuellex==posX and blobby7.posactuelley==posY and blobby7.HP>0:
                        blobby7.__degatsinfliges__(JL)
                    if blobby8.posactuellex==posX and blobby8.posactuelley==posY and blobby8.HP>0:
                        blobby8.__degatsinfliges__(JL)
                    if blobby9.posactuellex==posX and blobby9.posactuelley==posY and blobby9.HP>0:
                        blobby9.__degatsinfliges__(JL)
                    if blobby10.posactuellex==posX and blobby10.posactuelley==posY and blobby10.HP>0:
                        blobby10.__degatsinfliges__(JL)
                    if blobby11.posactuellex==posX and blobby11.posactuelley==posY and blobby11.HP>0:
                        blobby11.__degatsinfliges__(JL)
                    if blobby12.posactuellex==posX and blobby12.posactuelley==posY and blobby12.HP>0:
                        blobby12.__degatsinfliges__(JL)
                    if blobby13.posactuellex==posX and blobby13.posactuelley==posY and blobby13.HP>0:
                        blobby13.__degatsinfliges__(JL)
                    if blobby14.posactuellex==posX and blobby14.posactuelley==posY and blobby14.HP>0:
                        blobby14.__degatsinfliges__(JL)
                    if blobby15.posactuellex==posX and blobby15.posactuelley==posY and blobby15.HP>0:
                        blobby15.__degatsinfliges__(JL)
                    if Kylian.posactuellex==posX and Kylian.posactuelley==posY and Kylian.HP>0:
                        Kylian.__degatsinfliges__(JL)
                    if JL.HP<=0:
                        showwarning("", "Vous avez perdu !")
                        world_map.destroy()
            elif joueur==2:
                    if blobby.posactuellex==posX and blobby.posactuelley==posY and blobby.HP>0:
                        blobby.__degatsinfliges__(JP)
                    if blobby1.posactuellex==posX and blobby1.posactuelley==posY and blobby1.HP>0:
                        blobby1.__degatsinfliges__(JP)
                    if blobby2.posactuellex==posX and blobby2.posactuelley==posY and blobby2.HP>0:
                        blobby2.__degatsinfliges__(JP)
                    if blobby3.posactuellex==posX and blobby3.posactuelley==posY and blobby3.HP>0:
                        blobby3.__degatsinfliges__(JP)
                    if blobby4.posactuellex==posX and blobby4.posactuelley==posY and blobby4.HP>0:
                        blobby4.__degatsinfliges__(JP)
                    if blobby5.posactuellex==posX and blobby5.posactuelley==posY and blobby5.HP>0:
                        blobby5.__degatsinfliges__(JP)
                    if blobby6.posactuellex==posX and blobby6.posactuelley==posY and blobby6.HP>0:
                        blobby6.__degatsinfliges__(JP)
                    if blobby7.posactuellex==posX and blobby7.posactuelley==posY and blobby7.HP>0:
                        blobby7.__degatsinfliges__(JP)
                    if blobby8.posactuellex==posX and blobby8.posactuelley==posY and blobby8.HP>0:
                        blobby8.__degatsinfliges__(JP)
                    if blobby9.posactuellex==posX and blobby9.posactuelley==posY and blobby9.HP>0:
                        blobby9.__degatsinfliges__(JP)
                    if blobby10.posactuellex==posX and blobby10.posactuelley==posY and blobby10.HP>0:
                        blobby10.__degatsinfliges__(JP)
                    if blobby11.posactuellex==posX and blobby11.posactuelley==posY and blobby11.HP>0:
                        blobby11.__degatsinfliges__(JP)
                    if blobby12.posactuellex==posX and blobby12.posactuelley==posY and blobby12.HP>0:
                        blobby12.__degatsinfliges__(JP)
                    if blobby13.posactuellex==posX and blobby13.posactuelley==posY and blobby13.HP>0:
                        blobby13.__degatsinfliges__(JP)
                    if blobby14.posactuellex==posX and blobby14.posactuelley==posY and blobby14.HP>0:
                        blobby14.__degatsinfliges__(JP)
                    if blobby15.posactuellex==posX and blobby15.posactuelley==posY and blobby15.HP>0:
                        blobby15.__degatsinfliges__(JP)
                    if Kylian.posactuellex==posX and Kylian.posactuelley==posY and Kylian.HP>0:
                        Kylian.__degatsinfliges__(JP)
                    if JP.HP<=0:
                        showwarning("", "Vous avez perdu !")
                        world_map.destroy()
            else:
                    if blobby.posactuellex==posX and blobby.posactuelley==posY and blobby.HP>0:
                        blobby.__degatsinfliges__(JK)
                    if blobby1.posactuellex==posX and blobby1.posactuelley==posY and blobby1.HP>0:
                        blobby1.__degatsinfliges__(JK)
                    if blobby2.posactuellex==posX and blobby2.posactuelley==posY and blobby2.HP>0:
                        blobby2.__degatsinfliges__(JK)
                    if blobby3.posactuellex==posX and blobby3.posactuelley==posY and blobby3.HP>0:
                        blobby3.__degatsinfliges__(JK)
                    if blobby4.posactuellex==posX and blobby4.posactuelley==posY and blobby4.HP>0:
                        blobby4.__degatsinfliges__(JK)
                    if blobby5.posactuellex==posX and blobby5.posactuelley==posY and blobby5.HP>0:
                        blobby5.__degatsinfliges__(JK)
                    if blobby6.posactuellex==posX and blobby6.posactuelley==posY and blobby6.HP>0:
                        blobby6.__degatsinfliges__(JK)
                    if blobby7.posactuellex==posX and blobby7.posactuelley==posY and blobby7.HP>0:
                        blobby7.__degatsinfliges__(JK)
                    if blobby8.posactuellex==posX and blobby8.posactuelley==posY and blobby8.HP>0:
                        blobby8.__degatsinfliges__(JK)
                    if blobby9.posactuellex==posX and blobby9.posactuelley==posY and blobby9.HP>0:
                        blobby9.__degatsinfliges__(JK)
                    if blobby10.posactuellex==posX and blobby10.posactuelley==posY and blobby10.HP>0:
                        blobby10.__degatsinfliges__(JK)
                    if blobby11.posactuellex==posX and blobby11.posactuelley==posY and blobby11.HP>0:
                        blobby11.__degatsinfliges__(JK)
                    if blobby12.posactuellex==posX and blobby12.posactuelley==posY and blobby12.HP>0:
                        blobby12.__degatsinfliges__(JK)
                    if blobby13.posactuellex==posX and blobby13.posactuelley==posY and blobby13.HP>0:
                        blobby13.__degatsinfliges__(JK)
                    if blobby14.posactuellex==posX and blobby14.posactuelley==posY and blobby14.HP>0:
                        blobby14.__degatsinfliges__(JK)
                    if blobby15.posactuellex==posX and blobby15.posactuelley==posY and blobby15.HP>0:
                        blobby15.__degatsinfliges__(JK)
                    if Kylian.posactuellex==posX and Kylian.posactuelley==posY and Kylian.HP>0:
                        Kylian.__degatsinfliges__(JK)
                    if JK.HP<=0:
                        showwarning("", "Vous avez perdu !")
                        world_map.destroy()
            case(monde)
        elif touche == "Right":
            attaque=0
            posX +=1
            canevas.delete(ALL)
            if monde[posX][posY]=='0' or monde[posX][posY]=='M' or monde[posX][posY]=='N' or monde[posX][posY]=='5' or monde[posX][posY]=='6' or monde[posX][posY]=='A' or monde[posX][posY]=='7' or monde[posX][posY]=='8' or monde[posX][posY]=='9' or monde[posX][posY]=='T' or monde[posX][posY]=='Z' or monde[posX][posY]=='K':
                if monde[posX][posY]=='Z' and w==1 or monde[posX][posY]=='Z' and w==2:
                    showinfo("Panneau", "# Bienvenue dans BLOB Quest, le principe est simple, nettoyer le monde des villains bloby ! Pour y arriver vous aurez plusieurs touches : les flèches pour les déplacements, s pour sauvegarder, i pour voir ses stats, a pour attaquer, m pour afficher la carte en entière(non recommandé pour le gameplay et peut entraîner un léger crash). Le jeu se divise en 3 cartes où les monstres deviendront de plus en plus fort, dans l'ordre des monstres du plus faible au plus puissant : bleu,orange,violet,jaune,vert,métal,??? . Les gains d'expérience sont fixés à : zone 1 : 5 / zone 2 : 4 / zone 3 : 3. Le système de combat se repose sur un système de temps réel donc à chaque déplacement ou action les ennemis bougeront aussi et vous attaqueront si ils arrivent à atteindre votre case(corps à corps) , Bonne chance et Bon voyage (:")
                if monde[posX][posY]=='K' and w==2:
                    showinfo("Panneau", "Intentional game design :)")
                if monde[posX][posY]=='K' and w==3:
                    showinfo("Panneau", "Danger, ne pas aller plus loin.")
                if monde[posX][posY]=='Z' and w==3:
                    showinfo("Panneau", "t'as nettoyé les blobs Gg wp.")
                    world_map.destroy()
                posX-=1
            blobby.__deplacement__()
            blobby1.__deplacement__()
            blobby2.__deplacement__()
            blobby3.__deplacement__()
            blobby4.__deplacement__()
            blobby5.__deplacement__()
            blobby6.__deplacement__()
            blobby7.__deplacement__()
            blobby8.__deplacement__()
            blobby9.__deplacement__()
            blobby10.__deplacement__()
            blobby11.__deplacement__()
            blobby12.__deplacement__()
            blobby13.__deplacement__()
            blobby14.__deplacement__()
            blobby15.__deplacement__()
            Kylian.__deplacement__()
            if joueur==1:
                    if blobby.posactuellex==posX and blobby.posactuelley==posY and blobby.HP>0:
                        blobby.__degatsinfliges__(JL)
                    if blobby1.posactuellex==posX and blobby1.posactuelley==posY and blobby1.HP>0:
                        blobby1.__degatsinfliges__(JL)
                    if blobby2.posactuellex==posX and blobby2.posactuelley==posY and blobby2.HP>0:
                        blobby2.__degatsinfliges__(JL)
                    if blobby3.posactuellex==posX and blobby3.posactuelley==posY and blobby3.HP>0:
                        blobby3.__degatsinfliges__(JL)
                    if blobby4.posactuellex==posX and blobby4.posactuelley==posY and blobby4.HP>0:
                        blobby4.__degatsinfliges__(JL)
                    if blobby5.posactuellex==posX and blobby5.posactuelley==posY and blobby5.HP>0:
                        blobby5.__degatsinfliges__(JL)
                    if blobby6.posactuellex==posX and blobby6.posactuelley==posY and blobby6.HP>0:
                        blobby6.__degatsinfliges__(JL)
                    if blobby7.posactuellex==posX and blobby7.posactuelley==posY and blobby7.HP>0:
                        blobby7.__degatsinfliges__(JL)
                    if blobby8.posactuellex==posX and blobby8.posactuelley==posY and blobby8.HP>0:
                        blobby8.__degatsinfliges__(JL)
                    if blobby9.posactuellex==posX and blobby9.posactuelley==posY and blobby9.HP>0:
                        blobby9.__degatsinfliges__(JL)
                    if blobby10.posactuellex==posX and blobby10.posactuelley==posY and blobby10.HP>0:
                        blobby10.__degatsinfliges__(JL)
                    if blobby11.posactuellex==posX and blobby11.posactuelley==posY and blobby11.HP>0:
                        blobby11.__degatsinfliges__(JL)
                    if blobby12.posactuellex==posX and blobby12.posactuelley==posY and blobby12.HP>0:
                        blobby12.__degatsinfliges__(JL)
                    if blobby13.posactuellex==posX and blobby13.posactuelley==posY and blobby13.HP>0:
                        blobby13.__degatsinfliges__(JL)
                    if blobby14.posactuellex==posX and blobby14.posactuelley==posY and blobby14.HP>0:
                        blobby14.__degatsinfliges__(JL)
                    if blobby15.posactuellex==posX and blobby15.posactuelley==posY and blobby15.HP>0:
                        blobby15.__degatsinfliges__(JL)
                    if Kylian.posactuellex==posX and Kylian.posactuelley==posY and Kylian.HP>0:
                        Kylian.__degatsinfliges__(JL)
                    if JL.HP<=0:
                        showwarning("", "Vous avez perdu !")
                        world_map.destroy()
            elif joueur==2:
                    if blobby.posactuellex==posX and blobby.posactuelley==posY and blobby.HP>0:
                        blobby.__degatsinfliges__(JP)
                    if blobby1.posactuellex==posX and blobby1.posactuelley==posY and blobby1.HP>0:
                        blobby1.__degatsinfliges__(JP)
                    if blobby2.posactuellex==posX and blobby2.posactuelley==posY and blobby2.HP>0:
                        blobby2.__degatsinfliges__(JP)
                    if blobby3.posactuellex==posX and blobby3.posactuelley==posY and blobby3.HP>0:
                        blobby3.__degatsinfliges__(JP)
                    if blobby4.posactuellex==posX and blobby4.posactuelley==posY and blobby4.HP>0:
                        blobby4.__degatsinfliges__(JP)
                    if blobby5.posactuellex==posX and blobby5.posactuelley==posY and blobby5.HP>0:
                        blobby5.__degatsinfliges__(JP)
                    if blobby6.posactuellex==posX and blobby6.posactuelley==posY and blobby6.HP>0:
                        blobby6.__degatsinfliges__(JP)
                    if blobby7.posactuellex==posX and blobby7.posactuelley==posY and blobby7.HP>0:
                        blobby7.__degatsinfliges__(JP)
                    if blobby8.posactuellex==posX and blobby8.posactuelley==posY and blobby8.HP>0:
                        blobby8.__degatsinfliges__(JP)
                    if blobby9.posactuellex==posX and blobby9.posactuelley==posY and blobby9.HP>0:
                        blobby9.__degatsinfliges__(JP)
                    if blobby10.posactuellex==posX and blobby10.posactuelley==posY and blobby10.HP>0:
                        blobby10.__degatsinfliges__(JP)
                    if blobby11.posactuellex==posX and blobby11.posactuelley==posY and blobby11.HP>0:
                        blobby11.__degatsinfliges__(JP)
                    if blobby12.posactuellex==posX and blobby12.posactuelley==posY and blobby12.HP>0:
                        blobby12.__degatsinfliges__(JP)
                    if blobby13.posactuellex==posX and blobby13.posactuelley==posY and blobby13.HP>0:
                        blobby13.__degatsinfliges__(JP)
                    if blobby14.posactuellex==posX and blobby14.posactuelley==posY and blobby14.HP>0:
                        blobby14.__degatsinfliges__(JP)
                    if blobby15.posactuellex==posX and blobby15.posactuelley==posY and blobby15.HP>0:
                        blobby15.__degatsinfliges__(JP)
                    if Kylian.posactuellex==posX and Kylian.posactuelley==posY and Kylian.HP>0:
                        Kylian.__degatsinfliges__(JP)
                    if JP.HP<=0:
                        showwarning("", "Vous avez perdu !")
                        world_map.destroy()
            else:
                    if blobby.posactuellex==posX and blobby.posactuelley==posY and blobby.HP>0:
                        blobby.__degatsinfliges__(JK)
                    if blobby1.posactuellex==posX and blobby1.posactuelley==posY and blobby1.HP>0:
                        blobby1.__degatsinfliges__(JK)
                    if blobby2.posactuellex==posX and blobby2.posactuelley==posY and blobby2.HP>0:
                        blobby2.__degatsinfliges__(JK)
                    if blobby3.posactuellex==posX and blobby3.posactuelley==posY and blobby3.HP>0:
                        blobby3.__degatsinfliges__(JK)
                    if blobby4.posactuellex==posX and blobby4.posactuelley==posY and blobby4.HP>0:
                        blobby4.__degatsinfliges__(JK)
                    if blobby5.posactuellex==posX and blobby5.posactuelley==posY and blobby5.HP>0:
                        blobby5.__degatsinfliges__(JK)
                    if blobby6.posactuellex==posX and blobby6.posactuelley==posY and blobby6.HP>0:
                        blobby6.__degatsinfliges__(JK)
                    if blobby7.posactuellex==posX and blobby7.posactuelley==posY and blobby7.HP>0:
                        blobby7.__degatsinfliges__(JK)
                    if blobby8.posactuellex==posX and blobby8.posactuelley==posY and blobby8.HP>0:
                        blobby8.__degatsinfliges__(JK)
                    if blobby9.posactuellex==posX and blobby9.posactuelley==posY and blobby9.HP>0:
                        blobby9.__degatsinfliges__(JK)
                    if blobby10.posactuellex==posX and blobby10.posactuelley==posY and blobby10.HP>0:
                        blobby10.__degatsinfliges__(JK)
                    if blobby11.posactuellex==posX and blobby11.posactuelley==posY and blobby11.HP>0:
                        blobby11.__degatsinfliges__(JK)
                    if blobby12.posactuellex==posX and blobby12.posactuelley==posY and blobby12.HP>0:
                        blobby12.__degatsinfliges__(JK)
                    if blobby13.posactuellex==posX and blobby13.posactuelley==posY and blobby13.HP>0:
                        blobby13.__degatsinfliges__(JK)
                    if blobby14.posactuellex==posX and blobby14.posactuelley==posY and blobby14.HP>0:
                        blobby14.__degatsinfliges__(JK)
                    if blobby15.posactuellex==posX and blobby15.posactuelley==posY and blobby15.HP>0:
                        blobby15.__degatsinfliges__(JK)
                    if Kylian.posactuellex==posX and Kylian.posactuelley==posY and Kylian.HP>0:
                        Kylian.__degatsinfliges__(JK)
                    if JK.HP<=0:
                        showwarning("", "Vous avez perdu !")
                        world_map.destroy()
            case(monde)
        elif touche == "Left":
            attaque=0
            posX -=1
            canevas.delete(ALL)
            if monde[posX][posY]=='0' or monde[posX][posY]=='M' or monde[posX][posY]=='N' or monde[posX][posY]=='5' or monde[posX][posY]=='6' or monde[posX][posY]=='A' or monde[posX][posY]=='7' or monde[posX][posY]=='8' or monde[posX][posY]=='9' or monde[posX][posY]=='T' or monde[posX][posY]=='Z' or monde[posX][posY]=='K':
                if monde[posX][posY]=='Z' and w==1 or monde[posX][posY]=='Z' and w==2:
                    showinfo("Panneau", "# Bienvenue dans BLOB Quest, le principe est simple, nettoyer le monde des villains bloby ! Pour y arriver vous aurez plusieurs touches : les flèches pour les déplacements, s pour sauvegarder, i pour voir ses stats, a pour attaquer, m pour afficher la carte en entière(non recommandé pour le gameplay et peut entraîner un léger crash). Le jeu se divise en 3 cartes où les monstres deviendront de plus en plus fort, dans l'ordre des monstres du plus faible au plus puissant : bleu,orange,violet,jaune,vert,métal,??? . Les gains d'expérience sont fixés à : zone 1 : 5 / zone 2 : 4 / zone 3 : 3. Le système de combat se repose sur un système de temps réel donc à chaque déplacement ou action les ennemis bougeront aussi et vous attaqueront si ils arrivent à atteindre votre case(corps à corps) , Bonne chance et Bon voyage (:")
                if monde[posX][posY]=='K' and w==2:
                    showinfo("Panneau", "Intentional game design :)")
                if monde[posX][posY]=='K' and w==3:
                    showinfo("Panneau", "Danger, ne pas aller plus loin.")
                if monde[posX][posY]=='Z' and w==3:
                    showinfo("Panneau", "t'as nettoyé les blobs Gg wp.")
                    world_map.destroy()
                posX+=1
            blobby.__deplacement__()
            blobby1.__deplacement__()
            blobby2.__deplacement__()
            blobby3.__deplacement__()
            blobby4.__deplacement__()
            blobby5.__deplacement__()
            blobby6.__deplacement__()
            blobby7.__deplacement__()
            blobby8.__deplacement__()
            blobby9.__deplacement__()
            blobby10.__deplacement__()
            blobby11.__deplacement__()
            blobby12.__deplacement__()
            blobby13.__deplacement__()
            blobby14.__deplacement__()
            blobby15.__deplacement__()
            Kylian.__deplacement__()
            if joueur==1:
                    if blobby.posactuellex==posX and blobby.posactuelley==posY and blobby.HP>0:
                        blobby.__degatsinfliges__(JL)
                    if blobby1.posactuellex==posX and blobby1.posactuelley==posY and blobby1.HP>0:
                        blobby1.__degatsinfliges__(JL)
                    if blobby2.posactuellex==posX and blobby2.posactuelley==posY and blobby2.HP>0:
                        blobby2.__degatsinfliges__(JL)
                    if blobby3.posactuellex==posX and blobby3.posactuelley==posY and blobby3.HP>0:
                        blobby3.__degatsinfliges__(JL)
                    if blobby4.posactuellex==posX and blobby4.posactuelley==posY and blobby4.HP>0:
                        blobby4.__degatsinfliges__(JL)
                    if blobby5.posactuellex==posX and blobby5.posactuelley==posY and blobby5.HP>0:
                        blobby5.__degatsinfliges__(JL)
                    if blobby6.posactuellex==posX and blobby6.posactuelley==posY and blobby6.HP>0:
                        blobby6.__degatsinfliges__(JL)
                    if blobby7.posactuellex==posX and blobby7.posactuelley==posY and blobby7.HP>0:
                        blobby7.__degatsinfliges__(JL)
                    if blobby8.posactuellex==posX and blobby8.posactuelley==posY and blobby8.HP>0:
                        blobby8.__degatsinfliges__(JL)
                    if blobby9.posactuellex==posX and blobby9.posactuelley==posY and blobby9.HP>0:
                        blobby9.__degatsinfliges__(JL)
                    if blobby10.posactuellex==posX and blobby10.posactuelley==posY and blobby10.HP>0:
                        blobby10.__degatsinfliges__(JL)
                    if blobby11.posactuellex==posX and blobby11.posactuelley==posY and blobby11.HP>0:
                        blobby11.__degatsinfliges__(JL)
                    if blobby12.posactuellex==posX and blobby12.posactuelley==posY and blobby12.HP>0:
                        blobby12.__degatsinfliges__(JL)
                    if blobby13.posactuellex==posX and blobby13.posactuelley==posY and blobby13.HP>0:
                        blobby13.__degatsinfliges__(JL)
                    if blobby14.posactuellex==posX and blobby14.posactuelley==posY and blobby14.HP>0:
                        blobby14.__degatsinfliges__(JL)
                    if blobby15.posactuellex==posX and blobby15.posactuelley==posY and blobby15.HP>0:
                        blobby15.__degatsinfliges__(JL)
                    if Kylian.posactuellex==posX and Kylian.posactuelley==posY and Kylian.HP>0:
                        Kylian.__degatsinfliges__(JL)
                    if JL.HP<=0:
                        showwarning("", "Vous avez perdu !")
                        world_map.destroy()
            elif joueur==2:
                    if blobby.posactuellex==posX and blobby.posactuelley==posY and blobby.HP>0:
                        blobby.__degatsinfliges__(JP)
                    if blobby1.posactuellex==posX and blobby1.posactuelley==posY and blobby1.HP>0:
                        blobby1.__degatsinfliges__(JP)
                    if blobby2.posactuellex==posX and blobby2.posactuelley==posY and blobby2.HP>0:
                        blobby2.__degatsinfliges__(JP)
                    if blobby3.posactuellex==posX and blobby3.posactuelley==posY and blobby3.HP>0:
                        blobby3.__degatsinfliges__(JP)
                    if blobby4.posactuellex==posX and blobby4.posactuelley==posY and blobby4.HP>0:
                        blobby4.__degatsinfliges__(JP)
                    if blobby5.posactuellex==posX and blobby5.posactuelley==posY and blobby5.HP>0:
                        blobby5.__degatsinfliges__(JP)
                    if blobby6.posactuellex==posX and blobby6.posactuelley==posY and blobby6.HP>0:
                        blobby6.__degatsinfliges__(JP)
                    if blobby7.posactuellex==posX and blobby7.posactuelley==posY and blobby7.HP>0:
                        blobby7.__degatsinfliges__(JP)
                    if blobby8.posactuellex==posX and blobby8.posactuelley==posY and blobby8.HP>0:
                        blobby8.__degatsinfliges__(JP)
                    if blobby9.posactuellex==posX and blobby9.posactuelley==posY and blobby9.HP>0:
                        blobby9.__degatsinfliges__(JP)
                    if blobby10.posactuellex==posX and blobby10.posactuelley==posY and blobby10.HP>0:
                        blobby10.__degatsinfliges__(JP)
                    if blobby11.posactuellex==posX and blobby11.posactuelley==posY and blobby11.HP>0:
                        blobby11.__degatsinfliges__(JP)
                    if blobby12.posactuellex==posX and blobby12.posactuelley==posY and blobby12.HP>0:
                        blobby12.__degatsinfliges__(JP)
                    if blobby13.posactuellex==posX and blobby13.posactuelley==posY and blobby13.HP>0:
                        blobby13.__degatsinfliges__(JP)
                    if blobby14.posactuellex==posX and blobby14.posactuelley==posY and blobby14.HP>0:
                        blobby14.__degatsinfliges__(JP)
                    if blobby15.posactuellex==posX and blobby15.posactuelley==posY and blobby15.HP>0:
                        blobby15.__degatsinfliges__(JP)
                    if Kylian.posactuellex==posX and Kylian.posactuelley==posY and Kylian.HP>0:
                        Kylian.__degatsinfliges__(JP)
                    if JP.HP<=0:
                        showwarning("", "Vous avez perdu !")
                        world_map.destroy()
            else:
                    if blobby.posactuellex==posX and blobby.posactuelley==posY and blobby.HP>0:
                        blobby.__degatsinfliges__(JK)
                    if blobby1.posactuellex==posX and blobby1.posactuelley==posY and blobby1.HP>0:
                        blobby1.__degatsinfliges__(JK)
                    if blobby2.posactuellex==posX and blobby2.posactuelley==posY and blobby2.HP>0:
                        blobby2.__degatsinfliges__(JK)
                    if blobby3.posactuellex==posX and blobby3.posactuelley==posY and blobby3.HP>0:
                        blobby3.__degatsinfliges__(JK)
                    if blobby4.posactuellex==posX and blobby4.posactuelley==posY and blobby4.HP>0:
                        blobby4.__degatsinfliges__(JK)
                    if blobby5.posactuellex==posX and blobby5.posactuelley==posY and blobby5.HP>0:
                        blobby5.__degatsinfliges__(JK)
                    if blobby6.posactuellex==posX and blobby6.posactuelley==posY and blobby6.HP>0:
                        blobby6.__degatsinfliges__(JK)
                    if blobby7.posactuellex==posX and blobby7.posactuelley==posY and blobby7.HP>0:
                        blobby7.__degatsinfliges__(JK)
                    if blobby8.posactuellex==posX and blobby8.posactuelley==posY and blobby8.HP>0:
                        blobby8.__degatsinfliges__(JK)
                    if blobby9.posactuellex==posX and blobby9.posactuelley==posY and blobby9.HP>0:
                        blobby9.__degatsinfliges__(JK)
                    if blobby10.posactuellex==posX and blobby10.posactuelley==posY and blobby10.HP>0:
                        blobby10.__degatsinfliges__(JK)
                    if blobby11.posactuellex==posX and blobby11.posactuelley==posY and blobby11.HP>0:
                        blobby11.__degatsinfliges__(JK)
                    if blobby12.posactuellex==posX and blobby12.posactuelley==posY and blobby12.HP>0:
                        blobby12.__degatsinfliges__(JK)
                    if blobby13.posactuellex==posX and blobby13.posactuelley==posY and blobby13.HP>0:
                        blobby13.__degatsinfliges__(JK)
                    if blobby14.posactuellex==posX and blobby14.posactuelley==posY and blobby14.HP>0:
                        blobby14.__degatsinfliges__(JK)
                    if blobby15.posactuellex==posX and blobby15.posactuelley==posY and blobby15.HP>0:
                        blobby15.__degatsinfliges__(JK)
                    if Kylian.posactuellex==posX and Kylian.posactuelley==posY and Kylian.HP>0:
                        Kylian.__degatsinfliges__(JK)
                    if JK.HP<=0:
                        showwarning("", "Vous avez perdu !")
                        world_map.destroy()
            case(monde)

        elif touche == "s":
            if joueur==1:
                JL.__sauvegarde__()
            if joueur==2:
                JP.__sauvegarde__()
            if joueur==3:
                JK.__sauvegarde__()

        elif touche == "i":
            if joueur==1:
                showinfo("Statistiques", JL.__stats__() )
            elif joueur==2:
                showinfo("Statistiques", JP.__stats__() )
            else:
                showinfo("Statistiques", JK.__stats__() )
        elif touche == "a":
            if joueur ==1 and attaque==0:
                canevas.create_image((posX+1)*16,posY*16,anchor=NW,image=photoepee)
                canevas.create_image((posX+1)*16,(posY+1)*16,anchor=NW,image=photoepee)
                canevas.create_image(posX*16,(posY+1)*16,anchor=NW,image=photoepee)
                canevas.create_image((posX-1)*16,(posY+1)*16,anchor=NW,image=photoepee)
                canevas.create_image((posX-1)*16,posY*16,anchor=NW,image=photoepee)
                canevas.create_image((posX-1)*16,(posY-1)*16,anchor=NW,image=photoepee)
                canevas.create_image(posX*16,(posY-1)*16,anchor=NW,image=photoepee)
                canevas.create_image((posX+1)*16,(posY-1)*16,anchor=NW,image=photoepee)
                JL.__degatsinfliges__(blobby)
                JL.__degatsinfliges__(blobby1)
                JL.__degatsinfliges__(blobby2)
                JL.__degatsinfliges__(blobby3)
                JL.__degatsinfliges__(blobby4)
                JL.__degatsinfliges__(blobby5)
                JL.__degatsinfliges__(blobby6)
                JL.__degatsinfliges__(blobby7)
                JL.__degatsinfliges__(blobby8)
                JL.__degatsinfliges__(blobby9)
                JL.__degatsinfliges__(blobby10)
                JL.__degatsinfliges__(blobby11)
                JL.__degatsinfliges__(blobby12)
                JL.__degatsinfliges__(blobby13)
                JL.__degatsinfliges__(blobby14)
                JL.__degatsinfliges__(blobby15)
                JL.__degatsinfliges__(Kylian)
                attaque=1
            elif joueur==2 and attaque==0:
                canevas.create_image((posX+1)*16,posY*16,anchor=NW,image=photofeu)
                canevas.create_image((posX+1)*16,(posY+1)*16,anchor=NW,image=photofeu)
                canevas.create_image(posX*16,(posY+1)*16,anchor=NW,image=photofeu)
                canevas.create_image((posX-1)*16,(posY+1)*16,anchor=NW,image=photofeu)
                canevas.create_image((posX-1)*16,posY*16,anchor=NW,image=photofeu)
                canevas.create_image((posX-1)*16,(posY-1)*16,anchor=NW,image=photofeu)
                canevas.create_image(posX*16,(posY-1)*16,anchor=NW,image=photofeu)
                canevas.create_image((posX+1)*16,(posY-1)*16,anchor=NW,image=photofeu)
                JP.__degatsinfliges__(blobby)
                JP.__degatsinfliges__(blobby1)
                JP.__degatsinfliges__(blobby2)
                JP.__degatsinfliges__(blobby3)
                JP.__degatsinfliges__(blobby4)
                JP.__degatsinfliges__(blobby5)
                JP.__degatsinfliges__(blobby6)
                JP.__degatsinfliges__(blobby7)
                JP.__degatsinfliges__(blobby8)
                JP.__degatsinfliges__(blobby9)
                JP.__degatsinfliges__(blobby10)
                JP.__degatsinfliges__(blobby11)
                JP.__degatsinfliges__(blobby12)
                JP.__degatsinfliges__(blobby13)
                JP.__degatsinfliges__(blobby14)
                JP.__degatsinfliges__(blobby15)
                JP.__degatsinfliges__(Kylian)
                attaque=1
            elif joueur==3 and attaque==0:
                canevas.create_image((posX+1)*16,posY*16,anchor=NW,image=photolance)
                canevas.create_image((posX+1)*16,(posY+1)*16,anchor=NW,image=photolance)
                canevas.create_image(posX*16,(posY+1)*16,anchor=NW,image=photolance)
                canevas.create_image((posX-1)*16,(posY+1)*16,anchor=NW,image=photolance)
                canevas.create_image((posX-1)*16,posY*16,anchor=NW,image=photolance)
                canevas.create_image((posX-1)*16,(posY-1)*16,anchor=NW,image=photolance)
                canevas.create_image(posX*16,(posY-1)*16,anchor=NW,image=photolance)
                canevas.create_image((posX+1)*16,(posY-1)*16,anchor=NW,image=photolance)
                JK.__degatsinfliges__(blobby)
                JK.__degatsinfliges__(blobby1)
                JK.__degatsinfliges__(blobby2)
                JK.__degatsinfliges__(blobby3)
                JK.__degatsinfliges__(blobby4)
                JK.__degatsinfliges__(blobby5)
                JK.__degatsinfliges__(blobby6)
                JK.__degatsinfliges__(blobby7)
                JK.__degatsinfliges__(blobby8)
                JK.__degatsinfliges__(blobby9)
                JK.__degatsinfliges__(blobby10)
                JK.__degatsinfliges__(blobby11)
                JK.__degatsinfliges__(blobby12)
                JK.__degatsinfliges__(blobby13)
                JK.__degatsinfliges__(blobby14)
                JK.__degatsinfliges__(blobby15)
                JK.__degatsinfliges__(Kylian)
                attaque=1

        #time.sleep(0.25)


      ##
        ##




def jouer():
    canevas.focus_set()

canevas.bind("<Key>",deplacement)

jouer()
monde=création(ligne)

world_map.mainloop()
case(monde)

#Idée mettre peut etre le joueur directement dans le doc.txt de la map mais du coup modif case(monde) et déplacement avec a chaque touche une modif de la liste monde[i][j]
conn.close()
#pour lui faire plaisir