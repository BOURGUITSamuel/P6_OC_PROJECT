# coding: utf-8
import os
private = "private.pem"
public = "public.pem"
path = "/etc/ssh/key"
def sshkey_generate(private, public, path):
    """Génération de clé privée , public ssh"""
    try:
      import os
      from Crypto.PublicKey import RSA
      key = RSA.generate(2048)
      public_key = key.publickey()
      enc_data = public_key.encrypt("""admin-manager-hash""", 32)
      x = key.decrypt(enc_data)
      x = x.decode('utf-8')
      k = key.exportKey('PEM')
      p = key.publickey().exportKey('PEM')
      with open(private,'w') as kf:
              kf.write(k.decode())
              kf.close()
      with open(public,'w') as pf:
              pf.write(p.decode())
              pf.close()
      os.system("sudo mkdir" " "+path)
      os.system("sudo mv "+private+" "+path)
      os.system("sudo mv "+public+" "+path)

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
sshkey_generate(private, public, path)
