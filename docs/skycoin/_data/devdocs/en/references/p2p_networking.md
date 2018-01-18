{% comment %}
This file is licensed under the MIT License (MIT) available on
http://opensource.org/licenses/MIT.
{% endcomment %}
{% assign filename="_data/devdocs/en/references/p2p_networking.md" %}

## P2P Network
{% include helpers/subhead-links.md %}

{% autocrossref %}

This section describes the Skycoin P2P network protocol (but it is 
[not aspecification][]). All peer-to-peer communication occurs entirely over TCP.

**Note:** unless their description says otherwise, all multi-byte
integers mentioned in this section are transmitted in little-endian order.

{% endautocrossref %}

### Constants And Defaults
{% include helpers/subhead-links.md %}

{% autocrossref %}

The following constants and defaults are taken from Skycoin Core's
[skycoin.go at master][] and [skycoin.go at testnet][] source code files.

| Parameter | Mainnet                   | Testnet                       | Regtest 
|-----------|---------------------------|-------------------------------|----------
| Default Port       | 6000         | 16000                             | N/A
| Web Interface Port | 6420         | 16420                             | N/A
| Default Port       | 6430         | 16430                             | N/A
| Genesis Address    | 2jBbGxZRGoQG1mqhPBnXnLTxK6oxsTf8os6 | F5k1VyFHZGJgQADWpmMEW8Se2HNidFm9k3 | N/A
| Genesis Timestamp  | 1426562704   | 1505801448                        | N/A

Command line parameters can change what port a node listens on (see
`make run-help`). Start strings are hardcoded constants that appear at the start
of all messages sent on the Skycoin network; they may also appear in
data files such as Skycoin Core's block database.

Skycoin Core's source code also includes
other constants useful to programs, such as the Blockchain pubkey
for the different networks.

{% endautocrossref %}

### Protocol Versions
{% include helpers/subhead-links.md %}

{% autocrossref %}

The table below lists some notable versions of the P2P network protocol,
with the most recent versions listed first. (If you know of a protocol
version that implemented a major change but which is not listed here,
please [open an issue][docs issue].)

As of Skycoin Core 0.21.1, the most recent protocol version is `TODO`.

| Version | Initial Release                    | Major Changes
|---------|------------------------------------|--------------

{% endautocrossref %}

### Message Headers
{% include helpers/subhead-links.md %}

{% autocrossref %}

All messages in the network protocol use the same container format,
which provides a required multi-field message header and an optional payload.
The message header format is:

| Bytes | Name         | Data Type | Description
|-------|--------------|-----------|-------------
| 4     | payload size | uint32    | Number of bytes in payload.  The current maximum number of bytes ([`MaxMessageLength`][maximum message length]) allowed in the payload by the [Skycoin network][network] is 256 KiB---messages with a payload size larger than this will be dropped or rejected and sender disconnected.
| 4    | prefix        | char[4]   | ASCII string which identifies what message type is contained in the payload.  Followed by nulls (0x00) to pad out byte count; for example: `MSG\0`.

The following example is an annotated hex dump of a mainnet message
header from a `verack` message which has no payload.

{% highlight text %}
TODO : Message hex dump
{% endhighlight %}

{% endautocrossref %}

### Data Messages
{% include helpers/subhead-links.md %}

{% autocrossref %}


{% endautocrossref %}

#### Give Blocks
{% include helpers/subhead-links.md %}

{% autocrossref %}

The `GIVB` message transmits one or many serialized block in the format
described in the [serialized blocks section][section serialized blocks].
See that section for an example hexdump.  It can be sent for the following
different reasons:

- TODO: Broadcast block . See CreateAndPublishBlock -> broadcastBlock
- TODO: Response to GETB message . See GetBlocksMessage.Process
- TODO: Other reasons for sending GIVB messages

{% endautocrossref %}

#### Get Blocks
{% include helpers/subhead-links.md %}

{% autocrossref %}

