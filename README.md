# Cupcakes API

## Overview
The Cupcakes API is a RESTful web service designed as part of a learning project to demonstrate the ability to create, read, update, and delete (CRUD) resources on a server. This project utilizes Flask, a lightweight WSGI web application framework in Python, to build the API and manage interactions with a PostgreSQL database using SQLAlchemy. The API provides endpoints for managing cupcake data, including features like listing all cupcakes, retrieving the details of a specific cupcake, adding new cupcakes, updating existing cupcakes, and deleting cupcakes.

## Features
- **RESTful API Design**: Adheres to the principles of REST for creating readable and maintainable web services.
- **CRUD Operations**: Supports Create, Read, Update, and Delete operations on cupcake resources.
- **Database Integration**: Uses PostgreSQL for data storage and SQLAlchemy ORM for database interactions.
- **Error Handling**: Implements basic error handling to manage and respond to erroneous requests.
- **Frontend Integration**: Includes a basic frontend for interacting with the API, showcasing how a RESTful API can be consumed by a web application.

## Technologies Used
- Flask
- SQLAlchemy
- PostgreSQL
- HTML/CSS/JavaScript (for the frontend)
- Axios (for making API requests in the frontend)
- jQuery (for frontend DOM manipulation)

## API Endpoints
| Method | Endpoint                 | Description                         |
| ------ | ------------------------ | ----------------------------------- |
| GET    | `/api/cupcakes`          | List all cupcakes                   |
| GET    | `/api/cupcakes/<int:id>` | Retrieve a specific cupcake by ID   |
| POST   | `/api/cupcakes`          | Add a new cupcake                   |
| PATCH  | `/api/cupcakes/<int:id>` | Update an existing cupcake by ID    |
| DELETE | `/api/cupcakes/<int:id>` | Delete a specific cupcake by ID     |

## Installation and Setup
Simply create an virtual environment, install the dependencies from the requirement.txt, create a database named cupcakes (createdb cupcakes), run the seed.py, and flask run in terminal!







## Contact
You can reach out to me at jiahaoli0465@gmail.com or contact me on linkedin @jiahaoli0465