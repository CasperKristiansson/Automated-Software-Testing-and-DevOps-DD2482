module "example-db-dev" {
  source    	= "../../../modules/dynamodb"
  name      	= "kth-devops-example-db-dev"
  hash_key  	= "pk"
  range_key   = "sk"
	attributes = [
    {
			name = "pk",
			type = "S"
		},
    {
      name = "sk",
      type = "S"
    }
  ]
}
