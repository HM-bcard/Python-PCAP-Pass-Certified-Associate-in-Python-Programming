import random

def generate_tickets(ticket_count, max_number):
    
    tickets = []
    for i in range (ticket_count):
        tickets.append(random.randint(0,max_number))
    
        
    
    return(tickets,random.choice(tickets))


print(generate_tickets(10,6))
