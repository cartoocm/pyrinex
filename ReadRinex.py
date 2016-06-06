#!/usr/bin/env python
from matplotlib.pyplot import figure,show
#
from pyrinex.rinex_parser import Rinex

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='example of reading a RINEX 2 Navigation file')
    p.add_argument('rinexfn',help='path to RINEX file')
    p.add_argument('-o','--odir',help='directory in which to write data as HDF5')
    p.add_argument('--maxtimes',help='Choose to read only the first N INTERVALs of OBS file',type=int)
    p.add_argument('--profile',help='profile code for debugging',action='store_true')
    p = p.parse_args()

    Data = Rinex(p.rinexfn)     
    
    
    if rinexfn.lower().endswith('n'):
        nav = readRinexNav(rinexfn,p.odir)
        print(nav.head())
    elif rinexfn.lower().endswith('o'):
        if p.profile:
            import cProfile
            from pstats import Stats
            profFN = 'RinexObsReader.pstats'
            cProfile.run('rinexobs(rinexfn,p.odir,p.maxtimes)',profFN)
            Stats(profFN).sort_stats('time','cumulative').print_stats(20)
        else:
            blocks = rinexobs(rinexfn,p.odir,p.maxtimes)
               
            ax = figure().gca()
            ax.plot(blocks.items,blocks.ix[:,0,'P1'])
            ax.set_xlabel('time [UTC]')
            ax.set_ylabel('P1')
    #%% TEC can be made another column (on the minor_axis) of the blocks Panel.
    else:
        raise ValueError('I dont know what type of file youre trying to read')

    show()
