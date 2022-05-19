#include <iostream>

using namespace std;

class UserAccount {
  public :
    string userID;
    string password;
    vector<Booking> bookings;   
    
    UserAccount() {
      //Ask user for inputID
      //Ask user for password
    }
  
    Booking DoBooking() {
      Search searchObj = new Search();
      String movieTitle = "Avenger"
      Movie movie = searchObj.GetMovieByTitle(movieTitle);
      //Create Booking object and proceed further
    };
    vector<Booking> GetBookings();
}
