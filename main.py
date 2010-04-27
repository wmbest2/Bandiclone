import Game
 
class GameLoop():
 
	def __init__(self):
		game = Game.Game()
		game.run()

app = GameLoop()
app.run()
