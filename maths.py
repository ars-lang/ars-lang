def length(args):
  args = str(args)
  fn_length = len(args)
  return fn_length

def minimal(*args):
  fn_minimal = min(*args)
  return fn_minimal

def maximal(*args):
  fn_maximal = max(*args)
  return fn_maximal

def step(main, step):
  fn_step = pow(main, step)
  return fn_step
