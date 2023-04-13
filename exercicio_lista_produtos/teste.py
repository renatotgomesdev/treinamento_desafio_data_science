import os

if 'MSYSTEM' in os.environ:
    print('Executando no Git Bash')
else:
    print('Executando no CMD do Windows')
