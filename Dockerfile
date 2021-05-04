# We're using Ubuntu 20.10
FROM koala21/kampangbot/buster

#
# Clone repo and prepare working directory
#
RUN git clone -b alpha https://github.com/ximfine/Xbot-Remix /home/xnewbie/
RUN mkdir /home/xnewbie/bin/
WORKDIR /home/xnewbie/

# Upgrade pip
RUN pip install --upgrade pip

#Install python requirements
# RUN pip3 install -r https://raw.githubusercontent.com/ximfine/XBot-Remix/alpha/requirements.txt

CMD ["python3","-m","userbot"]
