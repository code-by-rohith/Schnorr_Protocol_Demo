from Crypto.Random import random
p = 112168960152510251143670142156426764066301248406606527220039233295444762385889
g = 3
def generate_keys():
    x = random.randint(1, p-1)  
    h = pow(g, x, p)           
    return x, h
def schnorr_protocol(x, h):
    r = random.randint(1, p-1)
    c = pow(g, r, p)
    e = random.randint(1, p-1)
    s = (r + e*x) % (p-1)
    c_prime = (pow(g, s, p) * pow(h, -e, p)) % p
    return c_prime == c
def main():
    x, h = generate_keys()
    result = schnorr_protocol(x, h)
    if result:
        print("Zero-knowledge proof successful. Prover knows the secret exponent x.")
    else:
        print("Zero-knowledge proof failed. Prover might not know the secret exponent x.")
if __name__ == "__main__":
    main()
