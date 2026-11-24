import os

LINE = "★☆☆☆☆ Swapped my usual food for a cheaper knock-off brand and expected me not to notice. I noticed. The cardboard box it came in tastes better than the food."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
