import subprocess
import time

def open_music():
  subprocess.Popen(["kitty"])
  time.sleep(1)

  subprocess.run("play")