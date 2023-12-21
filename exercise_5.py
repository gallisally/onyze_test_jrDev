#uso de la API etherscan
import requests
def run_exercise_5():
    def get_block_by_transaction_hash(transaction_hash):
        url = "https://api.etherscan.io/api?module=block&action=getblockbytransactionhash&txhash=" + transaction_hash
        response = requests.get(url)
        data = response.json()

        # Verificar si la clave 'blockNumber' está presente en el diccionario
        if 'blockNumber' in data:
            return data["blockNumber"]
        else:
            return "Block number not available"  # Puedes ajustar el mensaje según tus necesidades

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

if __name__ == "__main__":
    run_exercise_5()