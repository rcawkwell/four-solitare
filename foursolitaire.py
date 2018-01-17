#! /usr/bin/env python

import math 
import random, itertools
from collections import namedtuple 


BACKGROUND = 'lightblue'
HEARTS = 'Heart' 
DIAMONDS = 'Diamond' 
CLUBS = 'Club' 
SPADES = 'Spade' 
ACE = 1
JACK = 11
QUEEN = 12 
KING = 13

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
	def sameSuit(self, other): 
		if self.suit == other.suit: 
			return True
		return False
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
		else: 
			self.gameOver()
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
			return 'win' 
		return 'lost'
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
		print remove
		if remove == self.top1: 
			self.pile1.remove()
			self.top1 = self.pile1.peak() 
		elif remove == self.top2: 
			self.pile2.remove()
			self.top2 = self.pile2.peak()
		elif remove == self.top3: 
			self.pile3.remove()
			self.top3 = self.pile3.peak()
		elif remove == self.top4:
			self.pile4.remove()
			self.top3 = self.pile3.peak()

	def play(self): 
		while not self.deck.isEmpty():
			self.printTop()
			self.turn()		
			self.deal()


#Main function 
def main(): 
	g = SetUp()
	g.play()

if __name__ == '__main__': 
	main()
