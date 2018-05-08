Logs requests directed to it to a file.
---

See [here][1] for why I made this.

This requires docker and docker-compose.

cd into the folder, then issue the following commands:

    docker-compose build
    docker-compose up web

To accomplish what I said in [the comment][1], you need to add the following line to your hosts file (on Linux, you'll most likely find this at ```/etc/hosts```):

    127.0.0.1    ssh-decorate.cf
    
This associates the host ```ssh-decorate.cf``` with your local IP instead of asking a DNS server.

The log file will simply contain a bunch of lines like this:

    {"time": "2018-05-08T19:29:39.644605", "path": "/favicon.ico", "request": {"base_url": "http://127.0.0.1:8000/favicon.ico", "remote_addr": "127.0.0.1", "data": "", "args": {}, "form": {}, "files": {}, "method": "GET", "cookies": {}}}

And if you pretty-print one, it'll look more like this:

    {'path': '/favicon.ico',
     'request': {'args': {},
                 'base_url': 'http://127.0.0.1:8000/favicon.ico',
                 'cookies': {},
                 'data': '',
                 'files': {},
                 'form': {},
                 'method': 'GET',
                 'remote_addr': '127.0.0.1'},
     'time': '2018-05-08T19:29:39.644605'}
     
I went with this format because I think it'd work pretty well with MongoDB.

As per the docker-compose.yml file, the log will end up in ```/tmp/intrusionlog/log.txt```.

[1]: https://www.reddit.com/r/Python/comments/8hvzja/backdoor_in_sshdecorator_package/dymz55o
