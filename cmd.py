import argparse
from pathlib import Path
import datetime
import stat

def convert_mode(mode):
    ret=""
    m=['r', 'w', 'x', 'r', 'w', 'x', 'r', 'w', 'x']
    modestr=bin(mode)[-9:]
    for i,c in enumerate(modestr):
        if c=='1':
            ret+=m[i]
        else:
            ret+='-'
    return ret
            
def convert_type(file:Path):
    ret=''
    if file.is_symlink:
        ret='l'
    elif file.is_socket:
        ret='s'
    else:
        ret='-'
    return ret


def showdir(path='.',all=False,detail=False,human=False):
    p=Path(path)
    for file in p.iterdir():
        if not all and str(file.name).startswith('.'):
            continue
        if detail:
            st=file.stat()
            yield stat.filemode(st.st_mode),st.st_nlink,st.st_uid,st.st_gid,st.st_size,st.st_size,datetime.datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S'),file.name
        else:
            yield file.name

parser = argparse.ArgumentParser(prog='ls',add_help=False,description = 'this is a description')
parser.add_argument('path',nargs='?',default='.',help='path help')
parser.add_argument('-l',action='store_true')
parser.add_argument('-h',action='store_true')
parser.add_argument('-a','--all',action='store_true')

if __name__=='__main__':
    args=parser.parse_args(("D:/test",'-l'))
    parser.print_help()
    print('args={}'.format(args))
    print(args.path,args.all,args.l,args.h)
    for st in list(showdir(args.path,args.all,args.l,args.h)):
        print(st)


