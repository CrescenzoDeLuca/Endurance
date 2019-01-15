
class Calcolo: 
      def __init__(self,gall, cons):

          self.ora=gall/cons
          self.ora=int(self.ora)
    
          self.min=gall%cons
          cons=cons/60
          self.min=self.min/cons
          self.min=int(self.min)
   
          self.sec=gall%cons
          cons=cons/60
          self.sec=self.sec/cons
          self.sec=int(self.sec)


          print(self.ora, " h / ", self.min, " min / ", self.sec, " sec")





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
    Calcolo(gall, cons)