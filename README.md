# Restaurant Recommender


## Getting Started
The instructions in this section will help you set up and manage a a Python 3.6 virtual environment for this project.

### Create Anaconda Virtual Environment
To create your Python 3.6 Anaconda virtual environment, use

  > conda create -n restaurants python=3.6

### Activating and Deactivating Anaconda Virtual Environment
To activate this environment, use:
  > source activate restaurants

To deactivate this environment, use:
  > source deactivate restaurants

### Installing Python Dependencies
This project depends on a few Python packages. To install them, use:

  > pip install -r requirements.txt


## Data Files
The data files for this project are stored in the `\data\` directory. Accordingly, the notebooks in this projects expects the source data files to reside therein.

- `yelp_academic_dataset_business.csv` contains information about different business (e.g. restaurants)
- `yelp_academic_dataset_review.csv` contains reviews for the businesses in `yelp_academic_dataset_business`.
