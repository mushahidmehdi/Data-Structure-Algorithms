# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.

import unittest

def capitalize(inp: str):
	wordList = [word[0].upper() + word[1:] for word in inp.split()]
	return ' '.join(wordList)


def main():
	print(capitalize('1 w 2 r 3g'))


class CapitalizeTest(unittest.TestCase):
	def test_capitalize(self):
		self.assertEqual(capitalize('132 456 Wq m e'), '132 456 Wq M E')
		self.assertEqual(capitalize('q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J K L Z X C V B N M'), 'Q W E R T Y U I O P A S D F G H J K L Z X C V B N M Q W E R T Y U I O P A S D F G H J K L Z X C V B N M')
		self.assertEqual(capitalize('1 2 2 3 4 5 6 7 8 9'), '1 2 2 3 4 5 6 7 8 9')
		self.assertEqual(capitalize('1 w 2 r 3g'), '1 W 2 R 3g')
 
if __name__ == '__main__':
	unittest.main()