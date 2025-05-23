# Infomatrix App

This project is a web application built using FastAPI for managing products in a MongoDB database. It provides a RESTful API to perform CRUD (Create, Read, Update, Delete) operations on products.

## Project Structure

```
infomatrix-app
├── app
│   ├── main.py          # Contains the FastAPI application code
│   └── __init__.py      # Marks the app directory as a Python package
├── requirements.txt      # Lists the project dependencies
└── README.md             # Documentation for the project
```

## Installation

To set up the project, follow these steps:

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the FastAPI application, execute the following command:

```
uvicorn app.main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

## API Endpoints

- `GET /`: Returns a welcome message.
- `GET /get-product/{product_id}`: Retrieves a product by its ID.
- `GET /get-by-name?name={name}`: Retrieves a product by its name.
- `POST /add-product/`: Adds a new product.
- `PUT /update-product/{product_id}`: Updates an existing product.
- `DELETE /delete-product/{product_id}`: Deletes a product by its ID.

## Usage Examples

- To add a product, send a POST request to `/add-product/` with a JSON body:
  ```json
  {
    "name": "Product Name",
    "price": 100,
    "quantity": 10
  }
  ```

- To update a product, send a PUT request to `/update-product/{product_id}` with the fields you want to update.

## License

This project is licensed under the MIT License.