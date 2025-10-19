import sys
from time import sleep
import keyboard
import threading

stop_typing = False
gameover = 0

def game():
    global gameover
    leben = 100
    print("Wie Heißen sie?")
    name = input("Name; ")
    print("Hallo, " + name + " Du hast " + str(leben) + " leben")
    while True: 
        print("Möchtest du nach links oder rechts gehen?")
        direction = input("")
        if direction == "links":
            print(name + " du bist in einer Grube voller AIDS Nadeln gefallen , du stirbst an einem langsamen quallvollen, schreckllichen Tod, eine Nadel STößt direkt in dein Linkes Auge, und du siehst dein blut die Nadel runtertropfen. ENDE")
            gameover = 1
            return
        
        elif direction == "rechts":
            print("Du siehst ein Loch in der wand , perfekt für diene hand , du greift rein und merkst wie deine hand von rassierklingen geschnittenwerden . du ahst einnen schlüssel erhalten aber deine hand ist komplett zerfetzt.")
            leben -= 10
            print("Leben = " + str(leben))
            break
        else:
            print("no correct input")
    print("Der schlüssel passt in einer kleine tür rein wo du dich gerade so durchquetschen kannst , auf der anderen seite befindet sich einh Fernseher , willst du ihn anschalten ?")
    while True:
        choice = input("ja oder nein ?")
        if choice == "ja":
            print("Der Fernsehr zeigt eine dir bekannt aussehnde Person , aber du erkennst sie nicht richtig , du weist das du sie schonmal irgendwo gesehen hast...aber wo... . Bei genauem hinsehen erkennst du das es ein Schulfreund aus alten Tagen ist.  ")
            break
        elif choice == "nein":
            print("Die tür hinter dir knallt zu, du stehst in dem leeren raum, es ist still, sher still, die kalten bleichen wände scheinen trüb und das tropfen der abwasserrohre werden immer lauter. Du siehst dir den Fernsehr an aber schaltest ihn nicht an und wartest...gefangen in isolation..allein..")
            break
    if choice == "ja":
        print("Er scheint gefäässlt zu sein. Neben dem Fernsehr ist sind 2 Knöpfe die man betätigen kann, welchen möchtest du drücken , links oder rechts ?")
        button = input("")
        if button == "links":
            print("ein lautes geräusch ertönnt, auf dem Bildschirm siehst du wie eine Konstruktion dinem schulkameraden ein Loch ins bein sägt, seine schreie sind über die übersteuerten boxen des Fernsehr nicht zu überhören....es wird kurz still.\nder bildschirm ist kurz dunkel und geht nach einigen sekunden wieder an\ndein klassenkamerad guckt in die kamera mit müden roten augen und sagt langsam deinen namen...Er weiss das du es warst")
        elif button == "rechts":
            print("Am Fernseher selbst öffnet sich ein kleines geheimfach. Das Loch ist gerade groß genug, dass deine Hand rein passt. Du kannst nicht sehen was sich drin befindet. Möchtest du rein greifen?")
            choice = input("ja oder nein?")
            if choice == "ja":
                print("Du greifst vorsichtig in das Loch, es ist kalt und nass, es fühlt sich alienhaft an. Du spürst einen harten gegenstand. Mit etwas kraft ziehst du ihn aus dem Loch. Der Fernseher erlischt.")    
            if choice == "nein":
                print(f"Du schaust das Loch ängstlich an, greifst nicht rein und beobachtest weiter deinen Schulkameraden im Fernseher... er ist wütend. Er sagt: {name} du arsch, du verfickter hurensohn. Ich töte dich wenn ich dich in finger kriege. DU BASTARD!! - Er ist komplett außer sich und wirbelt herum, dabei siehst du wie sich seine fessel leicht lösen. Der Fernseher erlischt")
            print("Du drehst dich um und siehst eine Tür, einen Schrank und ein Fenster.")
            firstTimeDoor = True
            firstTimeWindow = True
            firstTimeCloset = True
            hasKey = False
            while True:
                print("Du bist in der Mitte des Raumes. Wo möchtest du hingehen?")
                choice = input("Tür, Schrank, Fenster?").lower()
                if choice == "tür":
                    if firstTimeDoor:
                        print("Du begibst dich zur Tür.")
                        print("Sie hat einen Spion.")
                        print("Möchtest du durch den Spion schauen?")
                        choice = input("Ja oder nein?").lower()
                        if choice == "ja":
                            print("Du streckst dich nach vorne und blickst dehutsam durch den Spion.")
                            print("Du blickst hindurch und siehst eine Wand. Die Wand ist vollgeschmiert mit Blut.")
                            print("Dein Blick bleibt auf das Blut gerichtet, du erkennst eine Ziffer.")
                            print("""
    ░▒▓████████▓▒░ 
    ░▒▓█▓▒░        
    ░▒▓█▓▒░        
    ░▒▓███████▓▒░  
        ░▒▓█▓▒░ 
        ░▒▓█▓▒░ 
    ░▒▓███████▓▒░  
    """)
                            print("Du begibst dich zurück in die Mitte des Raumes.")
                            firstTimeDoor = False           
                    else:
                        print("Du erkennst einen griff an der Tür.")
                        print("Möchtest du die Tür öffnen?")
                        choice = input("Ja oder nein?").lower()
                        if choice == "ja":
                            if hasKey:
                                return
                        elif choice == "nein": 
                            print("Du begibst dich zur Mitte des Raumes.")
                        else:
                            print("Du bist verwirrt und gehst zurück in die Mitte des Raumes.")
            
                elif choice == "schrank":
                    if firstTimeCloset:
                        print("Du gehst zum Schrank.")
                        print("(Du hörst geräusche im Schrank)")
                        print("Öffnen?")
                        choice = input("ja oder nein?")
                        if choice == "ja":
                            print("Du öffnest vorsichtig den Schrank und ....")
                            print("... eine Ratte schwirrt davon und fällt in das Nadel AIDS Loch.")
                            print("(Dumme Viecher)")
                            print("Es liegt viel gerümpel in den Fächern, du räumst ein wenig bei seite und siehst im Holz eine Ziffer eingraviert:")
                            print("""
. 
/| 
| 
| 
_|_
""")
                            print("(Ok)")
                            print("Im untersten Fach erkennst du einen Safe mit digitalem Code Eingabefeld.")
                            print("Code eingeben?")
                            choice = input("Ja oder nein?")
                            if choice == "ja":
                                while True: 
                                    user_code = int(input("Bitte eine 3-stellige Zahl eingeben!"))
                                    if user_code == 571:
                                        print("Der Safe öffnet sich und in ihm liegt ein Schlüssel.")
                                        print("Du hast den Schlüssel an dich genommen.")
                                        print("Du gehst zurück in die Mitte des Raumes.")
                                        hasKey = True
                                        break
                                    else:
                                        print("Leider Falsch!")
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
                        print("Du öffnest den Schrank und blickst auf die Ziffer")
                        print("""
. 
/| 
| 
| 
_|_
""")
                        print("Im untersten Fach erkennst du einen Safe mit digitalem Code Eingabefeld.")
                        print("Code eingeben?")
                        choice = input("Ja oder nein?").lower()
                        if choice == "ja":
                            while True: 
                                user_code = int(input("Bitte eine 3-stellige Zahl eingeben!"))
                                if user_code == 571:
                                    print("Der Safe öffnet sich und in ihm liegt ein Schlüssel.")
                                    print("Du hast den Schlüssel an dich genommen.")
                                    print("Du gehst zurück in die Mitte des Raumes.")
                                    hasKey = True
                                    break
                                else:
                                    print("Leider Falsch!")
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
                        print("Du begibst dich zum Fenster und schaust raus.")
                        print("Zwei Männer heben eine Frau aus dem Koffereaum eines Autos, sie ist leblos und blutverschmiert. Sie bringen sie zum Zaun am des Geländes und werfen sie über den Zaun. Sie fällt 30 m in die tiefe. Ihr extremitäten liegen in unnatürlichen Winkeln an ihrem Körper. Ihr Kleid ist am Rücken aufgerissen.")
                        print("(Du erkennst ein Brandmal)")
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
                        print("Du blickst aus dem Fenster, siehst die verdeht Frau auf dem Bauch liegen.")
                        print("(Du erkennst das Brandmal)")
                        print("""
____   
F __ J  
J '--' L 
J`---. | 
`---J J 
    J__L
    J__|
        
""")
                        print("Du gehst zurück zur Mitte des Raumes.")
                else:
                    gameover = 1
                    break        

