terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.67.0"
    }
  }

  backend "s3" {
    bucket         = "kth-devops-course-terraform-state-bucket-dev"
    key            = "terraform/state.tfstate"
    region         = "eu-north-1"
    dynamodb_table = "kth-devops-course-terraform-state-lock-dev"
    encrypt        = true
  }
}

provider "aws" {
  region  = "eu-north-1"
}
