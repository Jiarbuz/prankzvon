from flask import request, abort

CLOUDFLARE_IPS = [
    "173.245.48.0/20", "103.21.244.0/22", "103.22.200.0/22", "103.31.4.0/22",
    "141.101.64.0/18", "108.162.192.0/18", "190.93.240.0/20", "188.114.96.0/20",
    "197.234.240.0/22", "198.41.128.0/17", "162.158.0.0/15", "104.16.0.0/13",
    "104.24.0.0/14", "172.64.0.0/13", "131.0.72.0/22"
]

import ipaddress

def is_ip_in_cloudflare(ip):
    try:
        ip_addr = ipaddress.ip_address(ip)
        for net in CLOUDFLARE_IPS:
            if ip_addr in ipaddress.ip_network(net):
                return True
    except Exception:
        pass
    return False

def cloudflare_protect(app):
    @app.before_request
    def block_if_not_cloudflare():
        # Берём IP из заголовка от Cloudflare
        ip = request.headers.get('CF-Connecting-IP', request.remote_addr)
        if not is_ip_in_cloudflare(request.remote_addr):
            abort(403, "Access Denied — Use Cloudflare only.")
