from nose.tools import *
import numpy as np
import pandas as pd 
from ..pvsystem import physicaliam

def test_proper():
	IAM=physicaliam(.05,.5,.2,pd.DataFrame(range(90)))	
	assert(np.size(IAM)==90)
	

#def test_proper_salar():
	#IAM=pvl_ashraeiam.pvl_ashraeiam(.05,40)	
	#assert(np.size(IAM)==90)


def main():
    unittest.main()

if __name__ == '__main__':
    main()