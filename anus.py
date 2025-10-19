gameover = 0

def game():
    leben = 100
    print("Wie Heißen sie?")
    name = input("Name; ")
    print("Hallo, " + name + " Du hast " + str(leben) + " leben")
    while True: 
        print("Möchtest du nach links oder rechts gehen?")
        direction = input("")
        if direction == "links":
            print(name + " du bist in einer Grube voller AIDS Nadeln gefallen , du stirbst an einem langsamen quallvollen, schreckllichen Tod, eine Nadel STößt direkt in dein Linkes Auge, und du siehst dein blut die Nadel runtertropfen. ENDE")
            return
        
        elif direction == "rechts":
            print("Du siehst ein Loch in der wand , perfekt für diene hand , du greift rein und merkst wie deine hand von rassierklingen geschnittenwerden . du ahst einnen schlüssel erhalten aber deine hand ist komplett zerfetzt.")
            leben -= 10
            print("leben= " + str(leben))
            break
        else:
            print("no correct input")
    print("Der schlüssel passt in einer kleine tür rein wo du dich gerade so durchquetschen kannst , auf der anderen seite befindet sich einh Fernseher , willst du ihn anschalten ? ja oder nein ?")
    while True:
        choice = input("")
        if choice == "ja":
            print("Der Fernsehr zeigt eine dir bekannt aussehnde Person , aber du erkennst sie nicht richtig , du weist das du sie schonmal irgendwo gesehen hast...aber wo... . Bei genauem hinsehen erkennst du das es ein Schulfreund aus alten Tagen ist.  ")
            break
        elif choice == "nein":
            print("Die tür hinter dir knallt zu, du stehst in dem leeren raum, es ist still, sher still, die kalten bleichen wände scheinen trüb und das tropfen der abwasserrohre werden immer lauter. Du siehst dir den Fernsehr an aber schaltest ihn nicht an und wartest...gefangen in isolation..allein..")
            break
        else:
            print("no correct input")
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
                print("Du schaust das Loch ängstlich an, greifst nicht rein und beobachtest weiter deinen Schulkameraden im Fernseher...")
            print("Du hörst laute schreie und springts auf. ")
game()