import requests

def get_block_by_transaction_hash(transaction_hash):
    url = "https://api.etherscan.io/api?module=block&action=getblockbytransactionhash&txhash=" + transaction_hash
    response = requests.get(url)
    data = response.json()
    return data["blockNumber"]

def get_transaction_receipt(transaction_hash):
    url = "https://api.etherscan.io/api?module=transaction&action=gettransactionreceipt&txhash=" + transaction_hash
    response = requests.get(url)
    data = response.json()
    return data

transaction_hash = "0x4afbbeef1c35b78a825ae9e89276330d4fc75ffc38b2b53e58036f376ee25fd5"

block_number = get_block_by_transaction_hash(transaction_hash)
transaction_receipt = get_transaction_receipt(transaction_hash)

print("Bloque:", block_number)
print("Ethers enviados:", transaction_receipt["amount"])
print("Gas consumido:", transaction_receipt["gasUsed"])
print("Gas limit:", transaction_receipt["gasLimit"])
print("Gas price:", transaction_receipt["gasPrice"])