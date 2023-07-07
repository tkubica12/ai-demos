// Azure Cosmos DB for MongoDB vCore
resource "azapi_resource" "mongodb" {
  count     = var.enable_mongo ? 1 : 0
  type      = "Microsoft.DocumentDB/mongoClusters@2023-03-01-preview"
  name      = random_string.random.result
  location  = azurerm_resource_group.main.location
  parent_id = azurerm_resource_group.main.id
  body = jsonencode({
    properties = {
      administratorLogin         = var.user_name
      administratorLoginPassword = var.password
      nodeGroupSpecs = [
        {
          diskSizeGB = 128
          enableHa   = false
          kind       = "Shard"
          nodeCount  = 1
          sku        = "M30"
        }
      ]
    }
  })
}

resource "azapi_resource" "mongodb_firewall" {
  count     = var.enable_mongo ? 1 : 0
  type      = "Microsoft.DocumentDB/mongoClusters/firewallRules@2023-03-01-preview"
  name      = "AllowAll"
  parent_id = azapi_resource.mongodb[0].id
  body = jsonencode({
    properties = {
      startIpAddress = "0.0.0.0"
      endIpAddress   = "255.255.255.255"
    }
  })
}
