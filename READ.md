Theory: 
1.	Block Chain Basics
- Define Blockchain: Blockchain is complete new format/organisation of data handling involving validation , trustless and robust Secure infrastructure. It uses Format where in Blocks are interconnected linearly ideally in a form of chain where in any one alteration in any block within the chain will lead to all the block ahead of it getting absolute and invalid.
Here the ledger is not maintained by a single entity while it is the multiple users using the chain maintaining copy of the ledger and validating it within each other hence the term trustless and secure than traditional infrastructures like eg: AWS , SWIFT…etc
-RealLife uses of blockchain : 
Blockchain being a ground lvl infrastructure format its open on any usecase which involves maintaining high lvl data in a very secure way . For example : 
-Land records: Can be used to onboard all land records sequecially on a public ledger avoiding documental loss and misconceptions long term.
-Medical data: Can be used to maintain a mono profile across a region for a single user instead of cluttered medical files , can bypass diplomatic boundaries and still maintain immutability


2. Example:
-Supposing a block has 4 transactions: TxA, TxB, TxC, TxD.
Hash each transaction:
HashA = SHA-256(TxA)
HashB = SHA-256(TxB)
HashC = SHA-256(TxC)
HashD = SHA-256(TxD)
Pairing  and hashshing them:
HashAB = SHA-256(HashA + HashB)
HashCD = SHA-256(HashC + HashD)
Final Merkle root:
MerkleRoot = SHA-256(HashAB + HashCD)
This root is stored in the block header. Now to verify you don’t need entire chain Just the calculated Merkle root should match the one in the block header we just saw stored on.
![image](https://github.com/user-attachments/assets/7cc037d0-6bfb-4b5c-9430-85cfefbedf59)


3. What is Proof of Work and why does it require energy?
Ans: Proof of work is process which involved computational power for hashing to reach consensus in a chain and ultimately validating txn , hence to run this “computational power” you need a lot of electricity hence so it requires energy to run pow . 


What is Proof of Stake and how does it differ?
Ans: Pos is a consensus type where in the validator instead of computing hashes he stakes it on the chain as a form of security to approve transactions where in if one validator becomes malicious his staked amount shall be seized from his ownership. 


What is Delegated Proof of Stake and how are validators selected?
Ans: DPos is some selected validators on the chain which will stake and run the consensus , the way these validators are selected is a vote is done withing the community of the chain and the highest is voted in .
