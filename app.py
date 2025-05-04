from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# Load the data and print debug information
print("Loading data files...")
popular_df = pickle.load(open('popular.pkl','rb'))
print("\nPopular books DataFrame:")
print(f"Shape: {popular_df.shape}")
print("First few books:")
print(popular_df[['Book-Title', 'Book-Author']].head())

pt = pickle.load(open('pt.pkl','rb'))
print("\nPivot table:")
print(f"Shape: {pt.shape}")
print("First few indices:")
print(pt.index[:5])

books = pickle.load(open('books.pkl','rb'))
print("\nBooks DataFrame:")
print(f"Shape: {books.shape}")
print("First few books:")
print(books[['Book-Title', 'Book-Author']].head())

similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))
print("\nSimilarity scores:")
print(f"Shape: {similarity_scores.shape}")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    print(f"\nSearching for book: '{user_input}'")
    
    try:
        # Convert both to lowercase for case-insensitive comparison
        user_input_lower = user_input.lower()
        pt_index_lower = [x.lower() for x in pt.index]
        
        # Find matches (case-insensitive)
        matches = [i for i, title in enumerate(pt_index_lower) if user_input_lower in title]
        
        print(f"Found {len(matches)} matches")
        if matches:
            print(f"First match: {pt.index[matches[0]]}")
        
        if not matches:
            # Print debug information
            print(f"User input: {user_input}")
            print(f"First few books in database: {list(pt.index)[:5]}")
            print(f"Sample of book titles in database: {[x for x in pt.index if len(x) < 50][:5]}")
            return render_template('recommend.html', data=[], error="Book not found in our database. Please try another book.")
            
        # Use the first match
        index = matches[0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data.append(item)

        print(f"Generated {len(data)} recommendations")
        return render_template('recommend.html', data=data)
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print(f"Error type: {type(e)}")
        import traceback
        print(traceback.format_exc())
        return render_template('recommend.html', data=[], error="An error occurred while processing your request. Please try again.")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)