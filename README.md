<h1 align="center">Discord Music Bot</h1>
<p align="center">A simple Discord music bot.</p>

## Feature
- `!join` summon bot into your voice channel
- `!leave` make bot to leave your voice channel
- `!play` play the given song

## Setup with docker (RECOMENDED!)
1. Download and install docker
2. Build the docker image
```sh
$ docker build . -t discord
```
3. Run the docker images
```sh
$ docker run -d \
-e TOKEN=<YOUR BOT TOKEN HERE> \
--restart always \
--name discord \
discord
```

## Setup with python
1. Download and install python version `3.6` or higher
2. Install discord.py


Linux/macOS
```sh
$ python3 -m pip install -U "py-cord[voice]"
```
Windows
```sh
$ py -3 -m pip install -U py-cord[voice]
```

3. Install wavelink

```sh
$ pip install wavelink
```
4. Insert your bot token to main.py
You can get your bot token from https://discord.com/developers/applications

5. Finally, you can start the bot

Linux
```sh
$ python3 main.py
```
Windows
```sh
$ python main.py
```
## LAVALINK SERVER
<div align="center">
 <h1>Secure (HTTPS / SSL)</h1>

HOST
      
lavalink.kyuk.my.id

PORT
      
443

PASSWORD
    
www.kyuk.my.id


 <h1>Not Secure (HTTP)</h1>

HOST

lavalink.kyuk.my.id

PORT

80

PASSWORD

www.kyuk.my.id
</div>
