# We're using Ubuntu 20.10
FROM vckyouuu/geezprojects:buster

RUN git clone -b Geez-UserBot https://github.com/vckyou/GeezUserBot /root/geezuserbot/ \
    && chmod 777 /root/geezuserbot \
    && mkdir /root/geezuserbot/bin/

WORKDIR /root/geezuserbot/

CMD [ "python3" ,"start" ]
