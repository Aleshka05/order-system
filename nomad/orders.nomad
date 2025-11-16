# nomad/orders.nomad
job "order-system" {
  datacenters = ["dc1"]

  group "orders" {
    count = 2

    network {
      port "http" {
        to = 5000
      }
    }

    service {
      name = "order-service"
      port = "http"
      
      check {
        type     = "http"
        path     = "/health"
        interval = "10s"
        timeout  = "2s"
      }
    }

    task "order-service" {
      driver = "docker"

      config {
        image = "order-service:latest"
        ports = ["http"]
      }

      env {
        CONSUL_HOST = "consul-server"
      }
    }
  }

  group "notifications" {
    count = 1

    network {
      port "http" {
        to = 5001
      }
    }

    service {
      name = "notification-service"
      port = "http"
      
      check {
        type     = "http"
        path     = "/health"
        interval = "10s"
        timeout  = "2s"
      }
    }

    task "notification-service" {
      driver = "docker"

      config {
        image = "notification-service:latest"
        ports = ["http"]
      }
    }
  }
}