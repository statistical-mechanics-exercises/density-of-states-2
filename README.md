# The density of states I

What you should have seen in the previous exercise was that a system of 8 Ising spins the energy can only take one of five possible values; namely, -8, -4, 0, 4 and 8.  Rather than plotting the energies of all the states it might therefore be useful to plot the number of microstates that have an energy of -8, the number of microstates that have an energy of -4, the number of microstates that have an energy of 0, the number of microstates that have an energy of 4 and the number of microstates that have an energy of 8 as we are going to learn to do in this exercise.  In other words, what we are going to calculate is a histogram showing the number of microstates that have each of the possible values for the energy.

We are once again going to use the 1D Ising model in the absence of a magnetic field.  The Hamiltonian that you will need to implement in the box on the left here is thus:  

![](https://render.githubusercontent.com/render/math?math=E=-\sum_{i=1}^Ns_is_{i%2B1})

with ![](https://render.githubusercontent.com/render/math?math=N=8) and ![](https://render.githubusercontent.com/render/math?math=s_N%2B1=s_1).

In addition, to writing the code to calculate this Hamiltonian you will, once again, need to write a loop over all the possible microstates.  Within this loop you are going to calculate the energy of each microstate E by using your hamiltonian function.  You will then want to use the list called `number_of_microstates` to record the number of microstates that have each of five the possible energy values in the list called energies.  

Notice that we can express the ith element of `number_of_microstates` as:

![](https://render.githubusercontent.com/render/math?math=N(E_i)=\sum_{j=1}^M\delta(H(\mathbf{x}_j)-E_i)\quad\textrm{where}\quad\delta(0)=1\quad\textrm{and}\quad\delta(x)=0\quad\textrm{if}\quad\x\ne0)

where ![](https://render.githubusercontent.com/render/math?math=E_i) is the ith element of energies.  When the formula for the elements of `number_of_microstates` is written this way it is tempting to think that we need to write 5 if statements that check the value of each energy against the five values in the list called energies. We do not need to do this, however, as the 5 values in energies are evenly spaced.  This fact ensures that there is a formula that maps the values of the energy on to the corresponding index of `number_of_microstates` that we should add one to:

![](https://render.githubusercontent.com/render/math?math=-8\rightarrow\0\qquad-4\rightarrow\1\qquad0\rightarrow\2\qquad4\rightarrow\3\qquad\8\rightarrow\4)

Once you have worked out the formula to use to convert the energies on the left of the arrows above above to the indices on the right you will need to convert the real number that is output to an integer by using the Python command:

````
int_number = int( real_number )
````
