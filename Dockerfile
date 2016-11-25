FROM debian:jessie

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

RUN apt-get update && apt-get install -y vim

# extend Ansible
RUN mkdir /usr/local/zds-site
COPY . /usr/local/zds-site/
WORKDIR /usr/local/zds-site/deploy

# install galaxy

RUN ansible-galaxy install -vvv -r requirements.yml
RUN ansible-playbook -i "localhost," -c local provision.yml
EXPOSE 80 8983
