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
| Genesis Signature  | ieb10468d10054d15f2b6f8946cd46797779aa20a7617ceb4be884189f219bc9a164e56a5b9f7bec392a804ff3740210348d73db77a37adb542a8e08d429ac92700 | 07f46ce7502147a97f2fb32c7c1e66638af851c1cb532d893f1f360bb4ab1ccf0656f2f358695e8cb752e05080af69c8f44b0d72610bd11e3fb028ecdcfed2ea01 | N/A
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


TODO: Finish

{% endautocrossref %}

### Message Headers
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

{% endautocrossref %}

### Data Messages
{% include helpers/subhead-links.md %}

{% autocrossref %}


TODO: Finish

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
