# docker build -t guess_who .

# Use the official Python image as the base
FROM python:3.12

# Expose the port that Streamlit will run on
EXPOSE 8080

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project into the container
COPY . ./

# Install system dependencies for PyAudio and others (if applicable)
RUN apt-get update && apt-get install -y portaudio19-dev

# Update pip and install Poetry
RUN pip install --upgrade pip

# Install Poetry (if not already installed)
RUN curl -sSL https://install.python-poetry.org | python3 -

# Update PATH to include Poetry's installation directory
ENV PATH="$HOME/.local/bin:$PATH"

# Install Python dependencies using Poetry
RUN poetry install

# Install Streamlit (if not already installed)
RUN pip install streamlit

# Set the entrypoint to run the Streamlit app with the custom options
ENTRYPOINT ["streamlit", "run", "demo.py", \
  "--browser.serverAddress=localhost", \
  "--server.enableCORS=false", \
  "--server.enableXsrfProtection=false", \
  "--server.port=8080"]
