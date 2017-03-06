## Raspberry Pi Workshop - Scripts
This (ongoing) collection of scripts has been created for showing different applications that utilize features of the Raspberry Pi platform.  Each script is used in our *Introduction to Raspberry Pi* workshops.  The workshops are designed to provide some insight and demonstration the Pi platform while answering the *what? why? and how?* questions that one might have when being exposed to the board for the first time.


### switch.py
The switch.py script provides some demonstration of the ability to interact with a running program from the real world (push button).  A unique quality of the Raspberry Pi, and similar platforms, is the presence of the GPIO conntector, that allows for running code on the board to interact with the realworld enviroment via switches, sensors, and circuits.

The switch.py program gives a very basic demonstration of several wires and a dozen lines of instructions can get you started with the platform.

**Requirements**
A simple circuit wired as follows:

* GPIO 6 - wired to the switch
* GPIO 7 - wired to the LED

### switch_www.py
The switch_www.py script builds on the switch.py script to demonstrate rewriting a publically assible webpage each time the button is pushed.  

**Requirements**
A running webserver (such as apache) that stores the web root document in the /var/www/html/ directory.

To install on Raspbian:
`sudo apt-get update`
`sudo apt-get install apache2`

After installing the web server, run the `ifconfig` command to get the Pi's ip address.  Have workshop attendees visit this address from their own devices to view the page.
