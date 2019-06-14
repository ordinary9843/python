import base64

fp = open('resources\images\codedog.jpg', 'rb')
fp_read = fp.read()
fp.close()
base64_img = base64.b64encode(fp_read)
print(base64_img)