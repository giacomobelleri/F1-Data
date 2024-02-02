import os
import sys
import os.path as op

# Adds the source folder to the path
project_root = op.abspath(op.join(op.dirname(__file__), os.pardir))
sys.path.append(project_root)

# Imports the src package
import src

# Removes source folder from the path
sys.path.remove(project_root)