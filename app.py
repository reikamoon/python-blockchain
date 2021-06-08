from Flask import flask

# Creating the app node
app = Flask(__name__)

node_identifier = str(uuid4()).replace('-','')

# Initializing blockchain

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
   return "Mining a new Block"

@app.router('/chain', methods=['GET'])
def full_chain():
   response = {

       'chain' : blockchain.chain,

       'length' : len(blockchain.chain)

   }

   return jsonify(response), 200



@app.route('/transactions/new', methods=['POST'])
   def new_transaction():

       values = request.get_json()

       # Checking if the required data is there or not

       required = ['sender','recipient','amount']

       if not all(k in values for k in required):

           return 'Missing values', 400




       # creating a new transaction

       index = blockchain.new_transaction(values['sender'], values['recipient', values['amount']])

       response = {'message': f’Transaction is scheduled to be added to Block No. {index}'}

    return jsonify(response), 201



if __name__ == '__main__':

   app.run(host="0.0.0.0", port=5000)