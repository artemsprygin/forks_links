import requests
import argparse
import webbrowser
import os

if __name__ == '__main__':

    # Setting up arguments
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-l', '--link', type=str,
                        help='Link to original repository')
    args = argparser.parse_args()

    link = args.link

    if not link:
        link = input('Paste link to original repo here: ')

    # Converting link into a login and repo for API link
    # Deleting last '/' symbol
    if link[-1] == '/':
        link = link[:-1]

    # Parsing github's login and repo name from link
    link_parsed = link.split('/')
    github_login = link_parsed[3]
    github_repo = link_parsed[4]

    # Getting info from API
    url = 'https://api.github.com/repos/{}/{}/forks'\
                    .format(github_login, github_repo)
    forks_raw = requests.get(url)
    forks_list = forks_raw.json()

    # Getting forks links list
    fork_links = []

    for fork in forks_list:
        fork_owner_login = fork['owner']['login']
        fork_link = link.replace(github_login, fork_owner_login)
        fork_links.append(fork_link)

    # HTML-page generation
    headers = '''
        <!DOCTYPE html>
            <html>
            <head>
                <title>Forks from {}</title>
            </head>
            <body>
            <h2>Forks from {}:</h2>
        '''.format(link, link)
    body = '\n'
    for link in fork_links:
        body += '<a href="{}">{}</a><br/>\n'.format(link, link)
    footers = '''
            </body>
            </html>
        '''
    with open('links.html', 'w', encoding='utf-8') as html_page:
        html_page.write(headers)
        html_page.write(body)
        html_page.write(footers)

    want_open = input('Would you like to open generated html file in browser? y/n\n')

    if want_open == ('y' or 'yes'):
        os.system("open 'links.html'")
    else:
        print('Forks from {}:'.format(links))
        for link in fork_links:
            print(link)