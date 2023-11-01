import os

os.system('curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok')

os.system('ngrok authtoken 2UlnaBCFh4agJWZGqSrh7UmGMT9_2aQ3jsmPZUweowZA554zU')

os.system('ngrok http 80')
