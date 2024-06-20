import hashlib
import time


class Block:
    """A class representing a block in the blockchain."""

    def __init__(self, index, previous_hash, timestamp, data):
        """
        Initialize a block with the given index, previous_hash, timestamp, and data.

        Args:
            index (int): The index of the block.
            previous_hash (str): The hash of the previous block.
            timestamp (int): The timestamp of the block creation.
            data (str): The data stored in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash of the block using SHA-256.

        Returns:
            str: The SHA-256 hash of the block.
        """
        block_string = f'{self.index}{self.previous_hash}{self.timestamp}{self.data}'.encode()
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    """A class representing the blockchain."""

    def __init__(self):
        """Initialize the blockchain with the genesis block."""
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Create the genesis block with index 0, previous hash "0", and data "Genesis Block".

        Returns:
            Block: The genesis block.
        """
        return Block(0, "0", int(time.time()), "Genesis Block")

    def get_latest_block(self):
        """
        Get the latest block in the blockchain.

        Returns:
            Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Add a new block to the blockchain.

        Args:
            data (str): The data to be stored in the block.
        """
        latest_block = self.get_latest_block()
        new_block = Block(latest_block.index + 1, latest_block.hash, int(time.time()), data)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validate the blockchain by checking hashes and previous hashes.

        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


# Example usage:
blockchain = Blockchain()
blockchain.add_block("First Block")
blockchain.add_block("Second Block")

# Print each block in the blockchain
for block in blockchain.chain:
    print(f'Index: {block.index}, Timestamp: {block.timestamp}, Data: {block.data}, Hash: {block.hash}, Previous Hash: {block.previous_hash}')

# Print whether the blockchain is valid
print(f'Is blockchain valid? {blockchain.is_chain_valid()}')