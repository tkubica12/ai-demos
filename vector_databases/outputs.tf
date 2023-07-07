output "random_name" {
  value = random_string.random.result
}

output "cs_api_key" {
  value     = azurerm_search_service.main[0].primary_key
  sensitive = true
}