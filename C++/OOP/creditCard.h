#pragma once

#include <string>


class CreditCard
{
    private:
        std::string customer;
        std::string bank_name;
        int account_number;
        double limit;
        double balance = 0;

    public:

        CreditCard::CreditCard(std::string customer, std::string bank_name, int account_number, double limit)
                  :customer(customer), bank_name(bank_name),
                  account_number(account_number),
                  limit(limit), balance(balance) {};

        CreditCard::~CreditCard();

        std::string CreditCard::getCustomer() const;

        std::string CreditCard::getBankName() const;

        int CreditCard::getAccountNumber() const;

        double CreditCard::getAccountLimit() const;

        double CreditCard::getAccountBalance() const;

        bool CreditCard::getCardCharge(double price);

        double CreditCard::makePayment(double amount);
};