from voice import listen

while True:
  msg = input("Rei>").strip().lower()

  if msg in ("exit", "quit", "q"):
    break

  if msg == "voice":
    print("I am listening...")
    heard = listen()
    print("Heard:", heard)
  else:
    print("i dont recognize you")