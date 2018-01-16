# tradebot

Tradebot is a Go abstraction of cryptocoin trading exchanges. It abstract these four operations:
* placing a bid/ask order
* tracking the status of an existing order
* withdrawing bitcoin from the exchange
* depositing bitcoin to the exchange

Tradebot provides an internal Go API, a REST API, and a command line interface.

Currently tradebot supports the `cryptopia` and `c2cx` exchanges. Additional exchanges can be implemented in Go.

You can view [tradebot's source code](https://github.com/skycoin/exchange-api) via github.

## Terminology

briancaine note:

  so, I added this section in case we might want to clarify any terminology.

  I'm guessing we're using standard terminology but

  maybe we might need to (for technical reasons) clarify what we mean

  (ie, like, does a transaction include fees or not? do we want to clarify that somewhere?)

  if not, then we can just delete this section

## Go

### Library API

briancaine note:

  here's where we document tradebot if you wanted to link it into another program as a library. straightforward enough

### Exchange API

briancaine note:

  here's where we document implementing a new exchange for tradebot

## REST API

briancaine note: as above... where I'd document the rest API, including samples

## CLI

briancaine note: self explanatory, I'd think
