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

def draw_box(x0, y0, x1, y1):
  sw, sh = cmd.get_res()
  if y1 < 0 or y1 < 0 or y1 > sw or y1 > sh:
    print("[ERROR] box outside limits")
    return
  if y1 <= y0 or x1 <= x0:
    print("[ERROR] box coors inconsistent")
    return

  width = x1 - x0
  height = y1 - y0

  cmd.move(x0, y0)
  cmd.hprint("*", width-1)
  time.sleep(1)
  cmd.vprint("*", height-2, -1)
  time.sleep(1)
  cmd.hprint("*", width-1, -1)
  time.sleep(1)
  cmd.vprint("*", height-1)

def draw_border():
  width, height = cmd.get_res()
  cmd.clear()
  draw_box(0, 0, width, height)

def get_cursor():
  return cmd.pos

def read():
  return cmd.read()
