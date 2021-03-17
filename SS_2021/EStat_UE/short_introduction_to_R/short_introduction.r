

# The materials are protected by copyright and are only provided for 
#personal use for studies at TU Vienna. Further use is not permitted. 
#In particular, it is not permitted to distribute the materials or make 
#them publicly available (e.g. in social networks, on learning platforms, etc.).

# Authors: Michael Messer and Tijana Levajkovic 

#
##
###  Short introduction to R 
###  for comments please contact tijana.levajkovic@tuwien.ac.at
##
#



# What is R?


# R is a statistic package, a programming language, it is 
# free of charge and free software,
# it runs on various OS, is highly individually applicable etc.


# Unfortunately it is a little uncomfortable in the beginning 


# You'll find help in  

help.start()         

# or in www, during problem solving sessions, in the library 
# (e.g."Using R for Introductory Statistics" by John Verzani, 
# or more advanced Angewandte Statistik - Methodensammlung mit R 
# by Sachs und Hedderich)


# Very useful is ?command. This gives you an overview of "command", e.g.


?sort            
?qnorm          # But you need to know the commands.
?t.test

# An overview of important commands is given in   
# http://cran.r-project.org/doc/contrib/Short-refcard.pdf



#
##
###  Preliminaries
##
#



# Typically, working with R is done in two steps.


# 1.You write the R code 
# (i.e., the stuff you want to calculate/test/simulate) 
# with a text editor. 


# 2. The code is delivered to the R console (e.g. via copy and paste)
# and executed.
# This is the actual computation.

   
# As in Latex you can work with an external editor. 

# General:            R-Studio     http://www.rstudio.com

# Windows:        		Tinn-R       http://www.sciviews.org/Tinn-R/

# Mac/Linux/Unix:    	GNU Emacs    http://www.gnu.org/software/emacs/
#                 		XEmacs       http://www.xemacs.org/


# In order to read in data, and to properly save your work you need to set a 
# working directory. 
# For example, this could be the folder short_introduction_to_R

# Setting the working directory


# 1. In RStudio via task bar:


# Session -> Set Working Directory -> Choose Directory -> path->to->folder  



# 2. Via console 


# Windows: 
# setwd("C:/path/to/folder/short_introduction_to_R")     

# Mac, Linux, Unix: 
# setwd("/path/to/folder/short_introduction_to_R")


setwd("~/Desktop/short_introduction_to_R")


# setwd = set working directory. Confirmation with


getwd() # = get working directory





# Importance of the working directory: (syntax is discussed lateron)


hist(rnorm(100)) # creates a histogram


dev.print(device=pdf,file="histogram.pdf") # saves the histogram


# more precisely: In your working directory (!!!)
					# the file histogram.pdf is created.





#
##
###  Working with R
##
#




##
## Simple calculation: "+" "-" "*" "/" "^"
##



3 +       5   # R ignores spacing, 5+5 equals 5   +     5


2 ^ 3


4 / 7         # Division by "/" (not ":")


4 * 2 + 3     


4 * (2 + 3)   # R accounts for brackets


3.3 * 2       # Attention, the decimal marker is a point (not comma)


3 / 0         # that's the way it is ;-)... 
				# (Inf is interpreted as a number, i.e., R can calculate with it.)

Inf - 3


Inf - Inf     # NaN = not a number (undefined value)


# 3 + 5       # comments via #-sign, not executed in console  



##
## Logical relational operators:  "==", "<", "<=", ">", ">=", "!="
##



5 == 4        # "==" equals, logical values are either "TRUE" or "FALSE" 


5 >= 4        # ">=" larger or equals, analogously: ">", "<", "<="


5 != 4        # "!=" not equals



##
## Data types: "numeric", "character", "logical" etc.
##



# R differentiates from several data types. Whereas

# numeric    <-> set of real numbers

# character  <-> character strings (always in quotation marks)

# logical    <-> logical values (TRUE, FALSE, NA)


# You can verify your data type with the command is.data_type(date), e.g.


is.numeric(pi)


is.character("hello")

is.character(3^7)





##
## Data classes: "vector", "matrix", "list", "data.frame" etc.
##



# In order to properly create and file data, there are different 
	# data classes available.


# The data classes "vector" and "matrix" are easily created, but exhibit 
# the disadvantage that only data of the same data type is valid entry. 


