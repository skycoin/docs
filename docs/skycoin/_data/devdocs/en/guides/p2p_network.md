{% comment %}
This file is licensed under the MIT License (MIT) available on
http://opensource.org/licenses/MIT.
{% endcomment %}
{% assign filename="_data/devdocs/en/guides/p2p_network.md" %}

## P2P Network
{% include helpers/subhead-links.md %}

{% autocrossref %}

The Skycoin network protocol allows full nodes
(peers) to collaboratively maintain a
[peer-to-peer network][network]{:#term-network}{:.term} for block and
transaction exchange. Full nodes download and verify every block and transaction
prior to relaying them to other nodes. Archival nodes are full nodes which
store the entire blockchain and can serve historical blocks to other nodes.
Pruned nodes are full nodes which do not store the entire blockchain. Many SPV 
clients also use the Skycoin network protocol to connect to full nodes.

Consensus rules do not cover networking, so Skycoin programs may use
alternative networks and protocols, such as the
[high-speed block relay network][] used by some [Bitcoin miners][miner].

To provide practical examples of the Skycoin peer-to-peer network, this
section uses Skycoin Core as a representative full node and [Skycoin web wallet][]
as a representative SPV client. Both programs are flexible, so only
default behavior is described. Also, for privacy, actual IP addresses
in the example output below have been replaced with [RFC5737][] reserved
IP addresses.

{% endautocrossref %}

### Peer Discovery
{% include helpers/subhead-links.md %}

{% autocrossref %}

When started for the first time, programs don't know the IP
addresses of any active full nodes. In order to discover some IP
addresses, they query one or more IP names (called [network seeds][/en/glossary/network-seed]{:#term-network-seed}{:.term})
hardcoded into Skycoin Core and SPV clients. There is no lookup of any
[DNS A records][] to determine the IP addresses of full nodes that may accept new
incoming connections.

The network seeds are maintained by Skycoin community members
Nodes are added to the seed if they run on the default Skycoin ports of
`6000` for mainnet or `16000` for testnet. Since the beginning these default
connections are considered to be established to trusted peers.

<!-- paragraph below based on Greg Maxwell's email in
     http://comments.gmane.org/gmane.comp.bitcoin.devel/5378 -->

DNS is not used for seed results since they would not be authenticated, which
would allow for a malicious seed operator or
network man-in-the-middle attacker to return only IP addresses of
nodes controlled by the attacker, isolating a program on the attacker's
own network and allowing the attacker to feed it bogus transactions and
blocks.

Beyond this first step for discovering peers, Skycoin also looks for a peers
database stored in the local file system. Next , Skycoin retrieves
from the Internet a community-maintained list of
[well known public peers][] .

Once a program has connected to the [gnet network][network],
its peers can begin to send it [`GIVP` messages][givp messages]
(give peers<!--noref-->) messages with the IP addresses and port numbers of
other peers on the network, providing a fully decentralized method of
peer discovery. Skycoin Core keeps a record of known peers in a
persistent on-disk database which usually allows it to connect directly
to those peers on subsequent startups without having to use network seeds.

However, peers often leave the network or change IP addresses, so
programs may need to make several different connection attempts at
startup before a successful connection is made. This can add a
significant delay to the amount of time it takes to connect to the
network, forcing a user to wait before sending a transaction or checking
the status of payment.

{% comment %}

TODO: Look for equivalents of Bitcoin's 11 seconds rule in Skycoin Core
<!-- reference for "Bitcoin Core...11 seconds" below:
     https://github.com/bitcoin/bitcoin/pull/4559 -->

{% endcomment %}

<!-- reference for Skycoin Core behavior described below: search for
"DefaultConnections" in cmd/skycoin/skycoin.go; Skycoin has IPv4 seeds
in its configuration -->

Skycoin Core also includes a hardcoded list of IP
addresses and port numbers to a few nodes which were active
around the time that particular version of the software was first
released. Skycoin Core will start attempting to connect to these nodes
if none of the cached seed servers have responded to a query within
60 seconds, providing an automatic fallback option.

As a manual fallback option, Bitcoin Core also provides several
command-line connection options.  See the `-help` text for
details.  Other Skycoin client software should be programmed to do
the same thing.

{% endautocrossref %}

### Connecting To Peers
{% include helpers/subhead-links.md %}

{% autocrossref %}

Connecting to a peer is done by sending an
[`INTR` message][intr messages], which
contains your version number to the remote
node. The remote node responds with its own `INTR` message. No further
acknowledgement message is sent to the other node to indicate the
connection has been established.

Failure to meet the **exact** protocol version will lead to
disconnection.

Once connected, the client can send to the remote node [`GETP`][getp messages]
and [`GIVP`][givp messages] messages to gather additional peers.

In order to maintain a connection with a peer, nodes by default will
send a message to peers before 30 minutes of inactivity.
If 90 minutes pass without a message being received by a peer,
the client will assume that connection has closed.

{% endautocrossref %}

### Initial Block Download
{% include helpers/subhead-links.md %}

{% autocrossref %}

Before a full node can validate unconfirmed transactions and
recent blocks, it must download and validate all blocks from
block 1 (the block after the hardcoded genesis block) to the current tip
of the best block chain. This is the Initial Block Download (IBD) or
initial sync.

Although the word "initial" implies this method is only used once, it
can also be used any time a large number of blocks need to be
downloaded, such as when a previously-caught-up node has been offline
for a long time. In this case, a node can use the IBD method to download
all the blocks which were produced since the last time it was online.

{% endautocrossref %}

#### Blocks-First
{% include helpers/subhead-links.md %}

{% autocrossref %}

Skycoin Core uses a
simple initial block download (IBD) method we'll call *blocks-first*.
The goal is to download the blocks from the best block chain in sequence.

![Overview Of Blocks-First Method](/img/dev/en-blocks-first-flowchart.svg)

The first time a node is started, it only has a single block in its
local best block chain---the hardcoded genesis block (block 0).  When this
node chooses a remote peer, called the sync node, both nodes should 
automatically exchange `GETB` messages.

![First GETB Message Sent During IBD](/img/dev/en-ibd-getb.svg)

Starting node includes the local block height (i.e. `0`) in the
message it sends to its peer sync node.

Upon receipt of the `GETB` message, the sync node matches
message block height agains its local block chain.
Given the fact that nodes with signed blocks will have positive
block heights, quite likely the sync node will reply with
one or more `GIVB` messages including blockchain data starting
from block 1. The number of messages depends on the length of
the best block chain stored by peers as well as the buffering
capacity of nodes.

![First GIVB Message Sent During IBD](/img/dev/en-ibd-givb.svg)

It's important to blocks-first nodes that the blocks be requested and
sent in order because the whole synchronization process relies on block
heights (rather than IDs) and each block header references the header hash of
the preceding block. That means the IBD node can't fully validate a
block until its parent block has been received. Blocks that can't be
validated because their parents haven't been received are called orphan
blocks; a subsection below describes them in more detail.

The IBD node downloads and validates each block received in `GIVB`
messages, thus maintaining a local queue of blocks to download.
Immediately after this the node broadcasts an `ANNB` message so as to
announce the availability of new blocks to the rest of its peers.
Upon receipt of this message, peers will follow a similar process
and compare announced block height with its local height. Once
they detect they are behind the longest block chain subsequent
`GETB` messages will be sent back. The repetition of this workflow
ensures message propagation across the [gnet network][network].

![First ANNB Message Sent During IBD](/img/dev/en-ibd-annb.svg)

Following block validation and immediately after broadcasting
`ANNB` message to its peers the node also broadcasts a second
`GETB` message, now containing its updated block height.

{% comment %}
TODO: At this point forks might become evident, include in docs
{% endcomment %}

![Second GETB Message Sent During IBD](/img/dev/en-ibd-getb2.svg)

If one peer has a longer block chain it will reply with another `GIVB`
message. The repetition of this workflow ensures that the IDB
node will extend its local block chain until it eventually
reaches the longest path shared by its peers.

![Second GIVB Message Sent During IBD](/img/dev/en-ibd-givb2.svg)

Message propagation across the [gnet network][network] continues
while IBD node validates subsequent blocks and continues sending
`ANNB` messages to its peers.

![Second ANNB Message Sent During IBD](/img/dev/en-ibd-annb2.svg)

The cycle will repeat until the IBD node is synced to
the tip of the longest block chain. At that point, the node
will accept blocks sent through the regular block broadcasting described
in a later subsection.

{% endautocrossref %}

##### Blocks-First Advantages & Disadvantages
{:.no_toc}
{% include helpers/subhead-links.md %}

{% autocrossref %}

The primary advantage of blocks-first IBD is its simplicity.
It also has disadvantages with several implications:

* **Speed Limits:** All requests are eventually handled by the master node,
  so if a sync node has limited upload bandwidth, the IBD node will have
  slow download speeds.  This is partially mitgated by the fact that IBD
  node broadcasts `ANNB` and `GETB` messages, so fastest peers have a chance
  to jump in to make the process even faster. Nonetheless this happens at
  the cost of repeated reception of blocks stored by multiple peers that
  synchronized their block chains prior to the IBD.

{% comment %}
* **Download Restarts:** The sync node can send a non-best (but
  otherwise valid) block chain to the IBD node. The IBD node won't be
  able to identify it as non-best until the initial block download nears
  completion, forcing the IBD node to restart its block chain download
  over again from a different node. Bitcoin Core ships with several
  block chain checkpoints at various block heights selected by
  developers to help an IBD node detect that it is being fed an
  alternative block chain history---allowing the IBD node to restart
  its download earlier in the process.

* **Disk Fill Attacks:** Closely related to the download restarts, if
  the sync node sends a non-best (but otherwise valid) block chain, the
  chain will be stored on disk, wasting space and possibly filling up
  the disk drive with useless data.
{% endcomment %}

* **High Memory Use:** Whether maliciously or by accident, blocks sent by
  the sync node can arrive in out of order, creating orphan blocks which
  can't be validated until their parents have been received and validated.
  Orphan blocks are stored in memory while they await validation,
  which may lead to high memory use.

Even if all of these problems could be addressed in part or in full by a
headers-first IBD method, this is not supported by Skycoin [gnet][network].

**Resources:** The table below summarizes the messages mentioned
throughout this subsection. The links in the message field will take you
to the reference page for that message.

| **Message** | [`ANNB`][annb message] | [`GETB`][getb message]  | [`GIVB`][givb message]
| **From→To** | IBD→Peers              | IBD→Sync                | Sync→IBD
| **Payload** | Local block height     | Local block height and local block cache size   | An array of serialized blocks

{% endautocrossref %}

### Block Broadcasting
{% include helpers/subhead-links.md %}

{% autocrossref %}

When a node discovers a new block, it broadcasts the new block to its
peers using one of the following methods:

* **[Unsolicited Block Push][]{:#term-unsolicited-block-push}{:.term}:**
  the node sends to each of its full node peers a `GIVP` message with
  the new block. The miner can reasonably bypass the standard relay
  method in this way because it knows none of its peers already have the
  just-discovered block.

* **[Standard Block Relay][]{:#term-standard-block-relay}{:.term}:**
  the node, acting as a standard relay node, sends an `ANNB` message to
  each of its peers (both full node and SPV) with the updated block height
  of its local blockchain after discovering the new block. The most
  common response is a `GETB` message from peers with a shorter blockchain.
  The node replies to each request accordingly by sending the block(s)
  in a `GIVB` message.

**Note:**: Since Skycoin does not implement block header messages it
does not support neither sending headers only during standard block relay
nor [direct headers announcement][] method.

**Note:**: Since Skycoin does not implement Merkle tree messages it
does not provide SPV clients with Merkle block and transactions during
standard block relay.

By default, master nodes use unsolicited block push every time a new
block is discovered. At all other times Skycoin Core broadcasts blocks using
standard block relay for all peers. Skycoin Core
will accept blocks sent using any of the methods described above.

Full nodes validate received blocks. On success they advertise it to their
peers using the standard block relay method described above.

{% comment %}
TODO: Table : messages for block broadcasting
{% endcomment %}

{% endautocrossref %}

#### Orphan Blocks
{% include helpers/subhead-links.md %}

{% autocrossref %}

Blocks-first nodes may download orphan blocks---blocks whose previous
block header hash field refers to a block header this node
hasn't seen yet. In other words, orphan blocks have no known parent
(unlike stale blocks, which have known parents but which aren't part of
the best block chain).

![Difference Between Orphan And Stale Blocks](/img/dev/en-orphan-stale-definition.svg)

When a blocks-first node downloads an orphan block, it will silently
reject it. Blocks are processed in sequence.
This is particularly true when a *slow* node is a few blocks behind
the master at the moment the later discovers a new block. The master will
broadcast an unsolicited [`GIVB` message][givb message] and this slow
node will discard it because its header’s `PrevBlockHash` 
will not match the hash ID of the block at the tip of the chain.
Orphan blocks discarded this way will be retrasmitted and eventually
synchronized at a later time by following [standard block relay][]
given the fact that local block length for the node synchronizing with
the block chain will be smaller than the sequence number of the
orphan block.

{% endautocrossref %}

### Transaction Broadcasting
{% include helpers/subhead-links.md %}

{% autocrossref %}

Transaction broadcasting starts since the very same moment a successful
introduction handshake is established.  At that time nodes at both sides
of the connection gather TXID's of all valid unconfirmed transactions
in their respective memory pool and split the whole set in groups.
Transactons are announced by packaging each group in
[`ANNT` messages][annt message] which will be boadcast to the peers
of both nodes.

{% comment %}
TODO: Broadcasting vs direct message
{% endcomment %}

Each network node should reply to an [`ANNT` message][annt message]
with a [`GETT` message][gett message] including the TXID hashes of the
transactions which are neither found in the node's memory pool nor
previously confirmed. The peer receiving the `GETT` message should reply
with a [`GIVT` message][givt message] including the signatures, inputs,
outputs and all other data related to the TXID hashes included in
previous `GETT` message as long as they are still unconfimed in the
node's memory pool.

During the transaction broadcasting process invalid transactions
are filtered out.

{% endautocrossref %}

#### Memory Pool
{% include helpers/subhead-links.md %}

{% autocrossref %}

Full peers may keep track of unconfirmed transactions which are eligible to
be included in the next block. This is essential for master nodes actually
discovering new blocks including some or all of those transactions,
but it's also useful for any peer who wants to keep track 
of unconfirmed transactions, such as peers serving unconfirmed transaction 
information to SPV clients.

Because unconfirmed transactions have no permanent status in Skycoin,
Skycoin Core stores them in non-persistent memory, calling them a memory
pool or mempool. When a peer shuts down, its memory pool is lost except
for any transactions stored by its wallet. This means that
unconfirmed transactions tend to slowly disappear from the network as
peers restart or as they purge some transactions to make room in memory
for others.

As each new block is added, any transactions it confirms are removed
from the memory pool.

{% comment %}
TODO: Come back to this when we have consensus

Transactions included in signed blocks that later become stale blocks may be
added back into the memory pool. These re-added transactions may be
re-removed from the pool almost immediately if the replacement blocks
include them. This is the case in Bitcoin Core, which removes stale
blocks from the chain one by one, starting with the tip (highest block).
As each block is removed, its transactions are added back to the memory
pool. After all of the stale blocks are removed, the replacement
blocks are added to the chain one by one, ending with the new tip. As
{% endcomment %}

SPV clients don't have a memory pool for the same reason they don't
relay transactions. They can't independently verify that a transaction
hasn't yet been included in a block and that it only spends UTXOs, so
they can't know which transactions are eligible to be included in the
next block.

{% endautocrossref %}

### Misbehaving Nodes
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Finish

{% endautocrossref %}

### Final remarks
{% include helpers/subhead-links.md %}

{% autocrossref %}

Skycoin Core does not implement an alerts system.

{% endautocrossref %}

