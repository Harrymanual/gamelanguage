from game_definition import GameDefinition
from game_interpreter import GameInterpreter

interpreter = GameInterpreter()

# Define game
game = GameDefinition()
game.create_room("Living Room", "You are in the living room. It's cozy here.")
game.create_room("Kitchen", "You are in the kitchen. There's a delicious smell.")
game.create_item("Living Room", "Couch", "A comfortable couch.")
game.create_item("Kitchen", "Stove", "A shiny stove.")
game.connect_rooms("Living Room", "Kitchen", "east")

# Play game
interpreter.load_game(game)
interpreter.play()