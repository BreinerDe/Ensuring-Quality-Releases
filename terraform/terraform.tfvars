# Azure subscription vars
# credentials will be set via environment variables in the pipeline. See https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret#configuring-the-service-principal-in-terraform
# subscription_id = ""
# client_id = ""
# client_secret = ""
# tenant_id = ""

# Resource Group/Location
location = "west us 3"
resource_group = "ensuring-quality-releases"
application_type = "webnapp20222807"

# Network
virtual_network_name = "vnet1"
address_space = ["10.5.0.0/16"]
address_prefix_test = "10.5.1.0/24"
