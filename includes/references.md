
{% comment %}
This file is licensed under the MIT License (MIT) available on
http://opensource.org/licenses/MIT.
{% endcomment %}

[bitcoin addr message]: https://bitcoin.org/en/developer-reference#addr "The P2P network message which relays IP addresses and port numbers of active nodes to other nodes and clients, allowing decentralized peer discovery."
[bitcoin alert message]: https://bitcoin.org/en/developer-reference#alert "The P2P network message which sends alerts in case of major software problems."
[bitcoin block message]: https://bitcoin.org/en/developer-reference#block "The P2P network message which sends a serialized block"
[bitcoin feefilter message]: https://bitcoin.org/en/developer-reference#feefilter "The P2P network message which requests the receiving peer not relay any transactions below the specified fee rate"
[bitcoin filteradd message]: https://bitcoin.org/en/developer-reference#filteradd "A P2P protocol message used to add a data element to an existing bloom filter."
[bitcoin filterclear message]: https://bitcoin.org/en/developer-reference#filterclear "A P2P protocol message used to remove an existing bloom filter."
[bitcoin filterload message]: https://bitcoin.org/en/developer-reference#filterclear "A P2P protocol message used to send a filter to a remote peer, requesting that they only send transactions which match the filter."
[bitcoin getaddr message]: https://bitcoin.org/en/developer-reference#getaddr "A P2P protool message used to request an addr message containing connection information for other nodes"
[bitcoin getblocks message]: https://bitcoin.org/en/developer-reference#getblocks "A P2P protocol message used to request an inv message containing a range of block header hashes"
[bitcoin getdata message]: https://bitcoin.org/en/developer-reference#getdata "A P2P protocol message used to request one or more transactions, blocks, or merkle blocks"
[bitcoin getheaders message]: https://bitcoin.org/en/developer-reference#getheaders "A P2P protocol message used to request a range of block headers"
[bitcoin headers message]: https://bitcoin.org/en/developer-reference#headers "A P2P protocol message containing one or more block headers"
[bitcoin inv message]: https://bitcoin.org/en/developer-reference#inv "A P2P protocol message used to send inventories of transactions and blocks known to the transmitting peer"
[bitcoin mempool message]: https://bitcoin.org/en/developer-reference#mempool "A P2P protocol message used to request one or more inv messages with currently-unconfirmed transactions"
[bitcoin merkleblock message]: https://bitcoin.org/en/developer-reference#merkleblock "A P2P protocol message used to request a filtered block useful for SPV proofs"
[bitcoin notfound message]: https://bitcoin.org/en/developer-reference#notfound "A P2P protocol message sent to indicate that the requested data was not available"
[bitcoin ping message]: https://bitcoin.org/en/developer-reference#ping "A P2P network message used to see if the remote host is still connected"
[bitcoin pong message]: https://bitcoin.org/en/developer-reference#pong "A P2P network message used to reply to a P2P network ping message"
[bitcoin reject message]: https://bitcoin.org/en/developer-reference#reject "A P2P network message used to indicate a previously-received message was rejected for some reason"
[bitcoin sendheaders message]: https://bitcoin.org/en/developer-reference#sendheaders "A P2P network message used to request new blocks be announced through headers messages rather than inv messages"
[bitcoin tx message]: https://bitcoin.org/en/developer-reference#tx "A P2P protocol message which sends a single serialized transaction"
[bitcoin verack message]: https://bitcoin.org/en/developer-reference#verack "A P2P network message sent in reply to a version message to confirm a connection has been established"
[bitcoin version message]: https://bitcoin.org/en/developer-reference#version "A P2P network message sent at the begining of a connection to allow protocol version negotiation"
[block height]: /docs/skycoin/_data/glossary/en/block-height.yaml
[block sequence number]: /content/glossary/block-sequence-number.yaml
[blocks-first]: /content/devdocs/guides/p2p_network#blocks-first
[coin hour]: /content/devdocs/guides/transactions#coin-hours
[core executable]: /en/download
[core git]: https://github.com/skycoin/skycoin
[dev communities]: /en/development#devcommunities
[distribution addresses]: /content/glossary/distribution-addresses.yaml
[dns a records]: http://tools.ietf.org/html/rfc1035#section-3.2.2
[docs issue]: https://github.com/skycoin/docs/issues
[getb message]: /content/devdocs/references/p2p_networking#get-blocks
[gett message]: /content/devdocs/references/p2p_networking#get-transactions
[getp message]: /content/devdocs/references/p2p_networking#get-peers
[givb message]: /content/devdocs/references/p2p_networking#give-blocks
[givp message]: /content/devdocs/references/p2p_networking#give-peers
[givt message]: /content/devdocs/references/p2p_networking#give-transactions
[annt message]: /content/devdocs/references/p2p_networking#announce-transactions
[annb message]: /content/devdocs/references/p2p_networking#announce-blocks
[head block]: /content/glossary/head-block.yaml
[high-speed block relay network]: https://www.mail-archive.com/bitcoin-development@lists.sourceforge.net/msg03189.html
[intr message]: /content/devdocs/references/p2p_networking#introduction
[introduction handshake]:  https://en.wikipedia.org/wiki/Handshaking "A handshake is an automated process of negotiation between two communicating participants that establishes the protocols of a communications channel, at the start of the communication, before full communication begins. It follows the physical establishment of the channel and precedes normal information transfer."
[maximum message length]: /content/glossary/maximum-message-length.yaml
[miner]: https://bitcoin.org/en/developer-guide#mining
[network]: /en/developer-guide#term-network "The Skycoin gnet P2P network which broadcasts transactions and blocks"
[not a specification]: /content/devdocs/references/intro#not-a-specification
[proof of burn]: /content/devdocs/guides/block_chain#proof-of-burn
[proof of work]: https://en.wikipedia.org/wiki/Proof-of-work_system "A proof-of-work (POW) system (or protocol, or function) is an economic measure to deter denial of service attacks and other service abuses such as spam on a network by requiring some work from the service requester, usually meaning processing time by a computer."
[rfc5737]: http://tools.ietf.org/html/rfc5737
[section creating a bloom filter]: /en/developer-examples#creating-a-bloom-filter
[section message header]: /en/developer-reference#message-headers
[section protocol versions]: /en/developer-reference#protocol-versions
[section serialized blocks]: /en/developer-reference#serialized-blocks
[skycoin web wallet]: https://github.com/skycoin/skycoin-web
[skycoin-docs mailing list]: https://www.skycoin.net/mailing-list/
[skycoin.go at master]: https://github.com/skycoin/skycoin/tree/master/cmd/skycoin
[skycoin.go at testnet]: https://github.com/skycoin/skycoin/tree/testnet/cmd/skycoin
[tor]: https://en.wikipedia.org/wiki/Tor_%28anonymity_network%29
[well known public peers]: https://downloads.skycoin.net/blockchain/peers.txt "A public list of Skycoin nodes maintained by Skycoin community members. These are not trusted initial network seed nodes"
[unsolicited block push]: /en/developer-guide#term-unsolicited-block-push "When a master node sends a GIVB message without sending an ANNB message first"
[secp256k1 signature]: https://en.bitcoin.it/wiki/Secp256k1
[direct headers announcement]: https://bitcoin.org/en/developer-guide#block-broadcasting
