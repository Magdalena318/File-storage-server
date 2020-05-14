import os

import tornado

import socket

class ServeHandler(tornado.web.RequestHandler):
    download_directory = ""

    def initialize(self, download_directory):
        self.download_directory = download_directory
        if str(download_directory).endswith('/'):
            self.download_directory = self.download_directory[:-1]

    def get(self):
        print('Get')
        files = self.get_available_files()
        self.finish(self.get_html(files))

    @staticmethod
    def get_html(files):

        ip_address=socket.gethostbyname(socket.gethostname())

        html = """
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Directory Contents</title>
</head>
<body>
<h1>Directory Contents</h1>
    <table>
      <thead>
        <tr>
          <th>Filename</th>
        </tr>
      </thead>
      <tbody>
      """
        for file in files:
            html = html + "<tr><td><a href=\"http://"+ip_address+":8888/download/" + file + "\">" + file + "</a></td></tr>\n"
        html += """
      </tbody>
    </table>
</body>
</html>
        """
        return html

    def get_available_files(self):
        files = []
        for (root, directories, file_names) in os.walk(self.download_directory):
            for file_name in file_names:
                files.append(file_name)
        return files
