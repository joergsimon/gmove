#!/usr/bin/env python

# taken from http://www.jperla.com/blog/post/a-clean-python-shell-script

import os
import re
import subprocess
import logging
import optparse

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

def main():
    usage = "usage: %prog [options]"
    parser = optparse.OptionParser(usage)
    parser.add_option("-t", "--tag",
                    action="store", 
                    type="string", 
                    dest="tag",
                    help="the tag to change to")
    parser.add_option("-k", "--keep-old-stash", dest="keepoldstash",
                    action="store_true",
                    default=False,
                    help="keeps your old stash intact")
    parser.add_option("-j", "--just-stash", dest="juststash",
                    action="store_true",
                    default=False,
                    help="stash, but do not undo anything")
    parser.add_option("-c", "--clear-stash", dest="clearstash",
                    action="store_true",
                    default=True,
                    help="clears the complete stash after command")
    
    options, args = parser.parse_args()
    
    if not options.tag:
      parser.error('you have to enter a tag to go to, try -t tagname')
      
    
    output,_ = call_command('git stash')
    output,_ = call_command('git checkout '+ options.tag)
    if options.clearstash:
      output,_ = call_command('git stash clear')
    elif options.keepoldstash:
      output,_ = call_command('git stash drop')

def call_command(command):
    process = subprocess.Popen(command.split(' '),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    return process.communicate()

if __name__ == "__main__":
    main()
