"""
Utility functions using vulnerable dependencies.
"""

import urllib3
import requests
import yaml
from jinja2 import Template
from PIL import Image
from cryptography.fernet import Fernet


def load_config(config_path):
    """Load configuration from YAML file using PyYAML (CVE-2020-14343)"""
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


def render_template(template_string, context):
    """Render template using Jinja2 (CVE-2020-28493)"""
    template = Template(template_string)
    return template.render(**context)


def fetch_url(url):
    """Fetch URL using urllib3 (CVE-2021-33503, CVE-2021-23336)"""
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response.data


def fetch_url_requests(url):
    """Fetch URL using requests library"""
    r = requests.get(url, timeout=5)
    return r.text


def encrypt_data(data, key=None):
    """Encrypt data using cryptography (GHSA-79v4-65xg-pq4g)"""
    if key is None:
        key = Fernet.generate_key()
    f = Fernet(key)
    return f.encrypt(data.encode() if isinstance(data, str) else data)


def process_image(image_path):
    """Process image using Pillow (CVE-2021-27921)"""
    img = Image.open(image_path)
    return img.resize((800, 600))

