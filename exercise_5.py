import requests

def run_exercise_5():
    def get_block_by_transaction_hash(transaction_hash):
        url = "https://api.etherscan.io/api?module=block&action=getblockbytransactionhash&txhash=" + transaction_hash
        response = requests.get(url)
        data = response.json()

        if 'blockNumber' in data:
            return data["blockNumber"]
        else:
            return None  # O puedes manejar de otra manera si el campo no está presente

    def get_transaction_receipt(transaction_hash):
        url = "https://api.etherscan.io/api?module=transaction&action=gettransactionreceipt&txhash=" + transaction_hash
        response = requests.get(url)
        data = response.json()

        return data  # Devuelve el diccionario completo, maneja el acceso a campos específicos donde sea necesario

    transaction_hash = "0x4afbbeef1c35b78a825ae9e89276330d4fc75ffc38b2b53e58036f376ee25fd5"

    block_number = get_block_by_transaction_hash(transaction_hash)
    transaction_receipt = get_transaction_receipt(transaction_hash)

    if block_number is not None:
        print("Bloque:", block_number)
    else:
        print("ERROR 500: No se encontró el bloque para la transacción.Probablemente esté habiendo un problema al recibir informacion de la API")

    # Puedes acceder a otros campos del recibo de transacción según sea necesario
    print("Recibo de transacción:", transaction_receipt)

if __name__ == "__main__":
    run_exercise_5()