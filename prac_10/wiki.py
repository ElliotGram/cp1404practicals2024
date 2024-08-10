import wikipedia


def main():
    title = input("Enter page title: ").strip()
    while title != "":
        if title != "":
            get_wikipedia_page_details(title)
    print("Thank you.")

def get_wikipedia_page_details(title):

if __name__ == "__main__":
    main()
