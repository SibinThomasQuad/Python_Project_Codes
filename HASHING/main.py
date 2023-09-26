import hashlib

input_string = "sibin thomas v3"

# MD5 Hash
md5_hash = hashlib.md5(input_string.encode()).hexdigest()
print(f"MD5 Hash: {md5_hash}")

# SHA-1 Hash
sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()
print(f"SHA-1 Hash: {sha1_hash}")

# SHA-256 Hash
sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
print(f"SHA-256 Hash: {sha256_hash}")

# SHA-384 Hash
sha384_hash = hashlib.sha384(input_string.encode()).hexdigest()
print(f"SHA-384 Hash: {sha384_hash}")

# SHA-512 Hash
sha512_hash = hashlib.sha512(input_string.encode()).hexdigest()
print(f"SHA-512 Hash: {sha512_hash}")

# CRC32 Hash (Using zlib)
import zlib
crc32_checksum = zlib.crc32(input_string.encode())
print(f"CRC32 Checksum: {crc32_checksum}")

# Adler-32 Hash (Using zlib)
adler32_checksum = zlib.adler32(input_string.encode())
print(f"Adler-32 Checksum: {adler32_checksum}")

# Custom DJB2 Hash Function
def djb2_hash(s):
    hash = 5381
    for x in s.encode():
        hash = ((hash << 5) + hash) + x
    return hash & 0xFFFFFFFF  # Ensure 32-bit output

djb2 = djb2_hash(input_string)
print(f"DJB2 Hash: {djb2}")
