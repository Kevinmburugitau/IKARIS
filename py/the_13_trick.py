# this is a program in python to do the 13 trick a.k.a the power of 13
def King ():
    king =13
    if value == 13 :
        print("King")

def Queen ():
    Queen =12
    if value == 12 :
        print("Queen")

def Jack ():
    Jack =11
    if value == 11 :
        print("Jack")

def Ace ():
    Ace =1
    if value == 1 :
        print("Ace")

print("You'll need a full deck of cards")
input("")
print("Remove the jokers")
input("")
full_deck = 52

#the trick begins

# King = 13
#Queen = 12
#Jack = 11
#Ace = 1

#the rest of the cards have the same value as the face value
print("shuffle the deck and hold them face down")
input("")
print("deal the top card face up")
input("")
#deal_1 = input("enter it's value: ")

print("deal up to 13 cards from the value of the first card,group and flip'em")
input("")
print("repeat till you get the value 13 counting from the first card if not hold the remainder")
input("")
print("pick 3 random groups from the groups")
input("")
print("pick up the remainder groups and add to the remainder cards at hand")
input("")
print("from the slected three pick two at random")
input("")
print("flip the top card of the two groups to reveal their value")
input("")
print("add 10 + value of both cards")

value_card_1 = input("value of card 1: ")
value_card_2 = input("value of card 2: ")

magic_math = 10 + int(value_card_1) + int(value_card_2)

print("from the remainder group deal " + str(magic_math) + " cards" )

magic = int(input("how many cards are at hand? "))

if magic == King:
    magic = str("King")
 #   king()

if magic == Queen:
    magic = str("Queen")
 #   Queen()

if magic == Jack:
    magic = str("Jack")
 #   Jack()

if magic == Ace:
    magic = str("Ace")
 #   Ace()
input("")
print("the face value of the top card from the unrevealed group is " + str(magic))
