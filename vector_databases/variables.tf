variable "password" {
  type      = string
  default   = "Azure12345678"
  sensitive = true
}

variable "user_name" {
  type    = string
  default = "tomas"
}

variable "enable_cognitivesearch" {
  type    = bool
  default = true
}

variable "enable_dataexplorer" {
  type    = bool
  default = true
}

variable "enable_psql" {
  type    = bool
  default = true
}

variable "enable_sql" {
  type    = bool
  default = false
}

variable "enable_rediscontainer" {
  type    = bool
  default = true
}
  
variable "enable_mongo" {
  type    = bool
  default = true
}
  
