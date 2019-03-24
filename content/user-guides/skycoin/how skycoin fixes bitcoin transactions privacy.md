+++
title = "How skycoin fixes bitcoin transactions privacy?"
+++

As you may know, Bitcoin transactions are not totally anonymous, actually are pseudo-anonymous, users should implement techniques aside to improve their transaction privacy to avoid some else to trace, associate their public addresses to their identity or even stole their coins, you may say ok that's not a big deal because exists techniques that improve privacy, but there's an issue there, why? well, not all bitcoin's users know or research about bitcoins, some of them are just normal persons that hear about the cryptocurrency and want to participate, because they think that this new technology shall allow them to raise money anonymously without paying high fees to third-party, hence, those users can not implement any technique for their ignorance. Only dedicated researchers or developer can and will try to implement those techniques or even invent ones.

Skycoin exists for several reasons, two of them are, to allow users with non-technical knowledge to use the cryptocurrency without complicated tools or implementations, meaning that is for everyone and the other reason is to solve and improve bitcoin issues. One of those problems are the privacy, How privacy is enhanced? Skycoin use native support for Gmaxwell CoinJoin, right now you may be asking, What is CoinJoin?.

First of all, CoinJoin is a protocol that mixed multiples transactions in a single transaction called CoinJoin transaction,

![capitalize-btc](/user-guides/skycoin/capitalize-btc.png)

then send it to "unspent transaction pool". But, how it is created a CoinJoin transaction? and How this communication protocol works?, easy, first a CoinJoin server must exists to receive multiples transactions from Skycoin clients, then, the server shall add randomly those transactions into CoinJoin transaction, likewise, the server will send that transaction to skycoin clients, they'll sign that transaction and send it back to CoinJoin server and server shall mixed up those signatures into a valid transaction, after that process the CoinJoin server shall send that transaction onto the skycoin network. If transaction fails, you just need to try again until succeeds.

![coinjoin-is-correct-capitalization](/user-guides/skycoin/coinjoin-is-correct-capitalization.png)

Easy right?, but that's not all, Skycoin client will try to maximize privacy splitting up coins into multiples transactions that points to different addresses of the same wallet that will receive the coins(addresses should never be the same) and then send them to CoinJoin server to add them to different CoinJoin transactions that will be sent to "unspent transaction pool". By example:

Maria has the following balance [1, 3, 5, 7, 11, 17] and wants to send 12 skycoin to David, Maria query a list of unused address for user David, now Maria create two transactions, one of 5 skycoins for addr1 and the other of 7 skycoins for addr2 both belong to David's wallet, then those transactions are sent to CoinJoin server, the server will add those transactions into separate CoinJoin transactions, server will send those transactions back to Maria, she'll sign them and then sent back to server, lastly the server will send those CoinJoin transactions to "unspent transaction pool", when those transactions are done, David will have 12 skycoins more within his balance.

Afterwards this deeper explanation about CoinJoin, you may be asking yourself, Why transaction privacy is improved?, ok let me enumerate you some key points that highlight privacy on transactions:

![coinjoin-hardening.png](/user-guides/skycoin/coinjoin-hardening.png)

By example. Let's suppose that Veronica wants to check how many Skycoins Maria just sent to David, looking at blockchain record, she'll see a transaction with multiples inputs and outputs, each input came from different hash references that points to UXTOs with different addresses and each output will go to a different addresses, not matter how many transactions Veronica will check, she'll see the same pattern and she cannot associate Maria’s public address with her identity, hence, Veronica cannot know if Maria did really make a transaction to David or even if she really have a Skycoin wallet.

Now another question came out to light, Why CoinJoin it is a native protocol? Skycoin's team main goal is to create a coin that everyone can use no matter if a person is a software developer or journalist. Every user that wants to transfer their coins need a really fully anonymous transactions by default without implement any other technique to improve privacy, that's a skycoin's team task, hence, coinjoin protocol was implemented as native.
