# We're using Ubuntu 20.10
FROM vckyouuu/geezproject:buster

RUN git clone -b Geez-UserBot https://github.com/vckyou/Geez-UserBot /root/geezuserbot
RUN chmod 777 /root/geezuserbot \
RUN mkdir /root/geezuserbot/.bin
WORKDIR /root/geezuserbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/vckyou/Geez-UserBot/Geez-UserBot/requirements.txt

CMD [ "python3", "-m", "start" ]
