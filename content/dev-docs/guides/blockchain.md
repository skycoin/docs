+++
title = "Blockchain"
weight = 2
+++

<!-- MarkdownTOC autolink="true" bracket="round" levels="1,2,3,4,5,6" -->

- [Introduction](#introduction)
- [Blockchain Overview](#blockchain-overview)
- [Block Hash](#block-hash)

<!-- /MarkdownTOC -->

### Introduction

The blockchain provides Skycoin's public ledger, an ordered and timestamped record
of transactions. This system is used to protect against double spending
and modification of previous transaction records.

Each full node in the Skycoin network independently stores a blockchain
containing only blocks validated by that node.

### Blockchain Overview

The illustration above shows a simplified version of a blockchain.
A block of one or more new transactions
is collected into the transaction data part of a block.
Copies of each transaction are hashed, and the hashes are then paired,
hashed, paired again, and hashed again until a single hash remains, the
merkle root of a merkle tree.

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

A single transaction can create multiple outputs, as would be
the case when sending to multiple addresses, but each output of
a particular transaction can only be used as an input once in the
blockchain. Any subsequent reference is a forbidden double
spend---an attempt to spend the same coins twice.

Unspent outputs are identified by their SHA256 hash of the binary serialization,
encoded according to the
[Skycoin Binary Encoding Format](https://github.com/skycoin/skycoin/wiki/Skycoin-Binary-Encoding-Format).
An unspent output contains the SHA256 hash of the transaction that created it,
an address that owns the output, an amount of Skycoin and an amount of Coin Hours.
The amount of Skycoin must not be 0.

Because each output of a particular transaction can only be spent once,
the outputs of all transactions included in the blockchain can be categorized as either
Unspent Transaction Outputs (UTXOs)] or Spent Transaction Outputs. For a
payment to be valid, it must use only UTXOs as inputs.

If the coins or coin hours of a
transaction's outputs exceed its inputs, the transaction will be
rejected---but if the inputs' coin hours exceed the value of the outputs, any
difference in value is considered as a transaction fee, often called a coin hour burn.
Transaction fees are used to prioritize transactions for placement in a block.

Input coins must always equal output coins; the total number of coins in the unspent
output set never changes.

### Block Hash

Every block must include one or more transactions.

The binary serialization of a transaction is hashed to create the
transaction outer hash identifier (`txid`).
From these txids, the merkle tree is constructed by pairing each
txid with one other txid and then hashing them together. If there are
an odd number of txids, the txid without a partner is hashed with a
copy of itself.

The resulting hashes themselves are each paired with one other hash and
hashed together. Any hash without a partner is hashed with itself. The
process repeats until only one hash remains, the merkle root.

For example, if transactions were merely joined (not hashed), a
five-transaction merkle tree would look like the following text diagram:

```
       ABCDEEEE .......Merkle root
      /        \
   ABCD        EEEE
  /    \      /
 AB    CD    EE .......E is paired with itself
/  \  /  \  /
A  B  C  D  E .........Transactions
```
