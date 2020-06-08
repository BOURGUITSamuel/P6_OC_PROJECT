# coding: utf-8
import os

def logwatch_install(var1):
    """Installation et configuration de logwatch"""
    try:
      os.system("sudo apt-get -y install logwatch")
      os.system("sudo cp "+var1["confa"]+" "+var1["confb"])
      os.system("sudo cp "+var1["confb"]+" "+var1["confb"]+".bak")
      fin = open(var1["confb"], "rt")
      data = fin.read()
      data = data.replace('Format = text',var1["format"])
      data = data.replace('MailTo = root',var1["mailto"])
      data = data.replace('Detail = Low',var1["detail"])
      fin.close()
      fin = open(var1["confb"], "wt")
      fin.write(data)
      fin.close()
    except NameError:
        print('Une erreur de type "NameError" a été levée')
    except AttributeError:
        print('Une erreur de type "AttributeError" a été levée')
    except SyntaxError:
        print('Une erreur de type "SyntaxError" a été levée')
    except IOError:
        print('Une erreur de type "IOError" a été levée')
    except ImportError:
        print('Une erreur de type "ImportError" a été levée')
    except IndentationError:
        print('Une ereur de type "IndentationError" a été levée')
