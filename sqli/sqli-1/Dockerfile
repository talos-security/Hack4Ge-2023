FROM python:3
COPY src/ /home/src
COPY data/ /home/data
COPY requirements.txt /home/requirements.txt
WORKDIR /home
RUN pip3 install -r requirements.txt
CMD ["python3", "src/main.py"]