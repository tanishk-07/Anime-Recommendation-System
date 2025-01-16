# Anime Recommendation System

## Overview

This project is an **Anime Recommendation System** that suggests anime titles based on user preferences. The user inputs the name of an anime, and the system provides a list of similar anime by comparing the input with an extensive dataset using a machine learning model.

## Features

- Accepts user input for an anime title.
- Recommends similar anime based on the given title.
- Uses machine learning to calculate the similarity between anime titles.
- Provides personalized recommendations tailored to user interests.

## How It Works

1. **Input:** The user provides the name of an anime.
2. **Data Matching:** The system compares the input anime with entries in the dataset.
3. **Similarity Calculation:** A machine learning model evaluates how closely the input anime matches others in the dataset.
4. **Recommendations:** The system outputs a list of anime similar to the user's input.

## Machine Learning Model

- The model uses a similarity-based algorithm to calculate closeness between anime titles.
- It leverages natural language processing (NLP) techniques for text similarity.
- The dataset contains features such as anime titles, genres, descriptions, and user ratings to improve accuracy.

## Requirements

To run this project, ensure you have the following installed:

- Python 3.8 or higher
- Pandas
- NumPy
- Scikit-learn
- NLTK or SpaCy (for NLP preprocessing)

You can install the required libraries using:

```bash
pip install pandas numpy scikit-learn nltk
```

## Dataset

- The dataset includes a collection of anime titles with metadata such as genres, ratings, and descriptions.
- Ensure the dataset is in a CSV format and properly preprocessed before running the system.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Anime-Recommendation-System.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Anime-Recommendation-System
   ```


## Usage

1. Run the recommendation script:
   ```bash
   python app.py
   ```
2. Enter the name of an anime when prompted.
3. View the list of recommended anime.

## Example

**Input:**

```
Sword Art Online
```

**Output:**

```
Recommended Anime:
1)Sword Art Online
2)Cardfight!! Vanguard
3)Sword Art Online Movie: Ordinal Scale
4)Sword Art Online II
5)Kyuukyoku Shinka shita Full Dive RPG ga Genjitsu yori mo Kusoge Dattara
6)Sword Art Online: Progressive Movie - Hoshi Naki Yoru no Aria
```

##

## Future Enhancements

- Incorporate user feedback to refine recommendations.
- Add support for multiple input anime for enhanced recommendations.
- Expand the dataset with more anime titles and metadata.
- Integrate a web-based user interface.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Anime dataset: [Source of dataset]
- Libraries: Pandas, Scikit-learn, NLTK/SpaCy

---

Feel free to contribute to this project or suggest improvements!

