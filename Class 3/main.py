# counts = dict()
# emails = []
# try:
#     with open("mbox-short.txt", mode="r") as fhand:
#         for line in fhand:
#             if line.startswith("From "):
#                 emails.append(line.split()[1])
#         for mail in emails:
#             if mail not in counts:
#                 counts[mail] = 1
#             else:
#                 counts[mail] += 1
#         print(counts)
#         max1 = max(counts.values())
#         key = max(counts, key=counts.get)
#         print(key + ': ' + str(max1))
#
# except FileNotFoundError:
#     print("File not found. Please check the file name and try again.")
# except Exception as e:
#     print("An error occurred: ", e),


# import re
#
# text = "The rain in Spain"
# x = re.split('\s', text, 1)
# print(x)
#
# numbers = [37107287533902102798797998220837590246510135740250, 46376937677490009712648124896970078050417018260538,
#            74324986199524741059474233309513058123726617309629, 91942213363574161572522430563301811072406154908250,
#            23067588207539346171171980310421047513778063246676, 89261670696623633820136378418383684178734361726757,
#            28112879812849979408065481931592621691275889832738, 44274228917432520321923589422876796487670272189318,
#            47451445736001306439091167216856844588711603153276, 70386486105843025439939619828917593665686757934951,
#            62176457141856560629502157223196586755079324193331, 64906352462741904929101432445813822663347944758178,
#            92575867718337217661963751590579239728245598838407, 58203565325359399008402633568948830189458628227828,
#            80181199384826282014278194139940567587151170094390, 35398664372827112653829987240784473053190104293586,
#            86515506006295864861532075273371959191420517255829, 71693888707715466499115593487603532921714970056938,
#            54370070576826684624621495650076471787294438377604, 53282654108756828443191190634694037855217779295145,
#            36123272525000296071075082563815656710885258350721, 45876576172410976447339110607218265236877223636045,
#            17423706905851860660448207621209813287860733969412, 81142660418086830619328460811191061556940512689692,
#            51934325451728388641918047049293215058642563049483, 62467221648435076201727918039944693004732956340691,
#            15732444386908125794514089057706229429197107928209, 55037687525678773091862540744969844508330393682126,
#            18336384825330154686196124348767681297534375946515, 80386287592878490201521685554828717201219257766954,
#            78182833757993103614740356856449095527097864797581, 16726320100436897842553539920931837441497806860984,
#            48403098129077791799088218795327364475675590848030, 87086987551392711854517078544161852424320693150332,
#            59959406895756536782107074926966537676326235447210, 69793950679652694742597709739166693763042633987085,
#            41052684708299085211399427365734116182760315001271, 65378607361501080857009149939512557028198746004375,
#            35829035317434717326932123578154982629742552737307, 94953759765105305946966067683156574377167401875275,
#            88902802571733229619176668713819931811048770190271, 25267680276078003013678680992525463401061632866526,
#            36270218540497705585629946580636237993140746255962, 24074486908231174977792365466257246923322810917141,
#            91430288197103288597806669760892938638285025333403, 34413065578016127815921815005561868836468420090470,
#            23053081172816430487623791969842487255036638784583, 11487696932154902810424020138335124462181441773470,
#            63783299490636259666498587618221225225512486764533, 67720186971698544312419572409913959008952310058822,
#            95548255300263520781532296796249481641953868218774, 76085327132285723110424803456124867697064507995236,
#            37774242535411291684276865538926205024910326572967, 23701913275725675285653248258265463092207058596522,
#            29798860272258331913126375147341994889534765745501, 18495701454879288984856827726077713721403798879715,
#            38298203783031473527721580348144513491373226651381, 34829543829199918180278916522431027392251122869539,
#            40957953066405232632538044100059654939159879593635, 29746152185502371307642255121183693803580388584903,
#            41698116222072977186158236678424689157993532961922, 62467957194401269043877107275048102390895523597457,
#            23189706772547915061505504953922979530901129967519, 86188088225875314529584099251203829009407770775672,
#            11306739708304724483816533873502340845647058077308, 82959174767140363198008187129011875491310547126581,
#            97623331044818386269515456334926366572897563400500, 42846280183517070527831839425882145521227251250327,
#            55121603546981200581762165212827652751691296897789, 32238195734329339946437501907836945765883352399886,
#            75506164965184775180738168837861091527357929701337, 62177842752192623401942399639168044983993173312731,
#            32924185707147349566916674687634660915035914677504, 99518671430235219628894890102423325116913619626622,
#            73267460800591547471830798392868535206946944540724, 76841822524674417161514036427982273348055556214818,
#            97142617910342598647204516893989422179826088076852, 87783646182799346313767754307809363333018982642090,
#            10848802521674670883215120185883543223812876952786, 71329612474782464538636993009049310363619763878039,
#            62184073572399794223406235393808339651327408011116, 66627891981488087797941876876144230030984490851411,
#            60661826293682836764744779239180335110989069790714, 85786944089552990653640447425576083659976645795096,
#            66024396409905389607120198219976047599490197230297, 64913982680032973156037120041377903785566085089252,
#            16730939319872750275468906903707539413042652315011, 94809377245048795150954100921645863754710598436791,
#            78639167021187492431995700641917969777599028300699, 15368713711936614952811305876380278410754449733078,
#            40789923115535562561142322423255033685442488917353, 44889911501440648020369068063960672322193204149535,
#            41503128880339536053299340368006977710650566631954, 81234880673210146739058568557934581403627822703280,
#            82616570773948327592232845941706525094512325230608, 22918802058777319719839450180888072429661980811197,
#            77158542502016545090413245809786882778948721859617, 72107838435069186155435662884062257473692284509516,
#            20849603980134001723930671666823555245252804609722, 53503534226472524250874054075591789781264330331690]
#
# print(str(sum(numbers))[:10])
#

