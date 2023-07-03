resource "helm_release" "triton" {
  name         = "triton"
  chart        = "../charts/triton"
  force_update = true

  set {
    name  = "storage_account_name"
    value = azurerm_storage_account.main.name
  }

  set {
    name  = "storage_account_key"
    value = azurerm_storage_account.main.primary_access_key
  }

  depends_on = [ 
    azurerm_storage_blob.config,
    azurerm_storage_blob.models_v1,
    azurerm_storage_blob.models_v2,
  ]
}
