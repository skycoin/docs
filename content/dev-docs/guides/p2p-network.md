+++
title = "P2P Network"
weight = 3
+++

<!-- MarkdownTOC autolink="true" bracket="round" levels="1,2,3,4,5,6" -->

- [Introduction](#introduction)
- [Peer Discovery](#peer-discovery)
- [Connecting To Peers](#connecting-to-peers)
- [Disconnecting](#disconnecting)
- [Blockchain sync and block propagation](#blockchain-sync-and-block-propagation)
- [Transaction propagation](#transaction-propagation)

<!-- /MarkdownTOC -->

### Introduction

The Skycoin network protocol allows full nodes
(peers) to collaboratively maintain a peer-to-peer network for block and
transaction exchange. Full nodes download and verify every block and transaction
prior to relaying them to other nodes. Archival nodes are full nodes which
store the entire blockchain and can serve historical blocks to other nodes.

### Peer Discovery

Every client has a preset list of known public peers that are operated by Skycoin.
The client will maintain one and only one connection to a peer from this list.
This bootstraps the client to the network when connecting for the first time.

Additionally, some clients will download a list of known peers from a remote URL,
https://downloads.skycoin.net/blockchain/peers.txt. The IP addresses in this list
will seed the client's initial peers list.

Any peers already known to the client from previous operation will also be included
in their peer list.

Once a program has connected to the network
its peers can begin to send it
[`GIVP` messages](https://github.com/skycoin/skycoin/wiki/Wire-Protocol#give-peers)
with the IP addresses and port numbers of
other peers on the network.
The client will record these peers to an internal pool which is saved to a file
`peers.txt` in their
[data directory](https://github.com/skycoin/skycoin/wiki/Data-directory-and-wallet-folder-locations).
The peers in the pool will be connected to at random until the client reaches its
max outgoing connections (default 8).

Peers often leave the network or change IP addresses, so
programs may need to make several different connection attempts at
startup before a successful connection is made. This can add a
delay to the amount of time it takes to connect to the
network, forcing a user to wait before sending a transaction or checking
the status of payment.

### Connecting To Peers

Connecting to a peer is done by sending an
[`INTR` message](https://github.com/skycoin/skycoin/wiki/Wire-Protocol#introduction), which
contains your protocol version number, blockchain public key and user agent.
The remote node responds with its own `INTR` message. No further
acknowledgement message is sent to the other node to indicate the
connection has been established.

Failure to meet the **exact** protocol version and blockchain public key will lead to
disconnection.

Once connected, the client can send
[`GETP`](https://github.com/skycoin/skycoin/wiki/Wire-Protocol#get-peers)
messages to gather additional peers.

### Disconnecting

Upon normal disconnection, a `DISC` message is sent, which includes a reason code.
The `DISC` message is not guaranteed to be received for every disconnection, it is
only a courtesy for debugging.

### Blockchain sync and block propagation

Peers send `GETB` messages to each other. This message specifies their last known block,
and a number of blocks they want sent. If the receiving peer knows blocks beyond the
reported last known block, they send a `GIVB` message,
which contains sequence of blocks starting from the last block plus one.
The sequence will have at least one block and not more than the number of blocks requested.

Peers keep note of the last known block reported to each other, and use this value to estimate
the true blockchain height for measuring sync progress.

Upon receipt of a `GIVB` message, the client will validate and adds these blocks to the blockchain,
then send another `GETB` message for more blocks. They also send an `ANNB` message to
notify their peers that they have new blocks.

Blocks received out of order cannot be executed and are discarded.

### Transaction propagation

When a client injects a new unconfirmed
transaction to the network, they announce it to all of their peers with an
`ANNT` message. The peers will reply with a `GETT` message if they do not have
this transaction in their unconfirmed pool. The receiver of a `GETT` message
will reply with a `GIVT` message, containing the transaction. Upon receipt of
a `GIVT` message, the client will verify the transaction before adding it to
its unconfirmed transaction pool.
Transactions that are "hard-invalid" are rejected completely
and not injected into the pool. Transactions that are "soft-invalid" are injected
but marked as invalid. Valid transactions are injected and an `ANNT` message is
broadcast.

The unconfirmed transaction pool periodically checks the validity of unconfirmed transactions.
If any unconfirmed transaction transitions from invalid to valid, an `ANNT` message is
broadcast.

When a block is appended to the blockchain, its transactions are removed from the unconfirmed
transaction pool.

When a client starts, it announces all of its valid unconfirmed transactions to its peers.
Its possible to create and broadcast a transaction, but have no peer receive it. Then, this
transaction will apparently not confirm. If the user restarts their client, the transaction
will rebroadcast, and hopefully it will be received by a peer. This can sometimes confuse users,
because they thought the transaction failed, and they might send a second one. Users should be aware
of this behavior.

A random sample of valid transactions from the unconfirmed pool are announced to peers
on a timer.
