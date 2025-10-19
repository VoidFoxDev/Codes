import sys
from time import sleep
import keyboard
gameover = 0

def game():
    leben = 100
    sPrint("Wie Heißen sie?")
    name = input("Name; ")
    sPrint("Hallo, " + name + " Du hast " + str(leben) + " leben")
    while True: 
        sPrint("Möchtest du nach links oder rechts gehen?")
        direction = input("")
        if direction == "links":
            sPrint(name + " du bist in einer Grube voller AIDS Nadeln gefallen , du stirbst an einem langsamen quallvollen, schreckllichen Tod, eine Nadel STößt direkt in dein Linkes Auge, und du siehst dein blut die Nadel runtertropfen. ENDE")
            return
        
        elif direction == "rechts":
            sPrint("Du siehst ein Loch in der wand , perfekt für diene hand , du greift rein und merkst wie deine hand von rassierklingen geschnittenwerden . du ahst einnen schlüssel erhalten aber deine hand ist komplett zerfetzt.")
            leben -= 10
            sPrint("Leben = " + str(leben))
            break
        else:
            print("no correct input")
    sPrint("Der schlüssel passt in einer kleine tür rein wo du dich gerade so durchquetschen kannst , auf der anderen seite befindet sich einh Fernseher , willst du ihn anschalten ?")
    while True:
        choice = input("ja oder nein ?")
        if choice == "ja":
            print("Der Fernsehr zeigt eine dir bekannt aussehnde Person , aber du erkennst sie nicht richtig , du weist das du sie schonmal irgendwo gesehen hast...aber wo... . Bei genauem hinsehen erkennst du das es ein Schulfreund aus alten Tagen ist.  ")
            break
        elif choice == "nein":
            print("Die tür hinter dir knallt zu, du stehst in dem leeren raum, es ist still, sher still, die kalten bleichen wände scheinen trüb und das tropfen der abwasserrohre werden immer lauter. Du siehst dir den Fernsehr an aber schaltest ihn nicht an und wartest...gefangen in isolation..allein..")
            break
    if choice == "ja":
        sPrint("Er scheint gefäässlt zu sein. Neben dem Fernsehr ist sind 2 Knöpfe die man betätigen kann, welchen möchtest du drücken , links oder rechts ?")
        button = input("")
        if button == "links":
            sPrint("ein lautes geräusch ertönnt, auf dem Bildschirm siehst du wie eine Konstruktion dinem schulkameraden ein Loch ins bein sägt, seine schreie sind über die übersteuerten boxen des Fernsehr nicht zu überhören....es wird kurz still.\nder bildschirm ist kurz dunkel und geht nach einigen sekunden wieder an\ndein klassenkamerad guckt in die kamera mit müden roten augen und sagt langsam deinen namen...Er weiss das du es warst")
        elif button == "rechts":
            sPrint("Am Fernseher selbst öffnet sich ein kleines geheimfach. Das Loch ist gerade groß genug, dass deine Hand rein passt. Du kannst nicht sehen was sich drin befindet. Möchtest du rein greifen?")
            choice = input("ja oder nein?")
            if choice == "ja":
                sPrint("Du greifst vorsichtig in das Loch, es ist kalt und nass, es fühlt sich alienhaft an. Du spürst einen harten gegenstand. Mit etwas kraft ziehst du ihn aus dem Loch. Der Fernseher erlischt.")    
            if choice == "nein":
                sPrint(f"Du schaust das Loch ängstlich an, greifst nicht rein und beobachtest weiter deinen Schulkameraden im Fernseher... er ist wütend. Er sagt: {name} du arsch, du verfickter hurensohn. Ich töte dich wenn ich dich in finger kriege. DU BASTARD!! - Er ist komplett außer sich und wirbelt herum, dabei siehst du wie sich seine fessel leicht lösen. Der Fernseher erlischt")
                sPrint("Du drehst dich um und siehst eine Tür, einen Schrank und ein Fenster.")
                firstTimeDoor = True
                firstTimeWindow = True
                firstTimeCloset = True
                hasKey = False
                while True:
                    sPrint("Du bist in der Mitte des Raumes. Wo möchtest du hingehen?")
                    choice = input("Tür, Schrank, Fenster?").lower()
                    if choice == "tür":
                        if firstTimeDoor:
                            sPrint("Du begibst dich zur Tür.")
                            sPrint("Sie hat einen Spion.")
                            print("Möchtest du durch den Spion schauen?")
                            choice = input("Ja oder nein?").lower()
                            if choice == "ja":
                                sPrint("Du streckst dich nach vorne und blickst dehutsam durch den Spion.")
                                sPrint("Du blickst hindurch und siehst eine Wand. Die Wand ist vollgeschmiert mit Blut.")
                                sPrint("Dein Blick bleibt auf das Blut gerichtet, du erkennst eine Ziffer.")
                                print("""
        ░▒▓████████▓▒░ 
        ░▒▓█▓▒░        
        ░▒▓█▓▒░        
        ░▒▓███████▓▒░  
            ░▒▓█▓▒░ 
            ░▒▓█▓▒░ 
        ░▒▓███████▓▒░  
        """)
                                sPrint("Du begibst dich zurück in die Mitte des Raumes.")
                                firstTimeDoor = False           
                        else:
                            nPrint("Du erkennst einen griff an der Tür.")
                            print("Möchtest du die Tür öffnen?")
                            choice = input("Ja oder nein?").lower()
                            if choice == "ja":
                                if hasKey:
                                    # TODO ( Marvins Part)
                                    pass
                            elif choice == "nein": 
                                print("Du begibst dich zur Mitte des Raumes.")
                            else:
                                print("Du bist verwirrt und gehst zurück in die Mitte des Raumes.")
                
                    elif choice == "schrank":
                        if firstTimeCloset:
                            sPrint("Du gehst zum Schrank.")
                            sPrint("(Du hörst geräusche im Schrank)")
                            print("Öffnen?")
                            choice = input("ja oder nein?")
                            if choice == "ja":
                                sPrint("Du öffnest vorsichtig den Schrank und ....")
                                sPrint("... eine Ratte schwirrt davon und fällt in das Nadel AIDS Loch.")
                                nPrint("(Dumme Viecher)")
                                print("Es liegt viel gerümpel in den Fächern, du räumst ein wenig bei seite und siehst im Holz eine Ziffer eingraviert:")
                                print("""
    . 
    /| 
    | 
    | 
    _|_
    """)
                                nPrint("(Ok)")
                                nPrint("Im untersten Fach erkennst du einen Safe mit digitalem Code Eingabefeld.")
                                print("Code eingeben?")
                                choice = input("Ja oder nein?")
                                if choice == "ja":
                                    while True: 
                                        user_code = int(input("Bitte eine 3-stellige Zahl eingeben!"))
                                        if user_code == 571:
                                            sPrint("Der Safe öffnet sich und in ihm liegt ein Schlüssel.")
                                            nPrint("Du hast den Schlüssel an dich genommen.")
                                            nPrint("Du gehst zurück in die Mitte des Raumes.")
                                            hasKey = True
                                        else:
                                            nPrint("Leider Falsch!")
                                            print("Erneut versuchen?")
                                            choice = input("ja oder nein?")
                                            if choice == "ja":
                                                continue
                                            else:
                                                break

                                firstTimeCloset = False
                            else:
                                print("Du gehst zurück zur Mitte des Raumes.")
                        else:
                            nPrint("Du öffnest den Schrank und blickst auf die Ziffer")
                            print("""
    . 
    /| 
    | 
    | 
    _|_
    """)
                            nPrint("Im untersten Fach erkennst du einen Safe mit digitalem Code Eingabefeld.")
                            print("Code eingeben?")
                            choice = input("Ja oder nein?").lower()
                            if choice == "ja":
                                while True: 
                                    user_code = int(input("Bitte eine 3-stellige Zahl eingeben!"))
                                    if user_code == 571:
                                        sPrint("Der Safe öffnet sich und in ihm liegt ein Schlüssel.")
                                        nPrint("Du hast den Schlüssel an dich genommen.")
                                        nPrint("Du gehst zurück in die Mitte des Raumes.")
                                        hasKey = True
                                    else:
                                        nPrint("Leider Falsch!")
                                        print("Erneut versuchen?")
                                        choice = input("ja oder nein?")
                                        if choice == "ja":
                                            continue
                                        else:
                                            break
                            else: 
                                print("Du begibst dich zurück in die Mitte des Raumes.")
                    elif choice == "fenster":
                        if firstTimeWindow:
                            sPrint("Du begibst dich zum Fenster und schaust raus.")
                            sPrint("Zwei Männer heben eine Frau aus dem Koffereaum eines Autos, sie ist leblos und blutverschmiert. Sie bringen sie zum Zaun am des Geländes und werfen sie über den Zaun. Sie fällt 30 m in die tiefe. Ihr extremitäten liegen in unnatürlichen Winkeln an ihrem Körper. Ihr Kleid ist am Rücken aufgerissen.")
                            nPrint("(Du erkennst ein Brandmal)")
                            print("""
    ____   
    F __ J  
    J '--' L 
    J`---. | 
    `---J J 
        J__L
        J__|
            
    """)
                            firstTimeWindow = False
                        else:
                            nPrint("Du blickst aus dem Fenster, siehst die verdeht Frau auf dem Bauch liegen.")
                            sPrint("(Du erkennst das Brandmal)")
                            print("""
    ____   
    F __ J  
    J '--' L 
    J`---. | 
    `---J J 
        J__L
        J__|
            
    """)
                            nPrint("Du gehst zurück zur Mitte des Raumes.")
                    else:
                        print("")        





def sPrint(text):
    sleep(1)
    for char in text:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")

def nPrint(text):
    for char in text:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")

game()