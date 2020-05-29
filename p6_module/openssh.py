# coding: utf-8
import os

def openssh_install(var1):
    """installation et Configuration de openssh-server"""
    try:
      os.system("sudo apt-get -y install openssh-server")
      os.system("sudo cp "+var1["sshdfile"]+" "+var1["sshdfile"]+".bak")
      os.system("sudo systemctl enable ssh")
      os.system("sudo systemctl restart sshd")
      fin = open(var1["sshdfile"], "rt")
      data = fin.read()
      data = data.replace('#PermitRootLogin prohibit-password',var1["permit"])
      data = data.replace('#PubkeyAuthentication yes',var1["pubkey"])
      data = data.replace('X11Forwarding yes',var1["x11"])
      data = data.replace('#ClientAliveCountMax 3',var1["cac"])
      fin.close()
      fin = open(var1["sshdfile"], "wt")
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
