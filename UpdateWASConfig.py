import fileinput
import os
import stat
from copy import deepcopy
from pathlib import Path

from lxml import etree


def convert(file, org, new, file_type):
    if not Path(file).exists():
        return
    print(f'Converting file {file}')
    os.chmod(file, stat.S_IWRITE)
    for line in fileinput.input((file,), inplace=True):
        line = line.replace(org, new)
        if file_type == 'S' and line.find('log') >= 0:
            line = line.replace('w:', 'l:')
        print(line, end='')
    new_file = file.replace(org, new)
    os.rename(file, new_file)
    if file_type == 'A':
        update(new_file)


def update(new_file):
    print(f'Updating file {new_file}')
    xml = etree.parse(new_file)
    root = xml.getroot()
    root.extend(map(log_only, (deepcopy(x) for x in root.xpath('folder[contains(@name, "applications")]'))))
    print(etree.tostring(root, encoding='unicode', pretty_print=True), file=open(new_file, 'w+'))


def log_only(folder):
    for x in folder.xpath('folder[@name!="log"]'):
        folder.remove(x)
    folder.set('name', folder.get('name').replace('W$', 'L$'))
    folder.set('name', folder.get('name').replace('w$', 'L$'))
    return folder


def one_vob(vob_path):
    base_path = f'C:/Development/{vob_path}/was9open/ConfigFile/ConfigFile'
    sites = (('ITD', 'S'), ('UAT', 'U'), ('DRS', 'P'), ('PRD', 'D'))
    servers = (('71A', '81'), ('71B', '82'), ('72A', '91'), ('72B', '92'))
    for site in sites:
        if site[0] == 'ITD':
            org_path = f'{base_path}/SIT'
        else:
            org_path = f'{base_path}/{site[0]}'
        new_path = f'{base_path}/{site[1]}'
        for server in servers:
            org_server = f'{site[0]}1WAS{server[0]}'
            if site[1] == 'D':
                new_server = f'CWWS9APWH{server[1]}'
            else:
                new_server = f'{site[1]}WWS9APWH{server[1]}'
            file_name = f'{org_path}/ACL/acl_{org_server}.xml'
            convert(file_name, org_server, new_server, 'A')
            file_name = f'{org_path}/ShareFolder/share_{org_server}.xml'
            convert(file_name, org_server, new_server, 'S')
        if Path(org_path).exists():
            os.rename(org_path, new_path)


def main():
    vob_paths = ('MTX/mt', 'MRX/murex', 'TRS/fxintra', 'IRS/irs', 'ORS/ors', 'SAA/saa')
    for vob_path in vob_paths[0:1]:
        one_vob(vob_path)


if __name__ == '__main__':
    main()
