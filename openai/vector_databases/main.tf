// Resource Group
resource "azurerm_resource_group" "main" {
  name     = "d-vector-databases"
  location = "westeurope"
}

// Random string
resource "random_string" "random" {
  length  = 14
  special = false
  upper   = false
  lower   = true
  numeric = false
}


