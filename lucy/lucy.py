#!/usr/bin/env python

import os
import re
import sys
from datetime import datetime

import click
import requests
from requests.compat import urljoin

BASE_LIST_URL = 'https://api.github.com/licenses'
BASE_SEARCH_URL = 'https://api.github.com/licenses/'
HEADERS = {
    "Accept" : "application/vnd.github.drax-preview+json",
}

FILEPATH = os.path.abspath(os.path.join(os.getcwd(), 'LICENSE'))

def build_license_content(content, name):
    """Creates the license by replacing year and name in the original text."""
    year = datetime.now().year
    content = re.sub('\[year\]', str(year), content)
    content = re.sub('\[fullname\]', name, content)
    return content

def create_license_file(license_content):
    """Creates a file named LICENSE in the current directory with license content."""
    license_file = FILEPATH
    with open(license_file, 'w') as f:
        f.write(license_content)

@click.group()
def main():
    """It generates a license for your project."""
    pass

@main.command()
def list():
    """Lists all available licenses."""
    call_url = BASE_LIST_URL
    response = requests.get(call_url, headers=HEADERS)
    if response.status_code == requests.codes.ok:
        license_list = [str(x['key']) for x in response.json()]
        click.echo('\n'.join(license_list))
    else:
        click.echo("Service not working at the moment.")

@main.command()
@click.option('--name', prompt="Author's name please")
@click.argument('license_name')
def create(license_name, name):
    """Fetches the content of the requested license."""
    call_url = urljoin(BASE_SEARCH_URL, license_name)
    response = requests.get(call_url, headers=HEADERS)
    if response.status_code == requests.codes.ok:
        content = response.json()['body']
        license_content = build_license_content(content, name)
        create_license_file(license_content)
    else:
        click.echo("Please check the license name you provided.")

if __name__ == '__main__':
    main()
    sys.exit(0)
