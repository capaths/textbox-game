from .console import Console
import time

cmd = Console()

def cprint(msg, color=None, on_color=None):
  cmd.write(msg, color=color, on_color=on_color)

def clear():
  cmd.clear()

def move(x, y):
  cmd.move(x, y)

def rel_move(x, y):
  cmd.rel_move(x, y)

def draw_border():
  width, height = cmd.get_res()

  cmd.clear()
  cmd.hprint("*", width-1)
  time.sleep(1)
  cmd.vprint("*", height-2, -1)
  time.sleep(1)
  cmd.hprint("*", width-1, -1)
  cmd.rel_move(-1, 0)
  time.sleep(1)
  cmd.vprint("*", height-1, 1)

def get_cursor():
  return cmd.pos

def read():
  return cmd.read()
