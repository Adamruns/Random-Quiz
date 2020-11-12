from Question import Question

question_prompts = [
    "What is the most densely populated U.S. state?"
    "\n(a) Connecticut\n(b) New Jersey\n(c) Rhode Island\n(d) Maryland\n\n",
    "Where in the US is the Petrified Forest?"
    "\n(a) Arizona\n(b) Arkansas\n(c) California\n(d) Nevada\n\n",
    "Where was Albert Einstein born?"
    "\n(a) Germany\n(b) United States\n(c) France\n(d) Mexico\n\n",
    "Which vegetable gives Popeye his strength?"
    "\n(a) Broccoli\n(b) Spinach\n(c) Asparagus\n(d) Lentils\n\n",
    "Who was the ancient Greek goddess of love and beauty?"
    "\n(a) Aphrodite.\n(b) Calliope.\n(c)Athena.\n(d) Calypso.\n\n",
    "What does the Q in IQ stand for?"
    "\n (a)Quantity.\n(b) Quorum.\n(c) Quality.\n(d) Quotient.\n\n",
    "What is the name of Superman’s home planet?"
    "\n(a) Argon.\n(b) Rann.\n(c) Krypton.\n(d) Qward.\n\n",
    "What is the Latin word for “beyond”, often used as a prefix to signify an extreme?"
    "\n(a) Extra.\n(b) Super.\n(c) Ultra.\n(d) Mega.\n\n",
    "Bronze is mainly an alloy of tin and which other metal?"
    "\n(a) Brass.\n(b) Lead.\n(c) Iron.\n(d) Copper.\n\n",
    "In meteorology, what name is given to a line of equal pressure on a map?"
    "\n(a) Isotherm.\n(b) Isobar.\n(c) Isochor.\n(d) Isoquant.\n\n",
    "In which U.S. national park is the Old Faithful geyser found?"
    "\n(a) Yellowstone.\n(b) Death Valley.\n(c) Yosemite.\n(d) Carlsbad Caverns.\n\n",
    "Casablanca is the largest city in which African country?"
    "\n(a) Egypt.\n(b) Morocco.\n(c) Tunisia.\n(d) Algeria.\n\n",
    "What is the largest freshwater lake in the world by surface area?"
    "\n(a) Lake Superior.\n(b) Lake Victoria.\n(c) Lake Tanganyika.\n(d) Lake Baikal.\n\n",
    "What is the national flower of Scotland?"
    "\n(a) Heather.\n(b) Gorse.\n(c) Bluebell.\n(d) Thistle.\n\n",
    "Who was Roman emperor at the time of Christ’s crucifixion?"
    "\n(a) Nero.\n(b) Pontius Pilate.\n(c) Tiberius.\n(d) Julius Caesar.\n\n",
    "In what year did the Bay of Pigs invasion take place?"
    "\n(a) 1959.\n(b) 1961.\n(c) 1963.\n(d) 1965.\n\n",
    "What was the name of the first spacecraft to land on the moon?"
    "\n(a) Spider.\n(b) Eagle.\n(c) Intrepid.\n(d) Falcon.\n\n",
    "What is the name of the winged horse of Greek legend?"
    "\n(a) Centaur.\n(b) Hippocampus.\n(c) Pegasus.\n(d) Unicorn.\n\n",
    "Where was the second atomic bomb dropped in World War 2?"
    "\n(a) Nagasaki.\n(b) Hiroshima.\n(c) Osaka.\n(d) Yokohama.\n\n",
    "What is the capital city of Ukraine?\n(a) Kiev.\n(b) Vilnius.\n(c) Minsk.\n(d) Pristina.\n\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "d"),
    Question(question_prompts[6], "c"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "d"),
    Question(question_prompts[9], "b"),
    Question(question_prompts[10], "a"),
    Question(question_prompts[11], "b"),
    Question(question_prompts[12], "a"),
    Question(question_prompts[13], "d"),
    Question(question_prompts[14], "c"),
    Question(question_prompts[15], "b"),
    Question(question_prompts[16], "b"),
    Question(question_prompts[17], "c"),
    Question(question_prompts[18], "a"),
    Question(question_prompts[19], "a"),

]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            print("Correct")
        else:
            print("Incorrect")

    print("You got " + str(score) + "/" + str(len(questions)) + " Correct!")
    if score < 5:
        print("Better luck next time...")
    elif 6 < score < 10:
        print("You can do better")
    elif 11 < score < 16:
        print("You are Aight")
    elif 16 < score <= 20:
        print("You're a genius bro")


run_test(questions)
