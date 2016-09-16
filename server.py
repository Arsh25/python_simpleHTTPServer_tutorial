#!/usr/bin/env python2

import SimpleHTTPServer
import BaseHTTPServer
import urllib
import urlparse

class prettyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		page = open('index.html')
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(page.read())
		self.wfile.close()

	def do_POST(self):
		name = urlparse.urlparse(self.path).query
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(name + " is a pretty kitty")

if __name__ == '__main__':
	handler = prettyHandler
	serverAddress = ('',80)
	server = BaseHTTPServer.HTTPServer(serverAddress,handler)
	server.serve_forever()
