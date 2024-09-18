resource "aws_dynamodb_table" "dynamodb_table" {
  name           = "kth-devops-example-db-dev"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "pk"
  range_key      = "sk"

  attribute {
    name = "pk"
    type = "S"
  }

  attribute {
    name = "sk"
    type = "S"
  }

  tags = {
    Name = "kth-devops-example-db-dev"
    Stage = "dev"
  }
}
