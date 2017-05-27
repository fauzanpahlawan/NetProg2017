data = "position=Caster&name=Cap&address=USA"
data1 = data.split('&')


def get_data_by_keys(keys, data):
    for i in data:
        if keys in i:
            return i.split('=')[1]

print get_data_by_keys('position', data1)
