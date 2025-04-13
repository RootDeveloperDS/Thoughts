#for all directory where python looks


import sys
print(sys.path)

#______________________________________________________________________

print('\n','\n')

#for a specific module directory

import os
print("for os:::  ",os.__file__)
#eg:-
#using __file__ attribute
print('\n')
import pandas
print("for pandas:::  ",pandas.__file__)
