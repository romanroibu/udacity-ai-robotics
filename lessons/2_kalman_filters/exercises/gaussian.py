from math import *

class gaussian(object):
	def __init__(self, mean, variance):
		super(gaussian, self).__init__()
		self.mean = float(mean)
		self.variance = float(variance)

	def __repr__(self):
		return "N(mu=%.4f, sig2=%.4f)" % (self.mean, self.variance)

	def __call__(self, x):
		return (1/sqrt(2.0 * pi * self.variance)) * exp( (-1.0/2) * (x-self.mean)**2 / self.variance)

	def __add__(self, other):
		mean = self.mean + other.mean
		variance = self.variance + other.variance
		return gaussian(mean=mean, variance=variance)
