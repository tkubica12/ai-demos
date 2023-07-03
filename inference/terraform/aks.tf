resource "azurerm_kubernetes_cluster" "main" {
  name                = module.naming.kubernetes_cluster.name
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  dns_prefix          = module.naming.kubernetes_cluster.name

  default_node_pool {
    name                = "default"
    node_count          = 1
    min_count           = 1
    max_count           = 3
    vm_size             = "Standard_D4as_v5"
    os_sku              = "AzureLinux"
    enable_auto_scaling = true
  }

  identity {
    type = "SystemAssigned"
  }
}
