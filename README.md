# Documentation for Preprocessing of Data

## By Ivan Neto

## Purpose

The purpose of this project is to (1) download public medical data about drugs, diseases, and other important medical concepts, and (2) to preprocess these concepts into a dataset that can be later used for querying important information upon user request.

Further, this preprocessing step will create both (1) weighted TF-IDF vectors for each preprocessed document, and (2) unweighted TF-IDF vectors for each preprocessed document. The purpose of the class-weighted TF-IDF scores is to ensure that the class imbalance does not cause a lack of metrics when testing the model.

## Usage/Tutorial

1. Create virtual environment
2. Install packages
3. Run program


The following cell is the file structure of the project.

---

```
.
├──project
|	├── preprocessing
|	|	├── __init__.py
|	|	├── compile_csv.py
|	|	├── fix_sources.py
|	|	├── gather_definitions.py
|	|	├── start.py
|	|	├── unweighted_tfidf.py
|	|	└── weightedt_tfidf.py
|	├── utils
|	|	├── __init__.py
|	|	├── information.py
|	|	└── proceed.py
|	├── testing
|	|	├── __init__.py
|	|	├── visualize_concepts.py
|	|	└── test.py
|	├── main.py
|	├── create_unweighted_tfidf.py
|	├── create_weighted_tfidf.py
|	├── preprocess.py
|	└── scrape.py # WORK IN PROGRESS
```

---

Note: `preprocess.py` runs ONLY the preprocessing, and `scrape.py` runs ONLY the scraping. Meanwhile, `main.py` runs the entire scraping and preprocessing routines sequentially. Equally, `create_unweighted_tfidf.py` and `create_weighted_tfidf.py` both run ONLY the creation of these TF-IDF vectors, as well as saving them into the output file.

Note x2: We already have a scraping module that gathers data for us, just not in this layout. This requires further work, and it is a future feature.

<br>
<br>

# Tutorial

## Step 1: Create virtual environment

Run this step if you <ins>DO NOT</ins> yet have `virtualenv`
```
> python -m pip install virtualenv
```
Now create the virtual environment. I will name it `venv`, but feel free to name it however you like.
```
> virtualenv venv
```

### Windows
Now we can activate the virtual environment. Now that I am using a <ins>WINDOWS</ins> platform
```
> ./venv/Scripts/activate
```

### Unix/macOS
In a <ins>Unix/macOS</ins> platform, we use something along the lines of the following:
```
> source ./venv/bin/activate
```
You should be able to see something like the following:
```
(venv) path/to/working/directory>
```


## Step 2: Install packages

Begin by following step 1, creating and entering a virtual environment.

Now, install the following packages using the pip installs packages (pip)

```
> pip install pandas
> pip install numpy
> pip install cchardet
> pip install lxml
> pip install bs4
> pip install sklearn
> pip install nltk
```

Note: `cchardet` is a package that speeds up the preprocessing of the data by allowing BeautifulSoup (`bs4`) to be more quickly instantiated given a raw HTML string.


## Step 3: Run program

To run the program, you have a few options.

1. If you would like to run the entirety of the program:
   ```
   > python main.py
   ```
2. If you would like to only run the scraping part (WORK IN PROGRESS)
   ```
   > python scrape.py
   ```
3. If you would like to only run the preprocessing part
   ```
   > python preprocess.py
   ```
4. If you would like to only run the creation of TFIDF vectors within the dataset
   ```
   > python create_unweighted_tfidf.py
   ```
   OR
   ```
   > python create_weighted_tfidf.py
   ```

<br>
<br>

NOTE: This is a work in progress, and I still need to add the web scraping part of it into the file structure, etc.