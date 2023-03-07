import random
import copy

list_word=["aladin"]

def choose_word():
    rand_word=random.choice(list_word)
    lettre_list = []
    for lettre in rand_word:
        lettre_list.append(lettre)
    return(lettre_list)

def word_try(espace):
    print(espace)
    test_word = input()
    return(test_word)

def len_word(test_word, letter_list):
    if len(test_word) == len(letter_list):
        return 1
    else:
        print("il faut un mot de ",len(letter_list)," caractères")
        return 0
        
def good_word(test_word, lettre_list):
    lettre_include = []
    gd_lettre = 0
    l = copy.deepcopy(lettre_list)
    for i in range (len(test_word)):    
        if test_word[i] in l:
            if i == l.index(test_word[i]):
                print(test_word[i], " ", end="")
                gd_lettre += 1
                l[i] = "0"
            else:
                lettre_include.append(test_word[i])
                print("# ", end="")
        else:
            print("# ", end="")
#    print(lettre_list)        
    nouvelle_liste = []
    for element in lettre_include:
        if element in l and element not in nouvelle_liste:
            nouvelle_liste.append(element)
    if nouvelle_liste == []:
        print('\n')
        return(gd_lettre)
    else:
        print(nouvelle_liste)
        return(gd_lettre)


def principal():
    word_choose = choose_word()
    espace = "_ " * len(word_choose)
    cpt = 0
    find = False
    while cpt < 5:
        word = word_try(espace)
        while len_word(word, word_choose) != 1:
            word = word_try(espace)
#        print(word, word_choose)
        c = good_word(word, word_choose)
        if c == len(word_choose):
            cpt = 5
            find = True
        else:
            cpt = cpt + 1             
    if find == True:
        print("Bien joué tu as trouvé le mot")
    else:
        print("dommage, le mot était ", end="")
        for i in word_choose:
            print(i, end="")
    rejouer()

def rejouer():
    choix = input("Veux tu rejouer ? ['oui'] ou ['non'] ")
    if choix == "oui":
        principal()

principal()