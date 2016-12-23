## Quickstart

    git clone https://github.com/web2gram/tgcli.git
    cd tgcli
    python bootstrap.py
    ./bin/buildout

A python interpreter is ready in `./bin/python`.

## Send markdown message to channel

    ./bin/python tgcli.py <BOT_TOKEN> --send test.md --chat_id @channel_name

## Bot request
This is how telegram send the request:-

    POST / HTTP/1.1
    Host: xxx.ngrok.io
    Content-Type: application/json
    Content-Length: 247
    Accept-Encoding: gzip, deflate
    X-Forwarded-Proto: https
    X-Forwarded-For: 149.0.16.14

    {"update_id":695672305,
    "message":{"message_id":29,"from":{"id":3339704,"first_name":"Kamal","username":"kamal"},"chat":{"id":3339704,"first_name":"Kamal","username":"kamal","type":"private"},"date":1478650973,"text":"test ngrok"}}