The `GETB` message requests a `GIVB` message that provides block
header hashes starting from a particular point in the block chain. It
allows a peer which has been disconnected or started for the first time
to get the data it needs to request the blocks it hasn't seen.
A `GETB` message is exchanged between peers as a result of a successful
[introduction handshake][].

{% comment %}

TODO: Bitcoin's `getblocks` message allows for including header hashes. Useful for determining the starting point of the fork and sync subsequent header hashes . What about Skycoin? No data for this in message struct

{% endcomment %}

| Bytes    | Name                 | Data Type        | Description
|----------|----------------------|------------------|----------------
| 8        | last block           | uint64           | Instruct peer to send blocks with [height][block height] higher than value specified in this field.
| 8        | requested blocks     | uint64           | Expect at most this number of blocks in subsequent [GIVB message][].

The following annotated hexdump shows a `GETB` message.  (The
message header has been omitted.)

{% highlight text %}
TODO : Message hex dump
{% endhighlight %}

{% endautocrossref %}

#### Get Transactions
{% include helpers/subhead-links.md %}

{% autocrossref %}

The `GETT` message requests one or more transaction objects from another
node. The transactions are requested by TXID hash, which the requesting
node typically received previously by way of an [`ANNT` message][annt message].

The response to a `GETT` message most likely will be a `GIVT` message.

This message cannot be used to request arbitrary data, such as historic
transactions no longer in the memory pool or relay set. Full nodes may
not even be able to provide older data objects if they've pruned old
transactions from their block database. For this reason, the `GETT`
message should usually only be used to request data from a node which
previously advertised it had that data by sending an `ANNT` message.

The format and maximum size limitations of the `GETT` message are
identical to the [`ANNT` message][annt message]; only the message
header differs.

{% endautocrossref %}

#### GetHeaders
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Equivalent of GetHeaders in Skycoin?

{% endautocrossref %}

#### Headers
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Equivalent of Headers in Skycoin?

{% endautocrossref %}

#### Announce Blocks
{% include helpers/subhead-links.md %}

{% autocrossref %}

The `ANNB` message transmits the [block height][] of the [head block][]
known to the transmitting peer.  It can be sent unsolicited to
announce new blocks, or it can be sent as a follow-up of
receiving `GIVB` message so as to notify peers of
recently discovered blocks.

The receiving peer can compare [block height][] from an `ANNB` message
against the highest height value of the blocks it has already seen,
and then use a follow-up `GETB` message to request unseen objects.

| Bytes    | Name      | Data Type             | Description
|----------|-----------|-----------------------|-----------------
| 8        | max bkseq | uint64                | The highest [BkSeq][block sequence number] known to the transmitting peer

The following annotated hexdump shows an `ANNB` message with two
inventory entries.  (The message header has been omitted.)

{% highlight text %}
TODO: Message hex dump
{% endhighlight %}

{% endautocrossref %}

#### Announce Transactions
{% include helpers/subhead-links.md %}

