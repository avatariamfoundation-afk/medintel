"""
Secure data handler for biosync encryption/decryption.
Uses Fernet (AES-128) for encryption and HMAC for data authentication.
Enhanced for production security and integration with AI scripts.
"""

import os
import logging
import hmac
import hashlib
from cryptography.fernet import Fernet, InvalidToken
from typing import Dict, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants (load from environment for security)
ENCRYPTION_KEY_ENV = "ENCRYPTION_KEY"
HMAC_SECRET_ENV = "HMAC_SECRET"

def get_encryption_key() -> bytes:
    """
    Retrieve the encryption key from environment variables.
    Raises ValueError if key is not set to prevent accidental key generation.
    """
    key = os.getenv(ENCRYPTION_KEY_ENV)
    if not key:
        raise ValueError(
            f"{ENCRYPTION_KEY_ENV} not set. "
            "Generate a key with Fernet.generate_key(), store it securely, "
            "and set it in your environment variables."
        )
    return key.encode()  # Fernet expects bytes

def get_hmac_secret() -> bytes:
    """
    Retrieve the HMAC secret from environment variables.
    Raises ValueError if not set for security.
    """
    secret = os.getenv(HMAC_SECRET_ENV)
    if not secret:
        raise ValueError(
            f"{HMAC_SECRET_ENV} not set. "
            "Generate a secure secret (e.g., os.urandom(32)), store it securely, "
            "and set it in your environment variables."
        )
    return secret.encode()

def encrypt_data(data: bytes) -> Dict[str, bytes]:
    """
    Encrypt biosync data with Fernet and generate HMAC signature.

    Args:
        data: Raw biosync data to encrypt

    Returns:
        Dictionary containing:
        - 'encrypted': Fernet-encrypted data
        - 'signature': HMAC signature for authentication

    Raises:
        ValueError: If input data is empty
    """
    if not data:
        raise ValueError("Cannot encrypt empty data")

    key = get_encryption_key()
    cipher = Fernet(key)

    encrypted = cipher.encrypt(data)
    secret = get_hmac_secret()
    signature = hmac.new(secret, encrypted, hashlib.sha256).digest()

    return {
        "encrypted": encrypted,
        "signature": signature
    }

def decrypt_data(encrypted_data: Dict[str, bytes]) -> bytes:
    """
    Decrypt and verify biosync data.

    Args:
        encrypted_data: Dictionary containing:
            - 'encrypted': Fernet-encrypted data
            - 'signature': HMAC signature

    Returns:
        Decrypted biosync data

    Raises:
        ValueError: If signature is invalid or decryption fails
    """
    # Verify HMAC signature first
    secret = get_hmac_secret()
    expected_signature = hmac.new(
        secret,
        encrypted_data["encrypted"],
        hashlib.sha256
    ).digest()

    if not hmac.compare_digest(expected_signature, encrypted_data["signature"]):
        raise ValueError("Invalid signature: Data may be corrupted or tampered with")

    # Decrypt data
    try:
        key = get_encryption_key()
        cipher = Fernet(key)
        return cipher.decrypt(encrypted_data["encrypted"])
    except InvalidToken as e:
        raise ValueError("Decryption failed: Invalid or corrupted data") from e

def generate_new_key() -> bytes:
    """
    Generate a new Fernet key for encryption.
    Use this once to create your initial key, then store it securely.
    """
    return Fernet.generate_key()

def generate_hmac_secret() -> bytes:
    """
    Generate a new HMAC secret.
    Use this once to create your initial secret, then store it securely.
    """
    return os.urandom(32)  # 256-bit secret

if __name__ == "__main__":
    # Example usage (for testing only - not production safe)
    logger.info("This example is for testing only. Do not use in production.")

    # Generate and display new keys (only for initial setup)
    print("Sample key generation (run once and store securely):")
    print(f"Fernet Key: {generate_new_key().decode()}")
    print(f"HMAC Secret: {generate_hmac_secret().hex()}")
    print("\nSet these in your environment variables as ENCRYPTION_KEY and HMAC_SECRET\n")

    # Test with sample data
    try:
        sample_data = b"biosync_signal: [1.2, 3.4, 5.6]"

        # Set test keys (in real usage, this would come from environment)
        os.environ[ENCRYPTION_KEY_ENV] = Fernet.generate_key().decode()
        os.environ[HMAC_SECRET_ENV] = generate_hmac_secret().hex()

        encrypted = encrypt_data(sample_data)
        decrypted = decrypt_data(encrypted)

        logger.info(f"Original: {sample_data}")
        logger.info(f"Encrypted: {encrypted['encrypted']}")
        logger.info(f"Decrypted: {decrypted}")
        assert decrypted == sample_data

        logger.info("Encryption/decryption test successful!")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
