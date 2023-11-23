import socket as sv
import os
import time

Host = "127.0.0.1"
port = 55555

with sv.socket(sv.AF_INET, sv.SOCK_STREAM) as s: ## Get AF_INET and SOCK_STREAM
    s.bind((Host, port)) 
    s.listen() ## Listen server
    connect, address = s.accept() ## Accept Request
    with connect: ## When Connected the server
        print(f"Bağlanıldı {address}")
