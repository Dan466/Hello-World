from socket import *

def client():
    Host = 'localhost'
    Port = 8108
    addr = (Host,Port)
    Sock = socket(AF_INET, SOCK_DGRAM)

    while True:
        m = input("Please enter the number you guess: ")
        message = m.encode(encoding="UTF-8")
        if not message:
            break
        else:
            if(Sock.sendto(message,addr)):
                print("Let's try ",message)
                rec = Sock.recv(1024)
                rec_message = rec.decode('utf-8')
                if rec_message == "win":
                    print("Haha you got me You win lol")
                    break
                if rec_message == "Loss":
                    print("you loss")
                    break
                else:
                    print("Received: ", rec_message)
    Sock.close()
def main():
    client()
    return 0
main()
