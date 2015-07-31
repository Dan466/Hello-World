from socket import *

def server(number):
    Host = 'localhost'
    Port = 8108
    addr = (Host, Port)
    Sock = socket(AF_INET, SOCK_DGRAM)
    
    Sock.bind(addr)

    counter = 3
    found = False

    while not found:
        data, addr = Sock.recvfrom(1024)
        if not data:
            print ("He doesnt want play with you T_T")
            break
        else:
            print ("He guessed: ",data)
            deco_number = data.decode("utf-8")
            if deco_number == str(number):
                w_message = "win"
                winning_message = w_message.encode("utf-8")
                Sock.sendto(winning_message,addr)
                print("He's won ~_~")
                found = True
            elif counter > 0:
                error_1 = "NO, not this number :P Now you have %d chances"%(counter)
                counter-=1
                error_1_message = error_1.encode('utf-8')
                Sock.sendto(error_1_message,addr)
            else:
                error_2 = "Loss"
                error_2_message = error_2.encode('utf-8')
                Sock.sendto(error_2_message,addr)
                print("You win")
                break
    Sock.close()

def main():
    while True:
        try:
            number = int(input("Please enter your number: "))
        except ValueError:
            print("Please enter a integer number")
            continue
        else:break
    server(number)
    return 0

main()
