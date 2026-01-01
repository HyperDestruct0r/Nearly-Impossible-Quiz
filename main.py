# =============================
# Questions
# =============================

# ==========================
# ANSI Text Colors
# ==========================
RESET = "\033[0m"

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright colors
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# ==========================
# Background Colors
# ==========================
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# Bright backgrounds
BG_BRIGHT_BLACK = "\033[100m"
BG_BRIGHT_RED = "\033[101m"
BG_BRIGHT_GREEN = "\033[102m"
BG_BRIGHT_YELLOW = "\033[103m"
BG_BRIGHT_BLUE = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN = "\033[106m"
BG_BRIGHT_WHITE = "\033[107m"

# ==========================
# Text Styles
# ==========================
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
REVERSE = "\033[7m"
HIDDEN = "\033[8m"
STRIKETHROUGH = "\033[9m"

# ==========================
# Cursor / Screen Control
# ==========================
CLEAR_SCREEN = "\033[2J"
CLEAR_LINE = "\033[2K"
CURSOR_HOME = "\033[H"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"


questions = [
    {"question": "What is 2 + 2?",
     "choices": ["A) 3", "B) 4", "C) 5", "D) 22"],
     "correct": "B",
     "powerup": None},

    {"question": "Which is heavier: 1 kg of feathers or 1 kg of iron?",
     "choices": ["A) Feathers", "B) Iron", "C) Same", "D) Depends"],
     "correct": "C",
     "powerup": None},

    {"question": "Trick question: Press enter without typing anything!",
     "choices": ["A) Type anything", "B) Press enter", "C) Skip", "D) None"],
     "correct": "B",
     "powerup": "hint"},

    {"question": "I am light as a feather, yet the strongest man can’t hold me. What am I?",
     "choices": ["A) Breath", "B) Air", "C) Shadow", "D) Cloud"],
     "correct": "A",
     "powerup": None},

    {"question": "You see a boat filled with people, yet there isn’t a single person on board. How is that possible?",
     "choices": ["A) All married", "B) Everyone is invisible", "C) The boat is empty", "D) They are ghosts"],
     "correct": "A",
     "powerup": None},

    {"question": "A farmer has 17 sheep, and all but 9 die. How many are left?",
     "choices": ["A) 8", "B) 9", "C) 17", "D) 0"],
     "correct": "B",
     "powerup": None},

    {"question": "I have keys but no locks. I have space but no room. You can enter but can’t go outside. What am I?",
     "choices": ["A) Keyboard", "B) House", "C) Safe", "D) Map"],
     "correct": "A",
     "powerup": None},

    {"question": "Before Mount Everest was discovered, what was the highest mountain on Earth?",
     "choices": ["A) K2", "B) Mount Everest", "C) Kilimanjaro", "D) Denali"],
     "correct": "B",
     "powerup": None},

    {"question": "Two mothers and two daughters went out to eat, everyone ate one slice of pizza, yet only three slices were eaten. How’s that possible?",
     "choices": ["A) Grandmother, mother, daughter", "B) Two people shared slices", "C) Some slices were invisible", "D) A pizza was extra large"],
     "correct": "A",
     "powerup": None},

    {"question": "If there are six apples and you take away four, how many do you have?",
     "choices": ["A) 2", "B) 4", "C) 6", "D) None"],
     "correct": "B",
     "powerup": "skip"},

    {"question": "A rooster lays an egg on a rooftop. Which way does it roll?",
     "choices": ["A) East", "B) West", "C) Trick: roosters don't lay eggs", "D) Down the slope"],
     "correct": "C",
     "powerup": "hint"},

    {"question": "The more you take, the more you leave behind. What am I?",
     "choices": ["A) Footsteps", "B) Shadows", "C) Memories", "D) Time"],
     "correct": "A",
     "powerup": None},

    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?",
     "choices": ["A) The letter M", "B) The number 1", "C) A second", "D) A century"],
     "correct": "A",
     "powerup": "hint"},

    {"question": "Forward I am heavy, backward I am not. What am I?",
     "choices": ["A) Ton", "B) Stone", "C) Not", "D) Weight"],
     "correct": "A",
     "powerup": None},

    {"question": "Solve for x: 3x + 4 = 19",
     "choices": ["A) 5", "B) 6", "C) 7", "D) 4"],
     "correct": "A",
     "powerup": None},

    {"question": "If 5 cats can catch 5 mice in 5 minutes, how many cats are needed to catch 100 mice in 100 minutes?",
     "choices": ["A) 5", "B) 10", "C) 20", "D) 25"],
     "correct": "A",
     "powerup": None},

    {"question": "I am a three-digit number. My tens digit is five more than my ones digit, and my hundreds digit is eight less than my tens digit. What number am I?",
     "choices": ["A) 194", "B) 195", "C) 185", "D) 193"],
     "correct": "A",
     "powerup": None},

    {"question": "A clock shows 3:15. What is the angle between the hour and minute hands?",
     "choices": ["A) 7.5 degrees", "B) 0 degrees", "C) 90 degrees", "D) 180 degrees"],
     "correct": "A",
     "powerup": None},

    {"question": "If you multiply this number by any other number, the answer will always be the same. What is it?",
     "choices": ["A) 0", "B) 1", "C) 2", "D) -1"],
     "correct": "A",
     "powerup": None},

    {"question": "What is the next number in the Fibonacci sequence: 1, 1, 2, 3, 5, ?",
     "choices": ["A) 8", "B) 7", "C) 6", "D) 9"],
     "correct": "A",
     "powerup": None},

    {"question": "Type the first letter of the English alphabet",
     "choices": ["A) A", "B) B", "C) C", "D) Z"],
     "correct": "A",
     "powerup": None},

    {"question": "If a plane crashes on the border of two countries, where do you bury the survivors?",
     "choices": ["A) In country A", "B) In country B", "C) Trick: don't bury survivors", "D) Depends on the plane"],
     "correct": "C",
     "powerup": "hint"},

    {"question": "Unscramble the word: 'ODG'",
     "choices": ["A) Dog", "B) God", "C) Gods", "D) Go"],
     "correct": "A",
     "powerup": None},

    {"question": "What number is missing: 2, 4, 6, ?, 10",
     "choices": ["A) 8", "B) 7", "C) 9", "D) 6"],
     "correct": "A",
     "powerup": None},

    {"question": "Trick question: Press enter without typing anything!",
     "choices": ["A) Enter", "B) Nothing", "C) Space", "D) Skip"],
     "correct": "A",
     "powerup": "freeze"},

    {"question": "Which weighs more: 1 kg of cotton or 1 kg of iron?",
     "choices": ["A) Cotton", "B) Iron", "C) Same", "D) Depends on moisture"],
     "correct": "C",
     "powerup": None},

    {"question": "If today is Monday, what day will it be in 100 days?",
     "choices": ["A) Wednesday", "B) Thursday", "C) Friday", "D) Tuesday"],
     "correct": "A",
     "powerup": None},

    {"question": "I speak without a mouth and hear without ears. What am I?",
     "choices": ["A) Echo", "B) Shadow", "C) Wind", "D) Thought"],
     "correct": "A",
     "powerup": None},

    {"question": "What has cities, but no houses; forests, but no trees; and rivers, but no water?",
     "choices": ["A) Map", "B) Globe", "C) Picture", "D) Imagination"],
     "correct": "A",
     "powerup": None},

    {"question": "I’m tall when I’m young and short when I’m old. What am I?",
     "choices": ["A) Candle", "B) Tree", "C) Mountain", "D) Shadow"],
     "correct": "A",
     "powerup": None},

    {"question": "If Mr. Smith’s peacock lays an egg in Mr. Jones’ yard, who owns the egg?",
     "choices": ["A) Mr. Smith", "B) Mr. Jones", "C) Nobody: peacocks don’t lay eggs", "D) The government"],
     "correct": "C",
     "powerup": "hint"},

    {"question": "A man pushes his car to a hotel and tells the owner he’s bankrupt. Why?",
     "choices": ["A) Game of Monopoly", "B) Bankruptcy", "C) He owns a hotel", "D) It’s a riddle"],
     "correct": "A",
     "powerup": "freeze"},

    {"question": "Which weighs more, 2 kg of cotton or 2 kg of steel?",
     "choices": ["A) Cotton", "B) Steel", "C) Same", "D) Steel with iron nails"],
     "correct": "C",
     "powerup": None},

    {"question": "If a doctor gives you three pills and tells you to take one every half hour, how long will it take to finish them?",
     "choices": ["A) 1 hour", "B) 1.5 hours", "C) 2 hours", "D) 30 minutes"],
     "correct": "A",
     "powerup": None},

    {"question": "I can fly without wings. I can cry without eyes. Wherever I go, darkness flies. What am I?",
     "choices": ["A) Cloud", "B) Wind", "C) Time", "D) Shadow"],
     "correct": "A",
     "powerup": None},

    {"question": "Solve for x: 7x - 3 = 25",
     "choices": ["A) 4", "B) 5", "C) 6", "D) 3"],
     "correct": "A",
     "powerup": None},

    {"question": "What comes next in the sequence: 5, 10, 20, 40, ?",
     "choices": ["A) 80", "B) 60", "C) 100", "D) 70"],
     "correct": "A",
     "powerup": None},

    {"question": "Type the opposite of the word 'up'",
     "choices": ["A) Down", "B) Left", "C) Right", "D) Below"],
     "correct": "A",
     "powerup": None},

    {"question": "Unscramble: 'NITGHI'",
     "choices": ["A) Thing", "B) Night", "C) Hiting", "D) Hint"],
     "correct": "A",
     "powerup": None},

    {"question": "What is 15 divided by 3?",
     "choices": ["A) 5", "B) 4", "C) 6", "D) 3"],
     "correct": "A",
     "powerup": None},

    {"question": "Type 'yes' backwards",
     "choices": ["A) sey", "B) yes", "C) sye", "D) ezy"],
     "correct": "A",
     "powerup": None},

    {"question": "What is 111 + 222?",
     "choices": ["A) 333", "B) 332", "C) 223", "D) 3333"],
     "correct": "A",
     "powerup": None},

    {"question": "I’m always running but never move. What am I?",
     "choices": ["A) Clock", "B) River", "C) Time", "D) Wind"],
     "correct": "A",
     "powerup": None},

    {"question": "I can be cracked, made, told, and played. What am I?",
     "choices": ["A) Joke", "B) Egg", "C) Code", "D) Puzzle"],
     "correct": "A",
     "powerup": "hint"},

    {"question": "What number is missing: 1, 4, 9, 16, ?",
     "choices": ["A) 25", "B) 20", "C) 30", "D) 24"],
     "correct": "A",
     "powerup": None},

    {"question": "I’m light as a feather, yet the strongest man can’t hold me for long. What am I?",
     "choices": ["A) Breath", "B) Air", "C) Cloud", "D) Shadow"],
     "correct": "A",
     "powerup": None},

    {"question": "Type the word 'nothing'",
     "choices": ["A) nothing", "B) something", "C) space", "D) none"],
     "correct": "nothing",
     "powerup": "skip"},

    {"question": "Which is heavier: 2 tons of bricks or 1 ton of gold?",
     "choices": ["A) Bricks", "B) Gold", "C) Depends", "D) Same"],
     "correct": "A",
     "powerup": None},

    {"question": "I am an odd number. Take away a letter and I become even. What number am I?",
     "choices": ["A) Seven", "B) Eleven", "C) Nine", "D) Five"],
     "correct": "A",
     "powerup": "hint"},

    {"question": "If you have me, you want to share me. If you share me, you don’t have me. What am I?",
     "choices": ["A) Secret", "B) Money", "C) Knowledge", "D) Friendship"],
     "correct": "A",
     "powerup": None},

    {"question": "A man walks 1 mile south, 1 mile east, and 1 mile north. He ends up at the same place. Where is he?",
     "choices": ["A) North Pole", "B) South Pole", "C) Equator", "D) Unknown"],
     "correct": "A",
     "powerup": None},

    {"question": "If 6 children can eat 6 pizzas in 6 minutes, how long will it take 3 children to eat 3 pizzas?",
     "choices": ["A) 6 minutes", "B) 3 minutes", "C) 9 minutes", "D) 12 minutes"],
     "correct": "A",
     "powerup": None},
     
    {"question": "What is the next number: 2, 4, 8, 16, ?", 
     "choices": ["A) 20", "B) 32", "C) 24", "D) 18"], 
     "correct": "B", "powerup": None},

    {"question": "If a hen and a half lays an egg and a half in a day and a half, how many eggs does half a dozen hens lay in half a dozen days?", 
     "choices": ["A) 12", "B) 24", "C) 18", "D) 36"], 
     "correct": "D", "powerup": None},

    {"question": "Which weighs more: 1 pound of lead or 1 pound of feathers?", 
     "choices": ["A) Lead", "B) Feathers", "C) Same", "D) Cannot determine"], 
     "correct": "C", "powerup": None},

    {"question": "I am an odd number. Take away a letter and I become even. What number am I?", 
     "choices": ["A) Seven", "B) Five", "C) Nine", "D) Three"], 
     "correct": "A", "powerup": None},

    {"question": "If it takes 3 painters 3 hours to paint 3 walls, how long does it take 6 painters to paint 6 walls?", 
     "choices": ["A) 3 hours", "B) 6 hours", "C) 1.5 hours", "D) 12 hours"], 
     "correct": "A", "powerup": None},

    {"question": "Which number comes next: 1, 11, 21, 1211, 111221, ?", 
     "choices": ["A) 312211", "B) 111321", "C) 132112", "D) 213211"], 
     "correct": "A", "powerup": None},

    {"question": "What has keys but can't open locks?", 
     "choices": ["A) Map", "B) Piano", "C) Clock", "D) Dictionary"], 
     "correct": "B", "powerup": None},

    {"question": "Solve: 3 + 6 x (5 + 4) ÷ 3 - 7", 
     "choices": ["A) 14", "B) 18", "C) 20", "D) 21"], 
     "correct": "B", "powerup": None},

    {"question": "What comes next in the series: 1, 4, 9, 16, 25, ?", 
     "choices": ["A) 36", "B) 35", "C) 30", "D) 40"], 
     "correct": "A", "powerup": None},

    {"question": "You see me once in June, twice in November, but not at all in May. What am I?", 
     "choices": ["A) Letter E", "B) Letter N", "C) Letter J", "D) Letter O"], 
     "correct": "A", "powerup": None},
     
    {"question": "Trick question: Press enter without typing anything!", 
     "choices": ["A) Type something", "B) Press enter", "C) Skip", "D) None"], 
     "correct": "B", "powerup": "hint"},

    {"question": "I am light as a feather, yet no one can hold me for long. What am I?", 
     "choices": ["A) Breath", "B) Shadow", "C) Air", "D) Cloud"], 
     "correct": "A", "powerup": "freeze"},

    {"question": "Which weighs more: a kilogram of gold or a kilogram of silver?", 
     "choices": ["A) Gold", "B) Silver", "C) Same", "D) Cannot tell"], 
     "correct": "C", "powerup": "skip"},

    {"question": "Solve the puzzle: 1 + 4 + 9 + 16 + ? = 55", 
     "choices": ["A) 25", "B) 36", "C) 30", "D) 20"], 
     "correct": "A", "powerup": "hint"},

    {"question": "If you have two coins totaling 30 cents and one of them is not a nickel, what are the coins?", 
     "choices": ["A) Quarter + Nickel", "B) Dime + Dime", "C) Nickel + Quarter", "D) Penny + Quarter"], 
     "correct": "A", "powerup": "freeze"},
     
    {"question": "A bat and a ball cost $1.10. The bat costs $1 more than the ball. How much does the ball cost?", 
     "choices": ["A) 10¢", "B) 5¢", "C) 15¢", "D) 20¢"], 
     "correct": "B", "powerup": None},

    {"question": "If you multiply this number by any other number, the answer will always be the same. What number is it?", 
     "choices": ["A) 1", "B) 0", "C) 10", "D) -1"], 
     "correct": "B", "powerup": None},

    {"question": "Which is missing: J, F, M, A, M, ?, J, A, S, O, N, D", 
     "choices": ["A) M", "B) J", "C) F", "D) None"], 
     "correct": "A", "powerup": None},

    {"question": "If 5 cats catch 5 mice in 5 minutes, how many cats are needed to catch 100 mice in 100 minutes?", 
     "choices": ["A) 5", "B) 10", "C) 20", "D) 25"], 
     "correct": "A", "powerup": None},

    {"question": "I am always hungry and must be fed, but if you give me water I die. What am I?", 
     "choices": ["A) Fire", "B) Plant", "C) Sun", "D) Ice"], 
     "correct": "A", "powerup": None},

    {"question": "What disappears as soon as you say its name?", 
     "choices": ["A) Silence", "B) Shadow", "C) Secret", "D) Darkness"], 
     "correct": "A", "powerup": None},

    {"question": "What number comes next: 2, 3, 5, 8, 12, ?", 
     "choices": ["A) 17", "B) 18", "C) 16", "D) 19"], 
     "correct": "A", "powerup": None},

    {"question": "I speak without a mouth and hear without ears. I have nobody, but I come alive with the wind. What am I?", 
     "choices": ["A) Echo", "B) Shadow", "C) Wave", "D) Smoke"], 
     "correct": "A", "powerup": None},

    {"question": "Which 3-digit number has all digits the same and is divisible by 7?", 
     "choices": ["A) 111", "B) 222", "C) 777", "D) 999"], 
     "correct": "C", "powerup": None},

    {"question": "If you divide 30 by 1/2 and add 10, what do you get?", 
     "choices": ["A) 25", "B) 70", "C) 60", "D) 50"], 
     "correct": "C", "powerup": None},

    {"question": "I go up but never come down. What am I?", 
     "choices": ["A) Age", "B) Balloon", "C) Smoke", "D) Temperature"], 
     "correct": "A", "powerup": None},

    {"question": "If two’s company and three’s a crowd, what are four and five?", 
     "choices": ["A) Nine", "B) Seven", "C) Ten", "D) Twelve"], 
     "correct": "A", "powerup": None},

    {"question": "You have 10 apples and take away 3. How many do you have?", 
     "choices": ["A) 7", "B) 3", "C) 10", "D) 0"], 
     "correct": "B", "powerup": None},

    {"question": "What comes next: 1, 1, 2, 6, 24, ?", 
     "choices": ["A) 120", "B) 36", "C) 48", "D) 60"], 
     "correct": "A", "powerup": None},
     
    {"question": "What comes next in the series: 5, 10, 20, 40, ?", 
     "choices": ["A) 60", "B) 80", "C) 100", "D) 70"], 
     "correct": "B", "powerup": None},

    {"question": "A cowboy rode into town on Friday, stayed 3 days, and left on Friday. How is that possible?", 
     "choices": ["A) Time travel", "B) The horse's name is Friday", "C) Trick question", "D) None"], 
     "correct": "B", "powerup": None},

    {"question": "What occurs once in a minute, twice in a moment, but never in a thousand years?", 
     "choices": ["A) Letter M", "B) Letter O", "C) Letter N", "D) Letter E"], 
     "correct": "A", "powerup": None},

    {"question": "If there are 3 apples and you take away 2, how many do you have?", 
     "choices": ["A) 1", "B) 2", "C) 3", "D) 0"], 
     "correct": "B", "powerup": None},

    {"question": "Which weighs more: a ton of bricks or a ton of feathers?", 
     "choices": ["A) Bricks", "B) Feathers", "C) Same", "D) Cannot tell"], 
     "correct": "C", "powerup": None},

    {"question": "I have cities but no houses, forests but no trees, and rivers but no water. What am I?", 
     "choices": ["A) Map", "B) Imagination", "C) Globe", "D) Puzzle"], 
     "correct": "A", "powerup": None},

    {"question": "What number do you get if you multiply all the numbers on a telephone keypad?", 
     "choices": ["A) 0", "B) 1", "C) 45", "D) 9"], 
     "correct": "A", "powerup": None},

    {"question": "If you have me, you want to share me. If you share me, you haven’t got me. What am I?", 
     "choices": ["A) Secret", "B) Knowledge", "C) Treasure", "D) Time"], 
     "correct": "A", "powerup": None},

    {"question": "What comes next in the pattern: 1, 2, 4, 8, 16, ?", 
     "choices": ["A) 18", "B) 32", "C) 24", "D) 30"], 
     "correct": "B", "powerup": None},

    {"question": "If you are running a race and you pass the person in second place, what place are you in?", 
     "choices": ["A) First", "B) Second", "C) Third", "D) Cannot tell"], 
     "correct": "B", "powerup": None},

    {"question": "I am always in front of you but can’t be seen. What am I?", 
     "choices": ["A) Future", "B) Air", "C) Time", "D) Shadow"], 
     "correct": "A", "powerup": None},

    {"question": "What comes once in a year, twice in a week, and never in a day?", 
     "choices": ["A) Letter E", "B) Letter Y", "C) Letter W", "D) Letter A"], 
     "correct": "A", "powerup": None},

    {"question": "If a plane crashes on the border of the US and Canada, where do they bury the survivors?", 
     "choices": ["A) US", "B) Canada", "C) Both", "D) Nowhere"], 
     "correct": "D", "powerup": None},

    {"question": "What is always coming but never arrives?", 
     "choices": ["A) Tomorrow", "B) Future", "C) Time", "D) Event"], 
     "correct": "A", "powerup": None},

    {"question": "What goes up and never comes down?", 
     "choices": ["A) Age", "B) Balloon", "C) Temperature", "D) Smoke"], 
     "correct": "A", "powerup": None},

    {"question": "If you have a 3-gallon and a 5-gallon jug, how can you measure exactly 4 gallons?", 
     "choices": ["A) Fill 5, pour 3", "B) Fill 3 twice", "C) Fill 5, pour 3 twice", "D) Impossible"], 
     "correct": "C", "powerup": None},

    {"question": "I am not alive, but I grow; I have no lungs, but I need air; I have no mouth, but water kills me. What am I?", 
     "choices": ["A) Fire", "B) Plant", "C) Cloud", "D) Shadow"], 
     "correct": "A", "powerup": None},

    {"question": "What has hands but can’t clap?", 
     "choices": ["A) Clock", "B) Doll", "C) Statue", "D) Robot"], 
     "correct": "A", "powerup": None},

    {"question": "Which 3-digit number is divisible by 7 and 11?", 
     "choices": ["A) 154", "B) 161", "C) 203", "D) 210"], 
     "correct": "C", "powerup": None},

    {"question": "What gets wetter the more it dries?", 
     "choices": ["A) Towel", "B) Sponge", "C) Water", "D) Soap"], 
     "correct": "A", "powerup": None},

    {"question": "I am full of holes but still holds water. What am I?", 
     "choices": ["A) Sponge", "B) Net", "C) Bucket", "D) Sieve"], 
     "correct": "A", "powerup": None},

    {"question": "What is seen in the middle of March and April that can’t be seen at the beginning or end of either month?", 
     "choices": ["A) Letter R", "B) Letter A", "C) Letter M", "D) Letter L"], 
     "correct": "A", "powerup": None},

    {"question": "Forward I am heavy, backward I am not. What am I?", 
     "choices": ["A) Ton", "B) Net", "C) Stone", "D) None"], 
     "correct": "A", "powerup": None},

    {"question": "I have a head and a tail but no body. What am I?", 
     "choices": ["A) Coin", "B) Snake", "C) Comet", "D) Arrow"], 
     "correct": "A", "powerup": None},

    {"question": "If you mix red and white, what color do you get?", 
     "choices": ["A) Pink", "B) Purple", "C) Orange", "D) Brown"], 
     "correct": "A", "powerup": None},

    {"question": "I run but never walk, I have a bed but never sleep. What am I?", 
     "choices": ["A) River", "B) Clock", "C) Wind", "D) Shadow"], 
     "correct": "A", "powerup": None},

    {"question": "What is as light as a feather, yet the strongest person cannot hold it for more than a few minutes?", 
     "choices": ["A) Breath", "B) Shadow", "C) Air", "D) Cloud"], 
     "correct": "A", "powerup": None},

    {"question": "Which comes first, the chicken or the egg?", 
     "choices": ["A) Chicken", "B) Egg", "C) Trick question", "D) None"], 
     "correct": "C", "powerup": None},

    {"question": "Divide 30 by 1/2 and add 10. What is the result?", 
     "choices": ["A) 25", "B) 50", "C) 70", "D) 60"], 
     "correct": "D", "powerup": None},
]
questions += [

    {"question": "What is the smallest positive number divisible by both 6 and 8?",
     "choices": ["A) 12", "B) 24", "C) 36", "D) 48"],
     "correct": "B", "powerup": None},

    {"question": "If TODAY is two days after the day before yesterday, what day is it?",
     "choices": ["A) Today", "B) Tomorrow", "C) Yesterday", "D) Impossible"],
     "correct": "A", "powerup": None},

    {"question": "How many times can you subtract 1 from 100?",
     "choices": ["A) 100", "B) 99", "C) 1", "D) Infinite"],
     "correct": "C", "powerup": None},

    {"question": "Which number is missing: 1, 4, 9, 16, ?, 36",
     "choices": ["A) 20", "B) 24", "C) 25", "D) 30"],
     "correct": "C", "powerup": None},

    {"question": "If you flip a fair coin 5 times, what is the probability of getting exactly 5 heads?",
     "choices": ["A) 1/10", "B) 1/16", "C) 1/32", "D) 1/64"],
     "correct": "C", "powerup": None},

    {"question": "What comes next: 2, 6, 12, 20, ?",
     "choices": ["A) 28", "B) 30", "C) 32", "D) 36"],
     "correct": "A", "powerup": None},

    {"question": "A farmer has 17 sheep. All but 9 die. How many are left?",
     "choices": ["A) 8", "B) 9", "C) 17", "D) 0"],
     "correct": "B", "powerup": None},

    {"question": "What is the value of 0! (zero factorial)?",
     "choices": ["A) 0", "B) Undefined", "C) 1", "D) Infinity"],
     "correct": "C", "powerup": None},

    {"question": "Which number does NOT belong: 2, 3, 5, 7, 11, 15?",
     "choices": ["A) 2", "B) 3", "C) 11", "D) 15"],
     "correct": "D", "powerup": None},

    {"question": "If a clock shows 3:15, what is the angle between the hour and minute hand?",
     "choices": ["A) 0°", "B) 7.5°", "C) 15°", "D) 30°"],
     "correct": "B", "powerup": None},

    {"question": "Which has more letters when written out?",
     "choices": ["A) 1000", "B) 1000000", "C) Same", "D) Depends"],
     "correct": "A", "powerup": None},

    {"question": "What is half of half of half of 80?",
     "choices": ["A) 5", "B) 10", "C) 20", "D) 40"],
     "correct": "A", "powerup": None},

    {"question": "Which number is a palindrome?",
     "choices": ["A) 123", "B) 232", "C) 341", "D) 410"],
     "correct": "B", "powerup": None},

    {"question": "If you rearrange the letters of 'CIFAIPC', what do you get?",
     "choices": ["A) Pacific", "B) Specific", "C) Traffic", "D) Office"],
     "correct": "A", "powerup": None},

    {"question": "What is the next letter sequence: A, C, F, J, O, ?",
     "choices": ["A) T", "B) U", "C) V", "D) W"],
     "correct": "A", "powerup": None},

    {"question": "Which number makes the equation true: 8 ÷ ? = 2",
     "choices": ["A) 2", "B) 4", "C) 6", "D) 8"],
     "correct": "B", "powerup": None},

    {"question": "If you spell 'MOST' backward and alphabetize the letters, what is the second letter?",
     "choices": ["A) M", "B) O", "C) S", "D) T"],
     "correct": "B", "powerup": None},

    {"question": "What comes next: 100, 99, 97, 94, 90, ?",
     "choices": ["A) 86", "B) 87", "C) 88", "D) 89"],
     "correct": "A", "powerup": None},

    {"question": "Which fraction is largest?",
     "choices": ["A) 3/4", "B) 5/8", "C) 7/10", "D) 2/3"],
     "correct": "A", "powerup": None},

    {"question": "If you count from 1 to 100, how many times does the digit '9' appear?",
     "choices": ["A) 10", "B) 18", "C) 19", "D) 20"],
     "correct": "C", "powerup": None},

    {"question": "What is the only even prime number?",
     "choices": ["A) 1", "B) 2", "C) 4", "D) 6"],
     "correct": "B", "powerup": None},

    {"question": "Which shape has the most sides?",
     "choices": ["A) Triangle", "B) Square", "C) Pentagon", "D) Circle"],
     "correct": "D", "powerup": None},

    {"question": "What number is missing: 81, 27, 9, 3, ?",
     "choices": ["A) 0", "B) 1", "C) 2", "D) 6"],
     "correct": "B", "powerup": None},

    {"question": "How many degrees are in the interior angles of a triangle?",
     "choices": ["A) 90", "B) 180", "C) 270", "D) 360"],
     "correct": "B", "powerup": None},

    {"question": "What comes next: 1, 2, 6, 24, ?",
     "choices": ["A) 48", "B) 60", "C) 120", "D) 720"],
     "correct": "C", "powerup": None},

    # Rare power-up questions (ONLY 2)
    {"question": "Extra tricky: Answer the letter that appears MOST in the word 'MISSISSIPPI'",
     "choices": ["A) M", "B) I", "C) S", "D) P"],
     "correct": "C", "powerup": "hint"},

    {"question": "Extra tricky math: What is 1 + 2 + 3 + ... + 10?",
     "choices": ["A) 45", "B) 50", "C) 55", "D) 60"],
     "correct": "C", "powerup": "freeze"},

]
questions += [

    {"question": "What is the value of 7 + 7 ÷ 7 × 7 − 7?",
     "choices": ["A) 7", "B) 8", "C) 14", "D) 49"],
     "correct": "A", "powerup": None},

    {"question": "If it takes 2 machines 2 minutes to make 2 widgets, how long does it take 10 machines to make 10 widgets?",
     "choices": ["A) 2 minutes", "B) 10 minutes", "C) 20 minutes", "D) 1 minute"],
     "correct": "A", "powerup": None},

    {"question": "Which number does NOT belong: 2, 3, 5, 7, 11, 14, 17",
     "choices": ["A) 11", "B) 14", "C) 17", "D) 7"],
     "correct": "B", "powerup": None},

    {"question": "If you rearrange the letters of 'CIFAIPC', you get the name of a:",
     "choices": ["A) City", "B) Ocean", "C) Animal", "D) Country"],
     "correct": "C", "powerup": None},

    {"question": "What comes next: 1, 4, 9, 16, 25, 36, ?",
     "choices": ["A) 42", "B) 49", "C) 48", "D) 64"],
     "correct": "B", "powerup": None},

    {"question": "A clock strikes once at 1 o’clock, twice at 2 o’clock. How many times does it strike in 24 hours?",
     "choices": ["A) 78", "B) 136", "C) 156", "D) 144"],
     "correct": "C", "powerup": None},

    {"question": "What number is missing: 3, 6, 11, 18, ?",
     "choices": ["A) 25", "B) 27", "C) 29", "D) 31"],
     "correct": "A", "powerup": None},

    {"question": "If today is Monday, what day will it be in 100 days?",
     "choices": ["A) Tuesday", "B) Wednesday", "C) Thursday", "D) Friday"],
     "correct": "B", "powerup": None},

    {"question": "Which fraction is largest?",
     "choices": ["A) 3/7", "B) 4/9", "C) 5/11", "D) 6/13"],
     "correct": "B", "powerup": None},

    {"question": "What has one eye but cannot see?",
     "choices": ["A) Needle", "B) Storm", "C) Cyclops", "D) Camera"],
     "correct": "A", "powerup": None},

    {"question": "What is the smallest positive integer divisible by 2, 3, 4, and 5?",
     "choices": ["A) 30", "B) 60", "C) 120", "D) 20"],
     "correct": "B", "powerup": None},

    {"question": "What comes next: Z, X, V, T, ?",
     "choices": ["A) R", "B) S", "C) Q", "D) P"],
     "correct": "A", "powerup": None},

    {"question": "If you flip a fair coin 5 times, what is the probability of getting 5 heads?",
     "choices": ["A) 1/10", "B) 1/16", "C) 1/32", "D) 1/64"],
     "correct": "C", "powerup": None},

    {"question": "How many sides do three triangles have in total?",
     "choices": ["A) 6", "B) 9", "C) 12", "D) 3"],
     "correct": "B", "powerup": None},

    {"question": "What disappears when you stand up?",
     "choices": ["A) Chair", "B) Lap", "C) Shadow", "D) Balance"],
     "correct": "B", "powerup": None},

    {"question": "What number satisfies: x + x/2 = 12?",
     "choices": ["A) 6", "B) 8", "C) 9", "D) 12"],
     "correct": "C", "powerup": None},

    {"question": "Which word is spelled incorrectly in every dictionary?",
     "choices": ["A) Incorrectly", "B) Misspelled", "C) Wrong", "D) Dictionary"],
     "correct": "A", "powerup": None},

    {"question": "What is the next number: 100, 50, 25, 12.5, ?",
     "choices": ["A) 6", "B) 6.25", "C) 5", "D) 12"],
     "correct": "B", "powerup": None},

    {"question": "If all Bloops are Razzies and all Razzies are Lazzies, are all Bloops definitely Lazzies?",
     "choices": ["A) Yes", "B) No", "C) Cannot determine", "D) Only sometimes"],
     "correct": "A", "powerup": None},

    {"question": "Extra-tricky logic: Which answer is correct?",
     "choices": ["A) This one", "B) Not this one", "C) All are wrong", "D) All are correct"],
     "correct": "C", "powerup": "hint"},

    {"question": "What is the only number that when spelled has its letters in alphabetical order?",
     "choices": ["A) Four", "B) Five", "C) Eight", "D) One"],
     "correct": "C", "powerup": None},

    {"question": "Solve instantly or perish: What is 1?",
     "choices": ["A) 0", "B) 1", "C) 2", "D) Depends"],
     "correct": "B", "powerup": "freeze"},
]
questions += [
    {"question": "What is 5 + 7?",
        "choices": ["A) 10", "B) 11", "C) 12", "D) 13"],
        "correct": "C",
        "powerup": None,
        "powerdown": False},

    {"question": "Which number comes next in the series: 1, 4, 9, 16, ?",
        "choices": ["A) 20", "B) 25", "C) 30", "D) 24"],
        "correct": "B",
        "powerup": None,
        "powerdown": False},

    {"question": "I speak without a mouth and hear without ears. What am I?",
        "choices": ["A) Echo", "B) Shadow", "C) Wave", "D) Smoke"],
        "correct": "A",
        "powerup": None,
        "powerdown": False},

    {"question": "If two cats can catch two mice in two minutes, how long does it take 4 cats to catch 4 mice?",
        "choices": ["A) 1 minute", "B) 2 minutes", "C) 4 minutes", "D) 8 minutes"],
        "correct": "B",
        "powerup": None,
        "powerdown": False},

    {"question": "What has keys but can't open locks?",
        "choices": ["A) Map", "B) Piano", "C) Clock", "D) Dictionary"],
        "correct": "B",
        "powerup": None,
        "powerdown": False},

    {"question": "Solve: 3 + 6 x (2 + 1)",
        "choices": ["A) 15", "B) 21", "C) 18", "D) 20"],
        "correct": "C",
        "powerup": "hint",  # 5% chance type power-up
        "powerdown": False},

    {"question": "What is always coming but never arrives?",
        "choices": ["A) Tomorrow", "B) Future", "C) Time", "D) Event"],
        "correct": "A",
        "powerup": None,
        "powerdown": False},

    {"question": "I have cities but no houses, forests but no trees, and rivers but no water. What am I?",
        "choices": ["A) Map", "B) Imagination", "C) Globe", "D) Puzzle"],
        "correct": "A",
        "powerup": None,
        "powerdown": False},

    {"question": "Which is heavier: 1 kg of feathers or 1 kg of iron?",
        "choices": ["A) Feathers", "B) Iron", "C) Same", "D) Cannot tell"],
        "correct": "C",
        "powerup": None,
        "powerdown": False},

    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?",
        "choices": ["A) Letter M", "B) Letter O", "C) Letter N", "D) Letter E"],
        "correct": "A",
        "powerup": None,
        "powerdown": False},

    {"question": "If 5 pencils cost $1 each, how much do 8 pencils cost?",
        "choices": ["A) $5", "B) $8", "C) $10", "D) $12"],
        "correct": "B",
        "powerup": None,
        "powerdown": False},

    {"question": "What number comes next: 2, 4, 8, 16, ?",
        "choices": ["A) 20", "B) 24", "C) 32", "D) 30"],
        "correct": "C",
        "powerup": None,
        "powerdown": False},

    {"question": "Which month has 28 days?",
        "choices": ["A) February", "B) All months", "C) April", "D) June"],
        "correct": "B",
        "powerup": None,
        "powerdown": False},

    {"question": "I go up but never come down. What am I?",
        "choices": ["A) Age", "B) Balloon", "C) Smoke", "D) Temperature"],
        "correct": "A",
        "powerup": None,
        "powerdown": True},

    {"question": "Which 3-digit number has all digits the same and is divisible by 7?",
        "choices": ["A) 111", "B) 222", "C) 777", "D) 999"],
        "correct": "C",
        "powerup": None,
        "powerdown": False},

    {"question": "I am full of holes but still hold water. What am I?",
        "choices": ["A) Sponge", "B) Net", "C) Bucket", "D) Sieve"],
        "correct": "A",
        "powerup": "hint",  # another rare hint
        "powerdown": False},

    {"question": "Forward I am heavy, backward I am not. What am I?",
        "choices": ["A) Ton", "B) Net", "C) Stone", "D) None"],
        "correct": "A",
        "powerup": None,
        "powerdown": False},

    {"question": "What has hands but can’t clap?",
        "choices": ["A) Clock", "B) Doll", "C) Statue", "D) Robot"],
        "correct": "A",
        "powerup": None,
        "powerdown": False},

    {"question": "You see me once in June, twice in November, but not at all in May. What am I?",
        "choices": ["A) Letter E", "B) Letter N", "C) Letter J", "D) Letter O"],
        "correct": "A",
        "powerup": None,
        "powerdown": True},

    {"question": "What disappears as soon as you say its name?",
        "choices": ["A) Silence", "B) Shadow", "C) Secret", "D) Darkness"],
        "correct": "A",
        "powerup": None,
        "powerdown": False},
]
questions += [
    {
        "question": "Solve: 12 ÷ (2 × 3)",
        "choices": ["A) 1", "B) 2", "C) 3", "D) 6"],
        "correct": "A",
        "powerup": None,
        "powerdown": True
    },

    {
        "question": "What comes next: 1, 1, 2, 3, 5, ?",
        "choices": ["A) 6", "B) 7", "C) 8", "D) 9"],
        "correct": "C",
        "powerup": None,
        "powerdown": True
    },

    {
        "question": "If you rearrange the letters of 'CIFAIPC', you get the name of a:",
        "choices": ["A) Country", "B) Ocean", "C) Animal", "D) City"],
        "correct": "B",
        "powerup": None,
        "powerdown": True
    },

    {
        "question": "How many times can you subtract 2 from 10?",
        "choices": ["A) 5", "B) 4", "C) 1", "D) Infinite"],
        "correct": "C",
        "powerup": None,
        "powerdown": True
    },

    {
        "question": "Solve: 3² + 4² − 5²",
        "choices": ["A) 0", "B) 4", "C) 8", "D) 16"],
        "correct": "B",
        "powerup": None,
        "powerdown": True
    },

    {
        "question": "Which number is missing: 2, 4, 8, 16, 31, ?",
        "choices": ["A) 32", "B) 33", "C) 34", "D) 30"],
        "correct": "B",  # +2, +4, +8, +15, +16
        "powerup": None,
        "powerdown": True
    },

    {
        "question": "A farmer has 17 sheep. All but 9 die. How many are left?",
        "choices": ["A) 8", "B) 9", "C) 17", "D) 0"],
        "correct": "B",
        "powerup": None,
        "powerdown": True
    },

    {
        "question": "Solve: 5 + 5 × 5 − 5 ÷ 5",
        "choices": ["A) 25", "B) 26", "C) 29", "D) 30"],
        "correct": "C",
        "powerup": None,
        "powerdown": True
    },

    {
        "question": "What number do you get if you count the letters in the English alphabet?",
        "choices": ["A) 24", "B) 25", "C) 26", "D) 27"],
        "correct": "C",
        "powerup": None,
        "powerdown": True
    },

    {
        "question": "Which is correct?",
        "choices": [
            "A) 2 + 2 = 4",
            "B) 2 + 2 = 22",
            "C) Both",
            "D) Neither"
        ],
        "correct": "A",
        "powerup": None,
        "powerdown": True
    }
]

