FROM python

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . .
ENV FLASK_APP app.py
ENV FLASK_RUN_PORT 8000
ENV FLASK_RUN_HOST session1.demo
EXPOSE 8000
CMD ["python","app.py"]

