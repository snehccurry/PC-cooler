import subprocess

def get_power_schemes():
    output = subprocess.check_output(['powercfg', '/L'], universal_newlines=True)
    schemes = []
    lines = output.split('\n')
    for line in lines:
        if "Power Scheme GUID" in line:
            parts = line.split(':',)
            parts = line.split('(')
            guid = parts[0].split(":")[1]
            name = parts[1].strip(')')
            name = parts[1].strip('*')
            name = parts[1].strip(') *')
            schemes.append({'guid': guid, 'name': name})
    return schemes

if __name__ == "__main__":
    power_schemes = get_power_schemes()
    for scheme in power_schemes:
        print("Power Scheme Name:", scheme['name'])
        print("GUID:", scheme['guid'])

    print("***************************")

    #print(power_schemes[0]["name"])
