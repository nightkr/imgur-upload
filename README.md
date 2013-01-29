imgur_upload.py
=============== 

Since I couldn't find any good equivalent, this is a simple CLI for uploading files to imgur.


Usage
-----

`$ ./imgur_upload.py $client_id /path/to/file`

It will print a single line containing the status code (HTTP-style) and either the error message or the ID and the "deletion hash".  

Example output if upload fails:

```
$ ./imgur_upload.py $IMGUR_CLIENT_ID /path/to/file
403 Unauthorized
```

Example output on success:

```
$ ./imgur_upload.py $IMGUR_CLIENT_ID /path/to/file
200 AB3dEf fdasFSade2313
```

The return code is 2 upon an argument error (including an unexistant file), 1 upon an imgur error, or 0 upon success.


License
-------

It's 30 lines of glue code, many of which are whitespace. It's shorter than this README. I don't think copyright is applicable here.


Dependencies
------------

* Python 2.7
* Requests (tested against 1.1.0)
* Setuptools or Distribute (only if installing, running standalone does not require this)
