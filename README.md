# uaAiClub 

## About The Project

## Prerequisites 
* Django [https://www.djangoproject.com/](https://www.djangoproject.com/)
  * [Django Installation Help](https://docs.djangoproject.com/en/1.11/intro/install/)
  * Python 3 Latest Version [https://www.python.org/](https://www.python.org/) (and Pip, included with Python) 
  * **(HIGHLY RECOMMENDED)** Virtual Environment & Virtual Environment Wrapper
    * Short Explanation: Allows you to create an "environment" that seperates GLOBAL Python settings with LOCAL Python settings
    * Long Explanation: A virtual environment is similar to a virtual machine: it seperates the host from the guest machines. Libraries So, the way I understand it is, the host machine STORES the guest machines files, but the GUEST  machine has NO knowledge of the HOST. 
    * [Virtual Environment (All OSes)](https://virtualenv.pypa.io/en/stable/)
    * Virtual Environment Wrapper - [Windows](https://pypi.python.org/pypi/virtualenvwrapper-win) - [Mac,Unix/Linux](https://virtualenvwrapper.readthedocs.io/en/latest/)
* Github Account (to pull and push to deploy branch) 
* Git [https://git-scm.com/](https://git-scm.com/)

## Local Development


## Updating

Django uses "projects" and "apps".  Each webpage (index, projects, contact, about, and resources at the time of this write-up) is a seperate "app". 

Every file with the commit: 

>Copying EXACTLY from https://github.com/azureappserviceoss/DjangoAzure 

**SHOULD NOT BE CHANGED**
### Updating Database: e.g. Events, Schedule, Projects, Resources, etc. 


```python
$ python manage.py collectstatic
```

### Adding A Webpage 

### Remaking Website from Scratch (Warning: MAKE SURE YOU KNOW WHAT YOU'RE DOING)
Under construction:
