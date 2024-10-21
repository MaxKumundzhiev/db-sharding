FROM python:3.12.4-slim

WORKDIR /server

COPY ./requirements.txt /server
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY . /server

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run app.py when the container launches
CMD ["uvicorn", "main:application", "--host", "0.0.0.0", "--port", "8000"]