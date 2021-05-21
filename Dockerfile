FROM python:3.7
RUN python -m  pip install requests
RUN mkdir /app
WORKDIR /app
ADD  app.py /app/
ENV movie_name=""
ENV api_key=""
CMD ["python", "/app/app.py"]
