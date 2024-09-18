variable "region" {
  description = "The AWS region for the environment"
  type        = string
  default     = "eu-north-1"
}

variable "name" {
  description = "The name of the DynamoDB table"
  type        = string
}

variable "hash_key" {
  description = "The attribute to use as the hash (partition) key"
  type        = string
}

variable "range_key" {
  description = "The attribute to use as the range (sort) key"
  type        = string
  default     = null
}

variable "global_secondary_indexes" {
  description = "A list of global secondary indexes"
  type = list(object({
    name               = string
    hash_key           = string
    range_key          = string
    projection_type    = string
  }))
  default = []
}

variable "attributes" {
  description = "List of attributes used in the table and GSIs"
  type = list(object({
    name = string
    type = string
  }))
}
