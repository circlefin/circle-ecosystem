# USDC Ecosystem Catalog

The goal of this repository is to track the ecosystem of applications and businesses that support or
build on top of USDC.

To contribute to this catalog, please propose a PR with the following files by following the templates below:

1. An image of your app / company logo
2. A yaml file with the requested information about your app (one app per yaml file)

_By submitting your name and logo, you (i) represent and warrant that you are authorized to bind
your company or protocol; and (ii) hereby grant Circle permission to use your name and logo on its
website and in its marketing materials._

## Logo Constraints
Logos should conform to the following parameters:

- Acceptable File Types: .jpg, .png
- Image Size: 200 x 200 pixels
- Aspect Ratio: 1:1 (square)
- Max File Size: 5 MB

Note: Each app does not need its own logo. Logos may be reused by multiple apps under the same company / org.

## UUID Generation
For each app, please generate a UUID v4.

On Mac OS X:
```shell
uuidgen | awk '{print tolower($0)}'
```

On Linux:
```shell
uuidgen
```

You may also use an online tool to generate a UUID. (https://uuidonline.com/)

## Directory Structure
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
              coinbase.png
```

## YAML Schema
```yaml
# Copyright 2022 Circle Internet Financial Trading Company Limited
---
$id: https://circle.com/ecosystem.schema.json
$schema: https://json-schema.org/draft/2020-12/schema

title: Circle Ecosystem Catalog YAML Schema

maintainers:
  - Thomas Low <thomas.low@circle.com>

description: The YAML schema reference for Circle Ecosystem Catalog.

type: object

properties:
  id:
    description: UUID of the app.
    type: string
    minLength: 36
    maxLength: 36
    pattern: "^[0-9a-f]{8}\\b-[0-9a-f]{4}\\b-[0-9a-f]{4}\\b-[0-9a-f]{4}\\b-[0-9a-f]{12}$"

  companyName:
    description: Name of the company.
    type: string
    minLength: 1
    maxLength: 50

  appName:
    description: Name of the app.
    type: string
    minLength: 1
    maxLength: 50

  logo:
    description: Directory path to the logo file.
    type: string
    maxLength: 150
    pattern: "catalog\\/.+\\/logos\\/.+\\.(png|jpg|jpeg)$"

  website:
    description: URL of the app's website.
    type: string
    minLength: 8
    maxLength: 100
    pattern: "^https://.+"

  description:
    description: Description of the app.
    type: string
    minLength: 1
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
        - algorand
        - arbitrum
        - avalanche
        - ethereum
        - flow
        - hedera
        - near
        - optimism
        - polkadot
        - polygon
        - solana
        - stellar
        - tron

  categories:
    description: Array of all the applicable use cases.
    type: array
    items:
      type: string
      enum:
        - banking
        - borrowing_lending
        - cefi
        - charity
        - debit_cards
        - defi
        - ecommerce
        - entertainment
        - gaming
        - investing_yield
        - nft_marketplaces
        - payroll
        - remittances
        - restaurants
        - trading_exchanges
        - wallets

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
    minLength: 20
    maxLength: 75
    pattern: "^https://twitter.com/.+"

  telegram:
    description: Telegram handle.
    type: string
    minLength: 13
    maxLength: 50
    pattern: "^https://t.me/.+"

  discord:
    description: Discord server.
    type: string
    minLength: 19
    maxLength: 50
    pattern: "^https://discord.com/.+"

required:
  - id
  - companyName
  - appName
  - logo
  - website
  - categories
```

## YAML Example (coinbaseWallet.yml)
```yaml
---
id: "27d0cea3-d1d2-423e-b9a7-b849eaf79ac3"
companyName: "Coinbase"
appName: "Coinbase Wallet"
logo: "catalog/coinbase/logos/coinbase.png"
website: "https://www.coinbase.com/wallet"
description: "Coinbase Wallet is a self-custody mobile cryptocurrency wallet and Web3 dapp browser."
dao: false
fiatOnRamp: true
audiences:
  - consumers
blockchains:
  - algorand
  - arbitrum
  - avalanche
  - ethereum
  - flow
  - hedera
  - near
  - optimism
  - polkadot
  - polygon
  - solana
  - stellar
  - tron
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

## Linting & Validation
```shell
$ pip install -r requirements.txt
$ python linter.py
$ python logo_validator.py
```
