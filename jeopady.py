import random

#koda gurch kortspel 1v1
print("hej, är ni redå för Gursh!?")
spelare1 = input("Vad heter första spelaren? ")
spelare2 = input("vad heter andra spelare? ")
input(f"{spelare2} kolla bort nu så att {spelare1} kan se sina kort ifred")
print("Du fick")

kort1 = ["A♡","2♡","3♡","4♡","5♡","6♡","7♡","8♡","9♡","10♡","Kn♡","Q♡","K♡","A♤","2♤","3♤","4♤","5♤","6♤","7♤","8♤","9♤","10♤","Kn♤","Q♤","K♤","A♧","2♧","3♧","4♧","5♧","6♧","7♧","8♧","9♧","10♧","Kn♧","Q♧","K♧","A♢","2♢","3♢","4♢","5♢","6♢","7♢","8♢","9♢","10♢","Kn♢","Q♢","K♢",]
random.shuffle(kort1)
drag1 = kort1.pop()
print(drag1)
random.shuffle(kort1)
drag2 = kort1.pop()
print(drag2)
random.shuffle(kort1)
drag3 = kort1.pop()
print(drag3)
random.shuffle(kort1)
drag4 = kort1.pop()
print(drag4)
random.shuffle(kort1)
drag5 = kort1.pop()
print(drag5)
random.shuffle(kort1)
drag6 = kort1.pop()
print(drag6)

input(f"Nu får du kolla bort så kan {spelare2} se sin kort")
print("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Du fick")

random.shuffle(kort1)
drag13 = kort1.pop()
print(drag13)
random.shuffle(kort1)
drag12 = kort1.pop()
print(drag12)
random.shuffle(kort1)
drag8 = kort1.pop()
print(drag8)
random.shuffle(kort1)
drag9 = kort1.pop()
print(drag9)
random.shuffle(kort1)
drag10 = kort1.pop()
print(drag10)
random.shuffle(kort1)
drag11 = kort1.pop()
print(drag11)
#Slumpa ett till kort till varje spelare
input("Nu kan båda kolla igen")
input("Nu får ni ett till kort vars och den som har högst börjar spela. Det här korten får båda se.")
print(f"{spelare1} fick")
random.shuffle(kort1)
drag7 = kort1.pop()
print(drag7)
print(f"{spelare2} fick")
random.shuffle(kort1)
drag14 = kort1.pop()
print(drag14)
if drag7 > drag14:
    print(f"{spelare1} börjar")
elif drag7 == drag7:
    print("det blev lika, jag slumpar vem som börjar")
    börjar = random.randint(1,2)
    if börjar == 1:
        print(f"{spelare1} börjar")
    elif börjar == 1:
       print(f"{spelare2} börjar") 
elif drag7 < drag14:
    print(f"{spelare2} börjar") 

#Om spelare1 kort är högre print(spelare1 börjar) annars print(spellare två börjar)

