def rythem_checker():
    vowels="aeiouyаеёиоуыэюя"

    def equality_checker(array):
        i=1
        fact=True
        while(i<len(array)):
            if array[i]!=array[i-1]:
                fact = False
                break
            i+=1
        return fact
    def vowel_counter(phrase):
        counter=0
        for i in phrase: 
            if i in vowels:
                counter+=1
        return counter
    def is_a_rythem(str):
        phrases=str.split()
        phrases=list(map(vowel_counter, phrases))
        if equality_checker(phrases):
            print("param-pam-pam")
        else:
            print("pam-param")
    is_a_rythem(str=input("insert your poetry \n note that your phrases should be devided by space symbol \n words in one phrase should be devided by '-'\n : ")
    )
    

rythem_checker()