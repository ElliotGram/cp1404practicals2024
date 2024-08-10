import wikipedia


def main():
    title = input("Enter page title: ").strip()
    while title != "":
        if title != "":
            get_wikipedia_page_details(title)
    print("Thank you.")


def get_wikipedia_page_details(title):
    try:
        page = wikipedia.page(title, autosuggest=False)
        print(f"{page.title}\n{page.summary}\n{page.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(f'Page id "{title}" does not match any pages. Try another id!')
    except wikipedia.exceptions.RedirectError:
        print(f'The page "{title}" redirects to another page. Unable to retrieve information.')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
