# Slim version of Python
FROM python:3.11-slim

# Download package inforation
RUN apt-get update

# Install Tkinter library
RUN apt-get install python3-tk -y

# Commands to run app
CMD ["python3", "/src/main.py]
