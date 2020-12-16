import matplotlib.pyplot as plt 
import numpy as np 

def hamiltonian( spins ) :
  eng = 0
  # Your code to calculate the Hamiltonian goes here
  eng = -spins[0]*spins[-1]
  for i in range(1,len(spins)) : eng = eng - spins[i-1]*spins[i] 
  return eng
  
# Create a list of the posssible values the energy can take
energies = 5*[0]
for i in range(5) : energies[i] = -8+i*4

# Create a list that will hold the number of microstates with each energy 
number_of_microstates = 5*[0]
# Your code to do the loop over all the microstates and to count how many times each 
# of the energy values appear goes here
for index in range(2**8) :
  spins, ind = 8*[0], index
  # Your code to convert the integer index to the corresponding spin coordinates goes here
  for i in range(8) :
      spins[i] = np.floor( index / 2**(7-i) )
      index = index - spins[i]*(2**(7-i))
      if spins[i]==0 : spins[i] = -1
  nbin = int( hamiltonian(spins) / 4 ) + 2 
  number_of_microstates[nbin] = number_of_microstates[nbin] + 1 
  
# This will plot the possible values for the energy against the number of microstates with 
# that particular energy.
plt.bar( energies, number_of_microstates, width=0.1 )
plt.xlabel("energy / J")
plt.ylabel("Number of configurations")
plt.savefig( "density_of_states.png")
