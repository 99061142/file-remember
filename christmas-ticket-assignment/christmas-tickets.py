import json
from datetime import datetime
from random import choice


# Ask the user all the names
def get_names():
    names = []

    choosing_names = True


    # If the user is choosing names
    while choosing_names:
        name = input("Kies een naam om toe te voegen (als je wilt stoppen typ 'stop'): ")

        # If the user typed 'stop'
        if name == 'stop':
            # If the user chose already 2 names
            if len(names) >= 2:
                choosing_names = False # Stop the question
        
            # If the user did not chose already 2 names
            else:
                print("U moet meer dan 2 spelers hebben toegevoegd om te stoppen") # Error message
        else:
            # If the name is not already chosen
            if name not in names and len(name) > 0:
                # Add the name to the dictionary
                names.append(name)

            # If the name is already chosen
            else:
                print(f"De naam {name} is al gekozen, of de lengte van de naam is kleiner 0", end="\n") # Error message

    # If the user did not want to add more names
    else:
        return names # Return all the names


# Give a person another person to make a christmas present
def get_tickets(names):
    ticket_information = {} # Make a dictionary to store the tickets
    possible_names = names.copy()

    # For every name that is chosen
    for index, name in enumerate(names):
        random_name_choosing = True # When the random name is the same as the name that need a ticket

        while random_name_choosing:
            key_name = f"person_{index + 1}"

            random_name = choice(possible_names) # Choose a random name

            # If the name is not the same, and the name is not already used
            if random_name != name and random_name in possible_names:
                possible_names.remove(random_name)
                ticket_information[key_name] = {}
                ticket_information[key_name]['person'] = name
                ticket_information[key_name]['random_person'] = random_name # Add the random name to the personst ticket
                
                random_name_choosing = False # Go to the next person

    return ticket_information # Return the dictionary with all the persons and the person they got


def make_json_tickets(ticket_information):    
    json_tickets = json.dumps(ticket_information) # Set tdictionary to string

    time = datetime.now() # Get the local time

    # Get all the specific information about the local time
    year = time.year
    month = time.month
    day = time.day
    hour = time.hour
    minute = time.minute
    second = time.second

    # Route information
    time_str = f"{day}-{month}-{year}_{hour}-{minute}-{second}"
    file_name = f"christmas-ticket-assignment/data/{time_str}.txt"
    
    # Make a new file in the data folder
    with open(file_name, "w") as file:
        file.write(json_tickets) # Add the dictionary


    exit()

# Show which person got who
def show_tickets(ticket_information):
    # Show every person their respective ticket
    for person in ticket_information:
        print(f"persoon genaamd '{person}' heeft het lot van de persoon genaamd '{ticket_information[person]}' getrokken ")


# Call all the functions
def main():
    ticket_information = get_names() # Ask all the names
    ticket_information = get_tickets(ticket_information) # Give the persons another persons ticket
    make_json_tickets(ticket_information)
    show_tickets(ticket_information) # Show which person got who




# When the program starts
if __name__ == "__main__":
    main()