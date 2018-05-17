from math import *
from gaussian import *

class kalman_filter_1D(object):

	def __init__(self, mean, variance):
		self.belief = gaussian(mean=mean, variance=variance)

	def __repr__(self):
		return self.belief.__repr__()

	def sense(self, measurement):

		m1, s1 = self.belief.mean, self.belief.variance
		m2, s2 = measurement.mean, measurement.variance

		m3 = 1 / (s1 + s2) * (s2*m1 + s1*m2)
		s3 = 1 / (1/s1 + 1/s2)

		self.belief = gaussian(mean=m3, variance=s3)

	def move(self, motion):
		self.belief = self.belief + motion

	#Alternative terminology

	def update(self, measurement):
		self.sense(measurement)

	def predict(self, motion):
		self.move(motion)


filter = kalman_filter_1D(mean=8, variance=4)
print filter

filter.sense(measurement=gaussian(mean=13, variance=2))
print filter

filter.move(motion=gaussian(mean=10, variance=6))
print filter
