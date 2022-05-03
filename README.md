# Circle Ecosystem Catalog

The goal of this repository is to track the ecosystem of decentralized or centralized applications that
leverage Circle/Centre products across any supported blockchains.

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

### YAML Schema
```yaml
# Copyright 2022 Circle Internet Financial Trading Company Limited
---
$id: https://tbd.com/ecosystem.schema.json
$schema: http://json-schema.org/2020-12/schema#

title: Circle Ecosystem Catalog YAML Schema

maintainers:
  - Thomas Low <thomas.low@circle.com>

description: The YAML schema reference for the Circle Ecosystem Catalog.

type: object

properties:
  companyName:
    description: Name of the company.
    type: string
    maxLength: 50

  appName:
    description: Name of the app.
    type: string
    maxLength: 50

  products:
    description: Array of all applicable products.
    type: array
    items:
      type: string
      enum:
        - usdc
        - verite

  logo:
    description: Directory path to the logo file.
    type: string
    maxLength: 100

  website:
    description: URL of the app's website.
    type: string
    maxLength: 100

  description:
    description: Description of the app.
    type: string
    maxLength: 200

  dao:
    description: If the app is run as a DAO or a traditional company (non-DAO).
    type: boolean

  fiatOnRamp:
    description: The ability to convert fiat currency (e.g. USD) to USDC within the app.
    type: boolean

  audiences:
    description: Array of all intended audiences of the app.
    type: array
    items:
      type: string
      enum:
        - consumers
        - businesses

  blockchains:
    description: Array of all applicable blockchains that the app supports.
    type: array
    items:
      type: string
      enum:
        - ethereum
        - polygon
        - solana
        - avalanche
        - stellar
        - algorand
        - flow
        - tron
        - hedera
        - fantom
        - harmony
        - near
        - polkadot
        - cosmos

  categories:
    description: Array of all the applicable use cases.
    type: array
    items:
      type: string
      enum:
        - ecommerce
        - trading_exchanges
        - nft_marketplaces
        - cefi
        - defi
        - investing_yield
        - borrowing_lending
        - wallets
        - debit_cards
        - gaming
        - charity
        - banking
        - entertainment
        - restaurants
        - remittances
        - payroll

  platforms:
    description: Array of all applicable platforms that the app supports.
    type: array
    items:
      type: string
      enum:
        - web
        - ios
        - android

  regions:
    description: Array of all applicable regions that the app operates in.
    type: array
    items:
      type: string
      enum:
        - na
        - latam
        - emea
        - apac

  twitter:
    description: Twitter handle.
    type: string
    maxLength: 50

  telegram:
    description: Telegram handle.
    type: string
    maxLength: 50

  discord:
    description: Discord server.
    type: string
    maxLength: 50

required:
  - companyName
  - appName
  - products
  - logo
  - website
  - description
  - dao
  - fiatOnRamp
  - audiences
  - blockchains
  - categories
  - platforms
  - regions
```

### YAML Example (coinbaseWallet.yml)
```yaml
---
companyName: "Coinbase"
appName: "Coinbase Wallet"
products:
  - usdc
  - verite
logo: "catalog/coinbase/logos/coinbase.png"
website: "https://www.coinbase.com/wallet"
description: "Coinbase Wallet is a self-custody mobile cryptocurrency wallet and Web3 dapp browser."
dao: false
fiatOnRamp: true
audiences:
  - consumers
blockchains:
  - ethereum
  - polygon
  - solana
  - avalanche
  - stellar
  - algorand
  - flow
  - tron
  - hedera
  - fantom
  - harmony
  - near
  - polkadot
  - cosmos
categories:
  - wallets
platforms:
  - web
  - ios
  - android
regions:
  - na
  - latam
  - emea
  - apac
twitter: "https://twitter.com/coinbase"
```
