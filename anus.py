import sys
import time
import threading
import termios
import tty
import select

stop_typing = False
tvLeftButtonPressed = False
tookAlienItem = False

gameover = 0

def game():
    global gameover, tvLeftButtonPressed, tookAlienItem
    leben = 100
    print("Wie heißen sie?")
    name = input("Name: ")
    print("Hallo, " + name + "\n(Du hast " + str(leben) + " Leben! Sei Vorsichtig!)")
    while True: 
        direction = input("Möchtest du nach links oder rechts gehen?")
        if direction == "links":
            nPrint(name + " Du bist in eine Grube voller AIDS Nadeln gefallen, du stirbst an einem langsamen quallvollen und schreckllichen Tod als eine Nadel direkt in dein Linkes Auge sticht. Du siehst wie dein Blut die Nadel runtertropft und wirst ohnmächtig.\nENDE")
            gameover = 1
            return
        
        elif direction == "rechts":
            nPrint("Du siehst ein Loch in der Wand, perfekt für deine Hand, du greift rein und merkst wie deine Hand von Rassierklingen geschnitten wird. Du hast einen Schlüssel erhalten aber deine Hand ist komplett zerfetzt.")
            leben -= 10
            print("(Leben = " + str(leben)+ ")")
            break
        else:
            print("no correct input")
    nPrint("Der Schlüssel passt in eine kleine Tür rein wo du dich gerade so durchquetschen kannst. Auf der anderen seite befindet sich ein Fernseher, willst du ihn einschalten?")
    while True:
        choice = input("\nJa oder Nein?\n").lower()
        if choice == "ja":
            nPrint("Der Fernsehr zeigt dir eine bekannt aussehende Person, aber du erkennst sie nicht richtig. Du weißt das du sie schonmal irgendwo gesehen hast...aber wo...")
            nPrint("Bei genauem hinsehen erkennst du, dass es ein Schulfreund aus alten Tagen ist.")
            break
        elif choice == "nein":
            nPrint("Die Tür hinter dir knallt zu, du stehst in dem leeren Raum, es ist still, sehr still, die kalten bleichen Wände scheinen trüb und das tropfen der Abwasserrohre wird immer lauter. Du siehst dir den Fernseher an aber schaltest ihn nicht an und wartest...gefangen in isolation..allein..")
            break
    if choice == "ja":
        nPrint("Er scheint gefässelt zu sein. Neben dem Fernseher sind 2 Knöpfe die man betätigen kann.")
        while True:
            nPrint("Welchen möchtest du drücken?")
            button = input("links oder rechts?").lower()
            if button == "links":
                nPrint("Ein lautes Geräusch ertönnt, auf dem Bildschirm siehst du wie eine Konstruktion deinem Schulkameraden ein Loch ins Bein sägt, seine Schreie sind über die übersteuerten Boxen des Fernseher nicht zu überhören....es wird kurz still.\nDer Bildschirm ist kurz dunkel und geht nach einigen Sekunden wieder an.\nDein Klassenkamerad guckt in die Kamera mit müden roten Augen und sagt langsam deinen Namen...Er weiß das du es warst.")
                tvLeftButtonPressed = True
                break
            elif button == "rechts":
                nPrint("Am Fernseher selbst öffnet sich ein kleines Geheimfach. Das Loch ist gerade groß genug, dass deine Hand rein passt. Du kannst nicht sehen was sich drin befindet. Möchtest du rein greifen?")
                choice = input("Ja oder Nein?").lower()
                if choice == "ja":
                    nPrint("Du greifst vorsichtig in das Loch, es ist kalt und nass, es fühlt sich alienhaft an. Du spürst einen harten Gegenstand. Mit etwas Kraft ziehst du ihn aus dem Loch. Der Fernseher erlischt.")
                    nPrint("Du hast keine Ahung was das für ein Gegenstand ist, vielleicht wird er in Zukunft nützlich sein.")
                    tookAlienItem = True  
                if choice == "nein":
                    nPrint(f"Du schaust das Loch ängstlich an, greifst nicht rein und beobachtest weiter deinen Schulkameraden im Fernseher... er ist wütend. Er sagt: {name} du arsch, du verfickter hurensohn. Ich töte dich wenn ich dich in Finger kriege. DU BASTARD!! ") 
                    nPrint("(Du siehst zu wie er sich windet und flent. Seine Fesseln lösen sich leicht. Der Fernseher erlischt abrupt.")
                nPrint("Du schaust zum Loch von dem du gekommen bist. Es ist viel zu klein um zurück zu gehen.")
                nPrint("Du schaust dich weiter im Raum um und siehst eine Tür, einen Schrank und ein Fenster.")
                firstTimeDoor = True
                firstTimeWindow = True
                firstTimeCloset = True
                hasKey = False
                while True:
                    nPrint("Du bist in der Mitte des Raumes. Wo möchtest du hingehen?")
                    choice = input("Tür, Schrank, Fenster?").lower()
                    if choice == "tür":
                        if firstTimeDoor:
                            nPrint("Du begibst dich zur Tür.")
                            nPrint("Sie hat einen Spion.")
                            lookThroughSpy()    
                            firstTimeDoor = False   
                        else: 
                            lookThroughSpy()
                        nPrint("Du siehst einen griff an der Tür.")
                        nPrint("Möchtest du versuchen die Tür zu öffnen?")
                        choice = input("Ja | Nein?").lower()
                        if choice == "ja":
                            if hasKey:
                                return
                            else: 
                                nPrint("Die Tür ist verschlossen.")
                                nPrint("(Ich muss irgend wo einen Schlüssel finden)")
                        elif choice == "nein": 
                            nPrint("Du begibst dich zur Mitte des Raumes.")
                        else:
                            nPrint("Du bist verwirrt und gehst zurück in die Mitte des Raumes.")
                    
                    elif choice == "schrank":
                        if firstTimeCloset:
                            nPrint("Du gehst zum Schrank.")
                            nPrint("(Du hörst geräusche im Schrank)")
                            nPrint("Öffnen?")
                            choice = input("Ja oder Nein?").lower()
                            if choice == "ja":
                                openCloset(firstTimeCloset)
                                goToCodeDisplay()
                                firstTimeCloset = False
                        else:
                            openCloset(firstTimeCloset)
                            goToCodeDisplay()
                        nPrint("Du gehst zurück zur Mitte des Raumes.")
                    elif choice == "fenster":
                        if firstTimeWindow:
                            nPrint("Du begibst dich zum Fenster und schaust raus.")
                            nPrint("Zwei Männer heben eine Frau aus dem Koffereaum eines Autos, sie ist leblos und blutverschmiert. Sie bringen sie zum Zaun am des Geländes und werfen sie über den Zaun. Sie fällt 30 m in die tiefe. Ihr extremitäten liegen in unnatürlichen Winkeln an ihrem Körper. Ihr Kleid ist am Rücken aufgerissen.")
                            showBurnmark()
                            firstTimeWindow = False
                        else:
                            nPrint("Du blickst aus dem Fenster, siehst wie die komplett verdehte Frau auf dem Bauch liegt.")
                            showBurnmark()
                        nPrint("Du gehst zurück zur Mitte des Raumes.")
                    else:
                        gameover = 1
                        break        
                break
            else:
                print("Bitte nochmal eingeben!")
