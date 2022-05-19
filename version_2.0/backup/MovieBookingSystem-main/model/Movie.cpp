#include <iostream>

using namespace std;

class Movie {
  public :
    int movieID;
    string Name;
    vector<string> cast;
    string description;
    Genre genre;
    Date releaseDate;
    Language language;
    unordered_map<Date, Theatre> DateTheatreMap;
    
    Movie() {
      //set Movie-ID
    }
    
    int getMovieID();
    
    String getMovieName();
    void setMovieName(String movieName);
    
    vector<String> getCast();
    void setCast(vector<string> cast);
    
    string getDescription();
    void setDescription(string description);
    
    Genre getGenre();
    void setGenre();
    
    Date getReleaseDate();
    void setReleaseDate(Date date);
    
    Language getLanguage();
    void setLanguage(Language language);
    
    void setTheatre(Date date, Theatre theatre);
    vector<Theatre> getTheatre(Date date);
    
}
