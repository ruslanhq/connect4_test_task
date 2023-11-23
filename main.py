def main():
    game = Connect4Game()

    while True:
        game.print_board()
        try:
            column = int(input(f"Player {game.current_player}, choose a column (1-7): ")) - 1
            result = game.make_move(column)
            if result:
                game.print_board()
                print(f"Player {result} wins!")
                break
        except (ValueError, IndexError):
            print("Error: Invalid input. Please enter a valid column number.")

if __name__ == "__main__":
    main()
