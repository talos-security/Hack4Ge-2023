FROM python:3
COPY main.py /home/main.py
COPY static/ /home/static/
COPY templates/ /home/templates/
COPY sample.db /home/sample.db 
COPY test.sql /home/test.sql
COPY requirements.txt /home/requirements.txt
WORKDIR /home
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]