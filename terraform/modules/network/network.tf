resource "azurerm_virtual_network" "test" {
  name                 = "terra-virtualNetwork"
  address_space        = "${var.address_space}"
  location             = "${var.location}"
  resource_group_name  = "${var.resource_group}"
}
resource "azurerm_subnet" "test" {
  name                 = "terra-virtualNetwork-sub"
  resource_group_name  = "${var.resource_group}"
  virtual_network_name = "${azurerm_virtual_network.test.name}"
  address_prefixes       = ["10.5.0.0/24"]
}
