FROM vckyouuu/geezprojects:buster

RUN git clone -b Geez-UserBot https://github.com/viofenando/Vio-UserBot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools

WORKDIR /root/userbot

CMD ["python3", "-m", "userbot"]
