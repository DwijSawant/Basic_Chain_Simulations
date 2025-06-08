import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, prevhash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data 
        self.prevhash = prevhash
        self.nonce = nonce
        self.hash = self.mineBlock()  # Hash based only on nonce
    #here i have inserted hashing mechanism HERE !!!!!!!  
    def mineBlock(self):
        # Calculateing hash using only the nonce value just as an example
        difficulty=input("Tell difficuly eg:1,2,3: ")
        target_prefx = '0' * int(difficulty)
        nonce = 0
        start_time = time.time()
        print("Beep boop beep! Mining in progress...")
        while True :
            hashing=hashlib.sha256(str(self.nonce).encode()).hexdigest()
            if hashing.startswith(target_prefx) :
                print("sucsessfully mined ya block !!")
                print(f"Hash: {hashing}")
                print(f"Time elapsed: {time.time() - start_time:.2f} seconds")
                print(f"Your attempts/Nonce number : {nonce}")
                break
            self.nonce += 1 
    
        return hashlib.sha256(str(self.nonce).encode()).hexdigest()

def genesis_block():
    # Manually creating genesis block just for refference
    return Block(0, time.time(), "Genesis Block", "0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f")

def create_new_block(prev_block, data, nonce=0):
    #for new block generation
    index = prev_block.index + 1
    timestamp = time.time()
    prevhash = prev_block.hash
    return Block(index, timestamp, data, prevhash, nonce)

# Initialize blockchain
blockchain = [genesis_block()]
numberofblocks = int(input("Tell number of blocks u want to print: "))
# Adding upto 3 blocks
i=1
while i<=numberofblocks :
    blockchain.append(create_new_block(blockchain[-1], f"Transaction Data {i}", i))
    i += 1



for block in blockchain:
    print(f"Block {block.index}:")
    print(f"Time: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.prevhash}")
    print(f"Hash: {block.hash}")
    print(f"Nonce: {block.nonce}\n")

Manipulation = input("do you want to change hashes? y/n : ")
if Manipulation == "y" :
    block_num = int(input("what block no you wanna manipulate ? : "))
    new_nonce = int(input(f"Enter new nonce for Block {block_num}: "))
    blockchain[block_num].nonce = new_nonce
    blockchain[block_num].hash = blockchain[block_num].mineBlock()

#now we again verify chain 
for i in range(1, len(blockchain)):
    if blockchain[i].prevhash != blockchain[i-1].hash:
        print(f"\nChain broken between Block {i-1} and Block {i}!")
        print('error! Invalid blocks')
        corrupted_index = i-1
        blockchain = blockchain[:corrupted_index]
        print("Removed corrupted blocks. New blockchain:")
        for block in blockchain:
            print(f"Block {block.index}: Hash = {block.hash}")
        else:
            print("\n Blockchain integrity maintained")

        break
            
    if blockchain[i].prevhash == blockchain[i-1].hash:
        print("\n Blockchain integrity maintained (all hashes match)")
else:
    print("Invalid block number!")

for block in blockchain:
    print(f"Block {block.index}:")
    print(f"Time: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.prevhash}")
    print(f"Hash: {block.hash}")
    print(f"Nonce: {block.nonce}\n")

