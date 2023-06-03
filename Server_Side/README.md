# Pristine Apparels - Server Side

Welcome to the Server Side of Pristine Apparels, a web application designed to provide users with a seamless and enjoyable shopping experience for fashion products. This project focuses on the backend implementation and database management required to support the Pristine Apparels web application.

## Features
- API endpoints to manage products, orders, and user authentication.
- Database management using SQLite.
- File upload functionality for product images.

## Technologies Used
- Django: A high-level Python web framework for building secure and scalable applications.
- Django REST Framework: A powerful and flexible toolkit for building Web APIs.
- SQLite: A lightweight and serverless database engine.
- Python: The programming language used for server-side development.

## Project Setup
1. Clone the repository.
2. Navigate to the `Server_Side` directory.
3. Install the required Python packages by running `pip install -r requirements.txt`.
4. Run the migrations to set up the database by running `python manage.py migrate`.
5. Start the development server by running `python manage.py runserver`.
6. Open your browser and visit `http://localhost:8000` to verify the server is running.

## Project Structure
- `order`: Contains the order app responsible for managing orders and order-related functionality.
- `product`: Contains the product app responsible for managing products and product-related functionality.
- `Server_Side`: Contains the Django project configuration.
- `media/uploads`: Stores the uploaded product images.

## Contributions
Contributions to this project are welcome! If you have any ideas or improvements, feel free
