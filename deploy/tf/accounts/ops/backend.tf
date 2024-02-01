terraform {
  backend "s3" {
    bucket         = "circle-tf-514563129364-us-east-1"
    key            = "tf/ops/protractor/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = "true"
    dynamodb_table = "circle-tf-lock-514563129364-us-east-1"
  }

  required_providers {
    datadog = {
      source  = "DataDog/datadog"
      version = "~> 3.21.0"
    }
    elasticsearch = {
      source  = "phillbaker/elasticsearch"
      version = "~> 2.0.7"
    }
    pagerduty = {
      source  = "pagerduty/pagerduty"
      version = "~> 2.2.1"
    }
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4"
    }
  }
}
