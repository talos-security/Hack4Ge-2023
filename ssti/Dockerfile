FROM python:3
COPY src/ /home/
COPY requirements.txt /home/requirements.txt
WORKDIR /home
RUN pip3 install -r requirements.txt
CMD ["python3", "server.py"]