# docker build -t guess_who .
# docker run -p 8080:8080 guess_who

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
ENV PATH="/root/.local/bin:$PATH"

# Configure Poetry to create virtual environment inside the project directory
RUN poetry config virtualenvs.in-project true

# Install Python dependencies using Poetry
RUN poetry install --no-dev

# Check if Poetry's virtual environment exists and print the environment path
RUN echo "Poetry virtual environment path:" && poetry env info --path

# Check if the proper dependencies (e.g., openai) are installed in the virtual environment
RUN poetry run python -c "import openai; print('openai is installed')"

# Set the entrypoint to run Streamlit with Poetry's environment
ENTRYPOINT ["poetry", "run", "streamlit", "run", "demo.py", \
  "--browser.serverAddress=localhost", \
  "--server.enableCORS=false", \
  "--server.enableXsrfProtection=false", \
  "--server.port=8080"]
