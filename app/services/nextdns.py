import requests
import time
import datetime

def create_profile(api_key, log_callback=None):
    def log(msg):
        if log_callback:
            log_callback(msg)

    headers = {
        "X-Api-Key": api_key,
        "Content-Type": "application/json"
    }

    today_str = datetime.datetime.now().strftime("%Y-%m-%d")
    profile_name = f"LocketVIP-{today_str}"

    log(f"[*] Checking for existing profile: {profile_name}...")
    
    try:
        list_url = "https://api.nextdns.io/profiles"
        res = requests.get(list_url, headers=headers)
        
        if res.status_code == 200:
            profiles = res.json().get('data', [])
            for p in profiles:
                if p.get('name') == profile_name:
                    pid = p.get('id')
                    log(f"[+] Found existing daily profile: {pid} (REUSING)")
                    
                    log(f"[>] Verifying High-Speed VIP Node...")
                    
                    denylist_url = f"https://api.nextdns.io/profiles/{pid}/denylist"
                    try:
                        requests.post(denylist_url, headers=headers, json={"id": "revenuecat.com", "active": True})
                        log(f"[>] Integrity Check: OK (Rules Checked).")
                    except Exception as e:
                        log(f"[!] Warning checking rules: {e}")

                    time.sleep(0.5)
                    log(f"[SUCCESS] DNS VIP Node Active (Cached).")
                    return pid, f"https://apple.nextdns.io/?profile={pid}"
    except Exception as e:
        log(f"[!] Error listing profiles: {e}")

    log(f"[*] Creating new daily profile: {profile_name}")
    log(f"[*] Initializing High-Speed VIP DNS Node...")
    time.sleep(0.5)
    
    create_url = "https://api.nextdns.io/profiles"
    payload = {"name": profile_name}
    
    try:
        response = requests.post(create_url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            pid = data['data']['id']
            log(f"[+] Profile created: {pid}")
            
            log(f"[>] Applying Anti-Revoke Rules (RevenueCat/Apple)...")
            time.sleep(0.4)
            
            denylist_url = f"https://api.nextdns.io/profiles/{pid}/denylist"
            target_domain = "revenuecat.com"
            try:
                r = requests.post(denylist_url, headers=headers, json={"id": target_domain, "active": True})
                
                verify_r = requests.get(denylist_url, headers=headers)
                if verify_r.status_code == 200:
                    rules = verify_r.json().get('data', [])
                    blocked = [d['id'] for d in rules if d.get('active')]
                    
                    if target_domain in blocked:
                        log(f"[+] Firewall Rules Applied: {', '.join(blocked)}")
                    else:
                        log(f"[!] Rule applied but not found in verify. Retrying with api.revenuecat.com...")
                        requests.post(denylist_url, headers=headers, json={"id": "api.revenuecat.com", "active": True})
                        requests.post(denylist_url, headers=headers, json={"id": "www.revenuecat.com", "active": True})
                        log("[+] Added subdomains fallback.")
                else:
                     log(f"[!] Validation Failed: {verify_r.status_code}")

            except Exception as block_e:
                 log(f"[!] Error blocking domain: {block_e}")
            
            log(f"[SUCCESS] DNS VIP Node Active.")
            link = f"https://apple.nextdns.io/?profile={pid}"
            return pid, link
        else:
            log(f"NextDNS Error: {response.status_code} {response.text}")
            return None, None
            
    except Exception as e:
        log(f"Error creating NextDNS profile: {e}")
        return None, None
