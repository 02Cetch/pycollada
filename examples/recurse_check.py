import sys
import os, os.path
import traceback
import time
import argparse

try:
    import collada
except:
    sys.exit("Could not find pycollada library.")
        
def main():

    parser = argparse.ArgumentParser(
        description='Recursively scans a directory, loading any .dae file found.')
    parser.add_argument('directory', help='Directory to scan')
    parser.add_argument('--show-time', '-t', default=False, action='store_true',
                        help='Show how much time (in seconds) it took to load file')
    parser.add_argument('--show-warnings', '-w', default=False, action='store_true',
                        help='If warnings present, print warning type')
    parser.add_argument('--show-errors', '-e', default=False, action='store_true',
                        help='If errors present, print error and traceback')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.directory):
        sys.exit("Given path '%s' is not a directory." % args.directory)
    
    directories = [args.directory]
    collada_files = []
    while len(directories) > 0:
        directory = directories.pop()
        for name in os.listdir(directory):
            fullpath = os.path.join(directory,name)
            (root, ext) = os.path.splitext(fullpath)
            if os.path.isfile(fullpath) and ext.lower() == ".dae":
                collada_files.append(fullpath)
            elif os.path.isdir(fullpath):
                directories.append(fullpath)
    
    collada_files.sort()
    
    for c in collada_files:
        (root, leaf) = os.path.split(c)
        print "'%s'..." % leaf,
        sys.stdout.flush()
     
        start_time = time.time()
     
        try:
            col = collada.Collada(c, \
                ignore=[collada.DaeUnsupportedError, collada.DaeBrokenRefError])
            
            if col.scene is None:
                col.errors.append(collada.DaeIncompleteError("No scene node"))
            
            if len(col.errors) > 0:
                print "WARNINGS:", len(col.errors)
                err_names = [type(e).__name__ for e in col.errors]
                unique = set(err_names)
                type_cts = [(e, err_names.count(e)) for e in unique]
                if args.show_warnings:
                    for e, ct in type_cts:
                        print "   %s: %d" % (e, ct)
            else:
                print "SUCCESS"
                
            #do some sanity checks looping through result
            if not col.scene is None:
                for geom in col.scene.objects('geometry'):
                    for prim in geom.primitives():
                        assert(len(prim))
                for cam in col.scene.objects('camera'):
                    assert(cam.original.id)
                    assert(len(cam.position) == 3)
        except (KeyboardInterrupt, SystemExit):
            print
            sys.exit("Keyboard interrupt. Exiting.")
        except:
            print "ERROR"
            if args.show_errors:
                print
                traceback.print_exc()
                print
            
        end_time = time.time()
        if args.show_time:
            print "   Loaded in %.3f seconds" % (end_time-start_time)

if __name__ == "__main__":
    main()
