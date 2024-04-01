# Movie-Recommendation-System

## Import Libraries:
It uses libraries like numpy, pandas, difflib for data manipulation and matching, TfidfVectorizer from sklearn for feature extraction, and cosine_similarity for calculating similarity scores between movies.

## Mount Google Drive: 
The script demonstrates how to mount Google Drive in Colab for accessing the dataset stored in Drive.

## Data Preprocessing:

1. The movie dataset is loaded into a DataFrame.
2. It handles missing values by filling nulls with empty strings for the selected features.
3. Converts non-string columns to strings and combines selected features into a single string.

## Feature Extraction:
Converts the combined text data into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency), a method that reflects how important a word is to a document in a collection.

## Cosine Similarity: 
Calculates the cosine similarity between the feature vectors of all movies to find how similar they are to each other.

## Recommendation:

1. The user inputs their favorite movie name.
2. The script finds the closest match to the user's input from the dataset using the difflib library.
3. It retrieves the index of the matched movie and then calculates the similarity scores with all other movies.
4. Movies are then sorted based on their similarity scores, and the top recommendations are displayed.


## Example Outputs:
The script demonstrates two examples where the user inputs "Iron man" and "bat man", respectively, and it provides a list of recommended movies based on the input.

## Contributions
Contributions to this project are welcome! Feel free to fork the repository, make improvements, and submit a pull request. If you encounter any issues or have suggestions, please open an issue on the GitHub repository page.
