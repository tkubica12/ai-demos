// Azure Database for PostgreSQL Flexible Server
resource "azurerm_postgresql_flexible_server" "main" {
  count                  = var.enable_psql ? 1 : 0
  name                   = random_string.random.result
  resource_group_name    = azurerm_resource_group.main.name
  location               = azurerm_resource_group.main.location
  version                = "15"
  administrator_login    = var.user_name
  administrator_password = var.password
  storage_mb             = 32768
  sku_name               = "GP_Standard_D2s_v3"
  zone                   = 1
}

// Database
resource "azurerm_postgresql_flexible_server_database" "main" {
  count     = var.enable_psql ? 1 : 0
  name      = "mydb"
  server_id = azurerm_postgresql_flexible_server.main[0].id
  collation = "en_US.utf8"
  charset   = "utf8"
}

// Firewall rule
resource "azurerm_postgresql_flexible_server_firewall_rule" "main" {
  count            = var.enable_psql ? 1 : 0
  name             = "all"
  server_id        = azurerm_postgresql_flexible_server.main[0].id
  start_ip_address = "0.0.0.0"
  end_ip_address   = "255.255.255.255"
}

// Allow installation of vector extension
resource "azurerm_postgresql_flexible_server_configuration" "vector" {
  count     = var.enable_psql ? 1 : 0
  name      = "azure.extensions"
  server_id = azurerm_postgresql_flexible_server.main[0].id
  value     = "VECTOR"
}
