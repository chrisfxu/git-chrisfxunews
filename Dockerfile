FROM python:3.8.10
 
COPY . . 

RUN pip install -r requirements.txt
CMD python app.py 

