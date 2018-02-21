---
title: "Why bitcoin transactions are not anonymous?"
isdate: false

---


Each bitcoin transaction is recorded into the blockchain, which means that anyone can trace each transaction's address until the point to see the same address being sending or receiving bitcoins more than once. Is this bad? Yeah!, would you like that someone trace your transactions or even calculate your balance?, of course not, nobody wants that. The people want to keep their privacy over their money.

So!, why people think that bitcoin is anonymous? Short answer, thanks to marketing. Actually bitcoin is pseudo-anonymous which mean that a person identity can be associated with a bitcoin address, if they are neglected.

        pseudo-anonymous = address

If somehow your bitcoin address is associated with your real identity, every possible transaction will be linked to you. By example:

Brad has a webpage, where he offer some services about community manager with its prices in bitcoin and he has his bitcoin address public at his site, then, Carlos try to find how many transactions Brad has in the blockchain, that way Carlos can find Brad's balance easily. Now Brad is 100% vulnerable, that allows Carlos to any kind of attack to stole Brad's bitcoins.

![why bitcoin transactions are not anonymous?](/user-guides/bitcoin/why-bitcoin-transactions-are-not-anonymous.png)

Satoshi's original whitepaper, recommend to use new bitcoin address for every transaction to keep privacy and stop from being associated to a common owner.  This technique makes harder to trace an owner identity, because if every transaction an owner receive goes to a different address, bitcoins are spread out amongst multiple addresses instead being stored all within a single address.

Applying this technique by example, an owner **A** can send transactions that has multiples addresses as inputs, once that transaction is recorded at the blockchain, it can indicate, but not prove that those inputs addresses were belongs to owner **A**. Unless that owner **A** had associated some transactions to her or his name.

![why bitcoin transactions are not anonymous?.multiple addresses](/user-guides/bitcoin/why-bitcoin-transactions-are-not-anonymous-multiple-addresses.png)

Even so, your identity is vulnerable, but How? When a transaction is created, a bitcoin client should take **UXTOs** as inputs, right? Ok, if somehow an address does not has enough coins in it, client must take **UXTO** from another address, hence, inputs will has **UXTOs** with different address but, still belongs to the same wallet.

Another technique used to increment anonymity, is to have multiples bitcoin wallet, there exists a tool named multibit, that offers a way to manage multiples wallet within your desktop.

![Multi-wallet technique](/user-guides/bitcoin/Multi-wallet-technique.png)

As you notice, there exists a bunch of techniques out there or in the near future new techniques will be created to improve bitcoin privacy. But by itself bitcoin does not provide  anonymity, a bitcoin owner need to implement some techniques to keep privacy. But why this is bad? Because not all users are bitcoin researchers, they are normally persons that want to keep their money away from third-party entities, like banks.
