# resource "azurerm_virtual_network" "main" {
#   name                = "vector-databases"
#   location            = azurerm_resource_group.main.location
#   resource_group_name = azurerm_resource_group.main.name
#   address_space       = ["10.0.0.0/16"]
# }

# resource "azurerm_subnet" "vm" {
#   name                 = "vm"
#   resource_group_name  = azurerm_resource_group.main.name
#   virtual_network_name = azurerm_virtual_network.main.name
#   address_prefixes     = ["10.0.0.0/24"]
# }