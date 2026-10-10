
"""
DecodeLabs Internship - Project 3
AI Recommendation Logic
"""


def main():
    # Items and their categories
    items = {
        "Python Programming Course": {"programming", "ai", "beginner"},
        "Machine Learning Course": {"ai", "machine learning", "data science"},
        "Web Development Course": {"programming", "web development"},
        "Data Science Course": {"data science", "ai", "python"},
        "Graphic Design Course": {"design", "creativity"},
        "Cybersecurity Course": {"security", "networking", "programming"},
    }

    print("=" * 45)
    print("   AI RECOMMENDATION SYSTEM")
    print("=" * 45)
    print("Find courses based on your interests!")
    print("\nAvailable interests:")
    print("programming, ai, beginner, machine learning,")
    print("data science, web development, python, design,")
    print("creativity, security, networking")

    # Get user preferences
    user_input = input(
        "\nEnter your interests separated by commas: "
    ).strip().lower()

    if not user_input:
        print("Please enter at least one interest.")
        return

    preferences = {
        interest.strip()
        for interest in user_input.split(",")
        if interest.strip()
    }

    if not preferences:
        print("No valid interests entered.")
        return

    # Calculate similarity scores
    recommendations = []

    for item_name, categories in items.items():
        matches = preferences.intersection(categories)

        if matches:
            score = len(matches) / len(preferences) * 100
            recommendations.append(
                (item_name, score, matches)
            )

    # Sort by score, highest first
    recommendations.sort(key=lambda item: item[1], reverse=True)

    # Display results
    print("\n" + "=" * 45)
    print("YOUR RECOMMENDATIONS")
    print("=" * 45)

    if recommendations:
        for name, score, matches in recommendations:
            print(f"\nCourse: {name}")
            print(f"Matching interests: {', '.join(sorted(matches))}")
            print(f"Preference match: {score:.1f}%")
    else:
        print("No matching courses found.")
        print("Try interests from the available list.")

    print("\nThank you for using the recommendation system!")


if __name__ == "__main__":
    main()
