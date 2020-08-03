Project: CardGame.exe
Author: Alex Hamilton
Date: 30 April, 2016

Implementation---------------------------------------------------

-Getters of data members are implemented and used where needed

Card class
	-Ability to represent each card in a standard 52 card deck
	-Ace can be represented as either high or low
	-Default card is JOKER, which helps for error checking
	-Overloaded <, > operators to sort Cards by face value or suit
	
DeckOfCards class
	-Ability to store all 52 possible card representations in a vector
	-Ability to deal a single Card
	-Ability to shuffle deck using standard random shuffle
	-Ability return cards remaining in deck
	-Ability to check if there are cards left in the deck
	
HandOf5 class
	-Represents a hand as an integer array of 5 Cards
	-Constructed using a DeckOfCards to deal 5 Cards to the hand
	-Represents kickers in a vector of pairs since each hand has a different kicker size
	-Pairs in kickers are int index and int face
	-Able to store high card of hand, secondary high card of hand, and index of Cards to be drawn in draw hands
	-Able to if a hand represents each type of hand rank, up to royal flush (extra credit?)
	-Wrapper for access of hand data member
	-Can swap a Card given an index and a DeckOfCards to deal a new Card
	-Using a switch and enum type, can return the best rank of the hand
	-Can create a string that forms the predicate of the printed result
	
Dealer Class
	-Constructed using two hands and a deck
	-Can print a string deciding the winner and winning hand guven two hands
	-Intelligence dictating which cards the dealer should swap
	-Can change out for a fresh deck
		
Changelog 7-19-2020

	-Handof5.cc - New and updated functions lines 283 - 476
	-Dealer.cc - Updated priority queue for dealer draw AI lines 109-221
	-CardGame_driver.cc - new tests for 4 straight and 4 straight flush 149-259
	
To Do 7-19-2020:

New algorithms seem to work except is4StraightFlush() doesn't return false in the 
case where there is 4 to both a straight and a flush, but no straight 
flush draw - can't figure out why.

Further granulate AI - e.g. draw 3 when dealer has 2 high suited cards, 3 to royal flush - etc.

Graphical user interface

Testing tools










		




