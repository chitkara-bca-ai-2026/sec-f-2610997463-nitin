books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering"),
]

library_categories = set()
for title, author, year, category in books:
    library_categories.add(category)

student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

print("=" * 50)
print("LIBRARY BOOK & CATEGORY MANAGER")
print("=" * 50)

while True:
    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")
    print()
    choice = input("Enter your choice (1-6): ").replace(" ", "")

    if choice == "1":
        print("\n--- Current Library Catalog (Fixed Records) ---")
        n = 1
        for title, author, year, genre in books:
            print(f'{n}. "{title}" by {author} ({year}) | Genre: {genre}')
            n += 1
        print(f"Total Books: {len(books)}")

    elif choice == "2":
        print("\n--- Add New Book Record ---")
        title = input("Enter book title: ").replace(" ", "")
        author = input("Enter author name: ").replace(" ", "")
        year = input("Enter publication year: ").replace(" ", "")
        category = input("Enter category/genre: ").replace(" ", "")

        new_book = (title, author, year, category)
        books.append(new_book)
        library_categories.add(category)

        print()
        print(f'[SUCCESS] "{title}" added as an immutable catalog record.')
        print(f'[INFO] Category set updated with: "{category}"')

    elif choice == "3":
        print("\n--- Unique Categories Available in Library (Set) ---")
        for cat in sorted(library_categories):
            print(f" - {cat}")
        print(f"Total Unique Genres: {len(library_categories)}")

    elif choice == "4":
        print("\n--- Add to Student Wishlist ---")
        cat = input("Enter requested category: ").replace(" ", "")
        student_wishlist.add(cat)
        print(f'[SUCCESS] "{cat}" added to student wishlist.')

    elif choice == "5":
        print()
        print("============== CATEGORY GAP ANALYSIS ==============")
        print(f"Library Holdings (Set): {sorted(library_categories)}")
        print(f"Student Wishlist (Set): {sorted(student_wishlist)}")
        print("-" * 50)

        common = library_categories & student_wishlist
        missing = student_wishlist - library_categories
        all_genres = library_categories | student_wishlist

        print(f"1. Already in Stock (Intersection &):")
        print(f"   {sorted(common)}")
        print()
        print(f"2. Purchase Order Needed (Difference -):")
        print(f"   {sorted(missing)}")
        print()
        print(f"3. Full Combined Genre Coverage (Union |):")
        print(f"   {sorted(all_genres)}")
        print("=" * 50)

    elif choice == "6":
        print("\nThank you for using the Library Manager. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter 1-6.")