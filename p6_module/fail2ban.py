# coding: utf-8
import os

def fail2ban_jail(var1):
    """Installation de fail2ban et configuration du fichier jail.local"""
    try:
      os.system("sudo apt-get -y install fail2ban")
      os.system("sudo cp "+var1["conf"]+" "+var1["local"])
      fin = open(var1["local"], "rt")
      data = fin.read()
      data = data.replace('bantime  = 10m',var1["band"])
      data = data.replace('findtime  = 10m',var1["find"] )
      data = data.replace('maxretry = 5',var1["max"])
      data = data.replace('destemail = root@localhost',var1["dest"])
      data = data.replace('sender = root@<fq-hostname>',var1["send"])
      fin.close()
      fin = open(var1["local"], "wt")
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
  
def fail2ban_default(var1):
    """Configuration du fichier defaults-debian.conf"""
    try:
      fichier = open(var1["default"], "a")
      fichier.write(var1["sshd"]+"\n")
      fichier.write(var1["enable1"]+"\n")
      fichier.write(var1["rec"]+"\n")
      fichier.write(var1["enable2"]+"\n")
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
