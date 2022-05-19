#include <iostream>

using namespace std;

class Seat {
  int seatID;
  SeatType seatType;
  int amount
  SeatStatus status;
  
  Seat() {
    //Set seatID
    //Set seatType
    //set SeatStatus as AVAILAIBLE
    //Based on type set amount
  }
  
  void setSeatStatus(SeatStatus status);
  SeatStatus getSeatStatus();
}
