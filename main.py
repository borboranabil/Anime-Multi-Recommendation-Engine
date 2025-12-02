from pathlib import Path

from recommender import (
    load_items,
    build_tfidf_matrix,
    resolve_title_to_index,
    recommend_content,
)

DATA_DIR = Path(__file__).parent / "data"


# ----------------------------
# Menu helpers
# ----------------------------

def choose_mode():
    print("=== Anime / Manga / Manhwa Recommendation Engine ===")
    print("Select mode:")
    print("  1) Anime")
    print("  2) Manga")
    print("  3) Manhwa")

    while True:
        choice = input("Enter choice (1/2/3 or q to quit): ").strip().lower()
        if choice in {"q", "quit", "exit"}:
            return None
        if choice in {"1", "2", "3"}:
            return choice
        print("Invalid choice, please try again.\n")


def get_csv_for_mode(choice: str) -> Path:
    if choice == "1":
        return DATA_DIR / "anime.csv"
    elif choice == "2":
        return DATA_DIR / "manga.csv"
    elif choice == "3":
        return DATA_DIR / "manhwa.csv"
    else:
        raise ValueError(f"Unknown mode: {choice}")


def choose_top_n(default: int = 5) -> int:
    print("\nHow many recommendations do you want for each query?")
    raw = input(f"Enter a number (press Enter for default = {default}): ").strip()
    if not raw:
        return default
    try:
        n = int(raw)
        if n <= 0:
            print("Top-N must be positive; using default value.")
            return default
        return n
    except ValueError:
        print("Invalid number; using default value.")
        return default


# ----------------------------
# Core loop for one dataset
# ----------------------------

def run_recommender(csv_path: Path):
    print(f"\nLoading dataset from: {csv_path} ...")
    items = load_items(csv_path)
    _, matrix = build_tfidf_matrix(items)

    print(f"Loaded {len(items)} items.\n")

    # Ask user once for top-N
    topn = choose_top_n(default=5)

    print("\nYou can now:")
    print("  - Enter an item_id (e.g., 1)")
    print("  - OR type a title (e.g., Naruto)")
    print("  - OR 'b' to go back, 'q' to quit.\n")

    # Show a small preview of items
    print("Some available titles:")
    preview = items[["item_id", "title"]].head(10)
    print(preview.to_string(index=False))

    while True:
        raw = input("\nEnter item_id or title (or 'b' to go back, 'q' to quit): ").strip()
        if not raw:
            continue

        lower = raw.lower()
        if lower in {"q", "quit"}:
            return "quit"
        if lower in {"b", "back"}:
            return "back"

        # Case 1: numeric item_id
        if raw.isdigit():
            item_id = int(raw)
            matches = items.index[items["item_id"] == item_id].tolist()
            if not matches:
                print("No item with that item_id. Try again.")
                continue
            idx = matches[0]
            base_title = items.loc[idx, "title"]

        # Case 2: treat as title query
        else:
            idx, matched_title = resolve_title_to_index(items, raw)
            if idx is None:
                print("Could not find any title similar to that. Try again.")
                continue
            item_id = int(items.loc[idx, "item_id"])
            base_title = matched_title
            print(f"Using best match: '{matched_title}' (item_id={item_id})")

        # Get recommendations
        recs = recommend_content(items, matrix, item_index=idx, topn=topn)

        print(f"\nRecommendations for: {base_title} (item_id={item_id})")
        print("-" * 80)
        print(recs.to_string(index=False))


# ----------------------------
# Main entry
# ----------------------------

def main():
    while True:
        mode = choose_mode()
        if mode is None:
            print("Goodbye!")
            break

        csv_path = get_csv_for_mode(mode)
        action = run_recommender(csv_path)

        if action == "quit":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