# "data.frame" (and "list") are generalizations of the 
	# former ones



##
## Vectors
##



# R thinks in vectors!!! -> Vectors are the most extensive data class!!!

# A vector is a finite "sequence" of data of the same! type.

# A vector is constructed by the command "c(entry1,entry2,..)" .


c(1,2,4)


c("eins", "zwei", "drei")


c("eins", 2, TRUE)          # Attention: Transformation of the entries to the same type


vek <- c(1,2,-3,4,2)        # "<-" is the assignment arrow
                            # i.e. the vector c(1,2,..) is assign to the variable
                            # vek.
                            
                            # An assignment remains valid as long as it is not overwritten
                            # or removed. (rm(vek))
                            
vek                         # accesses the vector


Vek                         # case sensitivity 


# specific sequnces of numbers can be created via the colon operator ":", the 
# commands seq() and rep().

1:10                        # 1,2,...,10


5:-4                        # 5,4,...,-4


seq(1,10,0.32)              # syntax: seq(from, to, increment,...)


seq(10,1,-1)                # increment is negative


rep(3.4,5)                  # syntax: rep(object, quantity,...)



# !!!!Those were all vectors!!!!



2 * c(1,2,3)              # Scalar multiplication by components


c(1,3,5) + c(5,3,1)       # Addition by components
                  
                          # Addition only for vectors whose lengths are multiples
                              # of themselves.
              
                          # The shorter vector is "reproduced" until it has the 
                              # same length as the longer one.   
              
                              
c(1,2,3,4) +  0:1      		# = c(1,2,3,4) + c(0,1,0,1)


c(1,4,6) < 3              # Logical comparisons refer to all components.
                              







##
## Matrices
##



# Syntax: matrix(data , number of rows, number of columns,...)
# Whereas data should be a vector of length (no of rows * no of columns), e.g.


matrix(1:12,3,4)


vek <- c(TRUE,TRUE,FALSE,FALSE)


matrix(vek,2,2)                   # by default the matrix is filled by columns.


matrix(vek,2,2,byrow=TRUE)        # filling by row with the entry "byrow=TRUE"


mat <- diag(5)							      # identity matrix of dimension 5 


mat


##
## Access to subsets of vectors and matrices. 
##


# Access to subsets with square brackets [ ]
# Access often with the help of logical operators 
# "&" (AND), "|" (OR), "!" (negation)
# as well as with comparison operators


# For vectors


vek <- c(2:-2,rep(3,4))


vek


vek[4]           # grips the the fourth element.


vek[3:5]         # elements 3,4 und 5. The output is also a vector!!!


vek[-c(2,5,8)]   # "-" means "without". All elements without the second,
							# fifth and eighth. 

vek[vek < 2 & vek >= 0]   # All elements that are smaller < 2 and >= 0.


vek[vek > 2 | vek <= 0]   # All elements that are either > 2 or <= 0.


vek[!(vek < 2)] == vek[vek >= 2]  # All elements that are not <2, are >=2



# For matrices

# Syntax for submatrices
# matrix(...)[vector of referring rows, vector of referring columns]

mat <- matrix(1:20,4,5,byrow=TRUE)


mat


mat[2,4]              # Entry of row 2 and column 4.


mat[c(2,4),c(2,3,5)]  # Submatrix, of rows 2 and 4 and columns 2, 3 and 5


mat[c(2,3),]          # Submatrix of 2nd and 3rd row with all columns.


mat[-2,c(3,4)]        # Submatrix of all but the 2nd row and column 3 and 4



# Syntax for the choice of a subset of arbitrary elements:
# matrix(...)[selection stated by logical operation]


mat[mat > 10 & mat < 18] # output as vector!


# Analog to the data type, we can verify 
# the data class ( is.data_class(data) )


is.matrix(mat)


is.vector(mat[mat > 10 & mat < 18]) 



# Keep in mind: [ ]-brackets -> subset selection



##
## Commands
##


# Syntax: command(vector,...) 
# The output is a vector as well!!


sqrt(c(2,4))              # square root


abs(-5)                   # absolute value


exp(1:10)                 # exponential function


log(seq(1,2,0.1))         # natural logarithm, general: log(value,base)


vek <- c(seq(3,10,0.7),10:3)


vek


length(vek)               # length of the vector


