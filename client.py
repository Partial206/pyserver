import socket as sv

host = "127.0.0.1"
port = 5555

with sv.socket(sv.AF_INET, sv.SOCK_STREAM) as s:
    s.connect((host, port))
