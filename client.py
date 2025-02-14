import time
from socket import socket
from zlib import decompress
import pygame
import psutil
import threading

WIDTH = 1900
HEIGHT = 1000


###################################
def get_cpu_usage(interval_in_seconds: int) -> float:
    return psutil.cpu_percent(interval=interval_in_seconds)

def start_cpu:
    x = 'true'
    while x == 'true':
      print(get_cpu_usage(1))

t1 = threading.Thread(target=start_cpu(), name='t1')
def recvall(conn, length):
    """ Retreive all pixels. """

    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf


def main(host='127.0.0.1', port=5000):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    watching = True

    sock = socket()
    sock.connect((host, port))
    try:
        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break

            # Retreive the size of the pixels length, the pixels length and pixels
            size_len = int.from_bytes(sock.recv(1), byteorder='big')
            size = int.from_bytes(sock.recv(size_len), byteorder='big')
            pixels = decompress(recvall(sock, size))

            # Create the Surface from raw pixels
            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')

            # Display the picture
            screen.blit(img, (0, 0))
            pygame.display.flip()
            clock.tick(60)
            time.sleep(10)
            sock.close()
    finally:
        sock.close()


if __name__ == '__main__':
    main()
