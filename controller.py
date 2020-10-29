#!/usr/bin/python3

from model import Usuario
import vista
import cgi

def showAll():
       people_in_db = Usuario.getAll()
       #return view.showAllView(people_in_db)

def createUsr(cont,usuar):
       advice = Usuario.setUsr(usuar,cont)
       return advice

def consultDB(cont, usuar):
       request = Usuario.getUsr(usuar,cont)
       return request

def start():
        datos = cgi.FieldStorage()
        passw = format(datos.getvalue('pwd'))
        usern = format(datos.getvalue('email'))
        mssg = createUsr(passw,usern)
        vista.views(mssg, usern)

if __name__ == "__main__":
       start()
