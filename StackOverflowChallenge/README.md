By downloading these files you promise to complete the assignments and submit them before looking at files that might related to graded classwork, in accordance with coursera and stanfordML's code of honor.

If you wish to just work on the StackOverflowChallenge as an example of logistic regression (and neural networks, etc as the course progresses) you need only download the Octave folder.

If you don't know about StackOverflow, you should to stackoverflow.com and search on the tag "octave" which will pull up the most popular questions asked about octave.  You may run across some questions that have been closed for one of several reasons.  This will give you a feeling for what the competition is about.

**** Platforms **********
Currently, instructions are linux only, although if you can do a git download you can just work with the Octave folder.  Be the first to port to Mac or Windows!

******* Downloading from Kaggle ***********
If you wish to create your own training samples from the more complete repo see below.
If you wish to use the python scripts and compare Octave results to the scipy family
of ML routines, like RandomForest (used in basic_benchmark.py) then you will need the 
complete repo from here or from kaggle (note, i found a few bugs in the kaggle scripts
that are fixed here so you may want to use this repo for the scripts and kaggle to get the data.

Benchmarks for Kaggle's [Predict Closed Questions on Stack Overflow](https://www.kaggle.com/c/predict-closed-questions-on-stack-overflow) competition

The benchmarks require several Python packages:

 - numpy
 - pandas
 - sklearn

Also, reccommeded is the enhanced python interpreter
 - ipython
which has its own dependencies

These packages can be installed with easy_install or pip, or Windows users can [download compiled versions of these packages](http://www.lfd.uci.edu/~gohlke/pythonlibs/)

To run the benchmarks, you also need to [download the data](https://www.kaggle.com/c/predict-closed-questions-on-stack-overflow/data). The only files necessary for the benchmarks are train-sample.csv and public_leaderboard.csv. Two variables need to be updated in competition_utilities.py as well: data_path should be set to the path to the data, and submissions_path should be set to the location for writing the submission files.

Some of the files in kaggle/ directory have been modified from the original kaggle scripts by Kesten Broughton.

********** Directory Description **************
These files were edited using the Eclipse IDE with the PyDev plugin
for code completion, syntax highlighting etc
lr/ is for logistic regression scripts
ml/ is for more general machine learning files
kaggle/ is my modified version of the kaggle scripts
[wire_short.py was used to create the 1000 sample .csv file]
Octave/ should look a lot like exercise 3 from Anrew Ng's ML course
[Note that I have removed left some files required by the exercises in their original
state since the hard deadline for submission is not until Dec 3]

StackOChallenge_Conditioning.ipynb is an ipython notebook that calls many of the functions in competition_utilities.py in a graphically pleasing interactive session.  If you have ipython running, you can load the notebook by starting the notebook server 
$ ipython notebook --pylab inline
And browsing to load the .ipynb file.

I have included some very abbreviated files of 1000 samples in .csv format.
The real training files are 140,000 samples plus, and are required if you wish 
to run most scripts in kaggle/ .  You will also need to change the path names to this 
project in files like competition_utilities.py


************ Using Git ************************
If you wish to join the team and make contributions, I recommend you get to know Git a little bit.  

Create a "sandbox" repo by creating a directory, moving into it and
$ mkdir Sandbox
$ cd Sandbox
$ git init
Then add some directories and files and follow along some git tutorials, TESTING EVERYTHING ALONG THE WAY.
If you want to contribute your changes to the git repo, you will have to be careful not to treat your cloned git repo as a normal directory.  Moving, deleting and renaming things should be done using the git versions of these commands ($ git mv file1 file2 for example).
If you ever delet the .git hidden folder, you won't be able to merge back the github repo at a later time since it will no longer be considered a "descendent" of the github repo.

