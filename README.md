---

# Tambola Ticket Generator

## Overview

This project is a Tambola (also known as Housie or Bingo) ticket generator implemented in Python using Flask. It allows users to generate Tambola tickets, save them to a SQLite database, and retrieve the saved tickets with pagination.

## Features

- **Ticket Generation**: Generate Tambola tickets with random numbers.
- **Database Integration**: Store generated tickets in an SQLite database.
- **Pagination**: Retrieve saved tickets with pagination for better performance.

## Project Structure

The project is structured as follows:

- `app.py`: Main Flask application file.
- `ticket_generator.py`: Module for generating Tambola tickets.
- `database_service.py`: Module for handling database operations.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/meeran2021/tambula-ticket-generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd tambola-ticket-generator
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python app.py
    ```

The application will be accessible at `http://127.0.0.1:5000/`.

## API Endpoints

- **Generate Tickets**: `POST /generate_tickets`
  - Generates Tambola tickets and saves them to the database.

- **Show Tickets**: `GET /show_tickets`
  - Retrieves saved Tambola tickets with pagination.

## Usage

1. Generate Tickets:
   - Make a `POST` request to `/generate_tickets` with appropriate payload.

2. Show Tickets:
   - Make a `GET` request to `/show_tickets` with optional query parameters for pagination (`page` and `per_page`).

## Error Handling

The application includes robust error handling and logging to provide informative error messages.

## Data Validations

Input data is validated to ensure correctness, and appropriate error messages are returned for invalid requests.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Follow the standard [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

---

