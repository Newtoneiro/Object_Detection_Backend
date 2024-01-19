# Flask Application Setup and Configuration

This README provides step-by-step instructions on setting up and running a Python Flask application. The application has specific requirements, environment variables, and relies on a `firebase-sdk.json` file for proper functioning.

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
   pip install -r requirements.txt
   ```

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
