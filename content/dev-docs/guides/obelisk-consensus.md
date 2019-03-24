+++
title = "Obelisk Consensus"
weight = 8
+++

<!-- MarkdownTOC autolink="true" bracket="round" levels="1,2,3,4,5,6" -->

- [Introduction](#introduction)
- [Whitepapers](#whitepapers)
- [Reading Material](#reading-material)
- [Design Decisions](#design-decisions)
	- [*Design decision #1*: Performant consensus algorithm](#design-decision-1-performant-consensus-algorithm)
	- [*Design decision #2*: Survive intelligent attacks](#design-decision-2-survive-intelligent-attacks)
	- [*Design decision #3*: Impose low-barries to join the network](#design-decision-3-impose-low-barries-to-join-the-network)
	- [*Design decision #4*: Resilience to centralization](#design-decision-4-resilience-to-centralization)
	- [*Design Decision #5*: Keep complexity and logic outside of blockchains](#design-decision-5-keep-complexity-and-logic-outside-of-blockchains)
	- [*Design decision #6*: Nodes are intelligent.](#design-decision-6-nodes-are-intelligent)
	- [*Design decision #7*: Nodes are skeptical.](#design-decision-7-nodes-are-skeptical)
	- [*Design decision #8*: Nodes are sovereign.](#design-decision-8-nodes-are-sovereign)
	- [*Design decision #9*: Nodes are content generators.](#design-decision-9-nodes-are-content-generators)

<!-- /MarkdownTOC -->

### Introduction

Obelisk is a new consensus algorithm designed for Skycoin.

### Whitepapers

See [Obelisk Consensus Whitepapers](https://www.skycoin.net/whitepapers) for
whitepapers that describe the Obelisk consensus algorithm.

### Reading Material

See [Obelisk Consensus Blog Posts](https://www.skycoin.net/blog/tags/consensus/)

### Design Decisions

After thoughtful research of the state of the art in cryptocurrency technologies
and analysis of results of simulations, the underlying principles of Skycoin
are based on the following pilars.

#### *Design decision #1*: Performant consensus algorithm

The objective of the Skycoin is to run an optimal set of rules for each node
to follow during consensus trials, so that the final agreement between nodes
can be reached fast, and would require minimal network traffic.

#### *Design decision #2*: Survive intelligent attacks

The network should be operational even after a large-scale coordinated attack
by a well-organized network of malicious nodes.

#### *Design decision #3*: Impose low-barries to join the network

The algorithm is a scalable and computationally-inexpensive alternative to
proof of work, therefore both the consensus algorithm and block-making can
run on a budget hardware that have low price and low energy consumption.

#### *Design decision #4*: Resilience to centralization

Satoshi originally intended the Bitcoin network to be decentralized, over
hundreds of thousands of computers. Today, the Bitcoin network is completely
controlled by three mining pools. Bitcoin is no longer decentralized. Skycoin's
consensus algorithm is designed to achieve true decentralization of blockchain
consensus.

#### *Design Decision #5*: Keep complexity and logic outside of blockchains

Many blockchains implement both the control logic and the data storage plane at
the blockchain level. We believe that not using blockchains for
data storage is necessary for scalability and keeping complex logic outside of
blockchains is important for both security and scalability. Nodes on the
network should not be required to compute complex untrusted programs just to
stay synced with the network. Further, it’s hard to introduce new features to
blockchains after they’ve been deployed and gained real-world usage.

#### *Design decision #6*: Nodes are intelligent.

Each node is able to form its own independent opinion (e.g. best next block) by
doing a robust statistical analysis of the opinions it received.

#### *Design decision #7*: Nodes are skeptical.

Each node always performs authorship verification and fraud detection.

#### *Design decision #8*: Nodes are sovereign.

While other node’s opinions are taken into account, the node neither align itself
with any group or authority, nor it seeks a payment in return for supporting a
given opinion.

#### *Design decision #9*: Nodes are content generators.

The node is able to receive raw data (e.g. low-level, elementary events such as
transactions) and produce an independent research that leads to a new opinion
(e.g. block hash).
