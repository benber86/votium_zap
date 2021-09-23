import brownie
from .scrape_proofs import get_claim_params


def main():
    bribe_contract = brownie.Contract.from_explorer('0x19BBC3463Dd8d07f55438014b021Fb457EBD4595')
    params = get_claim_params()
    contract_params = []
    for token in params.keys():
        distributor = bribe_contract.tokenInfo(token)['distributor']
        distributor = brownie.Contract.from_explorer(distributor)
        distributor.claim(params[token]['index'],
                          ETHEREUM_WALLET_ADDRESS,
                          params[token]['amount'],
                          params[token]['proof'],
                          {'from': ETHEREUM_WALLET_ADDRESS})

