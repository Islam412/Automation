number = int(input("Enter Number:"))
def number_to_words(number):
    number2words = {'1' :"one" ,'2' :"two" ,'3' :"three" ,'4' :"four" ,'5' :"five" ,'6' :"six" ,'7' :"seven" ,'8' :"eight" ,'9' :"nine" ,'0' :"zero" ,}

    return " ".join(map(lambda i: number2words[i], str(number)))

print(number_to_words(number))