def flur():
    print("DU gehst durch die schwere Eisentür durch einen Korridor , irgendwas ist Komisch, Es gibt keine Türen. \nDie Tür hinter dir schliesst sich mit einem lauten knall")
    print("als du dich wieder umdrehst , ist eine andere Tür erschienen , die sich langsam öffnet.\nIm nächsten Raum, befindet sich ein kleines Mädchen mit einem sack über dem Kopf, leichte wunden und schwellungen am ganzen körper und gefässelt mit einer eisenkette am boden.")
    print("Du hörst das bitterliche schluchzen des Mädchens. Als sie dich bemerkt wie du ihr näher kommst fängt sie an zu zittern. BITTE BITTE tu mir nichts, weinte das mädchen.\nNeben ihr liegt ein Stumpfes Messer und  ein Zettel wo drauf steht:")
    print("Das Mädchen was du vor dir siehst, mobbt ihre Mitschüler in der Grundschule und klaut deren Geld und essen, aber das ist doch normal für Kinder in ihrem alter oder... ?\nverschohnst du das mädchen , werden die Kinder die sie beklaut hat sterben, Tötest du sie bleiben die anderen am leben, Wie entscheidest du dich ?")
    print("töten oder in ruhe lassen?: ")
    while True:
        choice = input("")
        if choice == "in ruhe lassen":
            print("eine versteckte wand öfffnet sich mit einem Bildschirm drinnen. Der bildschirm flackerte mit white noice bis auf einmal der bildschirm zu einer Liveübertragung wechselt.\nin der liveübertragung siehst du 5 Kinder in einem Spielzimmer spielen. es sieht eiegtnlich alles normal aus.Die Kamera wechelt zu einer tür.")
            print("Als die tür sich öffnet kammen Männer in Seuchenschutzanzügen in das Spielzimmer maschiert, und richteten die Waffen gegen die kinder...alles was du nur noch siehst und hörst sind die schüsse und das aufhellen der schussexplosionen....Der Bildschirm wird schwarz...")
            break
        elif choice == "töten":
            print("Du nimmst das Messer, deine hand fängt an zu schwitzen und du chaust dir das Mädchen an...\nDu fängst an deine hand zu heben und mit deiner ganzen kraft rammst du das Messer in die Brust des Mädchens .\n Sie schreit und fehlt dich an damit aufzuhören, aber dein einziger gedanke war das du hier nur noch raus willst. Du versuchst das Messer aus ihr raus zu ziehen aber es steckte fest zwischen ihren rippen. Das Rostige stumpfe Messer ging nur mit mühen raus. Du hast das Herz des Mädchens leicht verfehlt wodurch sie nicht direkt getötet worden ist. Sie weinte bitterlich voller schmerzen. Du musst es nochmal in ihr reinrammen...\nDeine gedanken spielen verrückt, dir kommen die Tränen und du fänsgt fast das kotzen an. Dieses mal rammst du es direkt in ihre halsschlagader mit ganz viel drück hast du es gschafft durch hier hals zu schneiden...")
            print("Sie ist tot...")
            break
        else:
            print("bitte Wählen: Töten oder in ruhe lassen.")
    if choice == "in ruhe lassen":
        print("Eine verdeckte tür ging auf aber als du hindurchgehen wolltest hörst du ein klicken...Die Ketten des angeketteten Mädchens werden unter starkstrom gesetzt weshalb sie augenblicklich stirbt. Der Anblick wie der Sack in flammen aufgeht und das Herzzereisende schreien des Mädchens lösen in dir eine unglaubliche Trauer aus aber dein einziger Gedanke ist...Du musst entkommen")
    elif choice == "töten":
        print("Eine verdeckte tür ging auf und du konntest hindurchgehen...raus aus dem Horror...")



def check_input():
    global stop_typing
    keyboard.wait('space')  # wartet auf Leertaste
    stop_typing = True

def sPrint(text):
    global stop_typing
    stop_typing = False

    # Starte Thread, der auf Leertaste oder Enter wartet
    t = threading.Thread(target=lambda: (keyboard.wait('space') or keyboard.wait('enter')))
    t.daemon = True
    t.start()

    sleep(1)
    for char in text:
        if stop_typing or keyboard.is_pressed('space') or keyboard.is_pressed('enter'):
            # Sofort alles anzeigen
            sys.stdout.write(text[text.index(char):])
            sys.stdout.flush()
            break
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")

def nPrint(text):
    global stop_typing
    stop_typing = False

    t = threading.Thread(target=lambda: (keyboard.wait('space') or keyboard.wait('enter')))
    t.daemon = True
    t.start()

    for char in text:
        if stop_typing or keyboard.is_pressed('space') or keyboard.is_pressed('enter'):
            sys.stdout.write(text[text.index(char):])
            sys.stdout.flush()
            break
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")


game()
if not gameover:
    flur()