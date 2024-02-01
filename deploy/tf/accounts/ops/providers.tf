provider "aws" {
  region = local.region
}

provider "datadog" {
  api_key = data.aws_secretsmanager_secret_version.dd_api_key.secret_string
  app_key = data.aws_secretsmanager_secret_version.dd_app_key.secret_string
}

data "aws_secretsmanager_secret_version" "dd_api_key" {
  secret_id = "/ops/utilities/datadog/api_key"
}

data "aws_secretsmanager_secret_version" "dd_app_key" {
  secret_id = "/ops/utilities/datadog/terraform_app_key"
}

provider "pagerduty" {
  token = data.aws_secretsmanager_secret_version.pagerduty_api_key.secret_string
}

data "aws_secretsmanager_secret_version" "pagerduty_api_key" {
  secret_id = "/ops/atlantis/pagerduty-api-key"
}
