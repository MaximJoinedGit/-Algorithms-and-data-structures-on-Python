x = 26
mod = 3001

def substr_count(s, l):
    hash = 0
    for i in range(l):
        hash = (hash * x + (ord(s[i]) - 97)) % mod
    pow_l = 1
    for i in range(l - 1):
        pow_l = (pow_l * x) % mod
    result = set()
    result.add(hash)
    for i in range(l, len(s)):
        hash = ((hash - pow_l * (ord(s[i - l]) - 97) + 2 * mod) * x + (ord(s[i]) - 97)) % mod
        result.add(hash)
    print(len(result))

substr_count("hello world!", 1)
substr_count("hello world!", 2)
substr_count("hello world!", 3)
substr_count("hello world!", 4)
substr_count("hello world!", 5)
substr_count("hello world!", 6)
substr_count("hello world!", 7)
substr_count("hello world!", 8)
substr_count("hello world!", 9)
substr_count("hello world!", 10)
substr_count("hello world!", 11)
