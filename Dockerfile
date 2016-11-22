FROM debian:8

ENV DEBIAN_FRONTEND noninteractive

# Install dependencies.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       sudo \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

# Install Ansible via pip.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential libffi-dev libssl-dev python-pip python-dev \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean
RUN pip install ansible cryptography

# extend Ansible
RUN mkdir /usr/local/deploy
COPY deploy /usr/local/deploy/
WORKDIR /usr/local/deploy
# install galaxy

RUN ansible-galaxy install -vvv -r requirements.yml
RUN ansible-playbook -i "localhost," -c local provision.yml
