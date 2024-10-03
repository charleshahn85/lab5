def is_valid_part(part):
    if not part.isdigit() or (len(part) > 1 and part[0] == '0'):
        return False
    num = int(part)
    return 0 <= num <= 255

def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    return all(is_valid_part(part) for part in parts)

def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

def binary_to_decimal(b):
    if not b:
        return 0
    return int(b[-1]) + 2 * binary_to_decimal(b[:-1])

def ip_to_binary(ip):
    if not is_valid_ip(ip):
        return "Invalid IP address"
    
    parts = ip.split('.')
    binary_parts = [decimal_to_binary(int(part)).zfill(8) for part in parts]
    return ".".join(binary_parts)

def ip_convert(ip_or_binary):
    if '.' in ip_or_binary:
        # Assume it's an IP address
        if is_valid_ip(ip_or_binary):
            return ip_to_binary(ip_or_binary)
        else:
            return "Invalid IP address"
    else:
        # Assume it's a binary representation
        if len(ip_or_binary) == 32 and all(bit in '01' for bit in ip_or_binary):
            parts = [ip_or_binary[i:i+8] for i in range(0, 32, 8)]
            decimal_parts = [str(binary_to_decimal(part)) for part in parts]
            return ".".join(decimal_parts)
        else:
            return "Invalid binary representation"

print("Testing is_valid_part:")
print(is_valid_part("255"))  
print(is_valid_part("256"))  
print(is_valid_part("01")) 
print(is_valid_part("0"))    

print("\nTesting is_valid_ip:")
print(is_valid_ip("192.168.1.1"))    
print(is_valid_ip("192.168.256.1"))  
print(is_valid_ip("192.168.1"))      
print(is_valid_ip("192.168.01.1"))   

print("\nTesting decimal_to_binary:")
print(decimal_to_binary(10))   
print(decimal_to_binary(255))  
print(decimal_to_binary(1))    

print("\nTesting binary_to_decimal:")
print(binary_to_decimal("1010"))      
print(binary_to_decimal("11111111"))  
print(binary_to_decimal("1"))         

print("\nTesting ip_to_binary:")
print(ip_to_binary("192.168.1.1"))   
print(ip_to_binary("255.255.255.0"))  
print(ip_to_binary("256.1.1.1"))      

print("\nTesting ip_convert:")
print(ip_convert("192.168.1.1"))                          
print(ip_convert("11000000101010000000000100000001"))     
print(ip_convert("256.1.1.1"))                            
print(ip_convert("11111111111111111111111100000000"))    
