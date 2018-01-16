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
`6000` for mainnet or `16000` for testnet. These default connections
are considered to be established to trusted peers initially.

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
[well known public peers](https://downloads.skycoin.net/blockchain/peers.txt).

{% comment TODO: No addr messages in Skycoin? %}

Once a program has connected to the gnet network, its peers can begin to send
it `addr`
(address<!--noref-->) messages with the IP addresses and port numbers of
other peers on the network, providing a fully decentralized method of
peer discovery. 

{% endcomment %}

Skycoin Core keeps a record of known peers in a
persistent on-disk database which usually allows it to connect directly
to those peers on subsequent startups without having to use network seeds.

However, peers often leave the network or change IP addresses, so
programs may need to make several different connection attempts at
startup before a successful connection is made. This can add a
significant delay to the amount of time it takes to connect to the
network, forcing a user to wait before sending a transaction or checking
the status of payment.

{% endautocrossref %}

### Connecting To Peers
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Finish

{% endautocrossref %}

### Initial Block Download
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Finish

{% endautocrossref %}

#### Blocks-First
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Finish

{% endautocrossref %}

##### Blocks-First Advantages & Disadvantages
{:.no_toc}
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Finish

{% endautocrossref %}

#### Headers-First
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Finish

{% endautocrossref %}

### Block Broadcasting
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Finish

{% endautocrossref %}

#### Orphan Blocks
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Finish

{% endautocrossref %}

### Transaction Broadcasting
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Finish

{% endautocrossref %}

#### Memory Pool
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Finish

{% endautocrossref %}

### Misbehaving Nodes
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Finish

{% endautocrossref %}

### Alerts
{% include helpers/subhead-links.md %}

{% autocrossref %}

TODO: Finish

{% endautocrossref %}

