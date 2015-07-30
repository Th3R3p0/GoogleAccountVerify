import sys
import urllib
import urllib2
import optparse

# Setup terminal colors
try:
    from blessings import Terminal
    color="true"
    t = Terminal()
except ImportError:
    color="false"

# email address list should be in a .txt file seperated by a new line in the same directory

#Global
url = 'https://accounts.google.com/accountLoginInfoXhr'

def do_list(filename):

    """

    Processes a list of emails
    Takes filename as an argument
    Returns if email is valid

    """

    with open(filename, 'r') as f:

        for line in f:

            # Local variables
            values = {'Email' : line}
            data = urllib.urlencode(values)

            try:

                req = urllib2.Request(url, data)
                response = urllib2.urlopen(req)
                the_page = response.read()

                if "ASK_PASSWORD" in the_page:
                    if color == "true":
                        print(t.green("[*] {0} - VALID".format(line.strip('\n'))))
                    else:
                        print "[*] {0} - VALID".format(line.strip('\n'))
                elif "ASK_PASSWORD" not in the_page:
                    if color == "true":
                        print(t.red("[*] {0} - NOT VALID".format(line.strip('\n'))))
                    else:
                        print "[*] {0} - NOT VALID".format(line.strip('\n'))
            # Handle HTTP exceptions
            except urllib2.HTTPError as e:
                raise e
            except urllib2.URLError as e:
                raise e

        # Close file descriptor
        f.close()


def do_email(email):

    """
    Processes a single email
    Takes email address as an argument
    Returns if email is valid

    """

    # Local variables
    values = {'Email': email}
    data = urllib.urlencode(values)

    try:

        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        the_page = response.read()

        if "ASK_PASSWORD" in the_page:
            if color == "true":
                print(t.green("[*] {0} - VALID".format(email)))
            else:
                print "[*] {0} - VALID".format(email)
        elif "ASK_PASSWORD" not in the_page:
            if color == "true":
                print(t.red("[*] {0} - NOT VALID".format(email)))
            else:
                print "[*] {0} - NOT VALID".format(email)

    # Handle HTTP exceptions
    except urllib2.HTTPError as e:
        raise e
    except urllib2.URLError as e:
        raise e


def main():

    # Create argument parser
    parser = optparse.OptionParser('Usage: python ' + sys.argv[0] + ' -e <email> || -f <filename.txt>')
    parser.add_option('-e', dest='email', type='string', help='specify single email or email from list')
    parser.add_option('-f', dest='filename', type='string', help='specify single email or email from list')

    (options, args) = parser.parse_args()

    email = options.email
    filename = options.filename

    if len(sys.argv) < 2:
        if color == "true":
            print(t.blue("[*] Usage python {0} -e email || -f <filename.txt>".format(sys.argv[0])))
        else:
            print "[*] Usage python {0} -e email || -f <filename.txt>".format(sys.argv[0])
        sys.exit(0)

    # Handle command line arguments
    if sys.argv[1] == '-e':
        do_email(email)
    elif sys.argv[1] == '-f':
        do_list(filename)
    else:
        print ('Usage: python ' + sys.argv[0] + ' -e <email> || -f <filename.txt>')
        print("[{0}] Exiting ...")
        sys.exit(0)


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print ('Usage: python ' + sys.argv[0] + ' -e <email> || -f <filename.txt>')
        print("[{0}] Exiting ...")
        sys.exit(0)
