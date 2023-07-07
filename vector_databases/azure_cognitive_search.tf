resource "azurerm_search_service" "main" {
  count               = var.enable_cognitivesearch ? 1 : 0
  name                = random_string.random.result
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  sku                 = "standard"
}
