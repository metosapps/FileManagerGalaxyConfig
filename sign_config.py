#!/usr/bin/env python3
"""Sign exactly one app-scoped payload without exposing the private key."""
import argparse
import base64
import json
from pathlib import Path
import subprocess
import tempfile
import time

parser = argparse.ArgumentParser()
parser.add_argument('--payload', type=Path, default=Path(__file__).parent / 'site/payload.json')
parser.add_argument('--key', type=Path, required=True)
parser.add_argument('--output', type=Path, default=Path(__file__).parent / 'site/config.json')
args = parser.parse_args()
payload = json.loads(args.payload.read_text())
assert payload['package_name'] == 'com.filegx.appsmanager'
assert payload['store'] == 'galaxy_store' and payload['schema_version'] == 1
assert payload['revision'] > 0
assert payload['issued_at'] <= time.time() + 300 < payload['expires_at']
assert 0 < payload['expires_at'] - payload['issued_at'] <= 7 * 86400
assert payload['android']['galaxy_store']['update_url'] == 'samsungapps://ProductDetail/com.filegx.appsmanager'
raw = json.dumps(payload, ensure_ascii=False, separators=(',', ':')).encode()
with tempfile.TemporaryDirectory() as folder:
    source = Path(folder) / 'payload'; source.write_bytes(raw)
    signature = subprocess.run(['openssl', 'dgst', '-sha256', '-sign', str(args.key), str(source)], check=True, capture_output=True).stdout
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps({'payload': base64.b64encode(raw).decode(), 'signature': base64.b64encode(signature).decode()}, separators=(',', ':')) + '\n')
print('Signed revision', payload['revision'], 'for', payload['package_name'])
