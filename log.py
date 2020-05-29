$ python urlcaller.py http://thisurlprobablydoesntexist.com
...
During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "urlcaller.py", line 5, in <module>
    response = requests.get(sys.argv[1])
  File "/path/to/requests/api.py", line 75, in get
    return request('get', url, params=params, **kwargs)
  File "/path/to/requests/api.py", line 60, in request
    return session.request(method=method, url=url, **kwargs)
  File "/path/to/requests/sessions.py", line 533, in request
    resp = self.send(prep, **send_kwargs)
  File "/path/to/requests/sessions.py", line 646, in send
    r = adapter.send(request, **kwargs)
  File "/path/to/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7faf9d671860>: Failed to establish a new connection: [Errno -2] Name or service not known',))

$ python urlcaller.py http://thisurlprobablydoesntexist.com
...
During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "urlcaller.py", line 5, in <module>
    response = requests.get(sys.argv[1])
  File "/path/to/requests/api.py", line 75, in get
    return request('get', url, params=params, **kwargs)
  File "/path/to/requests/api.py", line 60, in request
    return session.request(method=method, url=url, **kwargs)
  File "/path/to/requests/sessions.py", line 533, in request
    resp = self.send(prep, **send_kwargs)
  File "/path/to/requests/sessions.py", line 646, in send
    r = adapter.send(request, **kwargs)
  File "/path/to/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7faf9d671860>: Failed to establish a new connection: [Errno -2] Name or service not known',))

$ python urlcaller.py http://thisurlprobablydoesntexist.com
...
During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "urlcaller.py", line 5, in <module>
    response = requests.get(sys.argv[1])
  File "/path/to/requests/api.py", line 75, in get
    return request('get', url, params=params, **kwargs)
  File "/path/to/requests/api.py", line 60, in request
    return session.request(method=method, url=url, **kwargs)
  File "/path/to/requests/sessions.py", line 533, in request
    resp = self.send(prep, **send_kwargs)
  File "/path/to/requests/sessions.py", line 646, in send
    r = adapter.send(request, **kwargs)
  File "/path/to/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7faf9d671860>: Failed to establish a new connection: [Errno -2] Name or service not known',))

$ python urlcaller.py http://thisurlprobablydoesntexist.com
...
During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "urlcaller.py", line 5, in <module>
    response = requests.get(sys.argv[1])
  File "/path/to/requests/api.py", line 75, in get
    return request('get', url, params=params, **kwargs)
  File "/path/to/requests/api.py", line 60, in request
    return session.request(method=method, url=url, **kwargs)
  File "/path/to/requests/sessions.py", line 533, in request
    resp = self.send(prep, **send_kwargs)
  File "/path/to/requests/sessions.py", line 646, in send
    r = adapter.send(request, **kwargs)
  File "/path/to/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7faf9d671860>: Failed to establish a new connection: [Errno -2] Name or service not known',))

$ python urlcaller.py http://thisurlprobablydoesntexist.com
...
During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "urlcaller.py", line 5, in <module>
    response = requests.get(sys.argv[1])
  File "/path/to/requests/api.py", line 75, in get
    return request('get', url, params=params, **kwargs)
  File "/path/to/requests/api.py", line 60, in request
    return session.request(method=method, url=url, **kwargs)
  File "/path/to/requests/sessions.py", line 533, in request
    resp = self.send(prep, **send_kwargs)
  File "/path/to/requests/sessions.py", line 646, in send
    r = adapter.send(request, **kwargs)
  File "/path/to/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7faf9d671860>: Failed to establish a new connection: [Errno -2] Name or service not known',))

$ python urlcaller.py http://thisurlprobablydoesntexist.com
...
During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "urlcaller.py", line 5, in <module>
    response = requests.get(sys.argv[1])
  File "/path/to/requests/api.py", line 75, in get
    return request('get', url, params=params, **kwargs)
  File "/path/to/requests/api.py", line 60, in request
    return session.request(method=method, url=url, **kwargs)
  File "/path/to/requests/sessions.py", line 533, in request
    resp = self.send(prep, **send_kwargs)
  File "/path/to/requests/sessions.py", line 646, in send
    r = adapter.send(request, **kwargs)
  File "/path/to/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7faf9d671860>: Failed to establish a new connection: [Errno -2] Name or service not known',))

$ python urlcaller.py http://thisurlprobablydoesntexist.com
...
During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "urlcaller.py", line 5, in <module>
    response = requests.get(sys.argv[1])
  File "/path/to/requests/api.py", line 75, in get
    return request('get', url, params=params, **kwargs)
  File "/path/to/requests/api.py", line 60, in request
    return session.request(method=method, url=url, **kwargs)
  File "/path/to/requests/sessions.py", line 533, in request
    resp = self.send(prep, **send_kwargs)
  File "/path/to/requests/sessions.py", line 646, in send
    r = adapter.send(request, **kwargs)
  File "/path/to/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7faf9d671860>: Failed to establish a new connection: [Errno -2] Name or service not known',))

$ python urlcaller.py http://thisurlprobablydoesntexist.com
...
During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "urlcaller.py", line 5, in <module>
    response = requests.get(sys.argv[1])
  File "/path/to/requests/api.py", line 75, in get
    return request('get', url, params=params, **kwargs)
  File "/path/to/requests/api.py", line 60, in request
    return session.request(method=method, url=url, **kwargs)
  File "/path/to/requests/sessions.py", line 533, in request
    resp = self.send(prep, **send_kwargs)
  File "/path/to/requests/sessions.py", line 646, in send
    r = adapter.send(request, **kwargs)
  File "/path/to/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7faf9d671860>: Failed to establish a new connection: [Errno -2] Name or service not known',))



