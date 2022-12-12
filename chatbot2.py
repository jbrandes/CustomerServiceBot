

Name = input("Thank you for visiting the LS Electric home page. What is your name? ")

#To help the user navigate our site
def choice():
    if X == '1':
        print("For assistance with our products please call 800-891-2941 or email tech_support.us@lselectricamerica.com")
    elif X == '2':
        print("You can find our products on our main product finder website at https://pfinder.ls-electric.com/")
    elif X == '3':
        region()
        exit()
        
#A breakdown of each region for the sales rep           
def region():
    Location = input("What state are you located in " + Name + "? ")
    West = ("CA", "AZ", "NV", "OR", "ID", "UT", "MT", "WY", "CO", "WA")
    South = ("NM", "TX", "OK", "AR", "LA")
    East = ("MS", "AL", "FL", "TN", "SC", "GA", "NC", "WV","VA","PA", "NY", "VT", "ME", "NH", "MA", "RI")
    Midwest = ("IL", "WI", "IA", "KS", "NE", "SD", "ND", )
    if Location in West:
        print("Your sales rep is James Van Cura. He can be reached at 224-352-2255")
    if Location in South:
        print("Your sales rep is Mike Ellisor. He can be reached at 832-833-6113")
    if Location in East:
        print("Your sales rep is Paul Morrison. He can be reached at pmorrison@lselectricamerica.com.")
    if Location in Midwest:
        print("Your sales rep is David Waite. He can be reached at (847) 521-8700")
    

while True:
    X = input("It is nice to meet you today " + Name +  " what can I help you find? Press which category you would like to navigate to: 1 - Tech Support 2 - Find a Product 3 - Sales " + ".\n")
    choice()
    exit()
