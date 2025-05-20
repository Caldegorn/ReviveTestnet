import requests

def claim_faucet(wallet_address):
    faucet_url = 'https://faucet.testnet.revive.xyz/request'  # Replace with actual faucet URL
    payload = {
        "address": wallet_address
    }
    try:
        response = requests.post(faucet_url, json=payload)
        if response.status_code == 200:
            print(f"Faucet request successful: {response.json()}")
        else:
            print(f"Failed to claim faucet: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error during faucet request: {e}")

if __name__ == "__main__":
    my_wallet_address = "YourTestnetWalletAddressHere"
    claim_faucet(my_wallet_address)
