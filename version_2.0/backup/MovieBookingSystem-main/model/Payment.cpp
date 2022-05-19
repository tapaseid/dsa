#include <iostream>

using namepsace std;

class Payment {
  public:
    int paymentID;
    int amount;
    PaymentMode mode;
    UserAccount user;
    Date paymentDate;
    PaymentStatus paymentStatus;
    
    void makePayment();
    
}
