# We're using Ubuntu 20.10
FROM vckyouuu/geezprojects:buster

#
# Clone repo and prepare working directory
#
RUN git clone -b Geez-UserBot https://github.com/vckyou/Geez-UserBot /home/userbot/
RUN mkdir /home/userbot/bin/
WORKDIR /home/userbot/

# Upgrade pip
RUN pip install --upgrade pip

# Install python requirements
# RUN pip3 install -r https://raw.githubusercontent.com/vckyou/Geez-UserBot/Geez-UserBot/requirements.txt

CMD ["python3","-m","userbot"]
