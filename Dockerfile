FROM python:3


WORKDIR ./infobot
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./infobot.py" ]

