| Blockchain Name     | Type            | Consensus Mechanism Used | Permission Model | Speed / Throughput (TPS) | Smart Contract Support | Token Support    | Typical Use Case                        | Notable Technical Feature                          |
|---------------------|-----------------|--------------------------|------------------|--------------------------|------------------------|------------------|-----------------------------------------|---------------------------------------------------|
| Bitcoin             | Public          | PoW (Proof of Work)      | Open             | 4-7 TPS                  | N                      | Native (BTC)     | Digital Currency                        | Decentralization, Security                         |
| Hyperledger Fabric  | Private         | Pluggable (e.g., PBFT)   | Permissioned     | 1000+ TPS                | Y (Chaincode - Go, JS) | N (Optional)     | Enterprise Solutions                    | Modular Architecture, Privacy Features             |
| Quorum              | Consortium      | IBFT / Raft              | Permissioned     | 100-200 TPS              | Y (Solidity)           | N (Optional)     | Enterprise Banking, Supply Chain        | Privacy (Tessera), Ethereum Compatibility          |


As expressed in the above table all types of chain be it Public Private or Consortium being based on Blockchain technology can be differed by there type using there use cases and type of structure.

Here bitcoin being a public block chain which uses proof of work is a open permissioned model meaning where in anyone who desired to run a node on this network can run one without any permissioned prerequisites due to this and the consensus proof of work although we can see the Txn per sec (TPS) of this chain is lowest amongst the others it's the most Secure amongst all.

While for HyperLeger being a private has the highest TPS but in terms of security or immutability of data is the lowest meaning it is a single point failure for private chains as the node is run by a single entity.

While Quorum being Consortium type chain now is being run by not just one entity rather a small group of entities hence the mid TPS which we can notice, and same for security, it is like a group of board members within a grouped company which run nodes.

For a decentralised app it is sensible to use public blockchain type meaning chains like ethereum, polygon, avalanche.

For a supply chain network among known partners it is sensible to use Consortium blockchain like Quorum.

For interbank finance application private or consortium chain can be used depending if how many number of entities are involved like, hyperledger, Quorum..etc
