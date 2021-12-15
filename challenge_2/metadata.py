# Run this python script in AWS EC2 instance
# It will return metadata for that particular instance

import requests
import sys
from requests.packages.urllib3 import Retry


def get_instance_region():
    instance_identity_url = "http://169.254.169.254/latest/dynamic/instance-identity/document"
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=0.3)
    metadata_adapter = requests.adapters.HTTPAdapter(max_retries=retries)
    session.mount("http://169.254.169.254/", metadata_adapter)
    try:
        r = requests.get(instance_identity_url, timeout=(2, 5))
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError) as err:
        print("Connection to AWS EC2 Metadata timed out: " + str(err.__class__.__name__))
        print("Is this an EC2 instance? Is the AWS metadata endpoint blocked? (http://169.254.169.254/)")
        sys.exit(1)
    return r.json()

resp = get_instance_region()
print(resp)
