from brownie import SimpleStorage, accounts,config
from scripts.deploy import get_Account

def read_contract():
      simple_storage = SimpleStorage[-1]
      # updating value
      account = get_Account()
      simple_storage.store(30,{"from":account})

      print(simple_storage.retrieve())

def main():
      read_contract()