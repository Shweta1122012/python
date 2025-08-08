class india:
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the official language of India")
    def type(self):
        print("India is a developing country")
class USA:
    def capital(self):
        print("Whashington D.C is the capital of India")
    def language(self):
        print("English is the official language of India")
    def type(self):
        print("USA is a developed country")
objindia = india()
objusa = USA()
for country in (objindia, objusa):
    country.capital()
    country.language()
    country.type()  