questions += [
    {
        "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        "choices": ["A) Shadow", "B) Echo", "C) Fire", "D) Cloud"],
        "correct": "B",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "Which number comes next in the sequence: 2, 3, 5, 8, 13, ?",
        "choices": ["A) 18", "B) 20", "C) 21", "D) 34"],
        "correct": "C",
        "powerup": None,
        "powerdown": False
    },
    {
        "question": "If all Bloops are Razzies and all Razzies are Lazzies, which statement must be true?",
        "choices": [
            "A) All Lazzies are Bloops",
            "B) Some Bloops are not Lazzies",
            "C) All Bloops are Lazzies",
            "D) Some Lazzies are not Razzies"
        ],
        "correct": "C",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "What disappears the moment you say its name?",
        "choices": ["A) Silence", "B) Shadow", "C) Secret", "D) Thought"],
        "correct": "A",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "A bat and a ball cost $1.10 total. The bat costs $1 more than the ball. How much does the ball cost?",
        "choices": ["A) $0.10", "B) $0.05", "C) $0.01", "D) $0.15"],
        "correct": "B",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "Which word is spelled incorrectly in every dictionary?",
        "choices": ["A) Incorrectly", "B) Misspelled", "C) Wrong", "D) Dictionary"],
        "correct": "A",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "If you rearrange the letters 'CIFAIPC', you get the name of a:",
        "choices": ["A) City", "B) Country", "C) Ocean", "D) Animal"],
        "correct": "B",
        "powerup": None,
        "powerdown": False
    },
    {
        "question": "Which comes next: J, F, M, A, M, J, J, A, ?",
        "choices": ["A) S", "B) O", "C) N", "D) D"],
        "correct": "A",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "You see a boat filled with people. It hasn’t sunk, but when you look again you don’t see a single person. Why?",
        "choices": [
            "A) They jumped overboard",
            "B) The boat sank",
            "C) All the people were married",
            "D) It was a ghost ship"
        ],
        "correct": "C",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "What has many keys but can’t open a single lock?",
        "choices": ["A) Map", "B) Keyboard", "C) Piano", "D) Code"],
        "correct": "C",
        "powerup": None,
        "powerdown": False
    }
]
questions+=[
    {
        "question": "What comes once in a minute, twice in a moment, but never in a thousand years?",
        "choices": ["A) Time", "B) The letter M", "C) A second", "D) Memory"],
        "correct": "B",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "If all Glips are Plons and no Plons are Zargs, which statement must be true?",
        "choices": [
            "A) All Zargs are Glips",
            "B) Some Glips are Zargs",
            "C) No Glips are Zargs",
            "D) All Plons are Glips"
        ],
        "correct": "C",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "Which number logically completes the sequence: 1, 4, 9, 16, ?",
        "choices": ["A) 20", "B) 24", "C) 25", "D) 32"],
        "correct": "C",
        "powerup": "hint",
        "powerdown": False
    },
    {
        "question": "A farmer has 17 sheep. All but 9 run away. How many are left?",
        "choices": ["A) 8", "B) 9", "C) 17", "D) 26"],
        "correct": "B",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "Which word becomes shorter when you add two letters to it?",
        "choices": ["A) Short", "B) Long", "C) Small", "D) Tiny"],
        "correct": "A",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "If it takes 5 machines 5 minutes to make 5 widgets, how long does it take 100 machines to make 100 widgets?",
        "choices": ["A) 5 minutes", "B) 50 minutes", "C) 100 minutes", "D) 1 minute"],
        "correct": "A",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "Which letter comes next: O, T, T, F, F, S, S, ?",
        "choices": ["A) E", "B) N", "C) T", "D) S"],
        "correct": "A",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "You answer me, although I never ask you a question. What am I?",
        "choices": ["A) Phone", "B) Echo", "C) Doorbell", "D) Riddle"],
        "correct": "A",
        "powerup": None,
        "powerdown": False
    },
    {
        "question": "Which number is the odd one out: 2, 3, 5, 7, 11, 14?",
        "choices": ["A) 2", "B) 7", "C) 11", "D) 14"],
        "correct": "D",
        "powerup": "skip",
        "powerdown": False
    },
    {
        "question": "A bat and a ball cost $1.10 total. The bat costs $1 more than the ball. How much does the ball cost?",
        "choices": ["A) $0.10", "B) $0.05", "C) $0.01", "D) $0.15"],
        "correct": "B",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "Which month has 28 days?",
        "choices": ["A) February", "B) January", "C) All of them", "D) None of them"],
        "correct": "C",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "What comes next: 3, 6, 11, 18, ?",
        "choices": ["A) 25", "B) 27", "C) 29", "D) 30"],
        "correct": "C",
        "powerup": "hint",
        "powerdown": False
    },
    {
        "question": "What has a head, a tail, but no body?",
        "choices": ["A) Snake", "B) Coin", "C) Shadow", "D) Comet"],
        "correct": "B",
        "powerup": None,
        "powerdown": False
    },
    {
        "question": "If you overtake the person in second place, what position are you in?",
        "choices": ["A) First", "B) Second", "C) Third", "D) Last"],
        "correct": "B",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "Which word does not belong: inch, foot, yard, mile, gram?",
        "choices": ["A) Inch", "B) Yard", "C) Gram", "D) Mile"],
        "correct": "C",
        "powerup": "freeze",
        "powerdown": False
    },
    {
        "question": "What can travel around the world while staying in the same corner?",
        "choices": ["A) Airplane", "B) Stamp", "C) Satellite", "D) Shadow"],
        "correct": "B",
        "powerup": None,
        "powerdown": False
    },
    {
        "question": "Which number completes the pattern: 2, 6, 12, 20, ?",
        "choices": ["A) 28", "B) 30", "C) 32", "D) 36"],
        "correct": "A",
        "powerup": None,
        "powerdown": False
    },
    {
        "question": "What has many teeth but cannot bite?",
        "choices": ["A) Comb", "B) Saw", "C) Zipper", "D) Key"],
        "correct": "A",
        "powerup": None,
        "powerdown": False
    },
    {
        "question": "Which letter sequence comes next: A, C, F, J, O, ?",
        "choices": ["A) T", "B) U", "C) V", "D) W"],
        "correct": "A",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "A man builds a house with all four sides facing south. A bear walks by. What color is the bear?",
        "choices": ["A) Brown", "B) Black", "C) White", "D) Gray"],
        "correct": "C",
        "powerup": None,
        "powerdown": True
    },
    {
        "question": "What gets wetter the more it dries?",
        "choices": ["A) Rain", "B) Sponge", "C) Towel", "D) Ice"],
        "correct": "C",
        "powerup": None,
        "powerdown": False
    },
    {
        "question": "Which number does not belong: 4, 9, 16, 25, 36, 40?",
        "choices": ["A) 9", "B) 16", "C) 36", "D) 40"],
        "correct": "D",
        "powerup": "skip",
        "powerdown": False
    },
    {
        "question": "I have branches, but no fruit, trunk, or leaves. What am I?",
        "choices": ["A) Bank", "B) River", "C) Government", "D) Library"],
        "correct": "A",
        "powerup": None,
        "powerdown": False
    },
    {
        "question": "What goes up but never comes down?",
        "choices": ["A) Balloon", "B) Age", "C) Smoke", "D) Rocket"],
        "correct": "B",
        "powerup": None,
        "powerdown": True
    }
]
questions += [
    {"question": "Solve 7 x 6 - 4 ÷ 2", "choices": ["A) 40", "B) 41", "C) 42", "D) 43"], "correct": "C", "powerup": None, "powerdown": True},
    {"question": "What comes next in the sequence: 2, 6, 12, 20, ?", "choices": ["A) 30", "B) 28", "C) 26", "D) 32"], "correct": "B", "powerup": None, "powerdown": True},
    {"question": "Forward I am heavy, backward I am not. What am I?", "choices": ["A) Ton", "B) Net", "C) Stone", "D) None"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "Divide 50 by 1/2 and subtract 20. What is the answer?", "choices": ["A) 80", "B) 100", "C) 120", "D) 130"], "correct": "C", "powerup": None, "powerdown": True},
    {"question": "I am always hungry, feed me and I live, give me water and I die. What am I?", "choices": ["A) Fire", "B) Plant", "C) Sun", "D) Ice"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "What number do you get if you multiply all numbers on a telephone keypad?", "choices": ["A) 0", "B) 1", "C) 45", "D) 9"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "I go up but never come down. What am I?", "choices": ["A) Age", "B) Balloon", "C) Smoke", "D) Temperature"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "What disappears as soon as you say its name?", "choices": ["A) Silence", "B) Shadow", "C) Secret", "D) Darkness"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "If a plane crashes on the border of the US and Canada, where do they bury the survivors?", "choices": ["A) US", "B) Canada", "C) Both", "D) Nowhere"], "correct": "D", "powerup": None, "powerdown": True},
    {"question": "Solve 3 + 6 x (5 + 4) ÷ 3 - 7", "choices": ["A) 14", "B) 18", "C) 20", "D) 21"], "correct": "B", "powerup": None, "powerdown": True},
    {"question": "A bat and a ball cost $1.10. The bat costs $1 more than the ball. How much does the ball cost?", "choices": ["A) 10¢", "B) 5¢", "C) 15¢", "D) 20¢"], "correct": "B", "powerup": None, "powerdown": True},
    {"question": "You have 3-gallon and 5-gallon jugs. How can you measure exactly 4 gallons?", "choices": ["A) Fill 5, pour 3 twice", "B) Fill 3 twice", "C) Fill 5 once", "D) Impossible"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "A farmer has 17 sheep, all but 9 die. How many are left?", "choices": ["A) 8", "B) 9", "C) 17", "D) 0"], "correct": "B", "powerup": None, "powerdown": True},
    {"question": "If you multiply this number by any other number, the answer will always be the same. Which number?", "choices": ["A) 0", "B) 1", "C) 2", "D) Infinity"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "A truck driver is going opposite traffic. At which side does he drive?", "choices": ["A) Left", "B) Right", "C) Middle", "D) Depends on country"], "correct": "D", "powerup": None, "powerdown": True},
    {"question": "If an electric train is moving north at 100 mph and a wind is blowing east at 10 mph, which way does the smoke go?", "choices": ["A) North", "B) East", "C) South", "D) None"], "correct": "D", "powerup": None, "powerdown": True},
    {"question": "What can travel around the world while staying in a corner?", "choices": ["A) Stamp", "B) Plane", "C) Light", "D) Shadow"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "If you have me, you want to share me. If you share me, you do not have me. What am I?", "choices": ["A) Secret", "B) Money", "C) Love", "D) Knowledge"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "What 8-letter word can have a letter taken away and it still makes a word; take another letter away and it still makes a word?", "choices": ["A) Starting", "B) Staring", "C) String", "D) Sting"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "Which weighs more, a pound of gold or a pound of feathers?", "choices": ["A) Gold", "B) Feathers", "C) Same", "D) Cannot tell"], "correct": "C", "powerup": None, "powerdown": True},
    {"question": "I have keys but no locks, space but no rooms. You can enter, but you can’t go outside. What am I?", "choices": ["A) Piano", "B) Keyboard", "C) Map", "D) Computer"], "correct": "B", "powerup": None, "powerdown": True},
    {"question": "What has a head, a tail, is brown, and has no legs?", "choices": ["A) Coin", "B) Snake", "C) Penny", "D) Stick"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "choices": ["A) M", "B) O", "C) N", "D) E"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "Which number is missing: 1, 4, 9, 16, 25, ?", "choices": ["A) 36", "B) 35", "C) 34", "D) 37"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "Which letter comes next: O, T, T, F, F, S, S, ?", "choices": ["A) E", "B) N", "C) O", "D) T"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "I start with M, end with X, and have a never-ending amount of letters. What am I?", "choices": ["A) Mailbox", "B) Matrix", "C) Minix", "D) Mix"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "The more of me you take, the more you leave behind. What am I?", "choices": ["A) Footsteps", "B) Time", "C) Shadows", "D) Mistakes"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "What can fill a room but takes up no space?", "choices": ["A) Light", "B) Air", "C) Sound", "D) Heat"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "I’m tall when I’m young, and I’m short when I’m old. What am I?", "choices": ["A) Candle", "B) Pencil", "C) Shadow", "D) Tree"], "correct": "A", "powerup": None, "powerdown": True},
    {"question": "What can run but never walks, has a mouth but never talks?", "choices": ["A) River", "B) Clock", "C) Water", "D) Wind"], "correct": "A", "powerup": None, "powerdown": True},
]



import random
import threading
import sys

# ==========================
# Globals
# ==========================
coins = 0  # earned by correct answers
advancements_unlocked = set()
total_questions_wrong = 0
total_questions_correct = 0

shop_inventory = {
    "second_chance": 0,   # prevents next life loss
    "skip_voucher": 0,
    "freeze_chip": 0,
    "time_cushion": 0,    # cancels one time debuff layer
    "time_addition": 0,   # adds +5–10 sec once
    "bargain_life": 0
}

SHOP_LIMITS = {
    "second_chance": 2,
    "skip_voucher": 1,
    "freeze_chip": 2,
    "time_cushion": 3,
    "time_addition": 1,
    "bargain_life": 1
}

SHOP_PRICES = {
    "second_chance": 6,
    "skip_voucher": 4,
    "freeze_chip": 4,
    "time_cushion": 3,
    "time_addition": 5,
    "bargain_life": 8
}

SHOP_NAMES = {
    "second chance": "second_chance",
    "skip voucher": "skip_voucher",
    "freeze chip": "freeze_chip",
    "time cushion": "time_cushion",
    "time addition": "time_addition",
    "bargain life": "bargain_life"
}

SHOP_DESCRIPTIONS = {
    "second_chance": "🛡️ Prevents losing a life on the next wrong answer (limit 2).",
    "skip_voucher": "⏭️ Skips a question automatically (limit 1).",
    "freeze_chip": "🧊 Freezes the timer for one question (limit 2).",
    "time_cushion": "⏱ Cancels one layer of time debuff (limit 3).",
    "time_addition": "➕ Adds 5–10 seconds to next question (limit 1).",
    "bargain_life": "❤️ Instantly gain 1 life (limit 1)."
}

# Advancements still in progress!
ADVANCEMENTS_POSITIVE = {
    5:   ("Getting Warm", {"coins": 3, "remove_debuff": 1}),
    10:  ("In the Zone", {"coins": 5, "lives": 1}),
    25:  ("Momentum", {"freeze": 1, "remove_debuff": 1}),
    50:  ("Quiz Grinder", {"second_chance": 1, "coins": 8}),
    100: ("Unstoppable", {"lives": 1, "coins": 5}),
    250: ("Mental Fortress", {"hint": 1, "skip": 1}),
    500: ("Impossible Being", {"lives": 1, "coins": 2, "remove_debuff": 1}),
}

ADVANCEMENTS_NEGATIVE = {
    1:  "First Slip",
    2:  "Doubt Creeps In",
    3:  "Shaky Hands",
    5:  "Mental Fatigue",
    7:  "Confidence Shattered",
    11: "Spiral",
    15: "Collapse",
}

shop_cooldown = 0  # prevents shop spam

powerups = {"hint": 1, "skip": 1, "freeze": 1}
lives = 3
score = 0
questions_since_last_tax = 0
questions_since_last_shop = 0

current_level = 1
questions_correct_in_level = 0

BASE_TIME_LIMIT = 30
SHORT_TIME_LIMIT = BASE_TIME_LIMIT/2

# Time debuff state
time_debuff_queue = []
time_up = False

# Initial question time limit
next_question_time_limit = BASE_TIME_LIMIT

# ==========================
# Level-up system
# ==========================
level_up_table = {
    1: 2, 2: 3, 3: 5, 4: 6, 5: 8, 6: 10, 7: 12, 8: 14, 9: 16, 10: 18,
    11: 20, 12: 22, 13: 24, 14: 26, 15: 28, 16: 30, 17: 33, 18: 36,
    19: 39, 20: 42, 21: 45, 22: 48, 23: 51, 24: 54, 25: 57,
    26: 60, 27: 64, 28: 10000
}

# ==========================
# Fanum Tax
# ==========================
def apply_fanum_tax():
    global powerups
    removable = [k for k in powerups if k != "hint" and powerups[k] > 0]
    if not removable:
        return
    tax_amount = random.randint(1, 2)
    print("🧾 FANUM TAX INITIATED!")
    for _ in range(tax_amount):
        if not removable:
            break
        choice = random.choice(removable)
        powerups[choice] -= 1
        print(f"💸 {choice.capitalize()} confiscated!")
        if powerups[choice] <= 0:
            removable.remove(choice)

# ==========================
# Glitch effect
# ==========================
def glitch_text(text, total_correct):
    if 5995 <= total_correct <= 6000:
        return "".join(c if not c.isalpha() or random.random() > 0.2 else "?" for c in text)
    return text

# ==========================
# Shop
# ==========================
def open_shop():
    global coins, lives, shop_inventory
    print("\n🛒 ===== IMPOSSIBLE SHOP ===== 🛒")
    print(f"💰 Coins: {coins}\n")
    for item_key in SHOP_PRICES:
        owned = shop_inventory[item_key]
        limit = SHOP_LIMITS[item_key]
        status = "MAX" if owned >= limit else f"{SHOP_PRICES[item_key]} coins"
        print(f"{item_key.replace('_',' ').title():15} [{owned}/{limit}] → {status}")
        print(f"    {SHOP_DESCRIPTIONS[item_key]}")
    print("\nType item name to buy, or 'exit' to continue")
    while True:
        choice = input("> ").strip().lower()
        if choice == "exit":
            print("🛍️ Leaving shop...\n")
            return
        if choice not in SHOP_NAMES:
            print("❌ Invalid item")
            continue
        key = SHOP_NAMES[choice]
        if shop_inventory[key] >= SHOP_LIMITS[key]:
            print("🚫 Purchase limit reached")
            continue
        price = SHOP_PRICES[key]
        if coins < price:
            print("💸 Not enough coins")
            continue
        coins -= price
        shop_inventory[key] += 1
        print(f"✅ Purchased {choice.title()}!")
        print(f"    {SHOP_DESCRIPTIONS[key]}")
        if key == "bargain_life":
            lives += 1
            print("❤️ Life gained immediately!")
        print(f"💰 Coins left: {coins}")

# ==========================
# Advancements
# ==========================
def unlock_positive_advancement(count):
    """
    Unlocks a positive advancement based on total_questions_correct.
    Grants coins, power-ups, lives, or removes debuffs depending on milestone.
    """
    global coins, lives, powerups, time_debuff_queue

    if count not in ADVANCEMENTS_POSITIVE:
        return  # no advancement for this count

    name, rewards = ADVANCEMENTS_POSITIVE[count]
    advancements_unlocked.add(name)
    print(glitch_text(f"🏆 ADVANCEMENT UNLOCKED: {name}!", total_questions_correct))

    # Apply rewards
    if "coins" in rewards:
        coins += rewards["coins"]
        print(f"💰 Coins +{rewards['coins']} (total: {coins})")
    if "lives" in rewards:
        lives += rewards["lives"]
        print(f"❤️ Lives +{rewards['lives']} (total: {lives})")
    if "hint" in rewards:
        powerups["hint"] += rewards["hint"]
        print(f"💡 Hint +{rewards['hint']} (total: {powerups['hint']})")
    if "skip" in rewards:
        powerups["skip"] += rewards["skip"]
        print(f"⏭ Skip +{rewards['skip']} (total: {powerups['skip']})")
    if "freeze" in rewards:
        powerups["freeze"] += rewards["freeze"]
        print(f"🧊 Freeze +{rewards['freeze']} (total: {powerups['freeze']})")
    if "second_chance" in rewards:
        shop_inventory["second_chance"] += rewards["second_chance"]
        print(f"🛡️ Second Chance +{rewards['second_chance']} (total: {shop_inventory['second_chance']})")
    if "remove_debuff" in rewards:
        for _ in range(rewards["remove_debuff"]):
            if time_debuff_queue:
                removed = time_debuff_queue.pop(0)
                print(f"⏱ Time debuff removed ({removed}s)")

def unlock_negative_advancement(count):
    global coins, lives, time_debuff_queue, BASE_TIME_LIMIT
    name = ADVANCEMENTS_NEGATIVE[count]
    advancements_unlocked.add(name)

    print(glitch_text(f"🏆 ADVANCEMENT UNLOCKED: {name}", total_questions_correct))

    # ==========================
    # KILLER UPGRADE: FAILURE CASCADE
    # ==========================
    severity = min(count // 3, 6)

    if severity > 0:
        # Stack short timers aggressively
        time_debuff_queue.extend([SHORT_TIME_LIMIT] * severity)
        print(glitch_text(f"⏱ FAILURE CASCADE x{severity}", total_questions_correct))

        # Coin bleed
        bleed = min(coins, severity)
        coins -= bleed
        if bleed > 0:
            print(glitch_text(f"💸 Coin bleed: -{bleed}", total_questions_correct))

        # High severity starts hurting lives
        if severity >= 5 and random.random() < 0.4:
            lives -= 1
            print(glitch_text("💔 Collapse damage! Lost 1 life", total_questions_correct))

    # ==========================
    # Milestone punishments (upgraded)
    # ==========================
    if count == 1:
        coins = max(0, coins - 5)

    elif count == 2:
        time_debuff_queue.append(SHORT_TIME_LIMIT)

    elif count == 3:
        removable = [k for k in powerups if powerups[k] > 0]
        if removable:
            lost = random.choice(removable)
            powerups[lost] -= 1
            print(glitch_text(f"💥 Power-up corrupted: {lost}", total_questions_correct))

    elif count == 5:
        time_debuff_queue.append(max(BASE_TIME_LIMIT - 10, 3))

    elif count == 7:
        lives -= 1
        print(glitch_text("💔 Lost 1 life", total_questions_correct))

    elif count == 11:
        time_debuff_queue.extend([SHORT_TIME_LIMIT] * 3)

    elif count == 15:
        for _ in range(3):
            apply_fanum_tax()

        # Rare permanent damage
        if BASE_TIME_LIMIT > 15 and random.random() < 0.5:
            BASE_TIME_LIMIT -= 5
            print(glitch_text("🧠 PERMANENT TIME DAMAGE!", total_questions_correct))


    elif count == 15: 
        for i in range(3):
            apply_fanum_tax()

# ==========================
# Input with timeout
# ==========================
def input_with_timeout(prompt, timeout):
    global time_up
    answer = [None]
    def ask():
        answer[0] = input(prompt)
    thread = threading.Thread(target=ask)
    thread.daemon = True
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        time_up = True
        print("\n⏰ Time's up!")
        return None
    return answer[0]

# ==========================
# Terminal Chaos Mode Helpers
# ==========================

def trigger_mystery_box():
    """Randomly offer the player a Mystery Box with risk/reward."""
    global coins, lives, powerups
    if random.random() < 0.02:  # 2% chance per question
        cost = random.randint(2, 6)
        print(f"\n🎁 MYSTERY BOX AVAILABLE! Spend {cost} coins? (yes/no)")
        choice = input("> ").strip().lower()
        if choice == "yes":
            if coins < cost:
                print("💸 Not enough coins to buy the box.")
                return
            coins -= cost
            outcome = random.random()
            if outcome < 0.3:  # 30% gain a powerup
                key = random.choice(list(powerups.keys()))
                powerups[key] += 1
                print(f"🎉 Lucky! You gained a power-up: {key}")
            elif outcome < 0.6:  # 30% lose a powerup
                key = random.choice([k for k in powerups if powerups[k] > 0])
                powerups[key] -= 1
                print(f"💥 Oh no! Lost a power-up: {key}")
            elif outcome < 0.85:  # 25% gain a life
                lives += 1
                print("❤️ Life gained!")
            elif outcome < 0.99:  # 14% apply a temporary debuff
                print("⏱ Timer shrinks for next question!")
                # Example: push a short time limit
                time_debuff_queue.append(max(3, next_question_time_limit - 5))
            else:  # 1% instant game over
                print("💀 SYSTEM ERROR! Just kidding, game continues.")
                lives=0
        else:
            print("🚫 You skipped the Mystery Box.")

def trigger_brainrot():
    """Occasionally print chaotic text to distract player."""
    if random.random() < 0.03:  # 3% chance per question
        spam = ["🤯", "💀", "🤮", "🧠", "@#%$!", "QWERTY!!!", "###$$$%%%"]
        for _ in range(30):
            line = "".join(random.choice(spam) for _ in range(20))
            print(line)
            time.sleep(3)

def trigger_screen_blank():
    """Rarely blanks the terminal for psychological damage."""
    if random.random() < 0.005:  # 0.5% chance
        import time
        print("\n⚠️ TERMINAL FAILURE ⚠️")
        time.sleep(10)

        # Clear screen using ANSI
        print("\033[2J\033[H", end="")
        
# ==========================
# Chaos Mode: Psychological Trolls
# ==========================

fake_life_loss_active = False
fake_life_loss_counter = 0
FAKE_LIFE_LOSS_DURATION = 3  # number of questions affected

def trigger_fake_life_loss():
    """Temporarily convert all player answers to wrong to troll them."""
    global fake_life_loss_active, fake_life_loss_counter
    if not fake_life_loss_active and random.random() < 0.01:  # 1% chance
        fake_life_loss_active = True
        fake_life_loss_counter = FAKE_LIFE_LOSS_DURATION
        print("💀 CURSE OF THE WRONG ANSWER! For a few questions, your answers betray you...")

def apply_fake_life_loss(answer):
    """If fake life loss is active, override any answer to wrong."""
    global fake_life_loss_active, fake_life_loss_counter
    if fake_life_loss_active and fake_life_loss_counter > 0:
        fake_life_loss_counter -= 1
        # Randomly choose a wrong answer different from the correct one
        wrong_options = [c for c in ["A", "B", "C", "D"] if c != answer]
        return random.choice(wrong_options)
    else:
        fake_life_loss_active = False
        return answer

def trigger_gibberish_taunt():
    """Occasionally spam gibberish or taunt messages at the player."""
    if random.random() < 0.02:  # 2% chance per question
        gibberish_lines = [
            "??? ERROR ??? THE QUIZ HATES YOU !!! %$#@!^&*",
            "You think you can win? Hahaha!",
            "No one escapes the Impossible Quiz!",
            "🤯💀🤮🧠",
            "SYSTEM MALFUNCTION: ALL ANSWERS WRONG!!!"
        ]
        print("\n⚡ QUIZ IS ANGRY ⚡")
        for line in random.sample(gibberish_lines, k=3):
            print(line)

        time.sleep(random.uniform(5, 10))  # silence = panic

        # Restore
        print("\033[2J\033[H", end="")
        print("...System restored.")
        print("The quiz is not done with you.\n")

# ==========================
# Hehe
# ==========================

fake_life_loss_active = False
fake_life_loss_counter = 0
FAKE_LIFE_LOSS_DURATION = 3  # number of questions affected

def trigger_fake_life_loss():
    """Temporarily convert all player answers to wrong to troll them."""
    global fake_life_loss_active, fake_life_loss_counter
    if not fake_life_loss_active and random.random() < 0.01:  # 1% chance
        fake_life_loss_active = True
        fake_life_loss_counter = FAKE_LIFE_LOSS_DURATION
        print("💀 CURSE OF THE WRONG ANSWER! For a few questions, your answers betray you...")

def apply_fake_life_loss(answer):
    """If fake life loss is active, override any answer to wrong."""
    global fake_life_loss_active, fake_life_loss_counter
    if fake_life_loss_active and fake_life_loss_counter > 0:
        fake_life_loss_counter -= 1
        # Randomly choose a wrong answer different from the correct one
        wrong_options = [c for c in ["A", "B", "C", "D"] if c != answer]
        return random.choice(wrong_options)
    else:
        fake_life_loss_active = False
        return answer

def trigger_gibberish_taunt():
    """Occasionally spam gibberish or taunt messages at the player."""
    if random.random() < 0.02:  # 2% chance per question
        gibberish_lines = [
            "??? ERROR ??? THE QUIZ HATES YOU !!! %$#@!^&*",
            "You think you can win? Hahaha!",
            "No one escapes the Impossible Quiz!",
            "🤯💀🤮🧠",
            "6767676767676767676767676767676767676767676767676767676767676767676767676767676767"
            "skibidi mountain toaster aura glitch banana thunder ohio sideways pixel soda asphalt whisper crunch neon apple lag core memory unlocked feral cardboard wifi mosquito latte shadow NPC sidewalk battery depleted corecore spaghetti quantum elbow frog static noon hallway cinnamon laser backpack gravity socks internet penguin echo slime rooftop keyboard microwave fog notification velvet raccoon solar charger dream patch update failed spoon mirror jitter laggy pinecone subway bubble wrap Tuesday scream texture air fryer cactus vinyl pause menu broccoli portal screenshot hum vibration lemonade comet drywall cloud jpeg sneaker breadcrumbs signal lost lemon shark hoodie thermal ketchup sideways rain bookmark hamster cosmic printer stairwell pickle satellite ramen fossil earbuds milk carton dimension rip zip glitchcore lava lamp sidewalk mp3 rewind eyeball static hum cereal paperback cardboard thunder again again again hoverboard marble shoelace typo buffer overflow banana peel algorithm couch pixel dust napkin microwave II uncanny elevator core breach marshmallow bus stop echo echo receipt foghorn mailbox keyboard smash qwerty potato vibe check failed timestamp moth sweater soup crouton lunar socks.exe rebooting please wait neon gum static pop buzz whirr clank drip drop underscore underscore underscore skrrt plankton wifi dead emoji skull skull skull sideways chair aura minus ten breadcrumbs orbit noodle panic calm panic calm flashlight carpet citrus jingle chrome tab 47 still loading still loading still loading"
            "SYSTEM MALFUNCTION: ALL ANSWERS WRONG!!!"
        ]
        print("\n⚡ QUIZ IS ANGRY ⚡")
        for line in random.sample(gibberish_lines, k=3):
            print(line)


# ==========================
# Ask a single question
# ==========================
def ask_question(q):
    trigger_mystery_box()
    trigger_brainrot()
    trigger_screen_blank()
    trigger_fake_life_loss()
    trigger_gibberish_taunt()

    global time_up, lives, score, current_level, total_questions_correct, total_questions_wrong
    global questions_correct_in_level, next_question_time_limit, time_debuff_queue
    global questions_since_last_tax, questions_since_last_shop, coins

    time_up = False
    questions_since_last_tax += 1
    questions_since_last_shop += 1

    if questions_since_last_shop >= 5:
        questions_since_last_shop = 0
        open_shop()

    time_limit = time_debuff_queue.pop(0) if time_debuff_queue else next_question_time_limit

    # Display question
    print("\n==============================")
    print(glitch_text(f"{BLUE}Level {current_level}{RESET} → {RED}{questions_correct_in_level}/{level_up_table[current_level]}{RESET} → {YELLOW}Next Level{RESET}", total_questions_correct))
    print(glitch_text(f"{BRIGHT_MAGENTA}Time limit: {time_limit} seconds{RESET}", total_questions_correct))
    print(glitch_text(f"Lives remaining: {BRIGHT_RED}{lives}"+RESET, total_questions_correct))
    print(glitch_text(f"{BRIGHT_CYAN}Power-ups: {BRIGHT_YELLOW}Hint({powerups['hint']}){RESET}, {BRIGHT_GREEN}Skip({powerups['skip']}){RESET}, {BRIGHT_BLUE}Freeze({powerups['freeze']}){RESET}", total_questions_correct))

    print(f"{BRIGHT_BLACK}\n------------------------------\n{RESET}")
    print(glitch_text("Question:", total_questions_correct), glitch_text(q["question"], total_questions_correct))
    for choice in q["choices"]:
        print(glitch_text(choice, total_questions_correct))

    answer = input_with_timeout("Your answer (A/B/C/D) or 'hint', 'skip', 'freeze': ", time_limit)
    if time_up or answer is None:
        lives -= 1
        print(glitch_text("⏳ You lost a life.", total_questions_correct))
        total_questions_wrong += 1
        if total_questions_wrong in ADVANCEMENTS_NEGATIVE and ADVANCEMENTS_NEGATIVE[total_questions_wrong] not in advancements_unlocked:
            unlock_negative_advancement(total_questions_wrong)
        if lives <= 0:
            print(glitch_text("💀 GAME OVER 💀", total_questions_correct))
            sys.exit()
        return False

    answer = answer.strip().upper()
    # Apply fake life loss
    answer = apply_fake_life_loss(answer)
    if answer == "HINT" and powerups["hint"] > 0:
        powerups["hint"] -= 1
        print(glitch_text("💡 HINT: Trust nothing.", total_questions_correct))
        return ask_question(q)
    if answer == "SKIP" and powerups["skip"] > 0:
        powerups["skip"] -= 1
        print(glitch_text("⏭️ Skipped.", total_questions_correct))
        return True
    if answer == "FREEZE" and powerups["freeze"] > 0:
        powerups["freeze"] -= 1
        print(glitch_text("🧊 Timer frozen.", total_questions_correct))
        return ask_question(q)

    # Correct
    if answer == q["correct"]:
        print(glitch_text("✅ Correct!", total_questions_correct))
        score += 1
        questions_correct_in_level += 1
        coins += 1
        total_questions_correct += 1
        if total_questions_correct in ADVANCEMENTS_POSITIVE and ADVANCEMENTS_POSITIVE[total_questions_correct][0] not in advancements_unlocked:
            unlock_positive_advancement(total_questions_correct)
        if questions_correct_in_level >= level_up_table[current_level]:
            current_level += 1
            questions_correct_in_level = 0
            print(glitch_text(f"\n🎉 LEVEL UP → {current_level} 🎉", total_questions_correct))
        return True

    # Wrong
    print(glitch_text(f"❌ Wrong! Correct answer: {q['correct']}", total_questions_correct))
    total_questions_wrong += 1
    if shop_inventory["second_chance"] > 0:
        shop_inventory["second_chance"] -= 1
        print(glitch_text("🛡️ SECOND CHANCE used! Life saved.", total_questions_correct))
    else:
        lives -= 1
    if total_questions_wrong in ADVANCEMENTS_NEGATIVE and ADVANCEMENTS_NEGATIVE[total_questions_wrong] not in advancements_unlocked:
        unlock_negative_advancement(total_questions_wrong)
    if lives <= 0:
        print(glitch_text("💀 GAME OVER 💀", total_questions_correct))
        sys.exit()

    next_question_time_limit = BASE_TIME_LIMIT
    return False

# ==========================
# Game Loop
# ==========================
TOTAL_QUESTIONS = 10000
counter = 0
secret_sequence = []
secret_triggered = False

while counter < TOTAL_QUESTIONS:
    for q in random.sample(questions, len(questions)):
        ask_question(q)
        counter += 1

        if 5995 <= counter % 6000 <= 6000:
            print("⚠️ ??? GLITCH ??? ⚠️")

        # Track for secret ending (example pattern)
        secret_sequence.append(1 if q.get("correct") else 0)
        if len(secret_sequence) > 10:
            secret_sequence.pop(0)
        pattern = [0,0,0,0,0,1,1,0,0,0]
        if not secret_triggered and secret_sequence == pattern:
            print("\n🎉 SECRET ENDING REVEALED! 🎉")
            print("\n==============================")
            print("🏆 IMPOSSIBLE QUIZ COMPLETION 🏆")
            print("Congratulations, you've conquered the quiz!")
            print("\n🎉 Credits & Acknowledgments 🎉")
            print("Game Design & Development: Hyper Gaming")
            print("Special Thanks to ChatGPT for code review and shop mechanics!")
            print("All questions curated and verified by Hyper Gaming")
            print("Thank you for playing this monster of a quiz! 👾")
            print("\n==============================\n")
            secret_triggered = True

        if counter >= TOTAL_QUESTIONS:
            break
