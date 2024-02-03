import os.path as op

# Class of Directories 
class Directory:
    
    # Parent Directory
    parent = op.dirname(op.dirname(op.dirname(op.abspath(__file__))))
    
    # Subdirectories
    cache = op.join(parent, 'cache') # Cache directory
    data = op.join(parent, 'data')   # Data directory
    src = op.join(parent, 'src')     # Source directory
    cfg = op.join(src, 'cfg')        # Config directory
    fun = op.join(src, 'fun')        # Function directory
    
    if __name__ == '__main__':
        print(f"Parent directory: {parent}")
        print(f"Cache directory: {cache}")
        print(f"Data directory: {data}")
        print(f"Source directory: {src}")
        print(f"Config directory: {cfg}")
        print(f"Function directory: {fun} \n")