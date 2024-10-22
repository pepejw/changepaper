#!/usr/bin/python3
import argparse
from glob import glob as ls
from os.path import expanduser as xpuser
from os import system as sh
#cmdline args
parser = argparse.ArgumentParser(
        prog='changepaper',
        description='Change the wallpaper on hyprland')
parser.add_argument('-l', action='store_true')
parser.add_argument('-d', default=xpuser('~/wallpapers'))
parser.add_argument('-f')
args = parser.parse_args()


def main():
    valid = False
    if args.l:
        print("Available wallpapers are:")
        files = ls(args.d+'/*.png')
        for file in files:
            print(file)
    
    if args.f:
        filepath = args.d+'/'+args.f
        files = ls(args.d+'/*.png')
        for file in files:
            if file == filepath:
               valid = True
        if valid == True:
            sh("swww img "+filepath+" --transition-step 10 --transition-type any")
            sh("wal --cols16 -n -q -i "+filepath)
            sh("hyprctl reload")
            sh("pywal-discord -p ~/.var/app/dev.vencord.Vesktop/config/vesktop/themes")
            sh("pywalfox update")
if __name__ == '__main__':
    main()
