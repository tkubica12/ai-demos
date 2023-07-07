resource "azurerm_mssql_server" "main" {
  count                        = var.enable_sql ? 1 : 0
  name                         = random_string.random.result
  resource_group_name          = azurerm_resource_group.main.name
  location                     = azurerm_resource_group.main.location
  version                      = "12.0"
  administrator_login          = var.user_name
  administrator_login_password = var.password
}

resource "azurerm_mssql_database" "main" {
  count     = var.enable_sql ? 1 : 0
  name      = "mydb"
  server_id = azurerm_mssql_server.main[0].id
  collation = "SQL_Latin1_General_CP1_CI_AS"
  sku_name  = "GP_Gen5_2"
}

resource "azurerm_mssql_firewall_rule" "main" {
  count            = var.enable_sql ? 1 : 0
  name             = "all"
  server_id        = azurerm_mssql_server.main[0].id
  start_ip_address = "0.0.0.0"
  end_ip_address   = "255.255.255.255"
}
