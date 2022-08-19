ciclo = True
while ciclo: 
    
    
    print("INDOVINA LA MADONNA")
    print("  ")

    giocatore1 = str(input("inserisci nome: "))

    if giocatore1 != None:
        print("nuova partita.1")
        print("esci dal gioco.2")
        
            
            
        scelta = int(input())
        ciclo = True
        while ciclo:            
            if scelta == 1:
                    print("chi è porca ?")
                    print("madonna.1",
                    "nonna.2", "cugina.3")
                    
                    risposta = int(input(""))
                    
                    if risposta != 1:
                        print("ritenta!")
                
                    
                    
                    elif risposta == 1:
                        print("daje porca madonna!!")
                        ciclo = False


                    
            elif scelta == 2:
                print("ciao ciao") 
                ciclo = False
            
        
        
