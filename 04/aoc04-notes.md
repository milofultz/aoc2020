- Load up passports
    - Split data up into passports via '\n\n'
        - Split each passport into fields
            - Replace all newlines with spaces
            - Split these up by space
            - Strip of all leading and trailing spaces
- Test if valid
    - If has all 8 fields
    - If has only 7 fields and doesn't have 'cid' key