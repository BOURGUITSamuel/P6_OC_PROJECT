# coding: utf-8
import os

def cron_apt_config(var1):
    """Installation et configuration de cron-apt"""
    try:
      os.system("sudo apt-get -y install cron-apt")
      os.system("sudo grep security /etc/apt/sources.list > /etc/apt/security.sources.list")
      os.system("sudo cp "+var1["config"]+" "+var1["config"]+".bak")
      fichier = open(var1["config"], "a")
      fichier.write(var1["conf1"]+"\n")
      fichier.write(var1["conf2"]+"\n")
      fichier.write(var1["conf3"]+"\n")
      fichier.write(var1["conf4"]+"\n")
      fichier.close()
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
