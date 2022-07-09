# Find image online based on user input.

# Import the necessary modules
import webbrowser


def welcome_message():
    # Print the welcome message
    print("Welcome to the Python Image Search!")
    print("")


def author():
    # Print the author username
    print("Author: @SunlightKim")
    print("")


def software_info():
    # Print the software info
    print("Python Image Search")
    print("Version: 1.0")
    print("")

    # Print the software license
    print("This software is licensed under the MIT license.")
    print("")

    # Print the software disclaimer
    print("This software is not intended to be used for malicious purposes.")
    print("")


def search_image():
    # Ask user to describe the image they want to search for
    print("Please describe the image you want to search for:")
    user_input = input()

    # Lookup the image on Google Images
    url = "https://www.google.com/search?q=" + user_input + "&source=lnms&tbm=isch"

    # Display the image
    webbrowser.open(url)


def search_again():
    # Ask user if they want to search for an image again
    print("Would you like to search for an image again? (y/n)")
    user_input = input()
    if user_input == "y":
        search_image()
    elif user_input == "n":
        print("Thank you for using the Python Image Search!")
        print("")
        print("Have a nice day!")
        print("")
        # Exit the program
        exit()
    else:
        print("Invalid input.")
        search_again()


def main():
    # Print the welcome message
    welcome_message()

    # Print the author info
    author()

    # Print the software info
    software_info()

    # Search for the image
    search_image()

    # Ask user if they want to search for an image again
    search_again()


main()
