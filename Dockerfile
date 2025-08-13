FROM python:3.13


COPY . /projeto_dados

WORKDIR /projeto_dados

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

#CMD ["python", "carga.py"]