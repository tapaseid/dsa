#include <iostream>

using namespace std;

class Theatre {
  public:
    string ID;
    string name;
    Address address;
    unordered_map<Date, Movie> dateMovieMap;
    
    vector<Movie> getMovies(string date);
}
