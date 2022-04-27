# Circle Ecosystem Catalog

The goal of this repository is to track the ecosystem of decentralized or centralized applications that
leverage Circle's products across any supported blockchains.

To contribute to this catalog, propose a PR including your application and logo by following the templates
below:

### Directory Structure
```
circle-ecosystem
└───catalog
    └───companyName
    │   └───apps
    │   │     appName.yml
    │   │     ...
    │   └───logos
    │         logoName.jpg
    │         ...
    └───coinbase # example
        └───apps
        │     coinbaseWallet.yml
        └───logos
              coinbaseWallet.jpg
```
### YAML Template
```yaml
---
# One app per yaml file

companyName: [String]     # Required. Name of the company.
appName: [String]         # Required. Name of the app.
products: [List]          # Required. List of all applicable Circle products.
  - USDC
  - Verite
logo: [String]            # Required. Name of the logo file.
url: [String]             # Required. URL of the app's website.
description: [String]     # Required. Description of the app. Limit 200 characters.
entityType: [String]      # Required. Type of organization that runs the app. Choose either "dao" or "non-dao" (traditional company).
fiatOnRamp: [Boolean]     # Required. The ability to convert fiat currency (e.g. USD) to USDC within the app.
audience:                 # Required. The intended audience(s) of the app.
  - Consumers
  - Businesses
blockchain:               # Required. List of all applicable blockchains that the app supports.
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
category:                 # Required. List of all the applicable use cases.
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
platform:                 # Required. List of all applicable platforms that the app supports.
  - Web
  - iOS
  - Android
region:                   # Required. List of all applicable regions that the app operates in.
  - NA
  - LATAM
  - EMEA
  - APAC
twitter: [String]         # Optional. Twitter handle.
telegram: [String]        # Optional. Telegram handle.
discord: [String]         # Optional. Discord channel.
```

### YAML Example (coinbaseWallet.yml)
```yaml
---
companyName: "Coinbase"
appName: "Coinbase Wallet"
products:
  - USDC
  - Verite
logo: "coinbase.jpg"
url: "https://www.coinbase.com/wallet"
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

### Logo Constraints
Logos should conform to the following parameters:
- Acceptable File Types: .jpg, .png, .svg
- Image Size: 200 x 200 pixels
- Aspect Ratio: 1:1 (square)

Note: Each app does not need its own logo.
