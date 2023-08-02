# Usar una imagen base de Python
FROM python:3.9

# Establecer una variable de entorno para asegurarse de que la salida de Python se envíe directamente al terminal sin almacenamiento en búfer
ENV PYTHONUNBUFFERED=1

# Crear un directorio de trabajo
WORKDIR /app

# Copiar los requisitos y instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto que utiliza Flask
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python3", "main.py"]