min(vek)                  # least component, analog "max()"


sum(vek)                  # sum of components


sort(vek)                 # puts the elements in increasing order.


sort(vek, decreasing=TRUE) # order decreasing


mean(vek)                 # mean value of the components


var(vek)                  # (empirical) variance of the components
							# scaling with (n-1)

sd(vek)                   # (empirical) standard deviation of the components
							# scaling with (n-1)

sample(1:49, 6)           # The weekly lottery results. Uniformely choose
							# 6 elements from the set 1,2,...,49 (without 
							# replacement)

sample(c(0,1), 10, replace=TRUE, prob=c(0.2,0.8))

                          # choose 10 ten times an elment from {0,1}
                            # (with replacement ;-))
                            # whereas 0 is weighted with 0,2 and 1 with 0,8.



# Keep in mind: 
# [ ]-brackets -> subset selection
# ( )-brackets -> commands



##
## Distributions
##


# Besides the sample command, all common distributions are available.

# Example: Normal distribution, 
	# consider the normal distribution with mean=2
	# and standard deviation sd=3 (!not the variance!), for short N(2,3)


# iid Sample
rnorm(20,2,3)  # generates a sample of 20 independent normally distributed radom 
				# variables with parameter mean=2 and sd=3
				
				# Syntax: rnorm(sample size, mean, sd, ...)				
				# The r accounts for random


# Density
dnorm(4,2,3)   #value of the density at position 4, of the N(2,3) distribution
				
				# Syntax: dnorm(position, mean, sd, ...)				
				# The d accounts for density 



# CDF (cumulative distribution function):
pnorm(4,2,3)   	# Value of the cdf of N(2,3) distribution at position 4				
				# Syntax: pnorm(position, mean, sd, ...)	
			
			
# Quantile function:
qnorm(0.5,2,3) # Value of the qunatile function of the N(2,3) distr. at probability p = 0.5  				
				 # Syntax: qnorm(probability, mean, sd)
				
				 # q accounts for quantile


# Other distributions obey the same syntax:


# Exponential distribution. Only one parameter: rate (or lambda), here rate = 1


rexp(10,1)    # sample of size 10	 


dexp(2,1)		  # density at position 2


pexp(2,1)		  # cdf at position 2


qexp(0.25,1)	# quantile function at position 0.25


# Other distributions analogously, e.g.

rpois(5,2)  	 # sample of size 5 of the Poisson distr. with parameter lambda = 2 


rgamma(10,2,4)		# sample of size 10 of the gamma distr. with paramter shape = 2 
						# and rate = 4

rbinom(7,10,0.3)	# sample of size 7 of the binomial distr. with parameter n = 10 
						# and p = 0.3
						


# For all distributions you'll find the commands ddistr., pdistr. and qdistr.  


# The entries may be vector valued:


rnorm(10,1:10,seq(1,0.1,-0.1))


dnorm(1:20,1,1)








##
## Graphics
##


# R differentiates between "Highlevel-" and "Lowlevel-" graphics. Highlevelgraphics are own 
# "pictures". Lowlevelgraphics are additional elements that customize the former ones. 


##
## Highlevel graphics: "hist()", "plot()"  etc.
##


# The histogram


bell <- rnorm(1000,1,1)         # sample of 1000 N(1,1) random variables.


hist(bell)                      # Creates a histogram. Syntax: hist(vector,...)


?hist


hist(bell,breaks=seq(-3,5,0.5)) # "breaks" sets the breakpoints between the 
									# histogram cells
									

# Optical changes of the histogram via graphical parameters.


hist(bell,breaks=seq(-3,5,0.5),
			col="green",
			main="Is this bell shaped?",
			col.main="blue",
			cex.main=2,
        	xlab="Value of the random variable",
        	ylab="This is the frequency in the cell",
        	cex.lab=0.8,
        	col.lab="red",
        	cex.axis=2,
        	col.axis="purple",
        	xlim=c(-3,10),
        	ylim=c(0,300) 
      )



# main       ->    sets the title     (names are character strings -> quotation marks)


# col        ->    colors the histogram (colors always in quotation marks)


# col.main   ->    colors the title.  Analog:   col.lab  -> color of axeslabel

                                            	# col.axis -> color of axesannotations

# cex.main   ->    stes the size of the title. Analog:   cex.lab -> size of the axeslabel
                                            # cex.axis -> size of the axesannptations

