dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan')
]

country_codes = {country: code for code, country in dial_codes}
print(country_codes)