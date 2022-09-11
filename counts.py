import glob


easy_count = glob.glob("./leetcode_easy/*.py")
medium_count = glob.glob("./leetcode_medium/*.py")
hard_count = glob.glob("./leetcode_hard/*.py")

easy_total = 592
medium_total = 1285
hard_total = 530

result = """
## Let's solve all the Leetcode problems

### Easy Progress
* {easy_count}/{easy_total}

### Medium Progress
* {medium_count}/{medium_total}

### Hard Progress
* {hard_count}/{hard_total}
""".format(
    easy_count=len(easy_count),
    easy_total=easy_total,
    medium_count=len(medium_count),
    medium_total=medium_total,
    hard_count=len(hard_count),
    hard_total=hard_total
)

with open("README.md", 'w') as outfile:
    outfile.write(result)
