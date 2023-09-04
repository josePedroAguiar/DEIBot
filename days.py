import os
def link_disciplina(chave):
  AED=os.getenv('LINKS_AED').split(",")
  ATD=os.getenv('LINKS_ATD').split(",")
  BD=os.getenv('LINKS_BD').split(",")
  SO=os.getenv('LINKS_SO').split(",")
  RC=os.getenv('LINKS_RC').split(",")
  switcher = {
  '$AED':AED,
  '$ATD':ATD,
  '$BD':BD,
  '$SO':SO,
  '$RC':RC,
    }
  return switcher[chave]

def info_disciplina(chave):
  AED=os.getenv('LINKS_AED').split(",")
  ATD=os.getenv('LINKS_ATD').split(",")
  BD=os.getenv('LINKS_BD').split(",")
  SO=os.getenv('LINKS_SO').split(",")
  RC=os.getenv('LINKS_RC').split(",")
  switcher = {
  '-AED':AED,
  '-RC':RC,
  '-ATD':ATD,
  '-BD':BD,
  '-SO':SO,
    }
  return switcher[chave]

def links_pl(chave):
  AED=str(os.getenv('PL_AED'))
  ATD=str(os.getenv('PL_ATD'))
  BD=str(os.getenv('PL_BD'))
  SO=str(os.getenv('PL_SO'))
  RC=str(os.getenv('PL_RC'))
  switcher = {
  '*AED':AED,
  '*RC':RC,
  '*ATD':ATD,
  '*BD':BD,
  '*SO':SO,
    
    }
  return switcher[chave]


def aulas(data):
  if(data.strftime("%a")=="Mon"):
    if(data.strftime("%X").split(":")[0]=="14"and data.strftime("%X").split(":")[1]=="00"):
      return "$AED"
    elif(data.strftime("%X").split(":")[0]=="16"and data.strftime("%X").split(":")[1]=="00"):
      return "$AED"
    elif(data.strftime("%X").split(":")[0]=="17"and data.strftime("%X").split(":")[1]=="00"):
      return "$RC"
    elif(data.strftime("%X").split(":")[0]=="19"and data.strftime("%X").split(":")[1]=="00"):
      return "$RC"
    else:
      return 0
  elif(data.strftime("%a")=="Tue"):
    if(data.strftime("%X").split(":")[0]=="14"and data.strftime("%X").split(":")[1]=="00"):
      return "$SO"
    elif(data.strftime("%X").split(":")[0]=="16"and data.strftime("%X").split(":")[1]=="00"):
      return "$SO"
    elif(data.strftime("%X").split(":")[0]=="17"and data.strftime("%X").split(":")[1]=="00"):
      return "$ATD"
    elif(data.strftime("%X").split(":")[0]=="19"and data.strftime("%X").split(":")[1]=="00"):
      return "$ATD"
    else:
      return 0
  elif(data.strftime("%a")=="Fri"):
    if(data.strftime("%X").split(":")[0]=="14"and data.strftime("%X").split(":")[1]=="00"):
      return "$BD"
    elif(data.strftime("%X").split(":")[0]=="16"and data.strftime("%X").split(":")[1]=="00"):
      return "$BD"
    else:
      return 0 #Quando não há aulas  
  else:
      return 0


