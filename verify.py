import urllib
import urllib2

# email addresses should be in an emails.txt file seperated by a new line
# a emailsfinal.txt final should be created  before running the script(no contents inside)

with open('emails.txt') as f:
  for line in f:
    url = 'https://accounts.google.com/accountLoginInfoXhr'
    values = {'Email' : line }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print line
    if "ASK_PASSWORD" in the_page:
      file=open('emailsfinal.txt', 'a')
      file.write(line)
      file.close()