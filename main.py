import eel

@eel.expose
def helloFriendsPY(arg):
  print("Hello Friends", arg)

if __name__ == "__main__":
    eel.init("static")
    eel.start("index.html", size=(1000, 800))