# QRcode Segno

The following creates QRCodes using a program scripting language called python.  Python can be installed on many operating systems see https://www.python.org/ on how to install.

Why not just use one of the many free QACode creates on the web?  They are free for a reason to harvest data.

> Note: if you a Mac or Raspberry PI it might already be installed.

> Note: This is a command line tool which will require access to a shell terminal. 

## Install Python3

Verify that python is installed

```bash
python3 --version
```

You should have output like below. If not go to https://www.python.org/ on how to install.

```bash
Python 3.10.6
```

## Install pip3

Python package manager named pip3 will need to be installed to download the segno module. 

Verify that pip3 is installed.

```bash
pip3 --version
```

You should have out like below. If not got to https://pip.pypa.io/en/stable/installation/ on how to install.

```bash
pip 22.0.4 from /usr/local/lib/python3.10/site-packages/pip (python 3.10)
```

## Install Segno

Check if segno python library is installed.

```bash
pip3 list 
```

Look through the list to find segno. 

```bash
segno              1.5.2
```

If not installed run the following command to install.

```bash
pip3 install segno
```

Once installed verify the command.

```bash
segno -V
```

```bash
Segno 1.5.2
```

## Creating QRCodes

The command line tool can create QRCodes using command line. 

> NOTE: The image will be saved into your current directory.  Change into the directory you want to store your QRCode if required.

> NOTE: The image is an PNG file (Portable Network Graphic) and opens in a lot of viewers including web browsers. 

## Examples:

### URL 

This will create the file named qrcode-url-usdebtclock-org.png

```bash
segno --scale=4  "https://www.usdebtclock.org/" --output=qrcode-url-usdebtclock-org.png
```

### URL File Share 

Can also linking to a file URL

```bash
segno --scale=4  "https://drive.google.com/file/d/19R3v4XXn1tLmKLI1Os1oFq1ZM9dVqNS8/view?usp=sharing" --output=url-prepyourgarden.png
```

### V-CARDS

VCards are a little harder and requires a script file created.  

Create a script named qrcode-vcard-myvcard.py

Edit the script below replacing your information.

```python
import segno
from segno import helpers

qrcode = helpers.make_vcard(name='LastName;FirstName', displayname='FirstName LastName',                           
        email=('my@email.com', 'anotheremail@myemail.com'),
        phone='+1 555 555 1111')
qrcode.save('qrcode-vcard-myvcard.png', scale=4)
```

Run the command to create the QRCode

```bash
python3 qrcode-vcard-myvcard.py
```

The QRCode file named qrcode-vcard-myvcard.png is created

### Emails

Create a file qrcode-email-hello.py


```python
import segno
from segno import helpers

qrcode = helpers.make_email(to='my@email.com', cc=None,bcc=None,subject='Hello',body='Thanks')
qrcode.save('qrcode-email-hello.png', scale=4)
```

```bash
python3 qrcode-email-hello.py
```

### URL with Background Image

To create script file below named qrcode-url-preppernet-net-logo.py

Download the logo image place in in you current working directory which in this example is named logo-image-200x261.png.

```python
import segno

qrcode = segno.make('https://www.preppernet.net')
qrcode.save('qrcode-url-preppernet-net.png', scale=6)
qrcode.to_artistic(background='logo-image-200x261.png', target='qrcode-url-preppernet-net-logo.png', scale=6)
```

```bash
python3 qrcode-url-preppernet-net-logo.py
```