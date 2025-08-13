# 🔍 Lookup

#### This project was completed as part of the CS50 course.

#### Video Demo:  [video](https://www.youtube.com/watch?v=5m-e14IusHI)

#### Description:
**Lookup** is a command-line research intelligence tool designed to streamline academic discovery by retrieving detailed researcher profiles and citation metrics from the Scopus database. By providing simple search options—either by author name or ORCID ID—users can access up-to-date academic data without manually browsing through complex interfaces.

The tool is particularly useful for students, academics, and research administrators who require fast, reliable access to publication and citation statistics for academic evaluation, networking, or bibliometric analysis.

The project integrates with the Elsevier Scopus API to ensure accurate and authoritative information. Since Scopus data is widely used in academic evaluation, Lookup provides a valuable bridge between command-line tools and trusted scholarly databases.

---

## 🎯 Project Goals
The primary objectives of Lookup were:

- Simplified Access – Reduce the complexity of searching Scopus by allowing researchers to query directly from the terminal.

- Accurate Metrics – Provide citation counts and affiliations directly from the official API.

- Flexible Search – Enable lookups by first and last name or by ORCID ID.

- API Key Management – Allow the user to set their Scopus API key once, avoiding repeated authentication steps.

---
## 🗂 File Structure and Roles

The project currently consists of two main files:

- **`lookup.py`** – Core Python script containing all main functionalities.  
- **`requirements.txt`** – Dependency list for running the project.

---

### 1. `lookup.py`

This is the primary executable script.  

#### **Imports**
- `requests` – Handles API communication.  
- `argparse` – Parses command-line arguments.  
- `sys` – Manages system exits and error handling.  

#### **Global Variables**
- `API_KEY` – Stores the user's Scopus API key.  
- `HEADERS` – Defines HTTP headers required for API requests.  

#### **Functions**
- **`get_info_by_name(last_name, first_name, orcid=None)`**  
  Retrieves researcher details based on last and first names.  
  If an ORCID is provided, only matching profiles are returned.

- **`get_citations_by_id(id)`**  
  Fetches the total citation count for a given Scopus Author ID.

- **`get_info_by_orcid(orcid_id)`**  
  Retrieves basic author details (first and last name) from an ORCID identifier.

- **`insert_api_key(api_key, filename)`**  
  Updates the script to store the API key permanently.

- **`check_api_key()`**  
  Ensures that an API key is set before running queries.

- **`main()`**  
  Entry point of the program, parses arguments, and runs the appropriate functions.

---

### 2. `requirements.txt`

- Contains all dependencies required to run the project.

---

## ⚙️ Installation and Setup

Clone the repository
```bash
git clone https://github.com/your-username/lookup.git
cd lookup
```

Install dependencies:

```bash
pip install -r requirements.txt
```
---

## 🔑 Setting Up Your Scopus API Key

To use Lookup, you need a Scopus API key:

1. Register for an API key at the [Elsevier Developer Portal](https://dev.elsevier.com/).

2. Once you have your API key, run the script once to save it locally:


```bash
python lookup.py --api_key YOUR_SCOPUS_API_KEY
```

**You only need to do this once. After setting the key, you can run other commands without specifying the API key again.**

---

## 🚀 Usage Example

Search by first name and last name:

```bash
python lookup.py --last Nakamura --first Yasukazu
```

Or search by ORCID id:

```bash
python lookup.py --orcid 0000-0002-6782-5715
```
---

## 💡 Design Decisions

Several key design choices shaped this project:

- **Command-Line Interface (CLI)**  
  I chose a CLI instead of a GUI for speed, simplicity, and lower system requirements. Researchers often work in environments where quick terminal commands are preferred.

- **API Key Persistence**  
  I implemented `insert_api_key()` so that the user only needs to set the API key once. This avoids frustration from repeatedly typing it.

- **Error Handling**  
  The tool provides clear messages when searches fail due to missing API keys, incorrect names, or invalid ORCID IDs. This ensures users understand what went wrong without sifting through raw API responses.

- **Structured Output**  
  I used line separators and labeled fields so that the results are easy to read. For example, citations, affiliation, city, and country are clearly separated.

- **Optional ORCID Matching**  
  Since many researchers share similar names, I included optional ORCID verification within the name search function to ensure accuracy.

---

  ## 📈 Possible Improvements

Future enhancements could include:

- **Publication List Retrieval** – Returning titles, journals, and publication years.  
- **Export to CSV/JSON** – Allowing citation data to be saved for further analysis.  
- **Batch Processing** – Supporting multiple researchers from a file.  
- **Integration with Other Databases** – Adding PubMed or Web of Science search capability.  

---

## 🙌 Conclusion

Lookup successfully meets its core goal: enabling fast, reliable, and user-friendly access to Scopus researcher profiles. By combining a minimalistic CLI interface with robust API integration, it provides an efficient academic discovery tool for researchers and administrators. While future improvements could expand its features, the current version is already a practical and time-saving solution for bibliometric analysis.

