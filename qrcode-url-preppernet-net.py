import segno

qrcode = segno.make('https://www.preppernet.net')
qrcode.save('qrcode-url-preppernet-net.svg', scale=6)
qrcode.save('qrcode-url-preppernet-net.png', scale=6)
qrcode.to_artistic(background='qrcode-backgrounds/logo-image-200x261.png', target='qrcode-url-preppernet-net-logo.png', scale=6)