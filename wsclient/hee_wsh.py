# coding: utf-8

import mod_pywebsocket

current_count = 0
connections = []

def web_socket_do_extra_handshake(request):
    pass

def web_socket_transfer_data(request):
    global current_count
    global connections
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
            print("bump up: ", request.connection.remote_addr)
            current_count = current_count + 1
        else:
            print("unknown value: ", v)
            return

        try:
            for con in connections:
                con.ws_stream.send_message(str(current_count))
        except Exception, e:
            print(e)
            if request in connections:
                print("remove request")
                connections.remove(request)
            else:
                print("cannot remove: not exists")

