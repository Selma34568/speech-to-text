
# Speech-to-Text Application

This repository contains a Python application that converts spoken language into text using the Google Speech Recognition API.

## Features

- Continuous speech recognition.
- Output results are saved into `output.txt`.
- Handles and logs recognition errors.

## Prerequisites

Before you can run this project, you need to have Python installed on your machine. Python 3.6 or higher is recommended. You can download and install Python from [python.org](https://www.python.org/downloads/).

## Installation

To set up your local environment to run this application, follow these steps:

1. Clone the repository
  

2. Set up a virtual environment (optional, but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, use the following command from the root directory of the project:

```bash
python main.py
```

This will start the application in a mode that continuously listens to your microphone input and converts spoken words into text, which will then be appended to `output.txt`.

## Contributing

Contributions to this project are welcome. Please consider forking the repository and submitting a pull request.

## License

This project is open-sourced under the MIT License. See the `LICENSE` file for more details.
