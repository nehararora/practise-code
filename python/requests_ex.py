"""
Requests Module usage sample.

TestHttpClient starts up a dummy http server,
and exercises HttpClient class to make Http calls
against this server using the requests module.
"""

import unittest
import threading
import time
import requests
import urlparse
from wsgiref.simple_server import make_server


class HttpClient(object):
    """
    Sample Http client class for demonstrating
    requests module usage
    """

    def __init__(self):
        pass

    @staticmethod
    def get(url, params=None):
        return requests.get(url, params=params)

    @staticmethod
    def put(url):
        return requests.put(url)

    @staticmethod
    def post(url):
        return requests.post(url)

    @staticmethod
    def delete(url):
        return requests.delete(url)


class TestHttpClient(unittest.TestCase):
    """
    Http Client Test Class.
    """

    @classmethod
    def setUpClass(cls):
        cls.client = HttpClient()

        print('creating server...')
        cls.server = MyTestHttpServer()

        # startup http server...
        print('starting server...')
        cls.server.start()
        #print('listening at address {0}'.format(cls.server.address))

        #setup request parameter dict...
        cls.params = {'key': 'value', 'number': '2'}

    ###

    def test_get(self):
        """
        lets make a ws call!
        """
        url, port = self.server.address

        #couple of basic GETs
        r = self.client.get("http://{0}:{1}/".format(url, port))
        self.assertEqual(200, r.status_code)
        r = self.client.get("http://{0}:{1}".format(url, port))
        self.assertEqual(200, r.status_code)
        r = self.client.get("http://{0}:{1}/200".format(url, port))
        self.assertEqual(200, r.status_code)
        r = self.client.get("http://{0}:{1}/400".format(url, port))
        self.assertEqual(400, r.status_code)

        # GETs with params
        r = self.client.get("http://{0}:{1}/get_with_params".format(url, port),
                            params=self.params)
        self.assertEqual(200, r.status_code)
        self.assertEqual(str(self.params), r.text)

        # GETs with ...?
    ###

    def test_post(self):
        """
        lets make a ws call!
        """
        url, port = self.server.address

        #couple of basic POSTs
        #request parameters
        r = self.client.get("http://{0}:{1}/".format(url, port))
        self.assertEqual(200, r.status_code)
        r = self.client.get("http://{0}:{1}".format(url, port))
        self.assertEqual(200, r.status_code)
        r = self.client.get("http://{0}:{1}/200".format(url, port))
        self.assertEqual(200, r.status_code)
        r = self.client.get("http://{0}:{1}/400".format(url, port))
        self.assertEqual(400, r.status_code)

    ###

    def test_put(self):
        """
        lets make a ws call!
        """
        url, port = self.server.address

        #couple of basic POSTs
        r = self.client.get("http://{0}:{1}/".format(url, port))
        self.assertEqual(200, r.status_code)
        r = self.client.get("http://{0}:{1}".format(url, port))
        self.assertEqual(200, r.status_code)
        r = self.client.get("http://{0}:{1}/200".format(url, port))
        self.assertEqual(200, r.status_code)
        r = self.client.get("http://{0}:{1}/400".format(url, port))
        self.assertEqual(400, r.status_code)

        r = self.client.put("http://{0}:{1}/400?foo=bar".format(url, port))
        self.assertEqual(400, r.status_code)


    ###

    @classmethod
    def tearDownClass(cls):
        """Test class teardown"""
        print('stopping running server...')
        cls.server.stop()
        print('...done!')
#####


class MyTestHttpServer(threading.Thread):
    """
    WSGI based dummy http server used to demonstrate client code.
    """

    #codes handled by test server: server returns response based on code
    #specified in uri.
    codes = {'200': '200 OK',
             '201': '201 Created',
             '400': '400 Bad Request',
             '401': '401 Unauthorized',
             '403': '403 Forbidden',
             '404': '404 Not Found',
             '405': '405 Method Not Allowed',
             '500': '500 Internal Server Error',
             '501': '501 Not Implemented',
             '503': '503 Service Unavailable',
             }

    def __init__(self):
        """
        Initializes test server by setting the wsgi application object.
        :return:
        """

        # Every WSGI application must have an application object - a callable
        # object that accepts two arguments. For that purpose, we're going to
        # use a function (note that you're not limited to a function, you can
        # use a class for example). The first argument passed to the function
        # is a dictionary containing CGI-style environment variables and the
        # second variable is the callable object (see PEP 333).
        def application(environ, start_response):
            """
            WSGI application object. Returns request status.
            For specific endpoints (e.g. get_with_params), returns
            specific response bodies.
            """

            response_text = 'Hello World!'
            endpoint = environ['PATH_INFO'][1:]

            if endpoint == 'get_with_params':
                #echo back uri parameters as dict...
                response_text = str(dict(urlparse.parse_qsl(environ['QUERY_STRING'])))

            #set status code for response based on request...
            requested_status = environ['PATH_INFO'][1:]

            status = self.codes.get(requested_status, '200 OK')  # HTTP Status
            headers = [('Content-type', 'text/plain')]  # HTTP Headers
            start_response(status, headers)
            #print(environ)
            #print('pathInfo: {0}'.format(environ.get('PATH_INFO')))
            #print('queryString: {0}'.format(environ.get('QUERY_STRING')))
            #print('requestMethod:{0}'.format(environ['REQUEST_METHOD']))
            # The returned object is going to be printed
            return response_text

        threading.Thread.__init__(self)
        self.httpd = make_server('', 0, application)
        self.address = self.httpd.server_address

    def run(self):
        """
        Run server instance: called by the thread's start()
        :return:
        """
        self.httpd.serve_forever()

    def stop(self):
        """
        Stop running server.

        :return:
        """
        self.httpd.shutdown()
        self.join()
        time.sleep(0.2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHttpClient)
    unittest.TextTestRunner(verbosity=0).run(suite)

    #unittest.main()