# xlab       ->    sets the names of the x-axis (x-axislabel)  Analog: ylab


# xlim       ->    sets the limits of the x-axis. (entry is vector of the the left and right
					# boundary)        #analog: ylim




# Remark: Many graphical parameters may be defined globally, that means "outside" the
			# graphics command. Therefore you use the command par(...).



# Example			


hist(bell)			


par(cex.axis=2) 		# globally doubles the size of the labels.


hist(bell)			    # sizes of the labels in the next graphic appear doubled.


hist(rpois(200,5))	# -> labels still doubled.	 


#-> close graphical window -> parameters set to default. 
dev.off()


hist(bell) 			# -> labels back to normal. 


?par



# The plot function:


plot(c(1,2),c(5,0))   # Syntax: plot(vector of x-coordinates, vector of y-coordinates,...),
                      # demands vectors of the same length!!!


plot(c(1,2),c(5,0),type="l")	# "types" are for example. 
								# "p" - points, "l" - lines, "b" - both, etc.


x <- seq(0,2,0.01)


y <- exp(x)


plot(x,y, type="l", main="exp-function", col="red")  
								# visual graphical improvement is possible (same commands)







##
## Lowlevel Graphics: "lines", "points", "text" and much more
##


data <- rnorm(1000)


hist(data,prob=TRUE,main="sample of 1000 standard normal distributed rv",xlab="values",ylab="density")

                       	# Histogram of relative (prob=TRUE -> Total area of thge bars becomes 1)
                       	# frequencies of a sample of 1000 independent standardnormal distributed rv. 

x <- seq(-10,10,0.01)  	# sequence of  x-values


y <- dnorm(x) 			    # creates the values of the density. 


lines(x,y,col="red")    # Syntax: lines(vector of x-values, vector of y-values,...)
                        
                        # Although the x-values lie between -10 and 10, the graphic 
                        # is not fitted. 
                        
                        # This would have been done in the corresponding 
                        # highlevel graphic (histogram).
                             

text(-2,0.3,"green arrow",col="blue",pos=2)

                      	 # Syntax: text(x-coord, y-coord, "text",...)
                         
                         # "pos" determines the position in relation to the 
                         # specified coordinates:
                         # without indication -> centered, 1 -> below, 2 -> left, 
                         # 3 -> above, 4 -> right 
 
arrows(-2,0.32,-1,0.35,col="green", lwd=2)

                         # Syntax: arrows(x0,y0,x1,y1,...)
                         # whereas (x0,y0) are the coord. of the arrowending
                         # and (x1,y1) the coord of the arrowhead. 
                         
                         # Graphicparameter "lwd" -> linewidth 
                         # i.e. thickness of the arrow






##
## Saving graphics and data
##


dev.print(dev=pdf, file="histogram.pdf")

                      # Saves the created histogram in the working 
                      # directory in the file histogram.pdf
                              
                      # The graphic window must be opened while saving. 
                             
                      # Syntax: 
                      # dev.print(dev=pdf, file="name_of_the_picture.pdf",...)
                              
                      # Instead of pdf you can for example also choose postscript.                      
                     
                      # Attention: If there exists a file of the same name 
                      # in the working directory, this is will be overwritten!!


mat <- matrix(rep(4,6),2,3)
 

save(mat, file="matrix_mat.RData")

					# Saves the matrix "mat" in "matrix_mat.RData" 
					# in the working directory.
                    
                    # Syntax: save(date, file="name_of_file.RData",...)
                    
                    # "date" may derive from an arbitray data class.                                  					
                    # Attention: Be careful of overwriting existing files. 

mat					


rm(mat)				# Remove object mat from the working space


mat


load("matrix_mat.RData")          
					
					# Loads the file from the the working directory. 

					# Syntax: load("name_of_file.RData",...)
                                    
mat







##
## for - loops
##

## "for loops" -> Idea: "Automize" repeated execution of (similar) commands

# Here: create colored smilies.

plot(1,1,type="n",xlim=c(0,1),ylim=c(0,1),main="HAHAHA",xlab=":-)",ylab="(-:")

