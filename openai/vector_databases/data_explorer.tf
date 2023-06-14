resource "azurerm_kusto_cluster" "main" {
  count               = var.enable_dataexplorer ? 1 : 0
  name                = random_string.random.result
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  allowed_ip_ranges   = ["0.0.0.0/0"]
  engine              = "V3"

  sku {
    name     = "Standard_E2ads_v5"
    capacity = 2
  }
}

resource "azurerm_kusto_database" "main" {
  count               = var.enable_dataexplorer ? 1 : 0
  name                = "mydb"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  cluster_name        = azurerm_kusto_cluster.main[0].name
  hot_cache_period    = "P7D"
  soft_delete_period  = "P7D"
}
