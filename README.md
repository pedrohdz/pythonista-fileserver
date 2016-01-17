# Pythonista File Server

Based on [omz/FileTransfer.py][ORIGINAL].  Get Pythonista for iOS here:
[Pythonista][PYTHONISTA].

This script *attempts* to make transferring files to and from *Pythonista* a
little bit more secure by using SSL, and Basic authentication.

***Use at your own risk...***

## Setup

You will need an SSL self signed certificate before you start.  There are a
bunch of posts on the web on how to do this already.  Just looks around.  :-)

1. Get this script `PythonistFileServer.py` onto your *Pythonista*
   installation.
2. Run `PythonistFileServer.py`.  This first attempt will fail.  Running
   `PythonistFileServer.py` will make the module available in the console,
   which is needed for the next step.
3. Go to the *Pythonista* console and:
   ```
   >>> import PythonistFileServer
   >>> PythonistFileServer.init_config()
   ```
   That will create the `~/Documents/.httpfileserver` directory, and initialize
   the `config.cfg` file in there.
4. Swipe right to go back to the editor, you should see
   `~/Documents/.httpfileserver/config.cfg`.  **Make sure to fill in the
   `username`, and `password`**.
5. Upload your `server.key`, and `server.crt` files into the
   `~/Documents/.httpfileserver` directory.
6. Start up PythonistFileServer.  You should be good to go.


## Howtos

### From within Pythonista

#### Modify your configuration

1. From within *Pythonista*, run `PythonistFileServer`, then quit.  This will
   make `PythonistFileServer` available for import.
2. Swipe left to get the console, and
   ```
   >>> import PythonistFileServer
   >>> PythonistFileServer.edit_config()
   ```
3. Swipe right to bring up the editor then make your changes.


### Curl

The following examples assumes a *username* of `test`, and *password* of
`tester`.  Pick something more secure.

#### List files in a directory

To the document root:
```
$ curl --insecure --user "test:tester" "https://testserver.local:8843/"
{
    "cwd": "/",
    "files": [
        "PythonistFileServer.py",
        "Welcome.txt",
        "test1/Welcome.txt"
    ],
    "status": {
        "message": "success",
        "type": "success"
    }
}
```

To sub directories:
```
$ curl --insecure --user "test:tester" "https://testserver.local:8843/test1"
{
    "cwd": "/test1",
    "files": [
        "test1/Welcome.txt"
    ],
    "status": {
        "message": "success",
        "type": "success"
    }
}

```

#### Upload a file to a directory

To the document root:
```
$ curl --insecure --user "test:tester" -F "file=@somescript.py" \
        "https://testserver.local:8843/"
{
    "cwd": "/",
    "files": [
        "PythonistFileServer.py",
        "somescript.py",
        "Welcome.txt",
        "test1/Welcome.txt"
    ],
    "status": {
        "message": "success",
        "type": "success"
    }
}
```

To a sub directory:
```
$ curl --insecure --user "test:tester" -F "file=@somescript.py" \
        "https://testserver.local:8843/test1"
```

Uploading and excluding the `files` section, set the `short` query parameter to
`true`:
```
$ curl --insecure --user "test:tester" -F "file=@somescript.py" \
        "https://testserver.local:8843/test1?short=true"
{
    "cwd": "/test1",
    "status": {
        "message": "somescript.txt uploaded (renamed to somescript-3.txt).",
        "type": "success"
    }
}
```

#### Overwriting a file on upload

Set the `overwrite` query parameter to `true`:
```
$ curl --insecure --user "test:tester" -F "file=@somescript.py" \
        "https://testserver.local:8843/test1?short=true&overwrite=true"
```


## Change log

  - 0.0.0
    - Minor whitespace cleanup.
    - Added HTTP Basic Authentication.  Thanks to
      [StackOverflow - Stuck with Python HTTP Server with Basic Authentication using BaseHTTP][BASIC_AUTH].
    - SSL support.
    - Configuration file.
    - RESTish type interface with JSON output.
    - URL path validation.
    - And much more...



[ORIGINAL]: https://gist.github.com/omz/3823483
[PYTHONISTA]: http://omz-software.com/pythonista
[BASIC_AUTH]: http://stackoverflow.com/questions/4287019/stuck-with-python-http-server-with-basic-authentication-using-basehttp

