resource "azurerm_network_interface" "test" {
  name                = "NIC-dennisTerra"
  location            = var.location
  resource_group_name = var.resource_group

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.public_subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = var.public_ip_address_id
  }
}

resource "azurerm_linux_virtual_machine" "test" {
  disable_password_authentication = false
  name                  = "dennisTerraLinux-vm"
  location              = var.location
  resource_group_name   = var.resource_group
  size                  = "Standard_D2s_v3"
  admin_username        = var.admin_username
  admin_password = "TESTPW123456abcd!"

  network_interface_ids = [
    azurerm_network_interface.test.id
  ]  
  
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "16.04-LTS"
    version   = "latest"
  }
}