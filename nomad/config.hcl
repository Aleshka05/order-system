# nomad/config.hcl
datacenter = "dc1"
data_dir = "/tmp/nomad"

client {
  enabled = true
}

server {
  enabled = true
  bootstrap_expect = 1
}

consul {
  address = "consul-server:8500"
}