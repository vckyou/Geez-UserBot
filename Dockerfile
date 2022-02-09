# We're using Ubuntu 20.10
FROM vckyouuu/geezprojects:buster

RUN git clone -b Geez-UserBot https://github.com/vckyou/GeezUserBot /home/geezuserbot/ \
    && chmod 777 /home/geezuserbot \
    && mkdir /home/geezuserbot/bin/

COPY ./sample_config.env ./config.env* /home/geezuserbot/

WORKDIR /home/geezuserbot/

CMD [ "python3", "-m", "start" ]
