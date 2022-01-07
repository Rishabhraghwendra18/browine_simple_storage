from brownie import accounts,config,SimpleStorage,network

def deploy():
      account = get_Account()
      # account = accounts.add(config["wallets"]["from_keys"])
      simple_storage =  SimpleStorage.deploy({"from":account})
      simple_value =  simple_storage.retrieve()
      print(f'Intial: {simple_value}')
      transcation = simple_storage.store(15,{"from":account})
      transcation.wait(1)
      updated_stored_value= simple_storage.retrieve()
      print(f'New value is: {updated_stored_value}')

def get_Account():
      if(network.show_active()=="development"):
            return accounts[0]
      else:
            return accounts.add(config["wallets"]["from_keys"])

def main():
      deploy()