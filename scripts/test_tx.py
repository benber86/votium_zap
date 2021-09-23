import brownie
from .scrape_proofs import get_claim_params
from brownie import accounts, VotiumZap


def main():
    bribe_contract = brownie.Contract.from_explorer('0x19BBC3463Dd8d07f55438014b021Fb457EBD4595')
    params = get_claim_params()
    contract_params = []
    for token in params.keys():
        distributor = bribe_contract.tokenInfo(token)['distributor']
        contract_params.append((distributor,
                                params[token]['index'],
                                params[token]['amount'],
                                params[token]['proof']))

    zap = VotiumZap.deploy({'from': accounts[0]})
    zap.batchClaim(contract_params, {'from': ETHEREUM_WALLET_ADDRESS})

