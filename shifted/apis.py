# apis.py

import requests

class BlockchainAPI:
    def __init__(self):
        self.supported_blockchains = {
            "Ethereum": EthereumAPI,
            "Solana": SolanaAPI,
            "Binance Smart Chain": BinanceSmartChainAPI
        }
    
    def get_client(self, blockchain_name):
        if blockchain_name in self.supported_blockchains:
            return self.supported_blockchains[blockchain_name]()
        else:
            raise ValueError(f"[ERROR] Blockchain '{blockchain_name}' not supported.")
    
    def list_supported_blockchains(self):
        return list(self.supported_blockchains.keys())

class EthereumAPI:
    def __init__(self):
        self.base_url = "https://api.etherscan.io/api"
        self.api_key = "Your-Etherscan-API-Key"  # Replace with your API key

    def fetch_latest_transactions(self, address, limit=10):
        print(f"[INFO] Fetching latest Ethereum transactions for {address}")
        url = f"{self.base_url}?module=account&action=txlist&address={address}&sort=desc&apikey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["result"][:limit]
        else:
            print(f"[ERROR] Failed to fetch data: {response.status_code}")
            return []

class SolanaAPI:
    def __init__(self):
        self.base_url = "https://api.mainnet-beta.solana.com"

    def fetch_account_data(self, public_key):
        print(f"[INFO] Fetching Solana account data for {public_key}")
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getAccountInfo",
            "params": [public_key, {"encoding": "jsonParsed"}]
        }
        response = requests.post(self.base_url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[ERROR] Failed to fetch data: {response.status_code}")
            return {}

class BinanceSmartChainAPI:
    def __init__(self):
        self.base_url = "https://api.bscscan.com/api"
        self.api_key = "Your-BSCSCAN-API-Key"  # Replace with your API key

    def fetch_latest_transactions(self, address, limit=10):
        print(f"[INFO] Fetching latest BSC transactions for {address}")
        url = f"{self.base_url}?module=account&action=txlist&address={address}&sort=desc&apikey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["result"][:limit]
        else:
            print(f"[ERROR] Failed to fetch data: {response.status_code}")
            return []

# Example usage
if __name__ == "__main__":
    blockchain_api = BlockchainAPI()
    print("[INFO] Supported blockchains:", blockchain_api.list_supported_blockchains())
    
    # Fetch Ethereum transactions
    eth_client = blockchain_api.get_client("Ethereum")
    eth_data = eth_client.fetch_latest_transactions("0xYourEthereumAddressHere")
    print("[Ethereum Transactions]:", eth_data)
    
    # Fetch Solana account data
    sol_client = blockchain_api.get_client("Solana")
    sol_data = sol_client.fetch_account_data("YourSolanaPublicKeyHere")
    print("[Solana Account Data]:", sol_data)
    
    # Fetch Binance Smart Chain transactions
    bsc_client = blockchain_api.get_client("Binance Smart Chain")
    bsc_data = bsc_client.fetch_latest_transactions("0xYourBinanceAddressHere")
    print("[BSC Transactions]:", bsc_data)
