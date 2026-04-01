import re
import math

def extract_domain(url):
    return re.sub(r"https?://", "", url).split("/")[0]

def domain_length(domain):
    return len(domain)

def count_digits(domain):
    return sum(c.isdigit() for c in domain)

def entropy(domain):
    prob = [float(domain.count(c)) / len(domain) for c in set(domain)]
    return -sum([p * math.log2(p) for p in prob])
