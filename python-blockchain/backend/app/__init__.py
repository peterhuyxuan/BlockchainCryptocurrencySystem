from flask import Flask, jsonify

from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()


@app.route('/')
def test():
    return 'Welcome to the blockchain'


@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())


@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = 'stubbed_transaction_data'

    blockchain.add_block(transaction_data)

    block = blockchain.chain[-1]

    return jsonify(block.to_json())


app.run()
