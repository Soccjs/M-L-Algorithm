import random
from numpy import *
#test data
train_mat = array([\
		[0.12,0.25],\
		[3.24,4.33],\
		[0.14,0.45],\
		[7.30,4.23],\
	])

train_label = array([0,1,0,1])


class LinearRegression:
	def __init__(self, mat_data, label_data):
		self.mat_w = array([random.random() * 0.000001\
		 for i in range(len(mat_data[0]))])
		
		self.mat_w0 = random.random() * 0.000001
		print self.mat_w
		print self.mat_w0

		self.mat_data = mat_data
		self.label_data = label_data



	def batch_update(self, mat_data, label_data):
		yp = (self.mat_w * mat_data).sum(axis=1) + self.mat_w0		#axis=0 : row, axis=1 : col
		
		gd = (label_data - yp) #y-y'	, gradient descent

		dJ_dw = (gd * mat_data.T).sum(axis=1) * -2
		dJ_dw0 = gd.sum(axis=0) * -2

		self.mat_w = self.mat_w - (dJ_dw * self.lr)
		self.mat_w0 = self.mat_w0 - (dJ_dw0 * self.lr)
		r1 = self.predict([0.0,0.0])
		r2 = self.predict([5.0,5.5])
		print (r1, r2)
		#J = sum[ (y-y')^2 ]
		#J' =  sum[ dJ/dy' * dy'/dw] = sum [2 (y-y') * -1 * x]
		#w = w - J' * lr
		#J'w0 = sum[ 2(y-y') * -1 * 1]
		#w0 = w0 - J'w0 * lr

	def fit(self, epoch, lr):
		self.lr = lr
		for ep in range(epoch):
			print ep, "training..."
			self.batch_update(self.mat_data, self.label_data)


	def predict(self, input_array):
		return (self.mat_w * input_array).sum(axis=0) + self.mat_w0


linear_module = LinearRegression(train_mat, train_label)

linear_module.fit(epoch=1000, lr=0.001) # the number of rotate , learning rate

r1 = linear_module.predict([0.0,0.0])
r2 = linear_module.predict([5.0,5.5])


print ("result : ", r1, r2)