The `ANNT` message transmits one or more [TXID hashes][/en/glossary/txid]{:#term-txid}{:.term}
of transaction objects known to the transmitting peer. It can be sent
unsolicited to announce new transactions or as a side-effect of
[receiving transactions][givt message] so as to forward recently discovered
TXIDs to another peer.
Multiple `ANNT` messages may be exchanged between peers following
a successful [introduction handshake][].

The receiving peer can compare the TXIDs from an `ANNT` message
against the unconfirmed transactions it has in its memory pool, and
then use a follow-up [GETT message][] to request unseen transactions.

| Bytes    | Name      | Data Type             | Description
|----------|-----------|-----------------------|-----------------
| *Varies* | txns      | `cipher.SHA256`       | One or more TXIDs up to a maximum of 16 entries.

The following annotated hexdump shows an `ANNT` message with two
inventory entries.  (The message header has been omitted.)

{% highlight text %}
Message hex dump
{% endhighlight %}


#### MerkleBlock
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Equivalent of MerkleBlock in Skycoin

{% endautocrossref %}

#### NotFound
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Equivalent of NotFound in Skycoin

{% endautocrossref %}

#### Give Transactions
{% include helpers/subhead-links.md %}

{% autocrossref %}

The `GIVT` message transmits some transactions in the raw transaction
format. It can be sent in a variety of situations;

* **Transaction Response:** Skycoin Core will send it in
  response to a `GETT` message that requests transactions by TXID

* **Unsolicited:** Wallet and other SPV clients may send a `GIVT`
  message unsolicited for transactions they originate.

After processing a `GIVT` message a node should notify its peers
of the new transactions discovered by broadcasting an `ANNT` message.

For an example hexdump of the raw transaction format, see the [raw
transaction section][raw transaction format].

{% endautocrossref %}


### Control Messages
{% include helpers/subhead-links.md %}

{% autocrossref %}

The following network messages all help control the connection between
two peers or allow them to advise each other about the rest of the
network.

![Overview Of P2P Protocol Control And Advisory Messages](/img/dev/en-p2p-control-messages.svg)

Note that almost none of the control messages are authenticated in any
way, meaning they can contain incorrect or intentionally harmful
information. In addition, this section does not yet cover P2P protocol
operation over the [Tor network][tor]; if you would like to contribute
information about Tor, please [open an issue][docs issue].

{% endautocrossref %}

#### Give Peers
{% include helpers/subhead-links.md %}

{% autocrossref %}

The `GIVP` message relays connection information
for peers on the network. Each peer which wants to accept incoming
connections may create a `GIVP` message providing its connection
information and then send that message to its peers unsolicited. Some
of its peers send that information to their peers (also unsolicited),
some of which further distribute it, allowing decentralized peer
discovery for any program already on the network.

If the connections cache of a node is full and this node receives
yet another [`INTR` message][intr message] then it must send back
to the originating peer a `GIVP` message with a (random)
subset of the addresses in its local connection cache before
halting the [introduction handshake][intr message].

A `GIVP` message may also be sent in response to a `GETP` message.

| Bytes      | Name             | Data Type          | Description
|------------|------------------|--------------------|----------------
| *Varies*   | IP addresses     | network IP address | IP address entries.  See the table below for the format of a Skycoin network IP address.

Each encapsulated network IP address currently uses the following structure:


| Bytes | Name       | Data Type | Description
|-------|------------|-----------|---------------
| 4     | IP address | char      | IPv4 address in **big endian byte order**.
| 2     | port       | uint16_t  | Port number in **big endian byte order**.  Note that Skycoin Core will only connect to nodes with non-standard port numbers as a last resort for finding peers.  This is to prevent anyone from trying to use the network to disrupt non-Skycoin services that run on other ports.

The following annotated hexdump shows part of an `addr` message. (The
message header has been omitted and the actual IP address has been
replaced with a [RFC5737][] reserved IP address.)

{% highlight text %}
Message hex dump
{% endhighlight %}

{% endautocrossref %}


#### Alert
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Equivalent of Alert in Skycoin

{% endautocrossref %}

#### FeeFilter
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Equivalent of FeeFilter in Skycoin

{% endautocrossref %}


#### FilterAdd
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Equivalent of FilterAdd in Skycoin

{% endautocrossref %}

#### FilterClear
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Equivalent of FilterClear in Skycoin

{% endautocrossref %}


#### FilterLoad
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Equivalent of FilterLoad in Skycoin

{% endautocrossref %}

#### Get Peers
{% include helpers/subhead-links.md %}

{% autocrossref %}

The `GETP` message requests a [`GIVP` message][givp message] from the receiving
node, preferably one with lots of IP addresses of other receiving nodes.
The transmitting node can use those IP addresses to quickly update its
database of available nodes rather than waiting for unsolicited `GIVP`
messages to arrive over time.

There is no payload in a `GETP` message.  See the
[message header section][section message header] for an example of a
message without a payload.

{% endautocrossref %}


#### Ping
{% include helpers/subhead-links.md %}

{% autocrossref %}

The `PING` message helps confirm that the receiving peer is still
connected. If a TCP/IP error is encountered when sending the `PING`
message (such as a connection timeout), the transmitting node can assume
that the receiving node is disconnected. The response to a `PING`
message is the `PONG` message.

The `PING` message has no payload.

{% endautocrossref %}

#### Pong
{% include helpers/subhead-links.md %}

{% autocrossref %}

The `PONG` message replies to a `PING` message, proving to the pinging
node that the ponging node is still alive. Skycoin Core will, by
default, disconnect from any clients which have not responded to a
`PING` message within 20 minutes.

{% comment %}
TODO: Skycoin PING timeout
{% endcomment %}

To allow nodes to keep track of latency, the `PONG` message sends back
the same nonce received in the `PING` message it is replying to.

The format of the `PONG` message is identical to the `PING` message;
only the message header differs.

{% endautocrossref %}

#### Reject
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Equivalent of Reject in Skycoin

{% endautocrossref %}

#### SendHeaders
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Equivalent of SendHeaders in Skycoin

{% endautocrossref %}

#### VerAck
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Equivalent of VerAck in Skycoin

{% endautocrossref %}


#### Introduction
{% include helpers/subhead-links.md %}

{% autocrossref %}

The `INTR` message provides information about the transmitting node
to the receiving node at the beginning of a connection. Until both peers
have exchanged `INTR` messages, no other messages will be accepted.

| Bytes    | Name                  | Data Type        | Required/Optional                        | Description
|----------|-----------------------|------------------|------------------------------------------|-------------
| 4        | mirror                 | uint32           | Required                                 | A random nonce which can help a node detect a connection to itself.  If the nonce is 0, the nonce field is ignored.  If the nonce is anything else, a node should terminate the connection on receipt of an `INTR` message with a nonce it previously sent.
| 2        | port                   | uint16           | Required                                 | The port number of the transmitting node in **big endian byte order**.
| 4        | version               | int32            | Required                                 | The highest protocol version understood by the transmitting node.  See the [protocol version section][section protocol versions]. Protocol version mismatch leads to disconnection.

Peers of a given node may establish a single connection and no more.
Once an initial introduction handshake is established every node must
halt processing of subsequent `INTR` messages matching an already known
`address:mirror` combination. The best way to keep track of these pairs
is at the discretion of every node.

Immediately after accepting an introduction handshake each participating
node should [request blocks][getb message] from its peer. It is at the
discretion of each node to [announce unconfirmed transactions][annt message]
stored locally in its memory pool at this moment as well.

TODO: `INTR` retries

The following annotated hexdump shows a `version` message. (The
message header has been omitted and the actual IP addresses have been
replaced with [RFC5737][] reserved IP addresses.)


{% endautocrossref %}


#### Final remarks about the P2P network
{% include helpers/subhead-links.md %}

{% autocrossref %}

Skycoin is a next generation blockchain ledger technology. Therefore
some of their innovatve concepts do not map one-to-one to similar
elements present in other crypto-currencies. Some clarifications and
comparisons will follow.

Skycoin [gnet][network] does not implement [inventories][/en/glossary/inventory]{:#term-inventory}{:.term}.
Hence there is no equivalent to [Bitcoin `inv` message][bitcoin inv message].
The closest match in Skycoin is [ANNT message][], but its scope is
limited to transactions. [Bitcoin `getdata` message][bitcoin getdata message]
can not be mapped one-to-one to a single Skycoin messages type but many
e.g. to [get blocks][getb message] and to [get transactions][gett message].

Skycoin transactions are exchanged immediately after an
introduction handshake has been successfully established. Hence there
is no equivalent to [Bitcoin `mempool` message][bitcoin mempool message].

{% endautocrossref %}