for(s in 1:30) 	# index s runs from 1 to 30 (Idea: create smiley 1,2,...,30)
{	
  x  <- runif(1) 	# uniformly choose an x-value on [0,1]  
	y  <- runif(1)	# uniformly choose an y-value on [0,1] 
	co <- sample(c("red","green"),1) 		# choose a color, red or green
	points(x,y,cex=2.7,col=co,pch=19) 	# plot the smiley (head)
	text(x,y,":-)")							# plot the face
	text(x,y,s,pos=3)						# assign its number s
}


# Syntax: for (index in indexset) { do anything }  



### Again, the same thing, but now count the number of green and red smilies.


plot(1,1,type="n",xlim=c(0,1),ylim=c(0,1),main="Random generation of smilies on the unit square",xlab=":-)",ylab="(-:")


green <- rep(NA,30) # placeholder


green


for(s in 1:30) 
{ 	
	x  <- runif(1) 	
	y  <- runif(1)	
	co <- sample(c("red","green"),1) 	
	points(x,y,cex=2.7,col=co,pch=19) 		
	text(x,y,":-)")							
	text(x,y,s,pos=3)						
	green[s] <- co == "green"		# TRUE iff co is green
}


green


sum(green)		# number of green smilies. TRUE <-> 1, FALSE <-> 0


# Add a legend


legend(x="topleft",legend=c(sum(green),30-sum(green)),pch=rep(19,2),col=c("green","red"),title="No. Smilies")


# Syntax: legend(where, legend=vector, pch=vector, col=vector, title=character,...)


?legend					


# Remark:

# This is how we will typically perform simulations:
# 1. Define a placeholder.
# 2. Run through some loop. In each step perfom some calculation and substitute it with the placeholder.
# 3. Evaluate the derived quantities. 






##
## Conditions 
##


# if - else conditions

x <- 10
if(x>5){print("larger than 5")} 



x <- 3
if(x>5){print("larger than 5")} 



if(x>5){print("larger than 5")} else{print("smaller than 6")}


# Syntax: if ( logigal operation ) { do something if operation is TRUE }  else { do something else if operation is FALSE }






##
## repeat and while - loops
##


s <- 0
repeat 
  {
      s <- s+1 
      print(s) 
      if(s>10) break
  }

s

# syntax: repeat{ something }    
# the command break leaves the loop 



# same thing with while-loop


w <- 0
while(w<11)
  {
  w <- w+1 
  print(w)
  }

w


# syntax: while ( logical operation ) { do something while operation is TRUE }    








##
## Writing functions
##


4^3


cube <- function(x){x * x * x}


cube(4)


cube(1:10)

# syntax: function( input ) { calculate something and return last expression }



smilies <- function(n=10, second_color="red")
  {
  plot(1,1,type="n",xlim=c(0,1),ylim=c(0,1),main="Random generation of smilies on the unit square",xlab=":-)",ylab="(-:")
  
  green <- rep(NA,n) # depends on input n
  
  for(s in 1:n) # depends on input n
    { 	
    x  <- runif(1) 
    y  <- runif(1)	
    co <- sample(c("green",second_color),1)	# depends on input second_color
    points(x,y,cex=2.7,col=co,pch=19) 		
    text(x,y,":-)")						
    text(x,y,s,pos=3)					
    green[s] <- co == "green"				
    }
  
  sum(green)
  }


smilies() # default n=10 and second color_color="red"


smilies(n=20, second_color="blue")


# Keep in mind: 
# [ ]-brackets -> subset selection
# ( )-brackets -> commands
# { }-brackets -> functions, loops, conditions




##
## Importing data
##


# Most of the times we will want to work with data that is stored in an external file (e.g., .txt or .csv)
# Then we need to import the file first.


# 1. Read in txt file: 


dat <- read.table(file = "dataset.txt")


dat


# Set header=TRUE, so that variable names are not interpreted as information.


dat <- read.table(file = "dataset.txt", header=TRUE)


dat


year


attach(dat) # Gives access to variables


year


detach(dat) # Detaches variables


year


data.class(dat) # The class data.frame can handle columns of different data.type


attach(dat) 


is.logical(logical)


is.numeric(year)


# 2. Read in csv file


dat2 <- read.csv(file = "dataset.csv", header=TRUE)


dat2







######################
##
## Exercise 
##

# Given the following data 


data <- rexp(100,1)


# that shall represent waiting times in minutes. 


# Create a yellow histogram and mark the mean with a red line.

