
# Hardware Wallet

## Protocol for the signing of transactions

The fundamental objective of the development of the Hardware Wallet is the safe maintenance of the vital data of a wallet, such as the seed. Due to what is necessary for the signing of transactions, the implementation of a protocol that facilitates the signing of transactions internally in the Hardware Wallet is required.

In broad strokes, and after a series of steps the protocol provides the following result:

![long-transactions-intro](/_data/img/long-transaction-intro.png)

The signing process consists of three fundamental steps, wich are:

- Initialization
- Calculating inner hash of transaction
- Calculating signatures for all inputs

Each step is based on a cycle of sending and receiving groups of Inputs and Outputs, with at most 7 elements.