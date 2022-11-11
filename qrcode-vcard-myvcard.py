import segno
from segno import helpers

qrcode = helpers.make_vcard(name='LastName;FirstName', displayname='FirstName LastName',                           
        email=('my@email.com', 'anotheremail@myemail.com'),
        phone='+1 555 555 1111')
qrcode.save('qrcode-vcard-myvcard.png', scale=4)
