# File containing directory information as class variables.

# Importing relevant packasges:
import os.path as op

# Class of Directories 
class Directory:
    
    # Parent Directory
    parent = op.dirname(op.dirname(op.dirname(op.abspath(__file__))))
    
    # Subdirectories
    cache = op.join(parent, 'cache') # Cache directory
    data = op.join(parent, 'data')   # Data directory
    src = op.join(parent, 'src')     # Source directory
    cfg = op.join(src, 'cfg')     # Config directory
    fun = op.join(src, 'fun')       # Function directory