# longest_chain = 0
# starting_number = 0
#
# for number in range(100000, 1000000):
#     sequence = []
#     new_number = number
#     while new_number > 1:
#         sequence.append(new_number)
#         if new_number % 2 == 0:
#             new_number = new_number // 2
#         else:
#             new_number = 3 * new_number + 1
#     sequence.append(1)
#     if len(sequence) > longest_chain:
#         longest_chain = len(sequence)
#         starting_number = number
#
# print(starting_number)

# def number_of_letters(n):
#     """Returns the number of letters used to write out a number in words."""
#     if n == 1000:
#         return 11 # "one thousand"
#     ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
#             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
#     tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
#     if n < 20:
#         return len(ones[n])
#     elif n < 100:
#         return len(tens[n // 10]) + len(ones[n % 10])
#     elif n < 1000:
#         hundred_digit = ones[n // 100]
#         if n % 100 == 0:
#             return len(hundred_digit) + len("hundred")
#         else:
#             return len(hundred_digit) + len("hundredand") + number_of_letters(n % 100)
#
# total_letters = sum(number_of_letters(n) for n in range(1, 1001))
# print(total_letters)


# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def count_sundays_on_first_of_month():
#     # Start on 1 Jan 1901, which was a Tuesday
#     day_of_week = 2
#     count = 0
#
#     for year in range(1901, 2001):
#         for month in range(1, 13):
#             # Determine the number of days in the month
#             if month in [4, 6, 9, 11]:
#                 days_in_month = 30
#             elif month == 2:
#                 if is_leap_year(year):
#                     days_in_month = 29
#                 else:
#                     days_in_month = 28
#             else:
#                 days_in_month = 31
#
#             # If the first day of the month is a Sunday, we add 1
#             if day_of_week == 0:
#                 count += 1
#
#             # Advance the day of the week to the first day of the next month
#             day_of_week = (day_of_week + days_in_month) % 7
#
#     return count
#
#
# print(count_sundays_on_first_of_month())


# def divisors_of_n(n):
#     """Returns the sum of proper divisors of n"""
#     list_of_nums = []
#     for i in range(1, n):
#         if (n / i).is_integer():
#             list_of_nums.append(i)
#     return sum(list_of_nums)
#
#
# """Iterates from 2 to 10000 to check for amicables and then add
# them to a set to make sure they don't repeat"""
# amicable_numbers = set()
# for i in range(2, 10000):
#     sum_div_i = divisors_of_n(i)
#     if sum_div_i != i and divisors_of_n(sum_div_i) == i:
#         amicable_numbers.add(i)
#         amicable_numbers.add(sum_div_i)
# # Finally we sum all the numbers up
# print(sum(amicable_numbers))

# def sum_proper_divisors(n):
#     return sum(i for i in range(1, n) if n % i == 0)
#
#
# abundant_numbers = set()
# for i in range(1, 28123):
#     if sum_proper_divisors(i) > i:
#         abundant_numbers.add(i)
#
# sums_of_abundant_numbers = set()
# for i in abundant_numbers:
#     for j in abundant_numbers:
#         if i + j > 28123:
#             break
#         sums_of_abundant_numbers.add(i + j)
#
# total = sum(i for i in range(1, 28123) if i not in sums_of_abundant_numbers)
# print(total)
#
# """A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1,
# 2, 3 and 4. If all the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012 021 102 120 201 210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
#
# import math
#
# digits = list(range(10))
# n = len(digits)
# k = 1000000
# permutation = []
#
# while n > 0:
#     f = math.factorial(n-1)
#     index = math.ceil(k/f) - 1
#     digit = digits[index]
#     permutation.append(digit)
#     digits.remove(digit)
#     k = k % f
#     n -= 1
#
# print(''.join(str(d) for d in permutation))

def find_longest_recurring_cycle():
    # Initialize variables to store the max cycle length and the corresponding d value
    max_cycle_length = 0
    max_cycle_d = 0

    # Loop over possible values of d
    for d in range(1, 1000):
        # Initialize variables for the long division process
        remainders = []
        remainder = 1

        # Perform long division to find the decimal expansion of 1/d
        while remainder not in remainders:
            remainders.append(remainder)
            remainder = (remainder * 10) % d

        # If the long division process repeats a sequence of digits, it has a recurring cycle
        if remainder != 0:
            cycle_length = len(remainders) - remainders.index(remainder)
            if cycle_length > max_cycle_length:
                max_cycle_length = cycle_length
                max_cycle_d = d

    # Return the d value with the longest recurring cycle
    return max_cycle_d

print(find_longest_recurring_cycle())