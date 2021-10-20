import time

def write(*args):
  print(*args)

def take(*args):
  fn_take = input(*args)
  return fn_take

def pause(*args):
  time.sleep(*args)

def binary(*args):
  fn_binary = bin(*args)
  return fn_binary

def integer(*args):
  fn_integer = int(*args)
  return fn_integer

def string(*args):
  fn_string = str(*args)
  return fn_string

def boolean(*args):
  fn_boolean = bool(*args)
  return fn_boolean

def floating(*args):
  fn_floating = float(*args)
  return fn_floating

def absolute(*args):
  fn_absolute = abs(*args)
  return fn_absolute

def char(*args):
  fn_char = chr(*args)
  return fn_char

def ctd(*args):
  fn_ctd = ord(*args)
  return fn_ctd

def execute(args):
  args = str(args)
  fn_execute = exec(args)
  return fn_execute