def flur():
    nPrint("Du gehst durch die schwere Eisentür durch einen Korridor, irgendwas ist komisch. Es gibt keine Türen.\nDie Tür hinter dir schließt sich mit einem lauten knall.")
    nPrint("Als du dich wieder umdrehst, ist eine andere Tür erschienen, die sich langsam öffnet.\nIm nächsten Raum befindet sich ein kleines Mädchen mit einem Sack über dem Kopf. Es sind leichte Wunden und Schwellungen am ganzen Körper zu sehen. Sie ist am Boden mit einer Eisenkette gefässelt.")
    nPrint("Du hörst das bitterliche Schluchzen des Mädchens. Als sie dich bemerkt wie du ihr näher kommst, fängt sie an zu zittern.")
    nPrint("'BITTE BITTE tu mir nichts..' weint das Mädchen.")
    nPrint("Neben ihr liegt ein stumpfes Messer und ein Zettel wo drauf steht:")
    nPrint("'Das Mädchen, was du vor dir siehst, mobbt ihre Mitschüler in der Grundschule und klaut ihnen Geld und essen. Aber das ist doch normal für Kinder in ihrem alter oder... ?\nVerschohnst du das Mädchen, werden die Kinder, welche sie beklaut hat, sterben.\nTötest du sie, bleiben die anderen am leben.\nWie entscheidest du dich?'")
    while True:
        choice = input("'Töten' oder 'in ruhe lassen'? ").lower()
        if choice == "in ruhe lassen":
            nPrint("Eine versteckte Wand öffnet sich mit einem Bildschirm drinnen. Der Bildschirm flackerte mit white noise bis auf einmal der Bildschirm zu einer Liveübertragung wechselt.\nIn der Liveübertragung siehst du 5 Kinder in einem Spielzimmer spielen.\nEs sieht eigentlich alles normal aus. Die Kamera wechelt zu einer Tür.")
            nPrint("Als die Tür sich öffnet kammen Männer in Seuchenschutzanzügen in das Spielzimmer maschiert und richteten die Waffen auf die Kinder... alles was du noch siehst und hörst sind die Schüsse und das aufhellen der Schussexplosionen...\nDer Bildschirm wird schwarz...")
            break
        elif choice == "töten":
            nPrint("Du nimmst das Messer.\nDeine Hand fängt an zu schwitzen und du schaust dir das Mädchen an...\nDu fängst an deine Hand zu heben und mit deiner ganzen Kraft rammst du das Messer in die Brust des Mädchens.\n Sie schreit und fleht dich an damit aufzuhören aber dein einziger gedanke ist, dass du hier nur raus willst. Du versuchst das Messer aus ihr raus zu ziehen aber es steckt fest zwischen ihren Rippen. Das rostige stumpfe Messer geht nur mit Gewalt raus.")
            nPrint("Du hast das Herz des Mädchens leicht verfehlt wodurch sie nicht direkt stirbt. Sie weint bitterlich vor Schmerzen. Du musst es nochmal in sie reinrammen\nDeine gedanken spielen verrückt, dir kommen die Tränen und du fängst fast das kotzen an. Dieses mal rammst du es direkt in ihre Halsschlagader. Mit ganz viel Druck hast du es geschafft ihr durch den Hals zu schneiden...")
            nPrint("Sie ist tot...")
            break
        else:
            nPrint("Bitte Wählen: 'Töten' oder 'in ruhe lassen'.")
    if choice == "in ruhe lassen":
        nPrint("Eine verdeckte Tür geht auf aber als du hindurchgehen willst hörst du ein klicken...Die Ketten des angeketteten Mädchens werden unter Starkstrom gesetzt weshalb sie augenblicklich stirbt. Der Anblick wie der Sack in flammen aufgeht und das Herzzereißende schreien des Mädchens lösen in dir eine unglaubliche Trauer aus aber dein einziger Gedanke ist...Du musst entkommen")
    elif choice == "töten":
        nPrint("Eine verdeckte Tür ging auf und du konntest hindurchgehen...raus aus dem Horror...")


