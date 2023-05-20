FROM python:3.8-slim-buster

# Install utils
RUN DEBIAN_FRONTEND="noninteractive" apt-get update && apt-get install -y tzdata keyboard-configuration
RUN apt-get install -y curl unzip groff less

# install yq - a YAML query command line tool
RUN curl -Lso yq https://github.com/mikefarah/yq/releases/download/2.2.1/yq_linux_amd64 && \
    chmod +x yq && \
    mv yq /usr/local/bin



# AWS CLI installation commands
RUN	curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN	unzip awscliv2.zip && ./aws/install


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt