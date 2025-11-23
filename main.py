"""
Main application file demonstrating usage of vulnerable dependencies.
This project is intentionally created with known vulnerable package versions
for security testing purposes.
"""

import urllib3
import requests
import yaml
from jinja2 import Template
from PIL import Image
from cryptography.fernet import Fernet


def demonstrate_urllib3():
    """Demonstrates urllib3 usage (CVE-2021-33503, CVE-2021-23336)"""
    print("Using urllib3 for HTTP requests...")
    http = urllib3.PoolManager()
    print("urllib3 initialized")
    return http


def demonstrate_requests():
    """Demonstrates requests usage"""
    print("Using requests for HTTP requests...")
    # Note: requests uses urllib3 internally
    r = requests.get('https://example.com', timeout=5)
    print(f"Requests status: {r.status_code}")
    return r


def demonstrate_cryptography():
    """Demonstrates cryptography usage (GHSA-79v4-65xg-pq4g)"""
    print("Using cryptography for encryption...")
    # Generate a key (in real usage, this should be stored securely)
    key = Fernet.generate_key()
    f = Fernet(key)
    message = b"Secret message"
    encrypted = f.encrypt(message)
    print(f"Encrypted message: {encrypted[:20]}...")
    return key


def demonstrate_pillow():
    """Demonstrates Pillow usage (CVE-2021-27921)"""
    print("Using Pillow for image processing...")
    # Create a simple test image
    img = Image.new('RGB', (100, 100), color='red')
    print(f"Created image: {img.size}")
    return img


def demonstrate_jinja2():
    """Demonstrates Jinja2 usage (CVE-2020-28493)"""
    print("Using Jinja2 for templating...")
    template = Template("Hello {{ name }}!")
    rendered = template.render(name="World")
    print(f"Rendered template: {rendered}")
    return template


def demonstrate_pyyaml():
    """Demonstrates PyYAML usage (CVE-2020-14343)"""
    print("Using PyYAML for YAML parsing...")
    yaml_data = """
    name: Test Project
    version: 1.0.0
    dependencies:
      - urllib3
      - cryptography
    """
    parsed = yaml.safe_load(yaml_data)
    print(f"Parsed YAML: {parsed['name']}")
    return parsed


def main():
    """Main function to demonstrate all vulnerable dependencies"""
    print("=" * 50)
    print("Vulnerable Dependencies Test Project")
    print("=" * 50)
    print()
    
    try:
        http = demonstrate_urllib3()
        r = demonstrate_requests()
        key = demonstrate_cryptography()
        img = demonstrate_pillow()
        template = demonstrate_jinja2()
        data = demonstrate_pyyaml()
        
        print()
        print("=" * 50)
        print("All demonstrations completed successfully!")
        print("=" * 50)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