def lookThroughSpy() -> bool:
    nPrint("Möchtest du durch den Spion schauen?")
    choice = input("Ja oder nein?").lower()
    if choice == "ja":
        nPrint("Du streckst dich nach vorne und blickst dehutsam durch den Spion.")
        nPrint("Du blickst hindurch und siehst eine Wand. Die Wand ist vollgeschmiert mit Blut.")
        nPrint("Dein Blick bleibt auf das Blut gerichtet, du erkennst eine Ziffer.")
        print("""
    ░▒▓████████▓▒░ 
    ░▒▓█▓▒░        
    ░▒▓█▓▒░        
    ░▒▓███████▓▒░  
          ░▒▓█▓▒░ 
          ░▒▓█▓▒░ 
    ░▒▓███████▓▒░  
    """)

def openCloset(firstTime):
    if firstTime:
        nPrint("Du öffnest vorsichtig den Schrank und ....")
        nPrint("... eine Ratte schwirrt davon und fällt in das Nadel AIDS Loch.")
        nPrint("(Dumme Viecher)")
        nPrint("Es liegt viel gerümpel in den Fächern, du räumst ein wenig bei seite und siehst im Holz eine Ziffer eingraviert:")
        print("""
     . 
    /| 
     | 
     | 
    _|_
    """)
        nPrint("(Ok)")
    else:
        nPrint("Du öffnest den Schrank und blickst auf die Ziffer")
        print("""
     . 
    /| 
     | 
     | 
    _|_
""")

def goToCodeDisplay():
    global hasKey
    nPrint("Im untersten Fach erkennst du einen Safe mit digitalem Code Eingabefeld.")
    nPrint("Code eingeben?")
    choice = input("Ja oder nein?").lower()
    if choice == "ja":
        while True: 
            user_code = int(input("Bitte eine 3-stellige Zahl eingeben!"))
            if user_code == 591:
                nPrint("Der Safe öffnet sich und in ihm liegt ein Schlüssel.")
                nPrint("Du hast den Schlüssel an dich genommen.")
                nPrint("Du gehst zurück in die Mitte des Raumes.")
                hasKey = True
                break
            else:
                nPrint("Leider Falsch!")
                nPrint("Erneut versuchen?")
                choice = input("ja oder nein?").lower()
                if choice == "ja":
                    continue
                else:
                    break

def showBurnmark():
    sPrint("(Du erkennst ein Brandmal)")
    print("""
   ____   
F  __  J  
J '--' L 
J`---. | 
`---J  J 
    J__L
    J__|
        
""")

def key_listener():
    """Runs in a separate thread and sets stop_typing to True when space or enter is pressed."""
    global stop_typing
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        while True:
            dr, _, _ = select.select([sys.stdin], [], [], 0)
            if dr:
                ch = sys.stdin.read(1)
                if ch in [' ', '\n']:
                    stop_typing = True
                    break
            time.sleep(0.05)
    finally:
        # Always restore normal terminal mode
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def smart_print(text, delay=0.05, start_delay=0):
    """Prints text gradually; space or enter skips animation."""
    global stop_typing
    stop_typing = False

    # Start key listener
    listener = threading.Thread(target=key_listener, daemon=True)
    listener.start()

    time.sleep(start_delay)
    for i, char in enumerate(text):
        if stop_typing:
            sys.stdout.write(text[i:])
            sys.stdout.flush()
            break
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("")

    # Wait briefly so the listener can exit and restore terminal state
    time.sleep(0.05)

def sPrint(text):
    smart_print(text, delay=0.1, start_delay=1)

def nPrint(text):
    smart_print(text, delay=0.1, start_delay=0)

game()
if not gameover:
    flur()
