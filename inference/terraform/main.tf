module "naming" {
  source  = "Azure/naming/azurerm"
  prefix = [ "d" ]
  suffix = [ "inference" ]
}

resource "azurerm_resource_group" "main" {
  name     = module.naming.resource_group.name
  location = var.location
}

