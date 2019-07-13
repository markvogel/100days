# https://www.py4e.com/html3/12-network
import socket


# exercise2
def socket1(webpage="http://data.pr4e.org/romeo.txt"):
    total_text = ""
    try:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((webpage.split(sep="/")[2], 80))
        cmd = f"GET {webpage} HTTP/1.0\r\n\r\n".encode()
        mysock.send(cmd)

        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            text = data.decode()
            total_text += text
        mysock.close()

    except TabError:
        print("you entered an invalid url ")
        exit()
    printed_text = ""
    for c, l in enumerate(total_text):
        if c < 3000:
            printed_text += l
    print(printed_text)
    print(len(total_text))


# Code: http://www.py4e.com/code3/socket1.py


def get_page():
    return input("Please enter a webpage: ")


if __name__ == '__main__':
    socket1("http://data.pr4e.org/")
