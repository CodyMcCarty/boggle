import random
class BoggleBoard:  # Boggle is a word game played using a plastic grid of lettered dice, in which players attempt to find words in sequences of adjacent letters.
  
  def __init__(self):
    self.board = ['_'] * 16
    self.dice = [
      'AAEEGN',
      'ELRTTY',
      'AOOTTW',
      'ABBJOO',
      'EHRTVW',
      'CIMOTU',
      'DISTTY',
      'EIOSST',
      'DELRVY',
      'ACHOPS',
      'HIMNQU',
      'EEINSU',
      'EEGHNW',
      'AFFKPS',
      'HLNNRZ',
      'DEILRX',
    ]

  def print_board(self):
    for i in range(0, len(self.board), 4):
      print(' '.join(self.board[i:i+4]))


  def shake(self):
    random.shuffle(self.dice)
    for i, a in enumerate(self.board):
      letter = self.dice[i][random.randint(0,5)] + ' '
      if letter == 'Q ':
        letter = 'Qu'
      self.board[i] = letter

  # end BoggleBoard




# new_game = BoggleBoard()
# # print(new_game.board)
# new_game.shake()
# print (new_game.board)
# print
# # new_game.print_board()

