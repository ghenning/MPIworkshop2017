import numpy as np
import optparse

def readthefile(FILE):
    thefile = np.loadtxt(FILE,dtype='string')
    for i in range(len(thefile)):
        print thefile[i]

if __name__=='__main__':
    desc = "Hi, I'm a description"
    parser = optparse.OptionParser(description=desc)
    parser.add_option('--file',dest='thefile',type='string',\
        help="location of file")
    (opts,args) = parser.parse_args()
    readthefile(opts.thefile)

