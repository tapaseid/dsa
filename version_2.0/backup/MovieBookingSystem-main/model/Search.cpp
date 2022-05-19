#include <iostream>

using namespace std;

class Search {
  public:
    vector<Movie> GetMovieByLanguage(Language language);
    vector<Movie> GetMovieByGenre(Genre genre);
    Movie GetMovieByTitle(String name);
}
