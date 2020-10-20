# Discord - BOT

## System requirements
1. Have python 3.5.3 or higher
2. have pip installed in your system, in python 3.x, it is usually already installed. To check it:
>  pip --version

It is a good practice to keep the pip version up to date, you can do this by
> python -m pip install --upgrade pip

To install virtual environment using pip
> pip install virtualenv

#
Clone this repository in your system,
then in your terminal, create a virtual environment where you have cloned this repository by: 
> python3 -m virtualenv <virtual_environment_name>

## For Windows:
In your working directory where you have created the virtual environment, activate the virtual environment by:
> <virtual_environment_name>\Scripts\activate.bat

> pip install -r requirements.txt
 
## For Unix or MacOS:
In your working directory where you have created the virtual environment, activate the virtual environment by:
> source <virtual_environment_name>/bin/activate

> pip install -r requirements.txt

note: (This script is written for the bash shell. If you use the csh or fish shells, there are alternate activate.csh and activate.fish scripts you should use instead.)

You are all set now. Happy developing!