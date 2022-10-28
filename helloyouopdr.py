rungame = 0

while rungame == 0:
    print("Je wordt wakker in een donkere kamer en je kijkt om je heen. Je ziet weinig, maar je ziet wel wat licht onder een deur vandaan komen. Je blijft nog even in bed liggen en je herinnert je dat je gisteren bij een feestje was en dat dit het huis van een van je vrienden is, je was erg dronken en kon niet zelf naar huis. Je kijkt hoe laat het is. Het is al 13.00, ineens herinner jij je ook at je om 17.00 een sollicitatiegesprek hebt en je enige nette blousse ligt nog thuis. Je staat snel op en moet een keuze maken die de rest van je leven zal beinvloeden.")
    print("A. Eet ontbijt.")
    print("B. Eet geen ontbijt.")

    userinput0 = input("Wat doe je? ")

    if userinput0 == ("A") or ("a"):
        print("Je eet een lekker ontbijtje (fruit loops en sinaasappel sap), je kleedt je aan, poetst je tanden en rent snel naar buiten.")
        print("A. Gebruik google maps om je weg naar huis te vinden.")
        print("B. Gebruik een kaart om je weg naar huis te vinden.")
        print("C. Ga op gevoel naar huis.")

        userinput1 = input("Wat doe je nu? ")

        if userinput1 == ("A") or ("a"):
            print("Je telefoon is na een tijdje leeg.")
            print("A. Vraag een oud vrouwtje waar de weg naar huis is.")
            print("B. Vraag een verdachte man de weg naar huis.")
            print("C. Ga verder op gevoel.")

            userinput2 = input("Wat doe je nu? ")

            if userinput2 == ("A") or userinput2 == ("a"):
                print("Ze wijst je de weg naar huis, je komt veilig thuis en je komt op tijd bij je sollicitatiegesprek en je wordt aangenomen.")
                print("[GOOD ENDING UNLOCKED]")

            elif userinput2 == ("B") or userinput2 == ("b"):
                print("De verdachte man geeft je een paar instructies en je volgt die. Uiteindelij kom je terecht in een donker steegje en 3 guys willen je portomonnee.")
                print("A. Je geeft je portomonnee af.")
                print("B. Je weigert je portomonnee te geven.")
                print("C. Je rent zo snel mogelijk weg.")

                userinput3 = input("Wat doe je nu? ")

                if userinput3 == ("A") or userinput3 == ("a"):
                    print("Ze laten je gaan en nu moet je weer je weg naar huis vinden.")
                    print("A. Je vraagt een oud vrouwtje omn de weg naar huis.")
                    print("B. Je gaat verder op gevoel naar huis.")

                    userinput4 = input("Wat doe je nu? ")

                    if userinput4 == ("A") or userinput4 == ("a"):
                        print("Het oude vrouwtje geeft je goede instructies en je komt veilig thuis. Helaas wordt je niet aangenomen omdat je je ID niet bij je hebt.")
                        print("[NEUTRAL ENDING UNLOCKED]")

                    elif userinput4 == ("B") or userinput4 == ("b"):
                        print("Je raakt al snel verdwaald en je weet niet wat de weg terug naar huis is. Je bevind jezelf in de wildernis.")
                        print("A. Je probeert nog verder je weg naar huis te vinden.")
                        print("B. Je wacht op hulp.")

                        userinput3 = input("Wat doe je nu? ")

                        if userinput3 == ("A") or userinput3 == ("A"):
                            print("Je raakt nog meer de weg kwijt en je hebt totaal geen idee wat je nu moet doen.")
                            print("A. Je wacht op hulp.")
                            print("B. Je geeft je weg naar huis zoeken op en je start een nieuw leven in de wildernis.")

                            userinput4 = input("Wat doe je nu? ")

                            if userinput4 == ("A") or userinput4 == ("a"):
                                print("Je wacht heel lang op hulp maar niemand komt je redden. Je sterft uiteindelijk van de honger.")
                                print("[LOST ENDING UNLOCKED]")

                            elif userinput4 == ("B") or userinput4 == ("b"):
                                print("Je start een nieuw leven in de wildernis als nomaad en je vindt dit veel fijner dan als een simpele 9 to 5'er leven.")
                                print("[BLISS ENDING UNLOCKED]")

                        elif userinput3 == ("B") or userinput3 == ("b"):
                            print("Je wacht op hulp en je wordt na een paar dagen gevonden door je politie.")
                            print("[LOST AND FOUND ENDING UNLOCKED]")

                elif userinput3 == ("B") or userinput3 == ("b"):
                    print("Ze steken je neer en pakken nog steeds je portomonne :/")
                    print("[BAD ENDING UNLOCKED]")

                elif userinput3 == ("C") or userinput3 == ("c"):
                    print("Je probeert weg te rennen maar je wordt tegen gehouden en ze steken je met een mes en ze stelen nog steeds je portomonnee.")
                    print("[BAD ENDING UNLOCKED]")

            elif userinput2 == ("C") or userinput2 == ("c"):
                print("Je raakt al snel verdwaald en je weet niet wat de weg terug naar huis is. Je bevind jezelf in de wildernis.")
                print("A. Je probeert nog verder je weg naar huis te vinden.")
                print("B. Je wacht op hulp.")

                userinput3 = input("Wat doe je nu? ")

                if userinput3 == ("A") or userinput3 == ("A"):
                    print("Je raakt nog meer de weg kwijt en je hebt totaal geen idee wat je nu moet doen.")
                    print("A. Je wacht op hulp.")
                    print("B. Je geeft je weg naar huis zoeken op en je start een nieuw leven in de wildernis.")

                    userinput4 = input("Wat doe je nu? ")

                    if userinput4 == ("A") or userinput4 == ("a"):
                        print("Je wacht heel lang op hulp maar niemand komt je redden. Je sterft uiteindelijk van de honger.")
                        print("[LOST ENDING UNLOCKED]")

                    elif userinput4 == ("B") or userinput4 == ("b"):
                        print("Je start een nieuw leven in de wildernis als nomaad en je vindt dit veel fijner dan als een simpele 9 to 5'er leven.")
                        print("[BLISS ENDING UNLOCKED]")

                elif userinput3 == ("B") or userinput3 == ("b"):
                    print("Je wacht op hulp en je wordt na een paar dagen gevonden door je politie.")
                    print("[LOST AND FOUND ENDING UNLOCKED]")

        elif userinput1 == ("B") or userinput1 == ("b"):
            print("De kaart is heel oud en je komt op de verkeerde plek terecht. Je bent in een donker steegje en 3 guys willen je portomonnee.")
            print("A. Je geeft je portomonnee af.")
            print("B. Je weigert je portomonnee te geven.")
            print("C. Je rent zo snel mogelijk weg.")

            userinput2 = input("Wat doe je nu? ")

            if userinput2 == ("A") or userinput2 == ("a"):
                print("Ze laten je gaan en nu moet je weer je weg naar huis vinden.")
                print("A. Je vraagt een oud vrouwtje omn de weg naar huis.")
                print("B. Je gaat verder op gevoel naar huis.")
                
                userinput3 = input("Wat doe je nu? ")

                if userinput3 == ("A") or userinput3 == ("a"):
                    print("Het oude vrouwtje geeft je wel de goede instructies en je komt veilig thuis. Je wordt helaas niet aangenomen omdat je je ID mist.")
                    print("[NEUTRAL ENDING UNLOCKED]")
                
                elif userinput3 == ("B") or userinput3 == ("b"):
                    print("Je raakt al snel verdwaald en je weet niet wat de weg terug naar huis is. Je bevind jezelf in de wildernis.")
                    print("A. Je probeert nog verder je weg naar huis te vinden.")
                    print("B. Je wacht op hulp.")

                    userinput3 = input("Wat doe je nu? ")

                    if userinput3 == ("A") or userinput3 == ("A"):
                        print("Je raakt nog meer de weg kwijt en je hebt totaal geen idee wat je nu moet doen.")
                        print("A. Je wacht op hulp.")
                        print("B. Je geeft je weg naar huis zoeken op en je start een nieuw leven in de wildernis.")

                        userinput4 = input("Wat doe je nu? ")

                        if userinput4 == ("A") or userinput4 == ("a"):
                            print("Je wacht heel lang op hulp maar niemand komt je redden. Je sterft uiteindelijk van de honger.")
                            print("[LOST ENDING UNLOCKED]")

                        elif userinput4 == ("B") or userinput4 == ("b"):
                            print("Je start een nieuw leven in de wildernis als nomaad en je vindt dit veel fijner dan als een simpele 9 to 5'er leven.")
                            print("[BLISS ENDING UNLOCKED]")

                    elif userinput3 == ("B") or userinput3 == ("b"):
                        print("Je wacht op hulp en je wordt na een paar dagen gevonden door je politie.")
                        print("[LOST AND FOUND ENDING UNLOCKED]")

            elif userinput2 == ("B") or userinput2 == ("b"):
                print("Ze steken je neer en pakken nog steeds je portomonnee.")
                print("[BAD ENDING UNLOCKED]")

            elif userinput2 == ("C") or userinput2 == ("c"):
                print("Ze kunnen je inhalen en steken je dood en pakken nog steeds je portomonnee.")
                print("[BAD ENDING UNLOCKED]")

        elif userinput1 == ("C") or userinput1 == ("c"):
                print("Je raakt al snel verdwaald en je weet niet wat de weg terug naar huis is. Je bevind jezelf in de wildernis.")
                print("A. Je probeert nog verder je weg naar huis te vinden.")
                print("B. Je wacht op hulp.")

                userinput3 = input("Wat doe je nu? ")

                if userinput3 == ("A") or userinput3 == ("A"):
                    print("Je raakt nog meer de weg kwijt en je hebt totaal geen idee wat je nu moet doen.")
                    print("A. Je wacht op hulp.")
                    print("B. Je geeft je weg naar huis zoeken op en je start een nieuw leven in de wildernis.")

                    userinput4 = input("Wat doe je nu? ")

                    if userinput4 == ("A") or userinput4 == ("a"):
                        print("Je wacht heel lang op hulp maar niemand komt je redden. Je sterft uiteindelijk van de honger.")
                        print("[LOST ENDING UNLOCKED]")

                    elif userinput4 == ("B") or userinput4 == ("b"):
                        print("Je start een nieuw leven in de wildernis als nomaad en je vindt dit veel fijner dan als een simpele 9 to 5'er leven.")
                        print("[BLISS ENDING UNLOCKED]")

                elif userinput3 == ("B") or userinput3 == ("b"):
                    print("Je wacht op hulp en je wordt na een paar dagen gevonden door je politie.")
                    print("[LOST AND FOUND ENDING UNLOCKED]")
        



    if userinput0 == ("B") or userinput0 == ("b"):
        print("Je hebt heel veel strek maar je kiest er nog steeds voor om geen ontbijt te eten. Je kleed je aan, je poetst je tanden en je vertrekt snel van huis.")
        print("A. Gebruik google maps om je weg naar huis te vinden.")
        print("B. Gebruik een kaart om je weg naar huis te vinden.")
        print("C. Ga op gevoel naar huis.")

        userinput1 = input("Wat doe je nu? ")

        if userinput1 == ("A") or ("a"):
            print("Je telefoon is na een tijdje leeg.")
            print("A. Vraag een oud vrouwtje waar de weg naar huis is.")
            print("B. Vraag een verdachte man de weg naar huis.")
            print("C. Ga verder op gevoel.")

            userinput2 = input("Wat doe je nu? ")

            if userinput2 == ("A") or userinput2 == ("a"):
                print("Ze wijst je de weg naar huis, je komt veilig thuis en je komt op tijd bij je sollicitatiegesprek en je wordt aangenomen.")
                print("[GOOD ENDING UNLOCKED]")

            elif userinput2 == ("B") or userinput2 == ("b"):
                print("De verdachte man geeft je een paar instructies en je volgt die. Uiteindelij kom je terecht in een donker steegje en 3 guys willen je portomonnee.")
                print("A. Je geeft je portomonnee af.")
                print("B. Je weigert je portomonnee te geven.")
                print("C. Je rent zo snel mogelijk weg.")

                userinput3 = input("Wat doe je nu? ")

                if userinput3 == ("A") or userinput3 == ("a"):
                    print("Ze laten je gaan en nu moet je weer je weg naar huis vinden.")
                    print("A. Je vraagt een oud vrouwtje omn de weg naar huis.")
                    print("B. Je gaat verder op gevoel naar huis.")

                    userinput4 = input("Wat doe je nu? ")

                    if userinput4 == ("A") or userinput4 == ("a"):
                        print("Het oude vrouwtje geeft je goede instructies en je komt veilig thuis. Helaas wordt je niet aangenomen omdat je je ID niet bij je hebt.")
                        print("[NEUTRAL ENDING UNLOCKED]")

                    elif userinput4 == ("B") or userinput4 == ("b"):
                        print("Je raakt al snel verdwaald en je weet niet wat de weg terug naar huis is. Je bevind jezelf in de wildernis.")
                        print("A. Je probeert nog verder je weg naar huis te vinden.")
                        print("B. Je wacht op hulp.")

                        userinput3 = input("Wat doe je nu? ")

                        if userinput3 == ("A") or userinput3 == ("A"):
                            print("Je raakt nog meer de weg kwijt en je hebt totaal geen idee wat je nu moet doen.")
                            print("A. Je wacht op hulp.")
                            print("B. Je geeft je weg naar huis zoeken op en je start een nieuw leven in de wildernis.")

                            userinput4 = input("Wat doe je nu? ")

                            if userinput4 == ("A") or userinput4 == ("a"):
                                print("Je wacht heel lang op hulp maar niemand komt je redden. Je sterft uiteindelijk van de honger.")
                                print("[LOST ENDING UNLOCKED]")

                            elif userinput4 == ("B") or userinput4 == ("b"):
                                print("Je start een nieuw leven in de wildernis als nomaad en je vindt dit veel fijner dan als een simpele 9 to 5'er leven.")
                                print("[BLISS ENDING UNLOCKED]")

                        elif userinput3 == ("B") or userinput3 == ("b"):
                            print("Je wacht op hulp en je wordt na een paar dagen gevonden door je politie.")
                            print("[LOST AND FOUND ENDING UNLOCKED]")

                elif userinput3 == ("B") or userinput3 == ("b"):
                    print("Ze steken je neer en pakken nog steeds je portomonne :/")
                    print("[BAD ENDING UNLOCKED]")

                elif userinput3 == ("C") or userinput3 == ("c"):
                    print("Je probeert weg te rennen maar je wordt tegen gehouden en ze steken je met een mes en ze stelen nog steeds je portomonnee.")
                    print("[BAD ENDING UNLOCKED]")

            elif userinput2 == ("C") or userinput2 == ("c"):
                print("Je raakt al snel verdwaald en je weet niet wat de weg terug naar huis is. Je bevind jezelf in de wildernis.")
                print("A. Je probeert nog verder je weg naar huis te vinden.")
                print("B. Je wacht op hulp.")

                userinput3 = input("Wat doe je nu? ")

                if userinput3 == ("A") or userinput3 == ("A"):
                    print("Je raakt nog meer de weg kwijt en je hebt totaal geen idee wat je nu moet doen.")
                    print("A. Je wacht op hulp.")
                    print("B. Je geeft je weg naar huis zoeken op en je start een nieuw leven in de wildernis.")

                    userinput4 = input("Wat doe je nu? ")

                    if userinput4 == ("A") or userinput4 == ("a"):
                        print("Je wacht heel lang op hulp maar niemand komt je redden. Je sterft uiteindelijk van de honger.")
                        print("[LOST ENDING UNLOCKED]")

                    elif userinput4 == ("B") or userinput4 == ("b"):
                        print("Je start een nieuw leven in de wildernis als nomaad en je vindt dit veel fijner dan als een simpele 9 to 5'er leven.")
                        print("[BLISS ENDING UNLOCKED]")

                elif userinput3 == ("B") or userinput3 == ("b"):
                    print("Je wacht op hulp en je wordt na een paar dagen gevonden door je politie.")
                    print("[LOST AND FOUND ENDING UNLOCKED]")

        elif userinput1 == ("B") or userinput1 == ("b"):
            print("De kaart is heel oud en je komt op de verkeerde plek terecht. Je bent in een donker steegje en 3 guys willen je portomonnee.")
            print("A. Je geeft je portomonnee af.")
            print("B. Je weigert je portomonnee te geven.")
            print("C. Je rent zo snel mogelijk weg.")

            userinput2 = input("Wat doe je nu? ")

            if userinput2 == ("A") or userinput2 == ("a"):
                print("Ze laten je gaan en nu moet je weer je weg naar huis vinden.")
                print("A. Je vraagt een oud vrouwtje omn de weg naar huis.")
                print("B. Je gaat verder op gevoel naar huis.")
                
                userinput3 = input("Wat doe je nu? ")

                if userinput3 == ("A") or userinput3 == ("a"):
                    print("Het oude vrouwtje geeft je wel de goede instructies en je komt veilig thuis. Je wordt helaas niet aangenomen omdat je je ID mist.")
                    print("[NEUTRAL ENDING UNLOCKED]")
                
                elif userinput3 == ("B") or userinput3 == ("b"):
                    print("Je raakt al snel verdwaald en je weet niet wat de weg terug naar huis is. Je bevind jezelf in de wildernis.")
                    print("A. Je probeert nog verder je weg naar huis te vinden.")
                    print("B. Je wacht op hulp.")

                    userinput3 = input("Wat doe je nu? ")

                    if userinput3 == ("A") or userinput3 == ("A"):
                        print("Je raakt nog meer de weg kwijt en je hebt totaal geen idee wat je nu moet doen.")
                        print("A. Je wacht op hulp.")
                        print("B. Je geeft je weg naar huis zoeken op en je start een nieuw leven in de wildernis.")

                        userinput4 = input("Wat doe je nu? ")

                        if userinput4 == ("A") or userinput4 == ("a"):
                            print("Je wacht heel lang op hulp maar niemand komt je redden. Je sterft uiteindelijk van de honger.")
                            print("[LOST ENDING UNLOCKED]")

                        elif userinput4 == ("B") or userinput4 == ("b"):
                            print("Je start een nieuw leven in de wildernis als nomaad en je vindt dit veel fijner dan als een simpele 9 to 5'er leven.")
                            print("[BLISS ENDING UNLOCKED]")

                    elif userinput3 == ("B") or userinput3 == ("b"):
                        print("Je wacht op hulp en je wordt na een paar dagen gevonden door je politie.")
                        print("[LOST AND FOUND ENDING UNLOCKED]")

            elif userinput2 == ("B") or userinput2 == ("b"):
                print("Ze steken je neer en pakken nog steeds je portomonnee.")
                print("[BAD ENDING UNLOCKED]")

            elif userinput2 == ("C") or userinput2 == ("c"):
                print("Ze kunnen je inhalen en steken je dood en pakken nog steeds je portomonnee.")
                print("[BAD ENDING UNLOCKED]")

        elif userinput1 == ("C") or userinput1 == ("c"):
                print("Je raakt al snel verdwaald en je weet niet wat de weg terug naar huis is. Je bevind jezelf in de wildernis.")
                print("A. Je probeert nog verder je weg naar huis te vinden.")
                print("B. Je wacht op hulp.")

                userinput3 = input("Wat doe je nu? ")

                if userinput3 == ("A") or userinput3 == ("A"):
                    print("Je raakt nog meer de weg kwijt en je hebt totaal geen idee wat je nu moet doen.")
                    print("A. Je wacht op hulp.")
                    print("B. Je geeft je weg naar huis zoeken op en je start een nieuw leven in de wildernis.")

                    userinput4 = input("Wat doe je nu? ")

                    if userinput4 == ("A") or userinput4 == ("a"):
                        print("Je wacht heel lang op hulp maar niemand komt je redden. Je sterft uiteindelijk van de honger.")
                        print("[LOST ENDING UNLOCKED]")

                    elif userinput4 == ("B") or userinput4 == ("b"):
                        print("Je start een nieuw leven maar gaat al snel dood van de honger omdat je geen ontbijt hebt gegeten.")
                        print("[STARVED ENDING UNLOCKED]")

                elif userinput3 == ("B") or userinput3 == ("b"):
                    print("Je wacht op hulp maar je gaat snel dood van de honger omdat je geen ontbijt gegeten hebt.")
                    print("[STARVED ENDING UNLOCKED]")


    restart = input ("Opnieuw beginnen? Ja/Nee J/N ")
    if restart == "Ja" or restart == "J" or restart == "j" or restart == "ja":
        rungame = 0

    else:
        print("okie dokie")
        exit()