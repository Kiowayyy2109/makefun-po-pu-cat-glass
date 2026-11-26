import os

LINE = "Your Honour, the glass was already falling when I arrived. I merely supervised gravity, and I would do it again, from a higher shelf."

def main():
    assert len(LINE) == 133, f"line is {len(LINE)} chars, expected 133"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars")

if __name__ == "__main__":
    main()
