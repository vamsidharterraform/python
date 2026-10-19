text = "awsdevops"
characters = []

print(text)

for i in text:
    characters.append(i)

characters.append('engineer')
print(characters)

# ============================================

data = ["aws", "devops", "python"]

s = " ".join(data)

print(s)

# for i in data:
#     print(i)

# ========================================

servers = [
    "prod-web-01",
    "dev-web-01",
    "prod-api-01",
    "test-db-01",
    "prod-db-01"
]

prod_servers = []
non_prod_servers = []

for ser in servers:
    if ser.startswith("prod"):
        prod_servers.append(ser)
    else:
        non_prod_servers.append(ser)
print("Production servers:", prod_servers)
print("Non-production servers:", non_prod_servers)

# ====================================================
servers = {
    "web-server-01": 65,
    "web-server-02": 92,
    "api-server-01": 88,
    "db-server-01": 45,
    "worker-server-01": 97
}

High_CPU_servers = []
Normal_CPU_servers = []

# out:

# High CPU servers: ['web-server-02', 'api-server-01', 'worker-server-01']
# Normal CPU servers: ['web-server-01', 'db-server-01']

for i, t in servers.items():
    if t >= 80:
        High_CPU_servers.append(i)
    else:
        Normal_CPU_servers.append(i)
print("High CPU servers:" , High_CPU_servers)
print("Normal CPU servers:" , Normal_CPU_servers)

# ====================================================

# Create two empty lists: healthy_services and failed_services.
# Iterate through the dictionary using .items().
# If a service status is "running", append its name to healthy_services.
# Otherwise, append its name to failed_services.
# Print both lists.
# Print a warning for every failed service.    

Healthy_services = []
Failed_services = []

services = {
    "nginx": "running",
    "docker": "running",
    "kubelet": "failed",
    "prometheus": "running",
    "node_exporter": "failed"
}

# Healthy services: ['nginx', 'docker', 'prometheus']
# Failed services: ['kubelet', 'node_exporter']

# WARNING: kubelet is failed
# WARNING: node_exporter is failed

for key , val in services.items():
    if val == "running":
        Healthy_services.append(key)
    else:
        Failed_services.append(key)
        print("Warning " + key + " is failed")

print("Healthy services:", Healthy_services)
print("Failed services:", Failed_services)

# ==================================================================

disk_usage = {
    "web-server-01": "65%",
    "web-server-02": "92%",
    "api-server-01": "78%",
    "db-server-01": "88%",
    "worker-server-01": "45%"
}

high_disk_servers = []
normal_disk_servers = []

# Create two empty lists: high_disk_servers and normal_disk_servers.
# Iterate through the dictionary using .items().
# Remove the % character from each usage value.
# Convert the usage to an integer.
# If disk usage is greater than or equal to 85%, add the server name to high_disk_servers and print a warning.
# Otherwise, add the server name to normal_disk_servers.
# Print both lists at the end.

# WARNING: web-server-02 disk usage is 92%
# WARNING: db-server-01 disk usage is 88%

# High disk servers: ['web-server-02', 'db-server-01']
# Normal disk servers: ['web-server-01', 'api-server-01', 'worker-server-01']

for k , v in disk_usage.items():
    v = int(v.replace("%" , ""))
    
    if v >= 85:
        high_disk_servers.append(k)
        print( f"WARNING: {k} disk usage is: {v}%" )
    else:
        normal_disk_servers.append(k)
        
print()
print("High disk servers:" , high_disk_servers)
print("Normal disk servers:" , normal_disk_servers)
# ===========================================================================

