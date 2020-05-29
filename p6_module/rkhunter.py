# coding: utf-8
import os
def rkhunter_install(var1):
    """Installation et configuration de rkhunter"""
    try:
      os.system("sudo apt-get -y update")
      os.system("sudo apt-get -y install rkhunter")
      os.system("sudo rkhunter --update")
      os.system("sudo cp "+var1["rkconf"]+" "+var1["rkconf"]+".bak")
      fin = open(var1["rkconf"], "rt")
      data = fin.read()
      data = data.replace('CRON_DAILY_RUN=""',var1["cron"])
      data = data.replace('REPORT_EMAIL="root"',var1["report"] )
      fin.close()
      fin = open(var1["rkconf"], "wt")
      fin.write(data)
      fin.close()
      os.system("sudo rkhunter --propupd")
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
