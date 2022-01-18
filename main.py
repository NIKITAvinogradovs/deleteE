teksts = input ("Ievadi tekstu: ")
def deleteE (teksts):
  if teksts.count ("e")>0:
    teksts = teksts.replace ("e", " ")
    teksts = teksts.upper()
    print (teksts)
  else:
    teksts = "Teksta nav vajadzigo burtu"
    print (teksts)
  return (teksts)
deleteE (teksts)