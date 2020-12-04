import re

def validate_byr(byr):
    return 1920 <= int(byr) <= 2002

def validate_iyr(iyr):
    return 2010 <= int(iyr) <= 2020

def validate_eyr(eyr):
    return 2020 <= int(eyr) <= 2030

def validate_hgt(hgt):
    match = re.match(r'(\d+)(in|cm)', hgt)

    if not match:
        return False

    value, unit = match.groups()
    value = int(value)

    if unit == 'in':
        valid = 59 <= value <= 76
    elif unit == 'cm':
        valid = 150 <= value <= 193
    else:
        valid = False

    return valid

def validate_hcl(hcl):
    return re.search(r'#[0-9a-f]{6}', hcl)

def validate_ecl(ecl):
    return ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def validate_pid(pid):
    return re.search(r'^\d{9}$', pid)


def is_valid(passport):
    required = {
        'byr': validate_byr,
        'iyr': validate_iyr,
        'eyr': validate_eyr,
        'hgt': validate_hgt,
        'hcl': validate_hcl,
        'ecl': validate_ecl,
        'pid': validate_pid,
    }

    for field, validator in required.items():
        if val := passport.get(field):
            if validator(val):
                continue
        return False

    return True

def solve(docs):
    passports = []

    for doc in docs:
        passports.append({k: v for k, v in map(lambda x: x.split(':'), doc.split())})

    return len(list(filter(is_valid, passports)))

