import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# block of html to be written the index file
# inserts the date and time at the time of button press

html_str = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
	<title>Button Press</title>
	<meta http-equiv="content-type" content="text/html;charset=utf-8" />
</head>

<body>
<h2>Press the button to display the current time</h2>
<h1>{i}</h1>
</body>

</html>
"""

def write_file(page): 
    with open('/var/www/html/index.html', 'w') as file:
        file.write(page)
    print page
    return 0

while True:
    input_state = GPIO.input(6)
    if input_state == False:
        print('Button Pressed')
        i = str(datetime.now())
        page = html_str.format(i=i)
        write_file(page)
        time.sleep(0.2)
