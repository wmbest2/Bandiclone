from direct.showbase.ShowBase import ShowBase

class Game(ShowBase):

	def __init__(self):
		ShowBase.__init__(self)
		self.load_model()

	def load_model(self):
		self.environ = self.loader.loadModel("models/crash/crash_crude")
		self.environ.reparentTo(self.render)
		self.environ.setScale(0.25, 0.25, 0.25)
		self.environ.setPos(0, 5, 0)

