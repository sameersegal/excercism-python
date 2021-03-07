from python:3-alpine
ARG token
ENV token=$token
WORKDIR /root/exercism/python
RUN apk add --no-cache bash
RUN cd /tmp \
	&& wget https://github.com/exercism/cli/releases/download/v3.0.13/exercism-linux-64bit.tgz \ 
	&& tar -xf *.tgz \
	&& mv exercism /bin/exercism \
	&& chown root:root /bin/exercism \
        && exercism configure --token=$token --workspace=/root/exercism \
	&& rm -rf /tmp/*
COPY requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt
ENTRYPOINT ["bash"]
