# ☸️ Kubernetes Hardening Checklist

This document captures key hardening steps applied on a test Kubernetes cluster to reduce attack surface.

## 🔐 Control Plane Hardening

- [x] Disable anonymous access to Kube API
- [x] Enable RBAC authorization
- [x] Audit logs enabled (`--audit-log-path`)
- [x] API server only accessible via load balancer or VPN
- [x] Etcd encryption enabled

## 🛡️ Node & Pod Hardening

- [x] Disable privileged containers
- [x] Default deny all ingress/egress network policies
- [x] Drop NET_RAW and other dangerous capabilities
- [x] Use non-root user for app pods
- [x] Image scanning using Trivy

## 🔍 Monitoring Tools

- [x] Falco installed to detect runtime anomalies
- [x] Metrics Server enabled
- [x] Kubeaudit run for policy compliance
- [ ] OPA/Gatekeeper for policy enforcement (WIP)

_Cluster: Kind / Minikube (local test cluster)_  
