# GE501_HW
Code for completing assignments for GE501 Advanced Remote Sensing

# About

These programs provide the tools necessary to complete the homework assignments for GE501. Their purpose is to not only provide you with the answers, but walk you through how you get to the solution. It is important that this is used to help understand the problems (not just copy and pasting the solutions), as you will need to know them for the exams. 

The questions are written for the command line, meaning a Unix shell program is required to run the scripts. For Mac or Linux, there are Unix applications built-in (for Mac: search Terminal). For Windows, it will depend on your operating system, but a Google search of 'Windows shell' will find plenty of results. The most commonly used one is PowerShell, and Windows 10 can use a Bash shell. 

Some basic Bash knowledge is necessary to run the scripts. Once again, the best and easiest option is to Google or Youtube 'Intro to Bash' and you will find plenty of results. It is not as overwhelming as it seems (I promise). 

Some of the questions have parameters you can tune if you would like. The default are the ones listed on the homework, but I encourage changing them to see the effect. I would also encourage looking at the code itself. Programming languages can be overwhelming at first, but it is really good idea to atleast be able to comprehend the basics. In the end they can save you much time and open up research opportunities that might not be available otherwise.   

If you find any bugs or have any questions, feel free to send me an email: bullocke@bu.edu. 

#Installation

The repository can be cloned directly from Github using the command line: 

```
git clone https://github.com/bullocke/GE501_HW.git
```

In addition to a Unix Shell Python must be installed on your machine. It is recommended either Python 2.7 or 3.5, and other versions have not been tested. There are a few modules that need to be installed as well. Chances are the modules come with the version of Python you have installed, but if not you can install them with 'Pip' (https://pypi.python.org/pypi/pip). The command (at the command line) to install the packages is:

```
pip install future math docopt
```

The basic command to run the scripts are (in this example it's question 1):

```
python q1.py
```

If you want to bring up the help screen showing the problem and options:

```
python q1.py -h 

GE 501 HW#1 Question 1

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q1.py [options]

Options:
    -h --help                   Show help
    -o --orbit <orbit>          Satellite orbit in km (default 833)
Question:

    NOAA's POESS (Polar Orbiting Environmental Satellite System) platforms, which include
        the AVHRR sensor, have a sun-synchronous orbit with a height of 833 km (<orbit>).
        Find the angular speed theta associated with this orbit and the orbital period in
        minutes.

Example:

    > python q1.py -o 833
```

The commands can be run with options, for each the first problem you can change the orbit height and see the results:

```
python q1.py -o 1000
```
