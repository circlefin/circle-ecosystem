locals {
  aws_account_id  = module.account_ids.account_ids_by_name["ops"]
  region          = "us-east-1"
  service         = "circle-ecosystem"
  repository      = "circle-ecosystem"
  repository_org  = "circlefin"
  repository_url  = "https://github.com/circlefin/circle-ecosystem"
  business_domain = "web3"
  environment     = terraform.workspace
  owner           = "developer-ecosystem"
  owner_email     = "thomas.low@circle.com"
  tier            = 2
  sdlc            = "development"
}

module "account_ids" {
  source = "git@github.com:circlefin/terraform-aws-account-ids?ref=3.6.1"
}
