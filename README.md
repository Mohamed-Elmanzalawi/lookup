# 🔍 Lookup

**Lookup** is a research intelligence tool that helps you find information on researchers, their publications, and citations. It offers quick access to profiles, citation metrics, and collaboration networks, using data from the Scopus database to support accurate academic discovery and evaluation.

---

## ✨ Features

- **Researcher Search** – Quickly find detailed profiles by author name or Scopus Author ID.  
- **Publication Insights** – View citation counts.
  
---

## 🛠 Installation

Clone the repository:

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

## 🚀 Usage

Search by first name and last name:

```bash
python lookup.py --last Nakamura --first Yasukazu
```

Or search by ORCID:

```bash
python lookup.py --orcid 0000-0002-6782-5715
```
