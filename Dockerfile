FROM python:3.8.12-slim-buster
RUN echo "Building!"
RUN apt update
RUN apt install git -y
RUN pip install "python-telegram-bot>=13.8.1" "youtube-dl>=2021.6.6"
WORKDIR /app
COPY . .
RUN git clone https://github.com/alonitac/devOpsPlayground.git
CMD ["python3", "youtubeBot/bot.py"]