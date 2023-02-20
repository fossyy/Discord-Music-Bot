# PULLING IMAGE FROM DOCKER HUB
FROM kyuq2007/alpinepy

# DEFINE WORKING DIRECTORY 
WORKDIR /opt/discord

# COPY AND INSTALLING DEPEDENCY
COPY ./requirements.txt /opt/discord
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# COPY BOT FILR TO WORKING DIRECTORY 
COPY . /opt/discord

# MAIN COMMAND
CMD ["python3","main.py"]