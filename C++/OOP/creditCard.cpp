#include "CreditCard.h"

std::string CreditCard::getCustomer() const
{
    return customer;
}

std::string CreditCard::getBankName() const
{
    return bank_name;
}

int CreditCard::getAccountNumber() const
{
    return account_number;
}

 double CreditCard::getAccountLimit() const
 {
     return limit;
 }

 double CreditCard::getAccountBalance() const
 {
     return balance;
 }

 bool CreditCard::getCardCharge(double price)
 {
     if(price + balance > limit)
     {
             return false;
     }
     else
     {
         balance = balance + price;
         return true;
      }

 }

 double CreditCard::makePayment(double amount)
 {
     double newBalance = balance - amount;
     return newBalance;
 }