namn = input("Vad heter du?")
print(f"hej {namn}")
print("Alarmet ringer, Du ska ta dig till skolan.")
print("Gör egna val för att klara skolan")
val1 = input("Klockan är 07:00 snooza eller stig upp? ")

if val1 == ("snooza"):
    print("Du somnar om")
    val2 = input("klockan ringer 07:15 snoozar du eller stiger du upp? ")
    if val2 == ("snooza"):
        print("Du somnar om")
        val3 = input("klockan ringer 07:30 snoozar du eller stiger du upp? ")
        if val3 == ("snooza"):
            print("Du somnar om")
            exit("Du hunner inte latmask")
        else:
            print("Du stiger upp och är väldigt pigg men har brottom")
            #skriv här
    else:
        print("Du stiger upp och är pigg")
        #skri här
else:
    print("Du är trött men du stiger upp")
    val4 = input("Duschar du gör du frukost eller ger du dig av till skolan.")
    if val4 == ("duschar"):
        print ("du dushar klockan är nu 07:15")
        val5 = input("vill du göra frukost eller ge dig iväg till skolan")
        if val5 == ("frukost"):
            print("Du gör gröt och ätit färdigt kl 07:45")
            val6 = input("Åker du buss, går du eller cyklar du? ")
            if val6 == ("bus"):
                exit("Du missa bussen och du han inte till provet")
            elif val6 == ("går"):
                exit("Du han inte till skolan, du missa provet")
            elif val6 == ("cyklar"):
                exit("Du han till provet men du fick bara ett D")
            else:
                exit("du dog av fel skrivning")
                #klar här
        else: 
            exit("du har för lite energi och du dog")
    elif val4 == ("frukost"):
        print("Du gör en smarrig omelett klockan är 07:20 efter att du ätit upp omeletten")
        print("Nu ska du till skolan") 
        #skriv mer din fan
        valx = input("Åker du buss, går du eller cyklar du? ")
    else:
        exit("Du är för trött och har inge energi, Du dog.")


