import socket
import multiprocessing as mp
from time import time


def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        try:
            sock.connect((ip, port))
            print(f'TCP PORT : {port} is open.')
            sock.close()
        except:
            pass


def scan_tcp_ports(ip, left, right):
    processes = list()
    for port in range(left, right + 1):
        proc = mp.Process(target=scan_port, args=(ip, port))
        processes.append(proc)
        proc.start()
    for proc in processes:
        proc.join()


def main():
    host = input('Enter host: ')
    left, right = input('Enter left-right borders: ').split('-')
    border = '#' * (26 + len(left) + 1 + len(right))
    print(border)
    start_time = time()
    scan_tcp_ports(host, int(left), int(right))
    print(f'{border}\nTime: {time() - start_time} s.')


if __name__ == '__main__':
    main()
