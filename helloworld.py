def application(environ, start_response):
	status = '200 OK'
	output = b'Hello World! This is CI/CD Pipeline for Python-based Web App'
	response_header = [('Content-type','text/plain'),
	('Content-Length', str(len(output)))]
	start_response(status, response_headers)
return [output]
