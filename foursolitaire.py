#! /usr/bin/env python

import math 
import random, itertools
from collections import deque 
from python


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


class Stack(deque): 
   def __init__(self): 
  	super().__init__()
   def add(self, card): 
	self.append(card)
   def isEmpty(self): 
	return not self 
   def clear(self): 
	self[:] = []
   def grab (self) 
	answer = self.pop()
	return answer 
	
	     
