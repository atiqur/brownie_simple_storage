from brownie import accounts
import os


def deploy_simple_storage():
    # Uses the first account in the list of 10 accounts automatically created by brownie
    # account = accounts[0]
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    print(account)


def main():
    deploy_simple_storage()
