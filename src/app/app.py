"""
Application module demonstrating usage of vulnerable dependencies.
This file is part of the src/app structure for AST scanning.
"""

import urllib3
import requests
import yaml
from jinja2 import Template
from PIL import Image
from cryptography.fernet import Fernet


class VulnerableApp:
    """Application class that uses all vulnerable dependencies."""
    
    def __init__(self):
        """Initialize the application with all dependencies."""
        self.http = urllib3.PoolManager()
        self.fernet_key = Fernet.generate_key()
        self.cipher = Fernet(self.fernet_key)
    
    def make_http_request(self, url):
        """Make HTTP request using urllib3 (CVE-2021-33503, CVE-2021-23336)"""
        response = self.http.request('GET', url)
        return response.data
    
    def make_requests_call(self, url):
        """Make HTTP request using requests library"""
        r = requests.get(url, timeout=5)
        return r.text
    
    def encrypt_data(self, data):
        """Encrypt data using cryptography (GHSA-79v4-65xg-pq4g)"""
        encrypted = self.cipher.encrypt(data.encode() if isinstance(data, str) else data)
        return encrypted
    
    def process_image(self, width=100, height=100):
        """Process image using Pillow (CVE-2021-27921)"""
        img = Image.new('RGB', (width, height), color='blue')
        return img
    
    def render_template(self, template_str, **context):
        """Render template using Jinja2 (CVE-2020-28493)"""
        template = Template(template_str)
        return template.render(**context)
    
    def parse_yaml(self, yaml_string):
        """Parse YAML using PyYAML (CVE-2020-14343)"""
        return yaml.safe_load(yaml_string)


def test():
    """Test function that uses all vulnerable packages."""
    app = VulnerableApp()
    
    # Test urllib3
    http = urllib3.PoolManager()
    
    # Test requests
    r = requests.get('https://example.com', timeout=5)
    
    # Test cryptography
    key = Fernet.generate_key()
    f = Fernet(key)
    
    # Test Pillow
    img = Image.new('RGB', (100, 100))
    
    # Test Jinja2
    template = Template('Hello {{ name }}!')
    rendered = template.render(name="World")
    
    # Test PyYAML
    data = yaml.safe_load('key: value')
    
    return http, r, key, img, template, data


if __name__ == "__main__":
    test()

