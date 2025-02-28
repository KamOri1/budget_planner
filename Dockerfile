FROM python:3.13.2-bullseye

WORKDIR /app
# Upgrade pip
RUN pip install --upgrade pip

## Copy the Django project  and install dependencies
#COPY requirements.txt  /app/

# run this command to install all dependencies
#RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONHTTPSVERIFY=0
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


COPY pyproject.toml poetry.lock /app/
RUN pip3 install poetry
RUN poetry install --no-root


# Copy the Django project to the container
COPY . /app/

# Expose the Django port
EXPOSE 8000

# Run Django’s development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
