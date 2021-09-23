# Zap Contract to Batch Claims on Votium


Simple zap contract to claim all bribes on <a href="https://votium.app">Votium</a> in a single transaction to save some time and gas.

Proofs, amounts and indexes can be scraped from the websocket at `wss://s-usc1c-nss-243.firebaseio.com/.ws?v=5&ns=test-54f45-default-rtdb`

Distributor contract addresses can be obtained from the bribe contract at <a href='https://etherscan.io/address/0x19bbc3463dd8d07f55438014b021fb457ebd4595#readContract'>0x19BBC3463Dd8d07f55438014b021Fb457EBD4595</a>

The script folder contains two simple test scripts that can be run with brownie to compare gas costs. One to run the contract, one to run claims one by one from each distributor contract.
Both will need a dictionary of the format `{token_address: {'amount': int, 'proof': List(str), 'index': int}` filled with the information obtained from the ws.

