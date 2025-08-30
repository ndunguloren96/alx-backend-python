# Use a base image with Python pre-installed
FROM python:3.10-slim

# Install Jenkins agent tools
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

# Create a user for Jenkins agent
RUN groupadd -g 1000 jenkins && useradd -u 1000 -g 1000 -m -s /bin/bash jenkins
USER jenkins

# Set work directory
WORKDIR /home/jenkins/workspace
