FROM python:3.9-slim

WORKDIR /app

# Copiar archivos de tu proyecto al contenedor
COPY cliente_rpc.py ./ 
COPY servidor_rpc.py ./  
COPY index.html ./  
COPY requirements.txt ./ 

# Listar los archivos en el contenedor para depuración
RUN ls -l /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "servidor_rpc.py"]
