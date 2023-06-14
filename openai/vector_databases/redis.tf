# // Azure Cache for Redis Enterprise
# resource "azurerm_redis_enterprise_cluster" "main" {
#   name                = random_string.random.result
#   resource_group_name = azurerm_resource_group.main.name
#   location            = azurerm_resource_group.main.location
#   sku_name            = "Enterprise_E10-2"
# }
