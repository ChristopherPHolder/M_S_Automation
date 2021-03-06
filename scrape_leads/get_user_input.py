import pandas as pd

def get_wordlist_ql():
    wordlistfile = input("Insert wordlist: ")
    if wordlistfile == "":
        print("The default wordlist used")
        wordlistfile = "wordlist"
        return wordlistfile

def get_wordlist_locations():
    wordlistfile = input("Insert wordlist for locations: ")
    if wordlistfile == "":
        print("The default wordlist used")
        wordlistfile = "all_german_cities"
    return wordlistfile
    
def open_wordlist(wordlistfile):   
    try: 
        wordlist = pd.read_excel("wordlist/" + wordlistfile + ".xlsx")
        print("Succesfully imported wordlist from: " + wordlistfile)
        return wordlist

    except FileNotFoundError:
        print("\nError: Wordlist file not found!")
        print("Check if you did any typos and that the file is in the correct folder.\
            \nOnce you found the error, try to run the program again.\
            \nRemeber you can leave the field blank and it will use wordlist.xlsx \n")
        quit()

# Import leads data
def get_leadsfile_ql():
    leadsfile = input("\nInsert leads: ")
    
    # Import generic file for testing
    if leadsfile == "t":
        print("The the testing leads file was used.")
        leadsfile = "steuerberater_kärnten_test"
    try:
        df = pd.read_excel("leads/" + leadsfile + ".xlsx")
        print("Succesfully imported leads from: " + leadsfile + ".xlsx")
        return leadsfile

    except FileNotFoundError:
        print("\nError: leads file not found!\
            \n Check if you did any typos and that the file is in the correct folder\
            \nOnce you found the error, try to run the program again.")
        quit()

    except AssertionError:
        print("\nA leads file is necesarry for this program. No file name was provided.\n")
        quit()

    except IsADirectoryError:
        print("\nA leads file is necesarry for this program. No file name was provided.\n")
        quit()

def get_company_type():
    companytype = input("Enter the company type: ")
    if companytype == "":
        print("Company type was left empty")
        return companytype
    
    return companytype

def get_company_location():
    location = input("Enter the location: ")

    if location == "":
        print("Company location was left empty")

    return location

def get_search_limit():
    limit = int(input("Enter the percentage (number 0-100) of results to export: "))
    if limit == "":
        print("Default 100 percent search extraction was set")
        limit = 100
        return limit
    
    elif  0 < limit > 100:
        return limit

def open_excel():
    leadsfile = input("\nInsert leads: ")
    
    # Import generic file for testing
    if leadsfile == "t":
        print("The the testing leads file was used.")
        leadsfile = "steuerberater_kärnten_test"
    try:
        df = pd.read_excel("leads/" + leadsfile + ".xlsx")
        print("Succesfully imported leads from: " + leadsfile + ".xlsx")
        return df

    except FileNotFoundError:
        print("\nError: leads file not found!\
            \n Check if you did any typos and that the file is in the correct folder\
            \nOnce you found the error, try to run the program again.")
        quit()