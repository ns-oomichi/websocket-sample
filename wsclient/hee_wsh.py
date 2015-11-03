# coding: utf-8

import mod_pywebsocket

class MyCount(object):
    def __init__(self):
        self.reset()
    def reset(self):
        self.value = 0
    def add(self):
        self.value += 1
    def get_count(self):
        return self.value
    count = property(get_count)


c = MyCount()
connections = []

def web_socket_do_extra_handshake(request):
    pass

def web_socket_transfer_data(request):
    connections.append(request)

    while True:
        v = request.ws_stream.receive_message()
        if v is None:
            print("request is none")
            return
        if v == "0":
            print("reset count")
            current_count = 0
        elif v == "1":
            print("bump up")
            current_count = current_count + 1
        else:
            print("unknown value: ", v)
            return

        try:
            for con in connections:
                con.ws_stream.send_message(str(current_count))
        except e, Exception:
            print(e)
            connections.remove(request)

