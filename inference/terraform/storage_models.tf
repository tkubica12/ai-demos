resource "azurerm_storage_account" "main" {
  name                     = module.naming.storage_account.name_unique
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "models" {
  name                  = "models"
  storage_account_name  = azurerm_storage_account.main.name
  container_access_type = "private"
}

resource "azurerm_storage_blob" "models_v1" {
  name                   = "mymodel/1/model.pt"
  storage_account_name   = azurerm_storage_account.main.name
  storage_container_name = azurerm_storage_container.models.name
  type                   = "Block"
  source                 = "../models/mymodel/1/model.pt"
}

resource "azurerm_storage_blob" "models_v2" {
  name                   = "mymodel/2/model.pt"
  storage_account_name   = azurerm_storage_account.main.name
  storage_container_name = azurerm_storage_container.models.name
  type                   = "Block"
  source                 = "../models/mymodel/2/model.pt"
}

resource "azurerm_storage_blob" "config" {
  name                   = "mymodel/config.pbtxt"
  storage_account_name   = azurerm_storage_account.main.name
  storage_container_name = azurerm_storage_container.models.name
  type                   = "Block"
  source                 = "../models/mymodel/config.pbtxt"
}