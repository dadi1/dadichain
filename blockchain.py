class Blockchain (object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_blocks(self):
        # creates new blocks
        pass

    def new_transactions(self):
        # adds a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        # hashes a block
        pass

    @staticmethod
    def last_block(block):
        # returns the last block in the chain
        pass
