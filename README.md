# 🚀 Order System with Nomad & Consul

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-✓-blue.svg)](https://docker.com)
[![Consul](https://img.shields.io/badge/Consul-✓-red.svg)](https://consul.io)
[![Nomad](https://img.shields.io/badge/Nomad-✓-orange.svg)](https://nomadproject.io)
[![Flask](https://img.shields.io/badge/Flask-✓-green.svg)](https://flask.palletsprojects.com)
[![Microservices](https://img.shields.io/badge/Architecture-Microservices-purple.svg)]()

</div>

## 📋 About the Project

A microservices-based order management system using modern DevOps tools. This project demonstrates the complete lifecycle of microservices development with orchestration, service discovery, and dynamic configuration.

### 🎯 Key Features

- ✅ **Microservices Architecture** - two independent services
- ✅ **Dynamic Configuration** - via Consul KV store
- ✅ **Service Discovery** - automatic service detection
- ✅ **Health Checks** - service status monitoring
- ✅ **Containerization** - Docker for environment isolation
- ✅ **Orchestration** - Nomad for container management
- ✅ **REST API** - modern API for interaction


### 📊 System Components

| Component | Purpose | Port | Technologies |
|-----------|---------|------|--------------|
| **Order Service** | Order processing | 5000 | Python, Flask |
| **Notification Service** | Notifications | 5001 | Python, Flask |
| **Consul** | Service Discovery, Config Store | 8500 | HashiCorp Consul |
| **Nomad** | Container orchestration | 4646 | HashiCorp Nomad |
| **Docker** | Containerization | - | Docker Engine |

## 🚀 Quick Start

### 📋 Prerequisites

Before starting, make sure you have installed:

- **Docker** (version 20.10+)
- **Docker Compose** (version 2.0+)
- **Git** (for cloning the repository)


