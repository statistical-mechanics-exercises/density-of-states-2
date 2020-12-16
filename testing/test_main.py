import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_hamiltonian(self) :
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
                spins[j] = np.floor( num / 2**(4-j) )
                num = num - spins[j]*2**(4-j)
                if spins[j]==0 : spins[j] = -1
            energy = -spins[0]*spins[len(spins) - 1 ]
            for i in range(0,len(spins)-1) : energy = energy - spins[i]*spins[i+1]
            self.assertTrue( np.abs(hamiltonian( spins )-energy)<1e-7, "The hamiltonian has not been implemented correctly" )
            
    def test_graph(self) : 
        counts = 5*[0]
        for i in range(2**8) :
            num, spins = i, 8*[0]
            for j in range(8) :
                spins[j] = np.floor( num / 2**(7-j) )
                num = num - spins[j]*2**(7-j)
                if spins[j]==0 : spins[j] = -1
            binn = int( ( hamiltonian(spins)  + 8 ) / 4 )
            counts[binn] = counts[binn] + 1
  
        fighand=plt.gca()
        for k in range(5) :
           patch = fighand.patches[k]
           self.assertTrue( patch.get_xy()[0] + 0.5*patch.get_width() == (-8+k*4), "The graph is not correct" )
           self.assertTrue( patch.get_height()==counts[k], "The graph is not correct" )
