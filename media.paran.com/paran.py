#!/usr/bin/python
import urllib
base = 'http://cartoon.media.paran.com/ncartoon_view.php?id=%d&ord=%d&part=%d'

id = int(raw_input('cartoon id? (id=?)'))
start_ord = int(raw_input('start ord? (ord=?)'))
end_ord = int(raw_input('end ord? (ord=?)'))
name = raw_input('cartoon name?')
ext = raw_input('file type? (jpg, ..)')
multiple = False
#if raw_input('Multiple parts? (y, n)') == 'y':
#    multiple = True
log = open(name+'/log.txt', 'a')
log.write('Starting a tash withid=%d, start_ord=%d, end_ord=%d, name=%s, extension=%s\n' % (id, start_ord, end_ord, name, ext))
import re


while start_ord <= end_ord:
    part = 1
    found = []
    while True:
        html = urllib.urlopen(base % (id, start_ord, part))
        match = re.search(r'http://cartoonimg.paran.com/up/NEWTOON/\d{4}/\d*/.*.jpg', html.read())
        if match == None:
            print 'illegal page, retrying', base % (id, start_ord, part)
            log.write('illegal page, retrying '+base%(id, start_ord, part)+'\n')
            html.close()
        else:
            cur = match.group(0)
            if cur in found:
                html.close()
            
                numStr = str(start_ord)
                while len(numStr) < 4:
                    numStr = '0' + numStr
               
                
                for idx, image_url in enumerate(found):
                    image_name = numStr
                    if len(found) > 1:
                        image_name += '-' + str(idx+1)
                    print image_name, 'retrieving:', image_url
                    log.write(image_name + ' retrieving: ' + image_url + '\n') 
                    urllib.urlretrieve(image_url, name + '/' + image_name + '.jpg')
                break
            else:
                found.append(cur)
                part += 1
                html.close()
    start_ord += 1

log.close()
