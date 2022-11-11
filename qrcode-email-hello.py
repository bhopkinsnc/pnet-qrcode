import segno
from segno import helpers

qrcode = helpers.make_email(to='my@email.com', cc=None,bcc=None,subject='Hello',body='Thanks')
qrcode.save('qrcode-email-hello.png', scale=4)
