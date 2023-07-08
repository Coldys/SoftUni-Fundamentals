iterations = int(input())

for i in range(iterations):
    msg_code = int(input())
    if msg_code == 88:
        print("Hello")
    elif msg_code == 86:
        print("How are you?")
    elif msg_code < 88:
        print("GREAT!")
    else:
        print("Bye.")