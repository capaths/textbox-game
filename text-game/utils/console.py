import os
import sys
import subprocess
import time
from shutil import get_terminal_size
from colorama import init
from termcolor import colored

init()

class Console:
  def __init__(self):
    self.update_res()
    self.pos = (1, 1)
    self.clear()

  def get_res(self):
    self.update_res()
    return self._res

  def _register_move(self, x_pos, y_pos):
    self.last_pos = self.pos
    self.pos = (x_pos, y_pos)

  def update_res(self):
    self._res = get_terminal_size()
  
  def write(self, msg, color=None, on_color=None):
    msg = str(msg)
    sys.stdout.write(colored(msg, color=color, on_color=on_color))
    sys.stdout.flush()

    width = self.get_res()[0]
    if self.pos[0] + len(msg) > width:
      self.move(width-1, self.pos[1])
    else:
      self._register_move(self.pos[0] + len(msg), self.pos[1])
  
  def _esc_write(self, msg):
    sys.stdout.write("\x1b[%s" % (msg))
    sys.stdout.flush()

  def clear(self):
    self._esc_write('2J')
    self._register_move(0, 0)
  
  def read(self):
    x = input()
    self.move(self.pos[0], self.pos[1])
    return x

  # coors in box: (0, 0) x (width-1, height-1)
  def move(self, x, y):
    x = x + 1
    y = y + 1
    self._esc_write('%d;%dH' % (y, x))
    self._register_move(x, y)

  def rel_move(self, x, y):
    if x > 0:
      self._esc_write('%dC' % (x))
    elif x < 0:
      self._esc_write('%dD' % (-x))
    if y > 0:
      self._esc_write('%dA' % (y))
    elif y < 0:
      self._esc_write('%dB' % (-y))
    self._register_move(self.pos[0] + x, self.pos[1] + y)

  def go_back(self):
    self._register_move(*self.last_pos)

  def hprint(self, msg, rep=1, step=1):
    for _ in range(rep):
      self.write(msg)
      if step > 0:
        self.rel_move(step-1, 0)
      elif step < 0:
        self.rel_move(step-1, 0)
  
  def vprint(self, msg, rep=1, step=1):
    for _ in range(rep):
      self.write(msg)
      if step > 0:
        self.rel_move(-1, step)

