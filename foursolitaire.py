#! /usr/bin/env python

import math 
import random, itertools
from collections import namedtuple 


HEARTS = 'Heart' 
DIAMONDS = 'Diamond' 
CLUBS = 'Club' 
SPADES = 'Spade' 
ACE = 1
JACK = 11
QUEEN = 12 
KING = 13
EMPTY = 'Empty'

SUITLIST = [HEARTS, DIAMONDS, SPADES, CLUBS]
RANKLIST = [ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING]

class Card:
	'''
	Each card has a corresponding rank and suit 
	Cards are only comparble if they are the same suit 
	Only one deck of cards so no need for equal
	''' 
	def __init__(self, rank, suit): 
		self.rank = rank
		self.suit = suit
		self.idt = self.makeID()
	def sameSuit(self, other): 
		if self.suit == other.suit: 
			return True
		return False
	def makeID(self): 
		idt = self.rank 
		if self.suit == HEARTS: 
			return idt 
		elif self.suit == DIAMONDS:
			idt += 13
			return idt
		elif self.suit == SPADES:
			idt += 26
			return idt
		else:
			idt += 39
			return idt
	#overload lesss than and greater than operators
	def __lt__(self, other): 
		if self.sameSuit(other): 
			if self.rank < other.rank: 
			    return True  
			else: 
			    return False
		return False
	def __gt__(self, other):
		if self.sameSuit(other): 
			if self.rank > other.rank: 
				return True 
			else: 
				return False
		return False
	def __str__(self): 
		return "%d of %s" %(self.rank, self.suit)

class Stack(list): 
	'''
	The stack represents one of the four piles that the player works on 
	Only one card can be removed from the stack at a time 
	'''
	def __init__(self): 
		super(Stack, self).__init__()
	def add(self, card): 
		self.append(card)
	def isEmpty(self): 
		return not self 
	def clear(self): 
		self[:] = []
	def peak (self): 
		if self.isEmpty():
			return EMPTY
		else:		
			answer = self[len(self)-1]
			return answer
	def remove(self): 
		self.pop()

class SetUp: 
	def __init__(self): 
		self.deck = Stack()
		self.createDeck()
		self.pile1 = Stack()
		self.pile2 = Stack()
		self.pile3 = Stack()
		self.pile4 = Stack()
		self.deal()
		self.top1 = self.pile1.peak()
		self.top2 = self.pile2.peak()
		self.top3 = self.pile3.peak()
		self.top4 = self.pile4.peak()
		print 'Pile 1\t\tPile 2\t\tPile 3\t\tPile 4\n'
	def shuffle(self): 
		random.shuffle(self.deck)	

	def createDeck(self): 
		for rank, suit in itertools.product(RANKLIST, SUITLIST):
			self.deck.append(Card(rank, suit))
		self.shuffle()

	def canDeal(self): 
		return not self.deck.isEmpty()
			
	def deal(self): 
		'''
		If the deck is empty, checkt to see if won 
		Else add a new card to each of the four piles 
		'''
		if self.canDeal():  
			self.pile1.add(self.deck.pop())
			self.top1 = self.pile1.peak()
			self.pile2.add(self.deck.pop())
			self.top2 = self.pile2.peak()
			self.pile3.add(self.deck.pop())
			self.top3 = self.pile3.peak()
			self.pile4.add(self.deck.pop())
			self.top4 = self.pile4.peak() 
	def gameOver(self): 
		''' 
		if the four piles each only have one card 
		then you have won the game
		'''
		self.pile1.pop(); 
		self.pile2.pop(); 
		self.pile3.pop(); 
		self.pile4.pop(); 
		if not self.pile1.isEmpty() and not self.pile2.isEmpty() and not self.pile3.isEmpty() and not self.pile4.isEmpty(): 
			print 'Yay, you won' 
#		print 'Sorry, you lost'
	def printTop(self):  
		print self.top1,
		print '\t', 
		print self.top2, 
		print '\t', 
		print self.top3, 
		print '\t', 
		print self.top4 
	def turn(self):
		remove = raw_input("Enter card to remove: ")
		while remove:
			prmv = remove.split(" ")
			rmvID = int(prmv[0])
			if prmv[2] == DIAMONDS: 
				rmvID += 13
			elif prmv[2] == SPADES: 
				rmvID += 26
			elif prmv[2] == CLUBS: 
				rmvID += 39
  
			if rmvID == self.top1.idt: 
				self.pile1.remove() 
				self.top1 = self.pile1.peak()  
			elif rmvID == self.top2.idt: 
				self.pile2.remove()
				self.top2 = self.pile2.peak()
			elif rmvID == self.top3.idt: 
				self.pile3.remove()
				self.top3 = self.pile3.peak()
			elif rmvID == self.top4.idt:
				self.pile4.remove()
				self.top4 = self.pile4.peak()
			self.printTop()
			remove = raw_input("Enter card to remove: ")
	def play(self): 
		while not self.deck.isEmpty():
			self.printTop()
			self.turn()		
			self.deal()
		self.gameOver()

#Main function 
def main(): 
	print 'Welcome to 4 Card Solitaire' 
	playing = raw_input("To play, type yes: ") 
	while playing == 'yes' :
		g = SetUp()
		g.play()
		playing = raw_input("Play again? Type yes: ")
if __name__ == '__main__': 
	main()
