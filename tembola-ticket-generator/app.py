from flask import Flask, request, jsonify
import logging

from ticket_generator import generate_unique_tickets
from database_service import save_tickets_to_db, retrieve_tickets

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.ERROR)


#Generate tickets and save to DB
@app.route('/generate_tickets', methods=['POST'])
def generate_tickets():
    try:
        if request.method == 'POST':
            num_of_tickets = int(request.json.get('num_of_tickets'))
            if num_of_tickets <= 0:
                raise ValueError("Number of tickets must be greater than zero.")
        
        generated_tickets = generate_unique_tickets(num_of_tickets)

        save_tickets_to_db(generated_tickets)

        return jsonify({'message': f'Successfully generated and saved {num_of_tickets} tickets .'}), 200
    
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return jsonify({'error': str(ve)}), 400
    
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


#Fetch tickets from DB
@app.route('/show_tickets', methods=['GET'])
def show_tickets():
    try:
        if request.method == 'GET':   
            page = int(request.args.get('page', 1))
            tickets_per_page = int(request.args.get('tickets_per_page', 10))

            retrieved_tickets = retrieve_tickets(page=page, tickets_per_page=tickets_per_page)

            return jsonify({'tickets': retrieved_tickets}), 200  
            

    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    app.run(debug=True)