FROM xluxz/geezproject:buster

# Clone repo and prepare working directory
RUN git clone -b Geez-UserBot https://github.com/vckyou/Geez-UserBot /home/geezproject/ \
    && chmod 777 /home/geezproject \
    && mkdir /home/geezproject/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/geezproject/

# Setup Working Directory
WORKDIR /home/geezproject/

# Finalization
CMD ["python3","-m","userbot"]
