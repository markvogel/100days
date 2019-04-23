from under100.day65 import test
import string


# https://edabit.com/challenge/ivWdkjsHtKSMZuNEc
def findShortestWords(txt):
    s = txt.translate(str.maketrans('', '', string.punctuation)).lower().split()
    s = sorted(s)

    shortest = [i for i in s if len(i) == len(min(s, key=len))]
    print(shortest)
    return (shortest)


def test_suite():
    test(findShortestWords("Strive not to be a success, but rather to be of value.") == ['a'])
    test(findShortestWords("You miss 100% of the shots you don't take.") == ['of'])
    test(findShortestWords("Life is what happens to you while you're busy making other plans.") ==
         ['is', 'to'])
    test(findShortestWords("We become what we think about.") == ['we', 'we'])
    test(
        findShortestWords("The most common way people give up their power is by thinking they don't have any.") ==
        ['by', 'is', 'up'])
    test(
        findShortestWords("The best time to plant the tree was 20 years ago. The second best time is now.") ==
        ['is', 'to'])
    test(findShortestWords("Your time is limited, so don't waste it living someone else's life.") ==
         ['is', 'it', 'so'])
    test(
        findShortestWords("You can never cross the ocean until you have the courage to lose sight of the shore.") ==
        ['of', 'to'])
    test(
        findShortestWords("There is only one way to avoid criticism: do nothing, say nothing, and be nothing.") ==
        ['be', 'do', 'is', 'to'])
    test(findShortestWords("The only person you are destined to become is the person you decide to be.") ==
         ['be', 'is', 'to', 'to'])
    test(findShortestWords(
        "What lies behind us and what lies before us are tiny matters compared to what lies within us.") ==
         ['to', 'us', 'us', 'us'])
    test(findShortestWords(
        "If you are depressed you are living in the past. If you are anxious you are living in the future. If you are at peace you are living in the present.") ==
         ['at', 'if', 'if', 'if', 'in', 'in', 'in'])
    test(findShortestWords("Happiness depends upon ourselves.") == ['upon'])
    test(findShortestWords("Chase two rabbits, catch none.") == ['two'])
    test(findShortestWords("Only the truth of who you are, if realized, will set you free.") ==
         ['if', 'of'])
    test(findShortestWords(
        "If you end up with a boring miserable life because you listened to your parents, your teacher, your priest, or some guy on television, then you deserve it.") ==
         ['a'])
    test(findShortestWords(
        "To accomplish great things, we must not only act, but also dream; not only plan, but also believe.") ==
         ['to', 'we'])
    test(findShortestWords("A tiger doesn't lose sleep over the opinion of sheep.") == ['a'])
    test(findShortestWords("Kindness is a language that the deaf can hear and the blind can see.") == ['a'])
    test(findShortestWords("Being realistic is the most common path to mediocrity.") == ['is', 'to'])
    test(findShortestWords("Bravery means finding something more important than fear.") ==
         ['fear', 'more', 'than'])
    test(findShortestWords("Can you imagine what I would do if I could do all I can?") == ['i', 'i', 'i'])
    test(findShortestWords("Believe you can and you're halfway there.") == ['and', 'can', 'you'])
    test(findShortestWords("Remember that happiness is a way of travel, not a destination.") == ['a', 'a'])
    test(findShortestWords("May the best day of your past be the worst day of your future.") ==
         ['be', 'of', 'of'])
    # Test.assert_equals(findShortestWords("a. b, c! d_ e/ f? g# hi j$ k% l^ m& n* o( p) q- r= s+ t| u[ v] w{ x} y@ z< A>"), ['a', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])


if __name__ == '__main__':
    test_suite()
