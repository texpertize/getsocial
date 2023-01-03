import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the website and retrieve the HTML content of the page
url = input("Enter the URL of the website: ")
response = requests.get(url)
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the social links
social_links = {}
for link in soup.find_all('a'):
  href = link.get('href')
  if href and (href.startswith('https://www.facebook.com') or href.startswith('https://twitter.com') or href.startswith('https://www.linkedin.com') or href.startswith('https://www.instagram.com')):
    social_links[link.text] = href

# Find the email address
email = None
for meta in soup.find_all('meta'):
  if meta.get('name') == 'email':
    email = meta.get('content')

# Find the contact details
contact_details = {}
for div in soup.find_all('div'):
  if div.get('class') == ['contact-info']:
    for p in div.find_all('p'):
      if p.get('class') == ['phone']:
        contact_details['phone'] = p.text
      if p.get('class') == ['address']:
        contact_details['address'] = p.text

# Print the results
print("Social links:", social_links)
print("Email:", email)
print("Contact details:", contact_details)
