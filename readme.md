# Pizza Delivery API

This is a simple Pizza Delivery API built using Flask, Flask-RESTful, and Flask-SQLAlchemy. It allows you to manage pizza orders, retrieve orders by order ID, create new orders, and search for orders based on specific criteria.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)

## Features

- Create new pizza delivery orders.
- Retrieve pizza delivery orders by order ID.
- Search for pizza delivery orders based on criteria like user name, pizza type, and pizza size.
- Update existing orders, including order status, pizza type, and pizza size.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- A code editor or IDE (e.g., Visual Studio Code).
- pip package manager installed.
- Git (optional) for version control.

## Installation

1. Clone this repository to your local machine (or download the ZIP file).

   ```bash
   git clone https://github.com/yourusername/pizza-delivery-api.git

   Change into the project directory:

2. Change into the project directory:
   cd pizza-delivery-api
   
3. Create a virtual environment (recommended) and activate it:
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate

4. Install the required Python packages:
   pip install -r requirements.txt
   
## Usage

-Start the Flask development server:
 python app.py
-Access the API in your web browser or using a tool like curl or Postman.
-Use the available API endpoints to create, retrieve, update, and search for pizza delivery orders.

## API Endpoints
Retrieve Order:
GET /pizza-delivery-api/order/<order_id>: Retrieve a pizza delivery order by its order ID.

Create Order:
POST /pizza-delivery-api/order/: Create a new pizza delivery order by providing order details in the request body.

Search Orders:
GET /pizza-delivery-api/order/search: Search for pizza delivery orders based on user name, pizza type, and pizza size.

## Project Structure
The project structure is organized as follows:

app.py: The main application file.
models.py: Defines the database model for pizza orders.
resources.py: Contains the API resources for creating, retrieving, searching, and updating orders.
database.py: Initializes and configures the SQLAlchemy database.
requirements.txt: Lists the required Python packages.
