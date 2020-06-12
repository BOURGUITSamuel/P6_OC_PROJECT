# coding: utf-8
import os

def admin_create(var1):
    """Création de compte utilisateur Linux"""
    try:
      os.system("sudo useradd -m "+var1["user"]+" -p "+var1["pwd"])
      os.system("sudo usermod -aG sudo "+var1["user"])
      os.system("sudo usermod -aG root "+var1["user"])
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
