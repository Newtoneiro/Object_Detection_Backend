# Object Detection Backend Setup and Configuration

This README provides step-by-step instructions on setting up and running a Object Detection Backend application. The application has specific requirements, environment variables, and relies on a `firebase-sdk.json` file for proper functioning.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Prerequisites

Before setting up the Flask application, ensure the following prerequisites are met:

1. **Python and Pip**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Virtual Environment (Optional but Recommended)**: It's good practice to use a virtual environment to isolate dependencies. Install it using the following commands:

   ```bash
   pip install virtualenv
   ```

   Create a virtual environment:

   ```bash
   virtualenv venv
   ```

   Activate the virtual environment:

   - **On Windows:**
     ```bash
     .\venv\Scripts\activate
     ```
   - **On Unix or MacOS:**
     ```bash
     source venv/bin/activate
     ```

3. **Firebase SDK**: Obtain the `firebase-sdk.json` file from the Firebase console. Place it in the root directory of your Flask application. You probably have to create a new project and set it up, before you can access this file.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Newtoneiro/Object_Detection_Backend.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-flask-app
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements/requirements.txt
   ```

   Additionally you can install the ultralytics specific ones (I needed them for more advanced `ultralytics` stuff)

## Configuration

Set the required environment variables for your Flask application. Create a `.env` file in the root directory and add the following:

```dotenv
SERVER_API_ADDRESS=your_server_api_address
SERVER_API_PORT=your_server_api_port
```

Replace your_server_api_address and your_server_api_port with the desired values.

## Running the Application

Run the Flask application using the following command:

```bash
   python run.py
```

Your Flask application should now be running. Visit `http://your_server_api_address:your_server_api_port` in your web browser to access the application.

Remember to manage your virtual environment and ensure that the required dependencies and environment variables are set each time you run the application.

Feel free to customize the Flask application according to your specific needs. For additional information on Flask, refer to the official Flask documentation.

## License

OBJECT DETECTION Open Source License

Version 1.0, 19/01/2024

Permission is hereby granted, free of charge, to any person or organization obtaining a copy of the software and accompanying documentation covered by this license (the "Software") to use, reproduce, display, distribute, execute, and transmit the Software, and to prepare derivative works of the Software, and to permit third-parties to whom the Software is furnished to do so, all subject to the following:

1. Redistributions of source code must retain the above copyright notice, this list of conditions, and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions, and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of Object Detection nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contributing

We welcome contributions from the community. To contribute to Object Detection, follow these steps:

1. Fork the repository on GitHub.
2. Clone the forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them with descriptive commit messages.
5. Push your changes to your fork on GitHub.
6. Open a pull request to the `main` branch of the original repository.

Ensure your pull request includes:

- A clear description of the problem or feature.
- Tests and documentation for your changes.

We will review and merge well-documented and tested contributions. Thank you for contributing to Object Detection!

For more details, please read our [Contributing Guidelines](CONTRIBUTING.md).

## Acknowledgments

`No contributions yet`

Thank you for being a part of our open-source community!
