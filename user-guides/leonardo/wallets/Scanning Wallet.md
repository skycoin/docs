# Scanning wallet

It is a tool that allows you to scan N blocks of the blockchain to keep a record of the addresses that have received or not TXs, which were the minimum and maximum blocks scanned from each address and thus create a crypto wallet, which may be have a general balance of received cryptocurrencies.

## Addresses State

Each public address of the crypto wallet, will contain three states, which are: min_scan_block, mid_scan_block, max_scan_block. Each one of them contains a number that is the blockheight or index of the block inside the blockchain, which represents the block id that has been scanned, in search of those TXs that belong to at least one address of the crypto wallet. These states are used in the following way.

* **min_scan_block**, used as a record of the minimum or smallest block or blockheight index where a scan has been made, in search of TXs that belong to any of the crypto wallet addresses.

* **max_scan_block**, used as a record of the block or maximum blockheight index where a scan has been made, in search of TXs that belong to any of the crypto wallet addresses.

* **mid_scan_block**, this state is used as a control point, this allows scans in both directions of the main states (min_scan_block and max_scan_block). This state is updated when min_scan_block reaches it.

## Scanning

There are 4 scanning operations, which are used to scan N blocks of the blockchain, search and register the TXs that belong to each address of the crypto wallet according to the indexes of blocks provided; These operations are: update_min, update_max, update_far, update_short.

* **update_min**, will find the address with the minimum blockheight or minimum block index, with the same being able to find a block inside the blockchain, scan it and register those TXs that belong to the addresses of the crypto wallet; After performing this process, the min_scan_block state is updated.

* **update_max**, will find the address with the maximum blockheight or maximum block index, with the same being able to find a block inside the blockchain, scan it and register those TXs that belong to the addresses of the crypto wallet; After scanning and registering the TXs, the status max_scan_block is updated.

* **update_short**, will find the address with the blockheight or block index that is between the state min_scan_block and the state mid_scan_block, to be able to find the block inside the blockchain, scan it and register those TXs that belong to the addresses of the crypto wallet.

* **update_far**, will find the address with the blockheight or block index that is closer to the state mid_scan_block, to be able to find the block inside the blockchain, scan it and find those TXs that belong to the addresses of the crypto wallet.