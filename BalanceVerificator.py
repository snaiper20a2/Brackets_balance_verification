"""
Brackets balancing module
"""
from collections import deque
import re


class BalanceVerificator:
  """
  This class is for checking brackets balancing.
  Brackets are considered matched pair if it occurs that every open bracket has
  closing bracket of the exact the same type (‘(’, ‘{’, ‘[’)
  """
  OPEN_BRACKET = ['(', '{', '[']
  CLOSE_BRACKET = [')', '}', ']']
  PATTERN = r'[^\(\)\[\]\{\}]'

  def verify(self, data: str):
    """
    :param data: string with brackets
    :return: -1 if string is balanced or number of not balanced bracket
    """
    if data == '':
      raise ValueError('Input line is empty')
    match = re.search(self.PATTERN, data)
    if match:
      raise ValueError('A character ‘{}’ doesn’t belong '
                       'to any known brackets type'.format(match[0]))
    bracket_stack = deque()
    for letter in data:
      if self.OPEN_BRACKET.count(letter) == 1:
        bracket_stack.append(letter)
        continue
      if self.CLOSE_BRACKET.count(letter) == 1:
        open_bracket = self.OPEN_BRACKET[self.CLOSE_BRACKET.index(letter)]
        if bracket_stack.pop() != open_bracket:
          print('NOT BALANCED')
          return len(bracket_stack) + 1
    print('BALANCED')
    return -1
