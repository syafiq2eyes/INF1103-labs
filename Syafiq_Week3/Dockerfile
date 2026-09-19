FROM python:3.11-slim 
# Use the official Python runtime image as your baseline kitchen
WORKDIR /app                  
# Establish an active working directory inside the container
COPY modular_auditor.py .
# Copy our local auditor.py script into the container workspace
CMD [ "python", "modular_auditor.py" ]
# Define the execution command to run when the container

  