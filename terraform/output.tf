output "publicIP" {
  sensitive = false
  value = module.public_ip.public_ip_address_id
}