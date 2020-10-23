# QA Engineer Take Home Test from Censys

This project will show how to run automated scripts in Docker containers using Selenium Hub.

# Required apps and drivers

- Docker Desktop App (to create containers and run automated tests)
- VNC Viewer (to view test execution)
- Selenium WebDriver package (to use Remote Webdriver to create tests)

# Selenium WebDriver Package

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Selenium package.

```bash
$ pip install selenium
```

OR 

Alternarively, go to [Selenium website](https://www.selenium.dev/) and click `Download` on the top of the page. 
Scroll down to Selenium Client & WebDriver Language Bindings table and choose the binding for the preferred language. 

Click `Download` in the Links column next to the chosen language. On Selenium website you can also choose to download Alpha version of the package as well as Selenium API Docs. 

# VNC Viewer

If VNC Viewer is not installed on your computer, go to [download page](https://www.realvnc.com/en/connect/download/viewer/), choose your OS and click `Download`.

# Docker Desktop App 

Go to [Docker website](https://www.docker.com/products/docker-desktop) and download the most recent and stable version of the app. 
([Read more about installation](https://docs.docker.com/desktop/))

## Usage

To start creating Selenium containers in Docker we first need to pull selenium /hub, /node and /standalone images. All images and detailed instructions can be found on [GitHub](https://github.com/SeleniumHQ/docker-selenium).

1. Pull selenium images by typing `$ docker pull selenium/hub`, `$ docker pull selenium/standalone-firefox` and `$ docker pull selenium/node-firefox-degug` in bash terminal. You also can pull same images for Chrome browser by changing "firefox" to "chrome" in your commands. 

2. After pulling all images you need, type 

```bash
$ docker run -d -p 4545:4444 —-name selenium-hub selenium/hub
``` 
to create a Selenium Grid which will be available at `localhost:4545`.

`--name` tag allows you to give a container whatever name you want, in this case container name is "selenium-hub". When your container with Selenium Grid is created, Docker will also assign it a long ID number. 

3. When ID number is assigned, type `docker run -d -P --link selenium-hub:hub selenium/node-firefox-debug` in the terminal. This command is going to link Mozilla Firefox browser to Selenium Grid you created. NOTE: to link firefox, use the name you gave to your container in the previous step. 

At this point, the container is created and now is up and running.

# Test Script 

A step-by-step explanation on how to use Selenium Python bindings can be found [here](https://selenium-python.readthedocs.io/getting-started.html#selenium-remote-webdriver) 

```python
# Import all libraries and modules 
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from keyboard import press
import logging

class MyTestCase(unittest.TestCase):

    def setUp(self):     # set up a remote webdriver and all desiredCapabilities 
        self.driver = webdriver.Remote(
            command_executor = 'http://127.0.0.1:4545/wd/hub',
            desired_capabilities = {
            'browserName': 'firefox',
            'javascriptEnabled': True
            })
        
    def test_ipv4(self):    
        driver = self.driver
        driver.get('https://censys.io/ipv4')
        search = driver.find_element_by_id("q")
        search.send_keys("176.49.198.99")
        press('enter')

    def tearDown(self):
        self.driver.close()

# Create a standart output log to get a test report
logging.basicConfig(filename='standout.log', level=logging.DEBUG,
                    format='%(asctime)s|%(filename)s|%(message)s|%(pathname)s')

if __name__ == "__main__":
    unittest.main()
```

# Test Running

1. In -bash terminal type 

```bash
$ docker ps
```
and locate a port number for your container. 

2. Open VNC Viewer, type in a port number in the format `0.0.0.0:32778` and connect to a VNC Server (if asked for password, use 'secret').

3. Run your test script.


# Project Status

This project is finished, more information will be given in TODO.md file.
