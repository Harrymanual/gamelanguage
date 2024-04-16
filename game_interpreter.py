class GameInterpreter:
    def __init__(self):
        self.game = None
        self.current_room = None

    def load_game(self, game_definition):
        self.game = game_definition
        self.current_room = game_definition.start_room

    def play(self):
        print("Welcome to the Text Adventure Game!")
        while True:
            print("\nCurrent Room:", self.current_room.name)
            print("Description:", self.current_room.description)
            print("Items:", [item.name for item in self.current_room.items])
            print("Directions:", list(self.current_room.connections.keys()))

            command = input("> ").lower().split()
            if command[0] == "quit":
                print("Thanks for playing!")
                self.game.clear_game()
                break
            elif command[0] == "go":
                if len(command) > 1 and command[1] in self.current_room.connections:
                    self.current_room = self.current_room.connections[command[1]]
                else:
                    print("Invalid direction.")
            else:
                print("Invalid command.")