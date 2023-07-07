resource "azurerm_container_group" "redis" {
  count               = var.enable_rediscontainer ? 1 : 0
  name                = "redis"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  ip_address_type     = "Public"
  dns_name_label      = "redis${random_string.random.result}"
  os_type             = "Linux"

  container {
    name   = "redis"
    image  = "docker.io/redis/redis-stack"
    cpu    = "2"
    memory = "8"

    ports {
      port     = 6379
      protocol = "TCP"
    }

    ports {
      port     = 8001
      protocol = "TCP"
    }

    environment_variables = {
      REDIS_ARGS = "--requirepass ${var.password}"
    }
  }
}
