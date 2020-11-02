# Assignment 3, Web Scraping

# Importing libraries
from bs4 import BeautifulSoup
import requests

# Parses the webpage and returns a BeautifulSoup object
def parse_page(url_id):
    # BS object made for parsing data
    url = "https://www.ncbi.nlm.nih.gov/gene/" + str(url_id)
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    return soup

# Scrapes the page for gene info and returns a list of gene info
def scrape_page(soup, url_id):
    # Using ID to get elements
    summary = soup.find(id="summaryDiv")
    # details, to easily use variables to acquire wanted text from <dd>
    details = summary.find_all('dd')

    # Gene info elements
    gene_id = soup.find('span', class_='geneid').text[:13]
    official_symbol = details[0].text.replace("provided by HGNC", "")
    full_name = details[1].text.replace("provided by HGNC", "")
    gene_type = soup.find('dt', text="Gene type").find_next_sibling('dd').text
    organism = soup.find('dt', text="Organism").find_next_sibling('dd').text.strip()

    return [gene_id, official_symbol, full_name, gene_type, organism]

# Appends the gene info to the text file
def write_info(filename, gene_info, url_id):
    # Clears the text file if starting from gene 2000 (the first gene)
    if url_id == 2000:
        open("geneinfo.txt", "w").close()
    # Opens and writes to the text file
    with open(filename, "a") as f:
        f.write(gene_info[0])
        f.write("\nOfficial symbol: ")
        f.write(gene_info[1])
        f.write("\nFull name: ")
        f.write(gene_info[2])
        f.write("\nGene type: ")
        f.write(gene_info[3])
        f.write("\nOrganism: ")
        f.write(gene_info[4])
        if url_id != 2020:
            f.write("\n*****\n")

# Counts the frequency of each word in the text file
def count_frequency(filename):
    try:
        f = open(filename, "r")
        geneinfo = (f.read().split())
        freqs = dict()
        for word in geneinfo:
            if word in freqs:
                freqs[word] += 1
            else: 
                freqs[word] = 1
        print_dictionary(freqs)
    except IOError:
        print("Error.")

# Prints the frequency dictionary
def print_dictionary(dic):
    for word in dic:
        if word.endswith(":"):
            print(word + " " + str(dic[word]))
        else:
            print(word + ": " + str(dic[word]))

def main():
    url_id = 2000
    # Keep looping until we reach gene id 2021
    while url_id != 2021:
        soup = parse_page(url_id)
        gene_info = scrape_page(soup, url_id)
        write_info("geneinfo.txt", gene_info, url_id)
        url_id += 1

    count_frequency("geneinfo.txt")

if __name__ == "__main__":
    main()
