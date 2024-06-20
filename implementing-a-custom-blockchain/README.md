# Implementing a Custom Blockchain
* Create a simple blockchain implementation in Python. The blockchain should include the ability to add new blocks, validate the chain, and check for data integrity. Each block should contain an index, timestamp, data, previous hash, and current hash.

# Simple Blockchain Implementation
This project implements a simple blockchain using Python. The blockchain consists of blocks, each containing an index, a previous hash, a timestamp, and some data. The blocks are linked together through their hashes to form a secure chain.

## Files

- `blockchain.py`: Contains the main code for the blockchain implementation.

## Classes
### `Block`
Represents a block in the blockchain.

#### Methods

- `__init__(self, index, previous_hash, timestamp, data)`
   - Initializes a block with the given index, previous hash, timestamp, and data.

<li>`calculate_hash(self)`


- Calculates the hash of the block using SHA-256.
- Returns the SHA-256 hash of the block.

### `Blockchain`
Represents the blockchain.

#### Methods

- `__init__(self)`
   - Initializes the blockchain with the genesis block.

<li>`create_genesis_block(self)`


- Creates the genesis block with index 0, previous hash "0", and data "Genesis Block".
- Returns the genesis block.

<li>`get_latest_block(self)`


- Gets the latest block in the blockchain.
- Returns the latest block.

<li>`add_block(self, data)`


- Adds a new block to the blockchain.
- Args:
   - `data` (str): The data to be stored in the block.

<li>`is_chain_valid(self)`


- Validates the blockchain by checking hashes and previous hashes.
- Returns `True` if the blockchain is valid, `False` otherwise.

## Usage

- Create an instance of the `Blockchain` class.
- Add blocks to the blockchain using the `add_block` method.
- Check the validity of the blockchain using the `is_chain_valid` method.