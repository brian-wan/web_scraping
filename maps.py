import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])
    print(address)
# get address from clipboard
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
