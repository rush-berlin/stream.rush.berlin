# stream.rush.berlin

This repository is the web frontend for streaming video on [rush.berlin](https://rush.berlin).

It includes changes to simplify the web frontend, support https via letsencrypt,

## Credits

- We are using the flv.js library (https://github.com/bilibili/flv.js) for our webplayer
- The included Streaming Server is based on nginx (https://nginx.org) with the nginx-http-flv-module (https://github.com/winshining/nginx-http-flv-module)
- Big thanks to the kind folks behind [zom-bi/zomstream](https://github.com/zom-bi/zomstream), the repo this is based on.

## Components

stream.rush.berlin is a multiple container setup which should be setup using docker-compose. It consists of the following components.

### nginx

A basic nginx reverse-proxy to act as a certbot frontend.

### certbot

A service to ensure our https is always up to date.

### nginx-rtmp

`nginx` webserver with rtmp/flv patches.

This runs the actual streaming, receives rtmp streams from OBS / ffmpeg etc. and provides the streams in rtmp or http-flv format for web based players.

### auth

A simple PSK based authentication module to provide authentication for source connections.

### frontend

Provides the visible website containing a player of the stream if it's active, and a REST API.

There is more information about the API in [API.md](API.md)
