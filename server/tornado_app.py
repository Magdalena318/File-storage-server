import tornado


class MyTornadoApplication(tornado.web.Application):
    def __init__(self, handlers):
        tornado.web.Application.__init__(self, handlers)
