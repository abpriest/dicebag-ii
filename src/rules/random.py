from random import randint
from random import shuffle

tokens = ['DIE', 'HIGH', 'LOW', 'SEL', 'TO', 'BY', 'SHUFFLE', 'SORT']

literals = """pass"""

reserved = {
  'd'       : 'DIE',
  'l'       : 'LOW',
  'h'       : 'HIGH',
  'sel'     : 'SEL',
  'to'      : 'TO',
  'by'      : 'BY'
  'sort'    : 'SORT',
  'shuffle' : 'SHUFFLE'
}

precedence = {
  60  : ('nonassoc', 'BY'),
  50  : ('nonassoc', 'TO'),
  270 : ('left', 'DIE'),
  250 : ('left', 'LOW', 'HIGH'),
  240 : ('right', 'SEL', 'SHUFFLE', 'SORT'),
}

def p_range(tokens):
  '''expr : expr TO expr'''
  if tokens[1] < tokens[3]:
    tokens[0] = [x for x in range(tokens[1], tokens[3])]
  else:
    tokens[0] = [x for x in range(tokens[3], tokens[1], -1)]

def p_range_step(tokens):
  '''expr : expr TO expr BY expr'''
  step = abs(tokens[5])
  if tokens[1] < tokens[3]:
    tokens[0] = [x for x in range(tokens[1], tokens[3], step)]
  else:
    tokens[0] = [x for x in range(tokens[3], tokens[1], -step)]

def p_die(tokens):
  '''expr : expr DIE expr'''
  tokens[0] = [randint(1, tokens[3]) for x in range(tokens[1])]
  tokens[0] = tokens[0][0] if len(tokens[0]) == 1 else tokens[0]

def p_low(tokens):
  '''expr : expr LOW expr'''
  tokens[0] = sorted(tokens[1])[:tokens[3]]

def p_high(tokens):
  '''expr : expr HIGH expr'''
  tokens[0] = [x for x in reversed(sorted(tokens[1]))][:tokens[3]]

def p_shuffle(tokens):
  '''expr : SHUFFLE expr'''
  temp = tokens[2]
  shuffle(temp)
  tokens[0] = temp

def p_sort(tokens):
  '''expr : SORT expr'''
  tokens[0] = sorted(tokens[2])



