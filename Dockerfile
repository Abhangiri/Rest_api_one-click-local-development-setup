# Use a python base image
FROM python:3.9-slim  AS build

# SET THE WORKING DIRECTORY
WORKDIR /app        


# copy requirement.txt
COPY requirements.txt  /app/ 

# install dependency
RUN pip install --no-cache-dir -r requirements.txt 


# stage 2 : Final stage 

FROM python:3.9-slim 

# Set enviornment variable

ENV FLASK_APP=run.py
ENV FLASK_DEBUG=1 
ENV DATABASE_URI=mysql+pymysql://root:Admin%40123@host.docker.internal:3306/student_db1

# Set the working directory
WORKDIR /app


# CopY the application file from the build stage 

COPY . /app

# copy any dependencies if left any
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port flask to run

EXPOSE 5000


# Run the flask app

# CMD ["flask", "run", "--host=0.0.0.0"]

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]



