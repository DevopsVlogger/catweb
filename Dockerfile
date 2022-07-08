# our base image
FROM python:3.10

# app working directory
WORKDIR /usr/src/app


# copy al the files to the container
COPY . . 

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "./app.py"]