def filter_movies_by_genre(genre_list, movies_data):
    """
    Filters movies based on provided genres.
    Parameters:
    genre_list (list): List of genres to filter movies.
    movies_data (dict): Dictionary containing movie data with associated genres.
    Returns:
    list: List of filtered movies.
    """
    filtered_movies = []
    for movie, genres in movies_data.items():
        # Check if all genres in genre_list are present in the movie's genres
        if all(genre.lower() in [g.lower() for g in genres] for genre in genre_list):
            filtered_movies.append((movie, genres))
    return filtered_movies


def main():
    """
    Main function to run the program.
    """
    # Movie data with associated genres
    movies_data = {
        "Inception": ["mind-bending", "thrilling", "suspenseful", "violent", "thoughtful", "sci-fi"],
        "The Shawshank Redemption": ["inspiring", "dramatic", "hopeful", "thoughtful", "drama"],
        "The Matrix": ["action-packed", "sci-fi", "dystopian", "violent"],
        "Forrest Gump": ["heartwarming", "feel-good", "inspirational", "happy"],
        "The Dark Knight": ["intense", "dark", "suspenseful", "action-packed"],
        "Pulp Fiction": ["edgy", "quirky", "non-linear", "violent"],
        "Interstellar": ["epic", "thought-provoking", "emotional", "sci-fi"],
        "The Godfather": ["classic", "intense", "gripping", "drama"],
        "Eternal Sunshine of the Spotless Mind": ["surreal", "romantic", "thoughtful", "drama"],
        "Fight Club": ["gritty", "mind-bending", "dark", "violent"],
        "The Pursuit of Happyness": ["inspiring", "drama", "sad"],
        "12 Angry Men": ["intense", "angry", "drama"],
        "Inside Out": ["emotional", "animated", "happy"],
        "Schindler's List": ["dramatic", "emotional", "sad", "drama"],
        "Grave of the Fireflies": ["emotional", "animated", "sad"],
        "La La Land": ["romantic", "happy", "uplifting"],
        "Toy Story": ["animated", "family", "heartwarming"],
        "The Lion King": ["animated", "family"],
        "Finding Nemo": ["animated", "family", "heartwarming"],
        "The Avengers": ["action-packed", "superhero", "entertaining"],
        "Heat": ["action-packed", "dramatic", "violent"],
        "The Notebook": ["romantic", "drama", "heartfelt"],
        "Titanic": ["romantic", "drama"],
    }

    previous_movies = []

    while True:
        # Display available genres
        print("\nAvailable genres:")
        for genre in sorted(set(sum(movies_data.values(), []))):
            print("-", genre.capitalize())

        # Prompt the user to select genres
        user_input = input("\nEnter the genre(s) you want to watch (comma-separated, no spaces) or type 'exit' to quit: ").strip().lower()
        if user_input == 'exit':
            break

        genre_list = user_input.split(',')

        # Filter movies based on selected genres
        filtered_movies = filter_movies_by_genre(genre_list, movies_data)
        previous_movies.extend(filtered_movies)

        # Output the list of filtered movies
        if filtered_movies:
            print("\nThe movies that match the given genre(s) are:")
            for movie, genres in filtered_movies:
                print(f"{movie} - Genres: {', '.join(genres)}")

            more_movies = input("\nWould you like to see more movies? (yes/no): ").strip().lower()
            if more_movies != 'yes':
                break
        else:
            print("\nNo movies match the given genre(s).")

    # Output previous movies
    print("\nPrevious movies you've filtered through:")
    for movie, genres in previous_movies:
        print(f"{movie} - Genres: {', '.join(genres)}")


# Call the main function to run the program
if __name__ == "__main__":
    main()
