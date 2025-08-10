#using ta lightweight python image as the base  
FROM python:3.8-slim 
#selecting the directory for the container to use
WORKDIR /app
#taking the dependencies flask and redis within the requirments.txt
#copy this first so that docker has better caching
COPY requirements.txt .
#installing redis and flask dependencies from the requirments.txt
#install without caching to keep image small
RUN pip install --no-cache-dir -r requirements.txt
#copying the rest that is in this directory for the container
COPY . .
#setting the port the container should use
EXPOSE 5003
#running the flask application 
CMD [ "python", "app.py" ]