#!/usr/bin/env python3
"""
deploy_to_pythonanywhere.py
Automated deployment script to push HSK-review to PythonAnywhere via their REST API.
"""

import os
import sys
import argparse
import requests

sys.stdout.reconfigure(encoding='utf-8')

FILES_TO_DEPLOY = [
    'app.py',
    'wsgi.py',
    'requirements.txt',
    'build_master_database.py',
    'data_hsk1.py',
    'data_hsk2.py',
    'data_hsk3_grammar.py',
    'build_full_hsk_database.py',
    'generate_word_variations.py',
    'data/hsk3.db',
    'data/hsk3_database.json',
    'templates/index.html',
    'static/css/style.css',
    'static/js/app.js'
]

def upload_file(host, username, token, local_path, remote_path):
    url = f"https://{host}/api/v0/user/{username}/files/path{remote_path}"
    headers = {"Authorization": f"Token {token}"}
    
    with open(local_path, "rb") as f:
        files = {"content": f}
        res = requests.post(url, headers=headers, files=files)
        
    if res.status_code in (200, 201):
        status_text = "Created" if res.status_code == 201 else "Updated"
        print(f"  ✓ {local_path} -> {remote_path} ({status_text})")
        return True
    else:
        print(f"  ✗ Failed to upload {local_path}: {res.status_code} {res.text}")
        return False

def configure_wsgi(host, username, token, domain):
    wsgi_remote_path = f"/var/www/{domain.replace('.', '_')}_wsgi.py"
    wsgi_content = f"""# PythonAnywhere WSGI configuration for {domain}
import sys
import os

project_home = '/home/{username}/HSK-review'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application
"""
    url = f"https://{host}/api/v0/user/{username}/files/path{wsgi_remote_path}"
    headers = {"Authorization": f"Token {token}"}
    res = requests.post(url, headers=headers, files={"content": wsgi_content.encode('utf-8')})
    if res.status_code in (200, 201):
        print(f"  ✓ Configured WSGI file at {wsgi_remote_path}")
        return True
    else:
        print(f"  ✗ Warning: Could not auto-write WSGI file: {res.status_code} {res.text}")
        return False

def reload_webapp(host, username, token, domain):
    url = f"https://{host}/api/v0/user/{username}/webapps/{domain}/reload/"
    headers = {"Authorization": f"Token {token}"}
    res = requests.post(url, headers=headers)
    if res.status_code == 200:
        print(f"  ✓ Successfully reloaded web application: https://{domain}")
        return True
    else:
        print(f"  ! Note: Could not auto-reload webapp ({res.status_code}): {res.text}")
        print(f"    If you haven't created the Web App yet in your PythonAnywhere dashboard,")
        print(f"    go to the 'Web' tab, create a Web App for {domain}, and click 'Reload'.")
        return False

def main():
    parser = argparse.ArgumentParser(description="Push HSK-review to PythonAnywhere via REST API")
    parser.add_argument("--username", "-u", default=os.environ.get("PA_USERNAME"), help="PythonAnywhere username")
    parser.add_argument("--token", "-t", default=os.environ.get("PA_TOKEN"), help="PythonAnywhere API token")
    parser.add_argument("--host", default=os.environ.get("PA_HOST", "www.pythonanywhere.com"), help="www.pythonanywhere.com or eu.pythonanywhere.com")
    args = parser.parse_args()

    username = args.username
    token = args.token
    host = args.host

    print("=" * 60)
    print("🚀 PythonAnywhere Automated Deployment Tool")
    print("=" * 60)

    if not username:
        try:
            username = input("Enter your PythonAnywhere username: ").strip()
        except EOFError:
            pass

    if not token:
        try:
            token = input("Enter your PythonAnywhere API Token: ").strip()
        except EOFError:
            pass

    if not username or not token:
        print("\n[ERROR] Both PythonAnywhere username and API token are required.")
        print("To get your API token:")
        print("  1. Log in to https://www.pythonanywhere.com")
        print("  2. Go to 'Account' (top right) -> 'API token' tab")
        print("  3. Click 'Create a new API token'")
        print("\nUsage example:")
        print("  python deploy_to_pythonanywhere.py --username your_name --token your_token")
        sys.exit(1)

    domain = f"{username}.pythonanywhere.com"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    remote_base = f"/home/{username}/HSK-review"

    print(f"\nTarget Account: {username} ({host})")
    print(f"Target URL:     https://{domain}")
    print(f"Remote Folder:  {remote_base}\n")

    print("[1/3] Uploading application files...")
    success_count = 0
    for rel_path in FILES_TO_DEPLOY:
        local_path = os.path.join(base_dir, rel_path)
        if not os.path.exists(local_path):
            print(f"  ! Skipping {rel_path} (not found)")
            continue
        remote_path = f"{remote_base}/{rel_path.replace(os.sep, '/')}"
        if upload_file(host, username, token, local_path, remote_path):
            success_count += 1

    print(f"\n[2/3] Setting up WSGI configuration...")
    configure_wsgi(host, username, token, domain)

    print(f"\n[3/3] Reloading web application...")
    reload_webapp(host, username, token, domain)

    print("\n" + "=" * 60)
    print("🎉 DEPLOYMENT FINISHED!")
    print(f"Your HSK 3 Review App is accessible at:")
    print(f"👉 https://{domain}")
    print("=" * 60)
    print("\nNext step on iPhone/iPad:")
    print(f"  1. Open Safari and go to: https://{domain}")
    print("  2. Tap Share -> 'Add to Home Screen'")
    print("  3. Enjoy your 10-15 minute daily HSK 3 review!\n")

if __name__ == "__main__":
    main()
