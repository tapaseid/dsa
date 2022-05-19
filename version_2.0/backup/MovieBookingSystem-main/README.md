# MovieBookingSystem
Low Level Design of movie booking system

Below is what we discussed :

Entities:
UserAccount
City
Search
Movies
Theatre
Seats
Payment gateway
GenerateTicket
Notifications

UserAccount
    UserID(Integer)
    Password(string)
    History(Map)
    
City
    Name(String)
    State(String)
    
Search
    searchInput(String)
     
Movies
    Name(String)
    Cast(vector<string>)
    Description(String)
    Genre(String)
    ReleaseDate(String)
    Language(String)
    
Theatre
    Name(String)
    TimeSlots(vector<DateTime>
    Address(String)
    Movie(Movies Object)
    IsAvailable(Bool)
    Seats(Seat Object)
    
Seat
    ID(String)
    IsSeatAvailable(Bool)
    SeatType(String)
    
PaymentGateway
    Amount(Double)
    TransactionID(String)
    Status(Bool)
    
GenerateTicket
    TransactionID(String)
    Movies(String)
    Theatre(String)
    Seats(vector<Seat>)
    City(String)
    Amount(String)
