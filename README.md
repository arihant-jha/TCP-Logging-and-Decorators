# TCP-Logging-and-Decorators

1. TCP Connection
    - Upon running socket_server.py a socket is established, which binds itself to a port
    and now the server is listening to the port
    to keep it active we start a while loop, using which we are constantly looking for new connection requestions (it is analogous to polling).
    - socket.listen(1) tells that we will only have queue size of 1.
    - To make it concurrent, we can use multiple threads, refer, `threaded_socket_server.py`.
    - right after request is processed the thread is freed.

2. Decorating with a logger

---
3 Levels of decorators

1. Logging function call with args, kwargs
2. Parametrized decorator - lru_cache(num) -> num is the number of calls I want to cache
3. Class Based Decorator -> logging execution time