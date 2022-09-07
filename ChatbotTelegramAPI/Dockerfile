#
FROM python:3.8

# Maintainer info
LABEL maintainer="philip.kohlmann@studium.uni-hamburg.de"

# Make working directories
RUN  mkdir -p  /api
WORKDIR  /api

# Upgrade pip with no cache
RUN pip install --no-cache-dir -U pip

# Copy application requirements file to the created working directory
COPY requirements.txt .

# Install application dependencies from the requirements file
RUN pip install -r requirements.txt

# Copy every file in the source folder to the created working directory
COPY  . .

COPY output_final/ output_final/

#
CMD ["python", "main.py"]