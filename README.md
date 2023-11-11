# Request Catcher

Request Catcher is a Flask application that allows you to capture and view HTTP requests in real-time. It uses Flask and Socket.IO for server-client communication.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
## Getting Started

### Prerequisites

Make sure you have the following software installed on your machine:

- Python (version 3.x)
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/puthusseri/requestcatcher.git
   cd requestcatcher
   ```
2. Install the dependencies: 
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. The application will be accessible at http://localhost:5000
3. Open the application in your web browser.
4. As HTTP requests are sent to your server with different paths, they will be displayed in real-time on the web interface.


## Need to improve:

1. Can authentication be used in this case?
2. Adding subdomain based websockets.
