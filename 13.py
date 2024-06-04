from ipaddress import *

# сначала пишем сам адрес затем маску
net = ip_address('145.92.137.88/255.255.240.0', 0)

# напечатают адрес сети
print(net)
