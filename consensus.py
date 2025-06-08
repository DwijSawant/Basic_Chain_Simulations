import random

# Take input for miner power
miner_power = int(input("Enter miner power: "))
# Simulate hashrate for 3 miners

# Find the miner with the highest hashrate
hashrate1 = input("Enter hashrate for miner 1: ")
hashrate2 = input("Enter hashrate for miner 2: ")  
hashrate3 = input("Enter hashrate for miner 3: ")
highest_Hashrate = max(hashrate1, hashrate2, hashrate3) 
miner = {"power": highest_Hashrate}
print(f"Miner with highest hashrate: {miner['power']}hz/s")

# Take input for staker stake
staker_stake1 = int(input("Enter staker stake: "))
staker_stake2 = int(input("Enter staker stake: "))
staker_stake3 = int(input("Enter staker stake: "))
highest_value = max(staker_stake1, staker_stake2, staker_stake3)
staker = {"stake": highest_value}
print(f"Staker with highest stake: {staker['stake']}AVAX")
# Take input for number of voters
num_voters = 3
voters = []
for i in range(num_voters):
    account = input(f"Enter account address for voter {i+1}: ")
    vote = input(f"Enter vote for voter {i+1} : ")
    voters.append({"account": account, "vote": vote})
#Selecting voter with highest votes
highest_votes = max(voter['vote'] for voter in voters)
voters = [highest_votes]
print(f"Voter with highest votes: {highest_votes}")
# Count votes