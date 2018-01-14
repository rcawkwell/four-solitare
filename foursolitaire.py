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
	def __init__(self, rank, suit): 
		self.rank = rank
		self.suit = suit
	#only comparable if same suit
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
		self.createCards()
		self.stock1 = Stack()
		self.stock2 = Stack()
		self.stock3 = Stack()
		self.stock4 = Stack()
		self.deal()

	def shuffle(self): 
		random.shuffle(self.deck)	

	def createCards(self): 
		for rank, suit in itertools.product(RANKLIST, SUITLIST):
			self.deck.append(Card(rank, suit))

	#def deal(self): 
	'''
	if deck is empty 
	    self.gameOver() 
	if deck isnt empty 
	    for the four piles
	        pop deck and add to a pile 
	'''

	def gameOver(self): 
		''' 
		if the four piles each only have one card 
		then you have won the game
		so pop the stack and then check if it is empty
		'''
		stock1.pop(); 
		stock2.pop(); 
		stock3.pop(); 
		stock4.pop(); 
		if not stock1.isEmpty() and not stock2.isEmpty() and not stock3.isEmpty() and not stock4.isEmpty(): 
			return win 
		return lost
