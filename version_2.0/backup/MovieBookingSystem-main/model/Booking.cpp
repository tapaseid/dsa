#include <iostream>

using namespace std;

class Booking {
  public:
  int bookingID;
  Date bookingDate;
  Movie movie;
  Theatre theatre;
  int amount;
  GenerateTicket ticket;
  BookingStatus bookingStatus;
  
  //UserAccount and Booking share composition relationship
  UserAccount user;
  
  Booking() {
    //generateBookingID
    //bookingDate = TimeStamp
    //Copy current user details
    //Set bookingStatus = INITIALISED
    //user = this
  }
  
  int getBookingID(this);
  
  Movie getMovie();
  void setMovie(Movie movie);
  
  Theatre getTheatre();
  void setTheatre(Theatre theatre);
  
  int getBookingAmount();
  void setBookingAmount(int amount);
  
  int getBookingDate();
  void setBookingDate(Date bookingDate);
  
  BookingStatus getBookingStatus();
  void setBookingStatus(BookingStatus bookingStatus);
  
  bool isTicketGenerated();
  GenerateTicket getTicket();
  void setTicket(GenerateTicket ticket);
  
}
