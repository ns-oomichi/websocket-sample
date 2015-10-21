# coding: utf-8

from mod_pywebsocket import msgutil

connections = []

def web_socket_do_extra_handshake(request):
    pass

def web_socket_transfer_data(request):
    connections.append(request)
    while True:
        try:
            message = msgutil.receive_message(request)
            print message
        except Exception, ex:
            print ex
            return

        for con in connections:
            try:
                msgutil.send_message(con, message)
            except Exception, ex:
                print ex
                connections.remove(con)


