import os
from xml.dom import minidom

from lxml import etree

ITD_DOMAIN = 'ITD_DOMAIN'
P_DOMAIN = 'WHB_PDOMAIN'
sites = ('S', 'U', 'P', 'D')
servers = ('81', '82', '91', '92')


def update(file, domain):
    if not checkout(file):
        return
    print(f'Updating file {file}')
    xml = etree.parse(file)
    root = xml.getroot()
    for folder in root.xpath('//shareFolder'):
        remove(folder, 'Domain Admins')
        remove(folder, 'Administrators')
        if domain == ITD_DOMAIN:
            remove(folder, 'ITDDomain ServiceGrp')
        else:
            remove(folder, 'Pdomain Service Grp')
        remove(folder, 'WAS_Service_Group')
        insert(folder, fr'{domain}\WAS_Service_Group', 'Full')
        if domain == P_DOMAIN:
            remove(folder, 'drwpd161')
            insert(folder, fr'{domain}\drwpd161', 'Full')
    print(beautify(root), file=open(file, 'w+'))


def checkout(file):
    if not os.path.exists(file):
        return False
    if not os.access(file, os.W_OK) and os.system(f'cleartool checkout -nc {file}'):
        print(f'Failed to checkout {file}')
        return False
    else:
        return True


def remove(folder, account):
    for x in folder.xpath(f'permission[contains(@account, "{account}")]'):
        folder.remove(x)


def insert(folder, account, right):
    permission = etree.Element('permission', account=account, right=right)
    folder.insert(0, permission)


def beautify(element):
    for x in element.xpath('//*'):
        x.text = None
        x.tail = None
    dom = minidom.parseString(etree.tostring(element))
    return dom.toprettyxml()


def one_vob(vob_path):
    base_path = f'C:/Development/{vob_path}/was9open/ConfigFile/ConfigFile'
    for site in sites:
        domain = ITD_DOMAIN if site in ('S', 'U') else P_DOMAIN
        for server in servers:
            if site == 'D':
                server_name = f'CWWS9APWH{server}'
            else:
                server_name = f'{site}WWS9APWH{server}'
            file = f'{base_path}/{site}/ShareFolder/share_{server_name}.xml'
            update(file, domain)


def main():
    vob_paths = ('MTX/mt', 'MRX/murex', 'TRS/fxintra', 'IRS/irs', 'ORS/ors', 'SAA/saa')
    for vob_path in vob_paths[0:1]:
        one_vob(vob_path)


if __name__ == '__main__':
    main()
