# Circle Ecosystem Catalog

The goal of this repository is to track the ecosystem of decentralized or centralized applications that
leverage Circle's products across any supported blockchains.

To contribute to this catalog, please propose a PR with the following files by following the templates below:

1. An image of your app / company logo
2. A yaml file with the requested information about your app (one app per yaml file)

### Logo Constraints
Logos should conform to the following parameters:

- Acceptable File Types: .jpg, .png, .svg
- Image Size: 200 x 200 pixels
- Aspect Ratio: 1:1 (square)

Note: Each app does not need its own logo. Logos may be reused by multiple apps under the same company / org.

### Directory Structure
```
circle-ecosystem
└───catalog
    ├───companyName
    │   ├───apps
    │   │     appName.yml
    │   │     ...
    │   └───logos
    │         logoName.jpg
    │         ...
    └───coinbase # example
        ├───apps
        │     coinbaseWallet.yml
        └───logos
              coinbaseWallet.jpg
```

### YAML Template
```yaml
---
companyName: [String]     # Required. Name of the company.
appName: [String]         # Required. Name of the app.
circleProduct: [List]     # Required. List of all applicable Circle products.
  - USDC
  - Verite
logo: [String]            # Required. Name of the logo file.
website: [String]         # Required. URL of the app's website.
description: [String]     # Required. Description of the app. Limit 200 characters.
entityType: [String]      # Required. Type of organization that runs the app. Choose either "dao" or "non-dao" (traditional company).
fiatOnRamp: [Boolean]     # Required. The ability to convert fiat currency (e.g. USD) to USDC within the app.
audience:                 # Required. The intended audience(s) of the app.
  - Consumers
  - Businesses
blockchain: [List]        # Required. List of all applicable blockchains that the app supports.
  - Ethereum
  - Polygon
  - Solana
  - Avalanche
  - Stellar
  - Algorand
  - Flow
  - TRON
  - Hedera
  - Fantom
  - Harmony
  - NEAR
  - Polkadot
  - Cosmos
category: [List]          # Required. List of all the applicable use cases.
  - eCommerce
  - Trading/Exchanges
  - NFT Marketplaces
  - CeFi
  - DeFi
  - Investing/Yield
  - Borrowing/Lending
  - Wallets
  - Debit Cards
  - Gaming
  - Charity/Donations
  - Banking
  - Entertainment
  - Restaurants
  - Remittances
  - Payroll
platform: [List]          # Required. List of all applicable platforms that the app supports.
  - Web
  - iOS
  - Android
region: [List]            # Required. List of all applicable regions that the app operates in.
  - NA
  - LATAM
  - EMEA
  - APAC
twitter: [String]         # Optional. Twitter handle.
telegram: [String]        # Optional. Telegram handle.
discord: [String]         # Optional. Discord server.
```

### YAML Example (coinbaseWallet.yml)
```yaml
---
companyName: "Coinbase"
appName: "Coinbase Wallet"
circleProduct:
  - USDC
  - Verite
logo: "coinbase.jpg"
website: "https://www.coinbase.com/wallet"
description: "Coinbase Wallet is a self-custody mobile cryptocurrency wallet and Web3 dapp browser."
audience:
  - Consumers
fiatOnRamp: True
blockchain:
  - Ethereum
  - Polygon
  - Solana
  - Avalanche
  - Stellar
  - Algorand
  - Flow
  - TRON
  - Hedera
  - Fantom
  - Harmony
  - NEAR
  - Polkadot
  - Cosmos
category:
  - Wallets
entityType: "non-dao"
platform:
  - Web
  - iOS
  - Android
region:
  - NA
  - LATAM
  - EMEA
  - APAC
twitter: "https://twitter.com/coinbase"
```
