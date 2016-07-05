class Outcome:
	def __init__(self, option, result):
		self.option = option
		self.result = result

class TextResult:
	def __init__(self, text):
		self.text = text

	def ask(self):
		print ('\033[94m' + self.text + '\033[0m')
