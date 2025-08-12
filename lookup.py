# This is a tool to look up researcher profiles in a Scopus database and return their information.

import requests
import argparse
import sys

# Scopus API key and headers
LINE_LENGTH = 80
API_KEY = ''
HEADERS = {
    "X-ELS-APIKey": API_KEY,
    "Accept": "application/json"
}

def get_info_by_name(last_name, first_name, orcid=None):
    """Get author ID from Scopus."""
    check_api_key()
    url = 'https://api.elsevier.com/content/search/author?query='
    query = f'AUTHLASTNAME({last_name}) AND AUTHFIRST({first_name})'
    url = f"{url}{query}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        total_results = int(data.get('search-results', {}).get('opensearch:totalResults', '0'))
        if total_results > 0:
            for entry in data.get('search-results', {}).get('entry', []):
                if orcid:
                    if entry.get('orcid') != f"[{orcid}]":
                        continue
                author_id = entry.get('dc:identifier', '').split('/')[-1].split(":")[1]
                author_name = entry.get('preferred-name', {}).get('given-name', '') + ' ' + entry.get('preferred-name', {}).get('surname', '')
                affiliation = entry.get('affiliation-current', {}).get('affiliation-name', 'No affiliation found')
                city = entry.get('affiliation-current', {}).get('affiliation-city', 'No city found')
                country = entry.get('affiliation-current', {}).get('affiliation-country', 'No country found')
                citations = get_citations_by_id(author_id)
                print("-" * LINE_LENGTH)
                print()
                print(f"Name: {author_name}")
                print(f"Affiliation: {affiliation}")
                print(f"Scopus ID / Author ID: {author_id}")
                print(f"City: {city}")
                print(f"Country: {country}")
                print(f"Citations: {citations}")
                print()
                print("-" * LINE_LENGTH)

        else:
            print("No results found.")
    else:
        print("Failed to retrieve author information.")
        print("Error: ", response.status_code, "-", response.text)
        print("Please check the author name and try again.")
        exit(1)

def get_citations_by_id(id):
    """Get author information by Scopus ID."""
    abstract_url = f"https://api.elsevier.com/content/author/author_id/{id}"
    response = requests.get(abstract_url, headers=HEADERS)
    data = response.json()
    if response.status_code != 200:
        print("Failed to retrieve author information.")
        print("Error: ", response.status_code, "-", response.text)
        print("Please check the author ID and try again.")
        exit(1)

    citations = data.get('author-retrieval-response', {})[0].get('coredata', {}).get('citation-count', 'No citation count found')
    return citations


def get_info_by_orcid(orcid_id):
    """Get author information by ORCID."""
    check_api_key()
    query = f'orcid({orcid_id})'
    url = f"https://api.elsevier.com/content/search/author?query={query}"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    if response.status_code != 200:
        print("Failed to retrieve author information.")
        print(f"Error: {response.status_code} - {response.text}")
        print("Please check the ORCID ID and try again.")
        exit(1)

    last_name = data.get('search-results', {}).get('entry', [{}])[0].get('preferred-name', {}).get('surname', 'No last name found')
    first_name = data.get('search-results', {}).get('entry', [{}])[0].get('preferred-name', {}).get('given-name', 'No first name found')

    return first_name,last_name

def insert_api_key(api_key, filename="yourscript.py"):
    """Insert API key into the script file."""
    with open(filename, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith("API_KEY ="):
            lines[i] = f"API_KEY = '{api_key}'\n"
            break

    with open(filename, 'w') as file:
        file.writelines(lines)

def check_api_key():
    """Check if API key is set."""
    if not API_KEY:
        print("API key is not set. Please provide your Scopus API key using --api_key.")
        exit(1)

parser = argparse.ArgumentParser(description="Lookup: a tool to find researcher profiles in Scopus database.")
parser.add_argument('--last', type=str, help="Researcher's last name")
parser.add_argument('--first', type=str, help="Researcher's first name")
parser.add_argument('--orcid', type=str, help="Researcher's ORCID ID")
parser.add_argument('--api_key', type=str, help="Scopus API key. Only done once", default=API_KEY)
args = parser.parse_args()

def main():
    """Main function to run the lookup."""
    if args.api_key:
        global API_KEY
        API_KEY = args.api_key
        global HEADERS
        HEADERS = {
            "X-ELS-APIKey": API_KEY,
            "Accept": "application/json"
        }

    # Check if API key is set
    check_api_key()

    if args.last and args.first:
        get_info_by_name(args.last, args.first)
    elif args.orcid:
        first_name, last_name = get_info_by_orcid(args.orcid)
        get_info_by_name(last_name, first_name , orcid=args.orcid)
    else:
        print("Please provide either --last and --first or --orcid to look up a researcher.")
        exit(1)
    
    if '--api_key' in sys.argv:
        insert_api_key(args.api_key, __file__)
        print("API key has been set successfully. No need to set it again.\n")

if __name__ == "__main__":
    main()