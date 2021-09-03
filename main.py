#!/usr/bin/env python3

import wave
import numpy as np



class Main():
	wr = wave.open("House2_Lead.wav", 'r')
	
	
	def __init__(self):
		print("init")
		par = list(self.wr.getparams())
		
if __name__ == "__main__":
	main = Main()