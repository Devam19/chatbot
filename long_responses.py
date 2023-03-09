import random
R_RANK="VIT University ranks in the top colleges in India!"
R_ADMIT="In order to confirm your seat at VIT, you need to appear for VITEEE!!"
R_ABOUT="VIT is a college in Vellore that offers courses in various fields"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
