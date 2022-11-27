# Lab 5: Biometrics

Semester 2221, CSEC 472\
Bonus Lab: Biometrics\
Due by November 28, 2022 11:59 PM EST

> **Note**\
> This lab is available for extra credit towards individual grades.
> You may work with others outside your group on this lab.

## Learning Outcome

Students will refine their understanding of applied biometrics by performing both:

1. Fingerprint image processing.
2. Feature extraction for authentication decisions.

## Lab Set Up

1. For this lab, you can use your own computer or a VM.
2. You can use the programming language of your choice to perform the lab; you have some freedom to choose the tools you want to work with, but you'll probably need to import one or two image processing/machine learning libraries such as:
   
   Numpy, Scikit-image (skimage), Scikit-learn, PIL/Pillow, OpenCV-Python, SimpleCV, Mahotas, SimpleITK, pgmagick, pycairo, Scipy, Theano, TensorFlow, Keras, PyTorch, Pandas, Matplotlib, etc.
3. Download the [NIST 8-Bit Gray Scale Images of Fingerprint Image Groups (FIGS)](https://academictorrents.com/details/d7e67e86f0f936773f217dbbb9c149c4d98748c6) database from the torrent.
   NIST Special Database 4, [DOI 10.18434/T4RP4K](http://dx.doi.org/10.18434/T4RP4K).

> **Note**\
> Most images used in authentication systems are converted to grey scale.
> This transforms the image into a matrix (size = n * m, where n and m are the pixel size of the image).
> If it were in color, this image becomes an n * m * c matrix, where c represents specific color markers (like RGB).

> **Note**\
> I found this NIST dataset through [Google's Dataset Search](https://datasetsearch.research.google.com/).
> It may be a useful source of information in your group projects. 

## Instructions 

Each group member, will develop a features extraction system that makes accept/reject decisions, given a fingerprint.
As a group, the team will design a unified system and compare it tow hat they have built individually.

### 1. Feature Extraction System (Individual)

Download and examine the database.
It contains 400 image pairs of each of the 5 main fingerprint features (arches, loops, etc.).
The features are encoded in the `.txt` file that corresponds with the `.png`, the features are dispersed randomly throughout the dataset.
The database is organized as $\text{image pairs} = \\{f_i, s_i\\}$. 

You'll want to break the overall database into two sets:

1. **Train**: The first 1500 image pairs (`f0001-f1499` & `s0001-s1499`).
2. **Test**: The last 500 image pairs (`f1501-f2000` & `s1501-s2000`).

Process the training set to extract features (identify minutia).
Each group member will use three different methods.
This will inform the lab experiment.

To do this, you'll calculate minutia for each reference image ($f_i$) and its corresponding subject image ($s_i$).
You'll generally compare distances between these images.
Try three different ML techniques to do this.

**For each method:**\
Document your max, min, and average false rejection and false acceptance rates; calculate your equal error rate.

> **Note**\
> Don't compare notes with your pers until you get to the group work (step 2).
> Try to see what you can come up with individually without their input.

### 2. Build Table of Metrics (Group)

#### Description

Build a table documenting which methods you used, and the max, min, and average for both false reject and false accept rates, as well as the equal error rate (error crossover).

#### Submission (25%)

The table will have 8 columns: method, FRR average, FRR minimum, FRR maximum, FAR average, FAR minimum, FAR maximum, EER.
The table will have n rows, where $n = \text{the number of feature extraction methods each student used (by name)}$.
Minimum $n = \text{group size} * 3$.

### 3. Analyze the Table (Group)

#### Description

Analyze the table and re-design the feature extraction to reduce your average EER across the three best performing methods.
Your new system should apply all three methods and return the majority decision; this will create a hybrid system.
**Don't test the system yet!**
You'll do that in step 4.

#### Submission (25%)

Document your hypothesis – what do you think (as a group) will happen with your hybrid system?
Will the ERR go up, down, or not change compared to the other systems?

### 4. Run the Hybrid System (Group)

#### Submission (25%)

Add a row to your methods table documenting the FRR avg, min, max, FAR avg, min, max, and ERR for your group's hybrid system.

### 5. Interpret the Results (Group)

#### Submission (25%)

Write up & submit your answers to: 

- What happened?
- Was your hypothesis correct?
- Was there variability between EER findings when/if two students used the same method?
- What was most surprising to you?
- If you were to repeat the experiment, what would you do differently?
- What questions do you still have?


## Deliverables

1. **Lab Report:** Submit the table and writeup to MyCourses.
2. **Source Code:** Please put all team members' code into a single repository and send me the link with your lab report submission in MyCourses -> Assignments -> Lab 5.

## Grading

| Grade | Requirement                                                              |
|-------|--------------------------------------------------------------------------|
| `25%` | Table with individual results (min of n rows, where n = group size * 3). |
| `25%` | Group's hypothesis of what will happen with hybrid system.               |
| `25%` | Table with hybrid results (n += hybrid).                                 |
| `25%` | Write up your interpretation/analysis.                                   |



