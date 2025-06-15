# 📈 Falco Detection Test Cases

## 🔔 Case 1: Terminal shell spawned in a container

- **Rule**: `Terminal shell in container`
- **Test**: Ran `kubectl exec -it pod-name -- /bin/bash`
- **Falco Alert**:
  ```bash
  A shell was spawned in a container with sensitive mount

## 🔔 Case 2: Write to binary directory

- **Rule**: `Write below binary dir`
- **Test**: touch /usr/bin/test
- **Falco Alert**:
```bash
 A file below a known binary directory was written
```

## 📌 Investigation Steps

- Review Falco logs: /var/log/falco.log
- Correlate pod/container from alert metadata
- Use kubectl describe pod to investigate the conta
