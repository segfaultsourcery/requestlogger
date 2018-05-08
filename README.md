Logs requests directed to it to a file.
---

See [here][1] for why I made this.

This requires docker and docker-compose.

cd into the folder, then issue the following commands:

    docker-compose build
    docker-compose up web

As per the docker-compose.yml file, the log will end up in ```/tmp/intrusionlog/log.txt```.

[1]: https://www.reddit.com/r/Python/comments/8hvzja/backdoor_in_sshdecorator_package/dymz55o
