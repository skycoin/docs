---
title :  'Block Chain'
---

## Block Chain


The block chain provides Skycoin's public ledger, an ordered and timestamped record
of transactions. This system is used to protect against double spending
and modification of previous transaction records.

Each full node in the Skycoin network independently stores a block chain
containing only blocks validated by that node. When several nodes all
have the same blocks in their block chain, they are considered to be in
[consensus][/en/glossary/consensus]{:#term-consensus}{:.term}. The validation rules these
nodes follow to maintain consensus are called [consensus
rules][/en/glossary/consensus-rules]{:#term-consensus-rules}{:.term}. This section describes many of
the consensus rules used by Skycoin Core.


### Block Chain Overview


![Block Chain Overview](/img/dev/en-blockchain-overview.svg)

The illustration above shows a simplified version of a block chain.
A [block][/en/glossary/block]{:#term-block}{:.term} of one or more new transactions
is collected into the transaction data part of a block.
Copies of each transaction are hashed, and the hashes are then paired,
hashed, paired again, and hashed again until a single hash remains, the
[merkle root][/en/glossary/merkle-root]{:#term-merkle-root}{:.term} of a merkle tree.

The merkle root is stored in the block header. Each block also
stores the hash of the previous block's header, chaining the blocks
together. This ensures a transaction cannot be modified without
modifying the block that records it and all following blocks.

Transactions are also chained together. Skycoin wallet software gives
the impression that coins are sent from and to wallets, but
they really move from transaction to transaction. Each
transaction spends the coins previously received in one or more earlier
transactions, so the input of one transaction is the output of a
previous transaction.

![Transaction Propagation](/img/dev/en-transaction-propagation.svg)

A single transaction can create multiple outputs, as would be
the case when sending to multiple addresses, but each output of
a particular transaction can only be used as an input once in the
block chain. Any subsequent reference is a forbidden double
spend---an attempt to spend the same coins twice.

Output identifiers are formed by hashing the [hash identifier (TXIDs)][/en/glossary/txid]{:#term-txid}{:.term} of the corresponding transaction, together with
its coins, hours value and the receipt address.

Because each output of a particular transaction can only be spent once,
the outputs of all transactions included in the block chain can be categorized as either
[Unspent Transaction Outputs (UTXOs)][/en/glossary/unspent-transaction-output]{:#term-utxo}{:.term} or spent transaction outputs. For a
payment to be valid, it must only use UTXOs as inputs.

If the value of a
transaction's outputs exceed its inputs, the transaction will be
rejected---but if the inputs exceed the value of the outputs, any
difference in value is considered as a 
[transaction fee][/en/glossary/transaction-fee]{:#term-transaction-fee}{:.term}
that's automatically [burned][proof of burn] by the Skycoin system ledger.
For example, in the illustration above, each transaction spends 10,000 coins
fewer than it receives from its combined inputs, effectively paying a 10,000
coins transaction fee that can't be used any more.


### Design Decisions


After thoughtful research of the state of the art in cryptocurrency technologies
and analysis of results of simulations, the underlying principles of Skycoin
are based on the following pilars.

#### *Design decision #1* : Performant consensus algorithm

The objective of the Skycoin is to run an optimal set of rules for each node
to follow during consensus trials, so that the final agreement between nodes
can be reached fast, and would require minimal network traffic.

#### *Design decision #2* : Survive intelligent attacks

The network should be operational even after a large-scale coordinated attack by a well-organized network of malicious nodes.

#### *Design decision #3* : Impose low-barries to join the network

The algorithm is a scalable and computationally-inexpensive alternative to
[proof of work][], therefore both the consensus algorithm and block-making can
run on a budget hardware that have low price and low energy consumption.

#### *Design decision #4* : Resilience to centralization

Satoshi originally intended the Bitcoin network to be decentralized, over
hundreds of thousands of computers. Today, the Bitcoin network is completely
controlled by three mining pools. Bitcoin is no longer decentralized. Skycoin's
consensus algorithm is designed to achieve true decentralization of blockchain
consensus.

#### *Design Decision #5* : Keep complexity and logic outside of blockchains

Many blockchains implement both the control logic and the data storage plane at
the blockchain level. We believe that not using blockchains for
data storage is necessary for scalability and keeping complex logic outside of
blockchains is important for both security and scalability. Nodes on the
network should not be required to compute complex untrusted programs just to
stay synced with the network. Further, it’s hard to introduce new features to
blockchains after they’ve been deployed and gained real-world usage.

#### *Design decision #6* : Nodes are intelligent.

Each node is able to form its own independent opinion (e.g. best next block) by
doing a robust statistical analysis of the opinions it received.

#### *Design decision #7* : Nodes are skeptical.

Each node always performs authorship verification and fraud detection.

#### *Design decision #8* : Nodes are sovereign.

While other node’s opinions are taken into account, the node neither align itself
with any group or authority, nor it seeks a payment in return for supporting a
given opinion.

#### *Design decision #9* : Nodes are content generators.

The node is able to receive raw data (e.g. low-level, elementary events such as
transactions) and produce an independent research that leads to a new opinion
(e.g. block hash).


### Proof Of Burn


The block chain is collaboratively maintained by anonymous peers on the network.
Skycoin requires that each block resulted expensive enough for a node to create
it and include it into the blockchain in consensus to others. Skycoin consensus
relies on the generic mechanism of proof of burn combined with statistical opinion
dynamics framework. Coins are [burned][proof of burn] as blocks are included in
the blockchain. Therefore, opposite to other cryptocurrency consensus systems
based on [proof of work][/en/glossary/proof-of-work]{:#term-proof-of-work}{:.term}
Skycoin does not force nodes to spend significant amounts of life saving
resources and assets so as to add new blocks to the block chain.
Chaining blocks together makes it impossible to modify transactions included
in any block without modifying all following blocks. As a
result, the cost to modify a particular block increases with every new block
added to the block chain, magnifying the effect of the proof.

In Skycoin there is no notion of mining . No new coins are created as
blocks are included in the blockchain. There are no rewards. There are no fees
or other incentives awarded to network nodes.

In Skycoin an initial [genesis block][/en/glossary/genesis-block]{:#term-genesis-block}{:.term}
was created with 100M coins. This was split to 100 [addresses][distribution addresses],
1M each. Therefore there is no generation transaction in blocks.
All coins were created in
the [genesis block][/en/glossary/genesis-block]{:#term-genesis-block}{:.term}.
The [proof of burn][] used in Skycoin consists in the impossibility of spending
transaction fees. Fees are paid in [coin hours][coin hour]. A transaction must
spend at least one [coin hour][] to be valid, and half (rounded up) of the
[coin hours][coin hour] being spent must be destroyed.


### Block Height And Forking


TODO: Document block height and forking


### Transaction Data


Every block must include one or more transactions. All transactions are encoded
into blocks in binary rawtransaction format.

The rawtransaction format is hashed to create the
[transaction outer hash identifier (TXIDs)][/en/glossary/txid]{:#term-txid}{:.term}.
From these txids, the [merkle tree][/en/glossary/merkle-tree]{:#term-merkle-tree}{:.term}
is constructed by pairing each
txid with one other txid and then hashing them together. If there are
an odd number of txids, the txid without a partner is hashed with a
copy of itself.

The resulting hashes themselves are each paired with one other hash and
hashed together. Any hash without a partner is hashed with itself. The
process repeats until only one hash remains, the merkle root.

For example, if transactions were merely joined (not hashed), a
five-transaction merkle tree would look like the following text diagram:


~~~
       ABCDEEEE .......Merkle root
      /        \
   ABCD        EEEE
  /    \      /
 AB    CD    EE .......E is paired with itself
/  \  /  \  /
A  B  C  D  E .........Transactions
~~~


As discussed in the Simplified Payment Verification (SPV) subsection,
the merkle tree allows clients to verify for
themselves that a transaction was included in a block by obtaining the
merkle root from a block header and a list of the intermediate hashes
from a full peer. The full peer does not need to be trusted: it is
expensive to fake block headers and the intermediate hashes cannot be faked or
the verification will fail.

For example, to verify transaction D was added to the
block, an SPV client only needs a copy of the C, AB, and EEEE hashes in addition to the
merkle root; the client doesn't need to know anything about any of the
other transactions. If the five transactions in this block were all at
the maximum size, downloading the entire block would require over
500,000 bytes---but downloading three hashes plus the block header
requires only 140 bytes.


TODO: Sizes in bytes mentioned above are for Bitcoin. Update accordingly for Skycoin


Note: If identical txids are found within the same block, there is a possibility that the merkle tree may collide with a block with some or all duplicates removed due to how unbalanced merkle trees are implemented (duplicating the lone hash).
Since it is impractical to have separate transactions with identical txids, this does not impose a burden on honest software, but must be checked if the invalid status of a block is to be cached;
otherwise, a valid block with the duplicates eliminated could have the same merkle root and block hash, but be rejected by the cached invalid outcome, resulting in security bugs such as CVE-2012-2459.


### Consensus Rule Changes
{% include helpers/subhead-links.md %}


TODO: Document changes in consensus rules


#### Detecting Forks


TODO: Document fork detection