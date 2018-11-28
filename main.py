from lib import cameraDriver as cam
from lib import motionsensorDriver as motion
from lib import drawTheTableauLib as dtlib
from lib import drawTheTableauDriver as dtdriver
from lib import lcdDriver as lcd
import datetime as dt
import time as t


if __name__ == "__main__":
    dtlib.printDTT("DrawTheTableau")
	
    continuer = dtlib.inputDTT ("Voulez-vous prendre une image instantanée ?", "Prendre image ?")

    while continuer : 
	dtlib.printDTT("Photo dans 5 sec")
	t.sleep(5)
    	takeAndSavePic()
	dtlib.printDTT("Photo prise !")
	continuer = dtlib.inputDTT ("Voulez-vous prendre une autre image instantanée ?", "Prendre image ?")
	

    continuer = dtlib.inputDTT ("Voulez-vous effectuer une prise auto des images ?", "Continuer prise auto img ?")
    while continuer :

        dtlib.printDTT ("DEBUT DE LA PRISE AUTO D\'IMAGE")
        dtdriver.takeAutomatedPictures();
        dtlib.printDTT ("FIN DE LA PRISE AUTO D\'IMAGE")

        continuer = dtlib.inputDTT ("Voulez-vous continuer la prise auto des images ?", "Continuer prise auto img ?")

    rep = dtlib.inputDTT ("Voulez-vous envoyer les images sur une machine distante ?", "Envoyer sur machine distante ?")
    #TODO
    lcd.shutDownLCD()


