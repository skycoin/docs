# How Bitcoin transaction works?

`Party A wants to buy an asset and party B, only accepts bitcoins.`

In a common bitcoin transaction, everyone that wants to participate need to have a bitcoin wallet. Could be a personal or online wallet. Each bitcoin wallet is a file that provide access to a list of public and private keys. Both keys are hexadecial sequence of numbers, as follow:

![private public key](private-public-key.png)


You may ask, why do i need both keys?. Because, bitcoin uses asymetric cryptography to protect bitcoin’s owners.  The private key should not be shared with anyone, with that key someone could steal your bitcoins (keep it save), hence, public key should be shared or sended to other bitcoin’s owner that wants to send you bitcoins for any service or asset.

Each bitcoin address has its own balance, but the balance is not mixed together as they do in physical wallets,  instead, they are distinct amounts exactly as they arrived.  They are named as “unspent transaction outputs” or UTXO. By example:

If **A** received 0.1 BTC, 1 BTC, 0.002 BTC consecutively, in the total balance will show 1.102 BTC, but within the bitcoin's blockchain will stay separated. As follow.

![balance](balance.png)

Once party **A** and **B**, both have bitcoin wallets, a transaction could be achieved, following this steps:


### Step one, Both parties have to get a deal.

Before going straightforward to bitcoin transaction, both parties (**A** and **B**) should meet as it should happen in the real world when someone try to buy something with dolar, euro or other currency. They must stablish where they can talk, how the transaction could be done effectivaly.


### Step two, send public address.

After a deal is done, **B** send to **A**  it’s bitcoin address, why?. Well, bitcoin address is used by the bitcoin’s blockchain to record how much bitcoins **A** or **B** receive or send.


### Step three, submitting payment.

Once buyer **A** have received the address, it’s bitcoin client shall create a transaction request and signed off with **A**'s private key, a bitcoin transaction has the following form:

![bitcoin data structure](bitcoin-data-structure.jpg)

But, you may be asking, what a bitcoin transaction is?, what are all those fields above? and how bitcoin client calculate how much bitcoins should be sended?. The bitcoin transaction is a signed piece of data that if is valid will ends up within a blockchain’s block with the only purpose of transfer ownership(bitcoins) from one owner to another, the fields showed before, are necesary to create a valid form of transaction and the output calculation is performed by bitcoin client using one of the following strategies to satisfy the purchase amount: combining several smaller units, finding exact change, or using a single unit larger than the transaction value.

Transaction inputs are choosen by bitcoin client using the strategies already mentioned to consume and create transactions outputs. However, this transactions inputs are UTXO that a bitcoin client download when its balance is syncronized with the bitcoin network. Also each input has an unlocking script that only the owner knows to satisfy the conditions for spending the UTXO.

Transaction outputs consist in two parts, the amount of bitcoins to send to another owner and the change that will go back to bitcoin's sender, each output contains a locking script that of course lock this amount by specifying the conditions that must be met to spend the output, and  only the bitcoin’s owner knows those conditions, hence, those bitcoins can be spent by him.

By example:

**A** wants to purchase an asset that cost 3 BTC to **B** and only have 5 BTC as UTXO that already received before. This new transaction will have an UTXO of 5 BTC to consume as input and will produce two outputs, one of 3 BTC and the other of 2 BTC. The first output of 3 BTC has a locking script that only **B** has, that allows him to unlock those bitcoins, the second output of 2 BTC has a locking script as well, but, as this is the **A**'s change and only he knows the conditions to unlock those bitcoins.

![how bitcoin transaction work?](how-bitcoin-transaction-work.jpg)

Once transaction is created, can be broadcasted to bitcoin’s network, to an unconfirmed transaction pool, where it must wait until a bitcoin node or miner will take it to add it to a block.


### Step four, Transaction Verification.

The bitcoin network is conformed of nodes or miners, each of them has a copy of the blockchain encrypted in its file system. Miners will create a new block and add as much transaction as they can within 10 minutes, without exceeding the block's limit size (1 megabyte), but before a transaction is added to the block, it should be verifyed first, this is know as PoW(proof-of-work). This is a race between a lot of miners to fullfil a block, once a block's limit size is reached, the miner will broadcast it to anothers miners on the bitcoin network, waiting for block's confirmation. If the block is accepted by other miners, then, a new race should be started, otherwise, last race is restarted.

Why people are purchasing miners? Because they think that miners will give them a lot of bitcoins, but is that truth? well, yeah. Each miner get bitcoins as follow.

Each a transaction is verified and added to a block, a miner gets a transaction fees(bitcoins). That's a way to incentivate miners to work. But remenber, the larger the fee's rate, the greater the priority of validating the transaction, the miner always want to win as much fee as it can, looking for the highest fees transactions within the unconfirmed transaction pool.

Each time a block is created and confirmed by others miners, the block's creator(a miner), will get a reward.

![how bitcoin miners works?](how-bitcoin-miners-works.jpg)

As you may notice, miners act as supervisors and workers, each moment a new block is created and broadcasted to the bitcoin network, miners that didn't create the block shall verify it and if it is valid, add it to it's local blockchain and broadcast it again, otherwise, the block will be discarded.

Every time a block is added to the decentralised blockchain, PoW difficulty increase, making the process to resolve it computationally expensive, needing expensive and powerfull computers to resolve the PoW.

![how bitcoin miners works?-2](how-bitcoin-miners-works-2.jpg)


### Step Five, Transaction done.

**A** and **B** both have to wait until transaction is confirmed, once done, transaction cannot be changed or canceled, **B** now have more bitcoins than before and **A** has it's new asset, then, they can repeate the same steps already expleined to keep making transactions with others bitcoin’s owners.

![How bitcoin transaction work?-2](How-bitcoin-transaction-work-2.png)