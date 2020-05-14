import argparse

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from serve_handler import ServeHandler
from tornado_app import MyTornadoApplication
from upload_handler import UploadHandler

defaults = {
    'port': 8888,
    'username': 'root',
    'password': '123',
    'file_download_directory': 'uploads',
    'file_upload_directory': 'uploads'
}


def main(args):
    handlers = [
        (r"/", UploadHandler, {'username': args.username, 'password': args.password, 'upload_directory': args.upload_directory}),
        (r"/browse/", ServeHandler, {'download_directory': args.download_directory}),
        (r"/download/(.*)", tornado.web.StaticFileHandler, {'path': args.download_directory})
    ]
    print('Starting server on port {}'.format(args.port))
    http_server = tornado.httpserver.HTTPServer(MyTornadoApplication(handlers))
    http_server.listen(args.port)
    tornado.ioloop.IOLoop.instance().start()

    # path = os.getcwd() + '/' + defaults[;]


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            'Start a Tornado server to serve and upload files from/to given directory.'))
    parser.add_argument(
        '--port', type=int, default=defaults['port'],
        help='Port on which to run server.')
    parser.add_argument(
        '--username', type=str, default=defaults['username'],
        help='Username required for authentication.')
    parser.add_argument(
        '--password', type=str, default=defaults['password'],
        help='Password required for authentication.')
    parser.add_argument(
        '--download-directory', type=str, default=defaults['file_download_directory'],
        help='Directory from which to serve files.')
    parser.add_argument(
        '--upload-directory', type=str, default=defaults['file_upload_directory'],
        help='Directory to which upload files.')
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
