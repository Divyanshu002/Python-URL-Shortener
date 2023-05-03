import pyshorteners

# Initialize the PyShorteners client with the TinyURL API
s = pyshorteners.Shortener(api_key='KEY')

# Get the URL to shorten from the user
long_url = input('Enter the URL to shorten: ')

# Shorten the URL using the TinyURL API
short_url = s.tinyurl.short(long_url)

# Print the shortened URL
print('Short URL:', short_url)

# Offer to copy the shortened URL to the clipboard
copy_to_clipboard = input('Copy the shortened URL to clipboard? (y/n): ')
if copy_to_clipboard.lower() == 'y':
    import pyperclip
    pyperclip.copy(short_url)
    print('Short URL copied to clipboard!')

# Offer to open the shortened URL in the browser
open_in_browser = input('Open the shortened URL in browser? (y/n): ')
if open_in_browser.lower() == 'y':
    import webbrowser
    webbrowser.open(short_url)