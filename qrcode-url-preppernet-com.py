import segno

qrcode = segno.make('https://www.preppernet.com')
qrcode.save('qrcode-url-preppernet-com.svg', scale=6)
qrcode.save('qrcode-url-preppernet-com.png', scale=6)
qrcode.to_artistic(background='qrcode-backgrounds/logo-image-200x261.png', target='qrcode-url-preppernet-com-logo.png', scale=6)