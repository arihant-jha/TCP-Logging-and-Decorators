# TCP-Logging-and-Decorators

1. TCP Connection
    - Upon running socket_server.py a socket is established, which binds itself to a port
    and now the server is listening to the port
    to keep it active we start a while loop, using which we are waiting for a new connection using the socket.accept() thing, which is a blocking call.
    - socket.listen(1) tells that we will only have queue size of 1.
    - To make it concurrent, we can use multiple threads, refer, `threaded_socket_server.py`.
    - right after request is processed the thread is freed.

2. client_socket, addr = server_socket.accept()
    - this is a blocking call, server waits untill it receives a request, and pauses operations, also .recv is also a blocking call it waits for receiving the request

3. Basic LoggingWrapper
    - `socket_server_basic_logger.py`
    - `client_socket ----> LogSocket (logs the data) ----> Original socket ----> Network`

---
3 Levels of decorators in Pythonic Way

1. Logging function call with args, kwargs
    - `args_logger.py`
    - fun fact I have been using an implementation of this kind of wrapper in my apis, it's amazing!!
    - I push logs to bigquery, have error call reporting and everything. It's great.

2. Parametrized decorator - lru_cache(num) -> num is the number of calls I want to cache
3. Class Based Decorator -> logging execution time