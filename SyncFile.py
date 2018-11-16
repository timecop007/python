from shutil import copy2
import os
import stat

# files = (
#     r'was9open\Setup\setupAll.bat',
#     r'was9open\Setup\setup.bat',
#     r'was9open\Setup\setupFolder.bat',
# )
files = (
    r'was9open\Setup\setupFolder.bat',
)
# bases = (r'C:\Development', r'\\SWWS9APWH81\D$\temp\Ref_67678_irs_ors_fxintra_saa_murex_mt')
bases = (r'C:\Development', )
views = ('MTX', 'IRS', 'ORS', 'TRS', 'MRX', 'SAA')
vobs = ('mt', 'irs', 'ors', 'fxintra', 'murex', 'saa')


def main():
    for file in files:
        for i, base in enumerate(bases):
            for j, vob in enumerate(vobs):
                if i == 0 and j == 0:
                    continue
                folder = vob if i != 0 else fr'{views[j]}\{vob}'
                src = fr'{bases[0]}\{views[0]}\{vobs[0]}\{file}'
                target = fr'{base}\{folder}\{file}'
                print(src, '->', target)
                os.chmod(target, stat.S_IWRITE)
                copy2(src, target)


if __name__ == '__main__':
    main()
