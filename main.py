import matplotlib.pyplot as plt 
import numpy as np 

def hamiltonian( spins ) :
  eng = 0
  # Your code to calculate the Hamiltonian goes here
  
  return eng
  
# Create a list of the posssible values the energy can take
energies = 5*[0]
for i in range(5) : energies[i] = -8+i*4

# Create a list that will hold the number of microstates with each energy 
number_of_microstates = 5*[0]
# Your code to do the loop over all the microstates and to count how many times each 
# of the energy values appear goes here

  
# This will plot the possible values for the energy against the number of microstates with 
# that particular energy.
plt.bar( energies, number_of_microstates, width=0.1 )
plt.xlabel("energy / J")
plt.ylabel("Number of configurations")
plt.savefig( "density_of_states.png")
