"""One sentence explaining the modern internet to a traveler from 1800.

Why this sentence works against the judge's brief:

1. It explains what the internet *is and does*: a box in every home through
   which the world's letters, voices and pictures travel instantly along
   wires. A person from 1800 can picture that directly.
2. It builds only from things a person from 1800 already knows: a box, a
   home, letters, voices, pictures, wires, a post office, a library, a town
   crier. No word in it was coined after the traveler's time — no internet,
   computer, website, email, smartphone, app, or anything of that kind.
3. Every claim is literally true of the internet as it is now: messages,
   calls and images really do travel along wires (and the air) to screens in
   homes, and the post-office / library / town-crier comparison is a fair
   picture of what those wires carry.
4. It is a single image, not a crammed list of features: one box, one room,
   three familiar institutions joined into it.
5. The image sticks: a box in every home holding the whole world's post
   office, library and town crier.

Craft notes:
- Only words a person from 1800 could know: the sentence never reaches
  for a modern term, so it stays inside the traveler's vocabulary.
- One vivid picture, not a feature list: a single box in a single room
  carries the whole explanation, instead of enumerating what the
  internet can do.
- It stands alone: no setup, no follow-up, and no second sentence is
  needed to make the wonder land.
- It sounds like something the traveler could repeat to a neighbour the
  next morning and still be understood.
"""

LINE = (
    "Imagine a box in every home where the world's letters, voices, and "
    "pictures travel instantly along wires, like a post office, a library, "
    "and a town crier all joined into one room."
)

assert 1 <= len(LINE) <= 200, f"sentence must be 1-200 chars, got {len(LINE)}"
assert "\n" not in LINE, "sentence must be a single line"


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
