import blockchain as bc

from hashlib import sha256
import hashlib
import json
from time import time
from textwrap import dedent
from uuid import uuid4
from flask import Flask, jsonify, request

# initializing the node
app = Flask(__name__)

node_indentifier = str(uuid4()).replace('-','')

blockchain = bc.Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
#  run the proof of work algorithm to get the next proof
    last_block = blockchain.last
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(
        sender = "0",
        recipient= node_indentifier,
        amount = 1
    )

    bc.block = blockchain.new_block(proof, bc.previous_hash)
    
    bc.response = {
        'message': "New Block Forged",
        'index': bc.block['index'],
        'transactions': bc.block['transactions'],
        'proof': bc.block['proof'],
        'previous_hash': bc.block['previous_hash'],
    }

    return jsonify(bc.response), 200
    
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"
    
@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400
        
    index = blockchain.new_transacion(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transacion will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/nodes/register', methods=['Post'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400
    
    for node in nodes:
        bc.Blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }

    return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = bc.blockchain.resolve_conflicst()

    if replaced:
        response = {
            'message': 'Our chain in authoritative',
            'chain': blockchain.chain
        }
        return jsonify(response), 200
    
    response = {
        'message': 'Our chain is authoritative',
        'chain': blockchain.chain
    }
    return jsonify(response), 200
    
    
