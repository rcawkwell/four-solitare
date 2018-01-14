#! /usr/bin/env python

import math 
import random, itertools
from collections import deque 


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

class Stack(deque): 
	'''
	The stack represents one of the four piles that the player works on 
	Only one card can be removed from the stack at a time 
	'''
	def __init__(self): 
		super().__init__()
	def add(self, card): 
		self.append(card)
	def isEmpty(self): 
		return not self 
	def clear(self): 
		self[:] = []
	def grab (self): 
		answer = self.pop()
		return answer 

class Game: 
	def __init__(self): 
		self.deck = deque()
		self.createDeck()
		self.pile1 = Stack()
		self.pile2 = Stack()
		self.pile3 = Stack()
		self.pile4 = Stack()
		self.undoStack = Stack()
		self.deal()

	def shuffle(self): 
		random.shuffle(self.deck)	

	def createDeck(self): 
		for rank, suit in itertools.product(RANKLIST, SUITLIST):
			self.deck.append(Card(rank, suit))
		self.shuffle()

	def canDeal(self): 
		return not deck.isEmpty()
	def canUndo(self): 
		return not self.undoStack.isEmpty()
		
	def deal(self): 
		'''
		If the deck is empty, checkt to see if won 
		Else add a new card to each of the four piles 
		'''
		if self.deck.isEmpty():
			self.gameOver()
		else:  
			pile1.add(deck.pop())
			pile2.add(deck.pop())
			pile3.add(deck.pop())
			pile4.add(deck.pop())
	def gameOver(self): 
		''' 
		if the four piles each only have one card 
		then you have won the game
		'''
		pile1.pop(); 
		pile2.pop(); 
		pile3.pop(); 
		pile4.pop(); 
		if not pile1.isEmpty() and not pile2.isEmpty() and not pile3.isEmpty() and not pile4.isEmpty(): 
			return 'win' 
		return 'lost'
