# Docker Tag Images, Using Python Slim Buster.
FROM xluxz/xluxzuser:Buster
# ===========================================
#               Geez - Userbot
# ===========================================
RUN git clone -b Geez-Userbot https://github.com/vckyou/Geez-UserBot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --no-cache-dir --upgrade pip setuptools
WORKDIR /root/userbot

# Install Requirements Packages
RUN pip3 install --no-cache-dir -r https://raw.githubusercontent.com/vckyou/Geez-UserBot/Geez-UserBot/requirements.txt

# Finishim
CMD ["python3","-m","userbot"]
