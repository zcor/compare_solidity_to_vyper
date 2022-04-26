import brownie
from brownie import *

def main():
    solidity = Vanilla721A.deploy({'from': a[0]})
    vyper = VyperNFT.deploy({'from': a[0]})

    print("Deploy Cost")
    print(f"Solidity: {gas_cost(history[-2])}")
    print(f"Vyper: {gas_cost(history[-1])}")

    solidity.mint(1, {'from': a[0], 'value': Wei('.1 ether')})
    vyper.mint(a[0], 1, {'from': a[0], 'value': Wei('.1 ether')})

    print("\nMint Cost")
    print(f"Solidity: {gas_cost(history[-2])}")
    print(f"Vyper: {gas_cost(history[-1])}")




def gas_cost(tx):
    return tx.gas_used * Wei('50 gwei') / 10 ** 18
