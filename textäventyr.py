namn = input("Vad heter du? ")
print(f"hej {namn}")
print(f"{namn} du ska ta dig till skolan för att göra ett prov")
print(f"{namn} ditt alarm ringer, Du ska ta dig till skolan.")
print("Gör egna val för att klara skolan")
val1 = input("Klockan är 07:00 (snooza) eller (stig upp)? ")
if val1.lower() == "snooza":
    print("Du somnar om")
    val2 = input("klockan ringer 07:15 (snooza) eller (stiga upp)? ")
    if val2.lower() == "snooza":
        print("Du somnar om")
        val3 = input("klockan ringer 07:30 (snooza) eller (stiga upp)? ")
        if val3.lower() == "snooza":
            print("Du somnar om")
            exit("Du hinner inte latmask")
        elif val3.lower() == "stiga upp":
            print("Du stiger upp och är väldigt pigg men har brottom")
        val7 = input("(Duschar) du, äter du (frukost) eller ger du dig av till (skolan)")
        if val7.lower() == "duschar":
            exit("Du är för pigg och råkar vrida temperaturen till max och brinner upp")
        elif val7.lower() == "frukost":
            exit("Du väljer att göra en omelett men den tar för lång tid och du missar provet")
        elif val7.lower() == "skolan":
            val9 = input("Hur tar du dig till skolan. (buss), (cyckel), (gå)? ")
            if val9.lower() == "buss":
                exit("Du hinner till privet och får ett B")
            elif val9.lower() == "cyckel":
                exit("Du hinner till provet men du har inte mycket energi och får ett C")
            elif val9.lower() == "gå":
                exit("du hann inte till provet")     
    elif val2.lower() == "stiga upp":
        print("Du stiger upp och är pigg")
        val10 = input("Vill du Duscha och göra (frukost) eller ge dig iväg till (skolan)")
        if val10.lower() == "frukost":
            exit("Du gör två ost och skinkmackor och sen åker du buss till skolan och gör provet och får ett B")
        elif val10.lower() == "skolan":
            print("Hur tar du dig till skolan")
            val11 = input("(buss), (cykel) eller (gå)")
            if val11.lower() == "gå":
                exit("du han inte")
            elif val11.lower() == "cykel":
                exit("Du kom till skolan och gör ett bra prov. B ")
            elif val11.lower() == "buss":
                print("Du hann till skolan och skrev ett c på provet")
elif val1.lower() == "stig upp":
    print("Du är trött men du stiger upp")
    val4 = input("(Duschar) du gör du (frukost) eller ger du dig av till (skolan).")
    if val4.lower() == "duschar":
        print ("du dushar klockan är nu 07:15")
        val5 = input("vill du göra (frukost) eller ge dig iväg till (skolan)")
        if val5.lower() == "frukost":
            print("Du gör gröt och ätit färdigt kl 07:45")
            val6 = input("Åker du buss, går du eller cyklar du? ")
            if val6.lower() == "bus":
                exit("Du missa bussen och du han inte till provet")
            elif val6.lower() == "går":
                exit("Du han inte till skolan, du missa provet")
            elif val6.lower() == "cyklar":
                exit("Du han till provet men du fick bara ett D")
            else:
                exit("du dog av fel skrivning")
        else: 
            exit("du har för lite energi och du dog")
    elif val4.lower() == "frukost":
        print("Du gör en smarrig omelett klockan är 07:20 efter att du ätit upp omeletten")
        print("Nu ska du till skolan") 
        val8 = input("Åker du (buss), (cykel) eller (går) du? ")
        if val8.lower() == "buss":
            exit("Bussen missade din hållplats och du springer till skolan och är helt slut och du får ett c på provet")
        elif val8.lower() == "cykel":
            print("Du hann till provet och fick A")
            exit("Du vann!!")
        elif val8.lower() == "går":
            exit("Du han inte till provet")
    else:
        exit("Du är för trött och har inge energi, Du dog.")
else:
    exit("det finns inte som alternativ gör om gör rätt")
