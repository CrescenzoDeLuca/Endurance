

gall=input("inserisci Galloni --->")
gall=float(gall)


if(gall < 0):
  print("-!-ERROR-!-")
else:
  cons=input("consumo orario --->")
  cons=float(cons)
  
  if(cons < 0):  
    print("-!-ERROR-!-")
  else:

          ora=gall/cons
          ora=int(ora)
    
          minu=gall%cons
          cons=cons/60
          minu=minu/cons
          minu=int(minu)
   
          sec=gall%cons
          cons=cons/60
          sec=sec/cons
          sec=int(sec)


          print(ora, " h / ", minu, " min / ", sec, " sec")
