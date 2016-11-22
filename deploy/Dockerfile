FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

# Install dependencies.
RUN apt-get install -y software-properties-common
RUN apt-add-repository -y ppa:ansible/ansible

# Install Ansible via apt.
RUN apt-get -y update
RUN apt-get install -y ansible

# setup ssh
RUN mkdir ~/.ssh
ADD ansible_id_rsa ~/.ssh/id_rsa
ADD ansible_id_rsa.pub ~/.ssh/id_rsa.pub

# extend Ansible
ADD ansible.cfg  /etc/ansible/ansible.cfg
ADD hosts  /etc/ansible/inventory/hosts
