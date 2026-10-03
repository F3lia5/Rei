from voice import listen
from music import open_music

while True:
  msg = input("Rei>").strip().lower()

  if msg in ("exit", "quit", "q"):
    break

  if msg == "voice":
    print("I am listening...")
    heard = listen()
    print("Heard:", heard)
    if heard == "Rei play" or "Rei stop":
      open_music

  elif msg in ("can u play some music"):
    open_music
    print("playing")
  elif msg in ("can u stop the music"):
    open_music
    print("stopped")

  else:
    print("i dont recognize you")