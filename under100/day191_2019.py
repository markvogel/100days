import socket


def socket1(webpage="http://data.pr4e.org/romeo.txt"):
    try:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((webpage.split(sep="/")[2], 80))
        cmd = f"GET {webpage} HTTP/1.0\r\n\r\n".encode()
        mysock.send(cmd)

        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode(), end='')

        mysock.close()
    except:
        print("you entered an invalid url ")
        exit()


# Code: http://www.py4e.com/code3/socket1.py


def get_page():
    return input("Please enter a webpage: ")


if __name__ == '__main__':
    socket1(get_page())
