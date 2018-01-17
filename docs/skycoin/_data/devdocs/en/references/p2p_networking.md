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
| 4     | payload size | uint32    | Number of bytes in payload.  The current maximum number of bytes ([`MaxMessageLength`][maximum message length]) allowed in the payload by the [Skycoin network][gnet] is 256 KiB---messages with a payload size larger than this will be dropped or rejected and sender disconnected.
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

#### Block
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### GetBlocks
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### GetData
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### GetHeaders
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### Headers
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### Inv
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### MemPool
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### MerkleBlock
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### NotFound
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### Tx
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}





### Control Messages
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### Addr
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}




#### Alert
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### FeeFilter
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}


#### FilterAdd
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### FilterClear
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}


#### FilterLoad
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### GetAddr
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}


#### Ping
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### Pong
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### Reject
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### SendHeaders
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

#### VerAck
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}


#### Version
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}
