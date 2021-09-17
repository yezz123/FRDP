# Pull base image
FROM python:3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory for any subsequent
WORKDIR /app/

# Copy Requirements to app folder
COPY ./requirements.txt /app/requirements.txt

# install gcc and update environment
RUN apt-get update -y --no-install-recommends \
    && apt-get install -y --no-install-recommends gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Run the pip command to install the requirements
RUN pip install --no-cache-dir -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

# Copy files or folders from source to the dest path in the image's filesystem.
COPY . /app/

# Set the environment variable key to the value value.
ENV ACCESS_LOG=${ACCESS_LOG:-/proc/1/fd/1}
ENV ERROR_LOG=${ERROR_LOG:-/proc/1/fd/2}

# Define the network ports that this container will listen on at runtime.
EXPOSE 8000