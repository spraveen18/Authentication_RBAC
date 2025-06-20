import secrets
import base64

# Generate secure random key
key = secrets.token_urlsafe(32)  # 32 bytes, URL-safe
print(f"SECRET_KEY={key}")

# Or base64 encoded
key_bytes = secrets.token_bytes(32)
key_b64 = base64.b64encode(key_bytes).decode()
print(f"JWT_SECRET_KEY={key_b64}")