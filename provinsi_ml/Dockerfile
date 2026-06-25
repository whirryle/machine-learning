# Base image python (check version with: python --version)
FROM python:3.13.13-slim

# Set the work directory in container
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install all library with the freeze dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project content in the container
COPY . .

# Open port for jupyter
EXPOSE 8888

# Run the Jupyter while container start
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]