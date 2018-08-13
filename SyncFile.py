from shutil import copy2

files = (
    r'was9open\Setup\setupAll.bat',
    r'was9open\Setup\setup.bat',
    r'was9open\Setup\setupFolder.bat',
)
bases = (r'C:\Development', r'\\SWWS9APWH81\D$\temp\Ref_55559_mt_murex_fxintra_irs_ors_saa')
views = ('MTX', 'IRS', 'ORS', 'TRS', 'MRX', 'SAA')
vobs = ('mt', 'irs', 'ors', 'fxintra', 'murex', 'saa')

for file in files:
    for i, base in enumerate(bases):
        for j, vob in enumerate(vobs):
            if i == 0 and j == 0:
                continue
            folder = vob if i != 0 else r'%s\%s' % (views[j], vob)
            src = r'%s\%s\%s\%s' % (bases[0], views[0], vobs[0], file)
            target = r'%s\%s\%s' % (base, folder, file)
            print(src, '->', target)
            copy2(src, target)
