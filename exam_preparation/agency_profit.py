company = input()
total_tickets_for_adults = int(input())
total_tickets_for_kids = int(input())
price_ticket_for_adult = float(input())
price_ticket_for_kid = price_ticket_for_adult - price_ticket_for_adult*0.7
taxes = float(input())

profit = (total_tickets_for_adults*(price_ticket_for_adult+taxes)
          + total_tickets_for_kids*(price_ticket_for_kid+taxes))*0.2

print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")
