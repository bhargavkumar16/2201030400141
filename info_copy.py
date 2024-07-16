import sys
import requests
import socket
import json

# Get the hostname and IP address of the local machine
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("YOU ARE WORKING ON: " + hostname)
print("YOUR IP: " + ip_address)

# Prompt the user to input the URL
url = input("Enter the URL: ")

# Fetch the headers of the provided URL
req = requests.get("https://" + url)
print("\n" + str(req.headers))

# Get the IP address of the provided URL
get_host_by = socket.gethostbyname(url)
print("\nThe IP address of " + url + " is: " + get_host_by + "\n")

# Use the IP address to fetch location information using ipinfo.io API
req_two = requests.get("https://ipinfo.io/" + get_host_by + "/json")
resp_ = json.loads(req_two.text)

# Print location information
print("Location: " + resp_["loc"])
print("Region: " + resp_["region"])
print("City: " + resp_["city"])
print("Country: " + resp_["country"])

# Additional IP information
print("Organization: " + resp_["org"])
print("Postal Code: " + resp_["postal"])
print("Timezone: " + resp_["timezone"])

# Check if ASN (Autonomous System Number) exists before printing
if "asn" in resp_:
    print("ASN: " + resp_["asn"])
else:
    print("ASN: N/A")






