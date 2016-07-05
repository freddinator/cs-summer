import random

class Question:
	def __init__(self, number, default_cap = 20):
		self.number = number
		self.a = random.randint(1,default_cap)
		self.b = random.randint(1,default_cap)
		self.operator = ""

	def output(self):
		return str(self.a) + " " + self.operator + " " + str(self.b)

	def getAnswer(self):
		raise NotImplementedError

	def ask(self):
		answer = int(input(str(self.number) + ": " + self.output() + " > "))

		if answer == self.getAnswer():
			return True, self.getAnswer()
		else:
			return False, self.getAnswer()

class AddQuestion(Question):
	def __init__(self, number):
		super().__init__(number)
		self.operator = "+"

	def getAnswer(self):
		return self.a + self.b

class SubtractQuestion(Question):
	def __init__(self, number):
		super().__init__(number)
		self.operator = "-"

	def getAnswer(self):
		return self.a - self.b

class MultiplyQuestion(Question):
	def __init__(self, number):
		super().__init__(number, 10)
		self.operator = "×"

	def getAnswer(self):
		return self.a * self.b


