def p_and(tokens):
  '''expr : expr AND expr'''
  tokens[0] = tokens[1] and tokens[3]

def p_or(tokens):
  '''expr : expr OR expr'''
  tokens[0] = tokens[1] and tokens[3]

def p_not(tokens):
  '''expr : NOT expr'''
  tokens[0] = not tokens[2]

def p_in(tokens):
  '''expr : expr IN expr'''
  tokens[0] = tokens[1] in tokens[3]


