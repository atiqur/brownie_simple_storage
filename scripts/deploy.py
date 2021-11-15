from brownie import accounts


def deploy_simple_storage():
    # Uses the first account in the list of 10 accounts automatically created by brownie
    account = accounts[0]
    print(account)


def main():
    deploy_simple_storage()
