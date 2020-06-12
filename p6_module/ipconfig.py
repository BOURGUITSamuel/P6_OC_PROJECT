# coding: utf-8
import os

def set_ipconfig(var1):
    """Configuration du fichier interfaces de l'OS Debian"""
    try:
      fichier = open("/etc/network/interfaces", "a")
      fichier.write(var1["int"]+"\n")
      fichier.write(var1["type"]+"\n")
      fichier.write(var1["ip"]+"\n")
      fichier.write(var1["mask"]+"\n")
      fichier.write(var1["gaw"]+"\n")
      fichier.close()
      os.system("sudo systemctl restart networking")
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
        
def hostname(var1):
    """Modification du hostname et du fichier hosts"""
    try:
       os.system("sudo hostname" " " +var1["hostname"])
       fichier = open("/etc/hosts", "a")
       fichier.write(var1["hosts"])
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
