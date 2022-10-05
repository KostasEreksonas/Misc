#!/usr/bin/env python3

def sofia_hash(self, var):
    md5 = hashlib.md5(bytes(password, "utf-8")).digest()
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return "".join([chars[sum(x) % 62] for x in zip(md5[::2], md5[1::2])])

sofia_hash(string)
