import hashlib
from time import time
from urllib import response
from urllib.parse import urlparse

class Blockchain (object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        #cretion of the genesis block
        self.new_block(previous_hash=1, proof= 100)
    
    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1
        
        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n--------------\n")

            if block['previous_hass'] != self.hash(last_block):
                return False
            
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False
            
            last_block = block
            current_index += 1

        return True
    
    def resolve_conflicts(self):
        neighbours = self.nodes
        new_chain = None

        if response.status_code == 200:
            length = response.json()['length']
            chain = response.json()['chain']
            

            if length > max_length and self.valid_chain(chain):
                max_length = length
                new_chain = chain
        
        if new_chain:
            self.chain = new_chain
            return True
        
        return False
    
    def new_blocks(self, proof, previous_hash = None):
        #crate the new block inside the blockchain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transacions': self.current_transcions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # reset the current list of transctions
        self.current_transactions = []

        # adds the block to the blockchain
        self.chain.append(block)
        # return the new block
        return block

    def new_transactions(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1
    
    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        # hashes a block
        pass

    @staticmethod
    def last_block(block):
        # returns the last block in the chain
        pass

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1
    
    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof
    
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
