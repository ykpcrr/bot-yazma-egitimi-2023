# breaking into pieces and index string

name = "Yakubi"

print(name[0])
print(name[0:3])
print(name[3:])
print(name[0::2])
print(name[6::-2])
print(name[::-1])

# Change and remove strings

text = "Hello World"
print(text[:6] + "Türkiye")

# del text[2] => ERROR

# String combining and reset

word1 = "hello"
word2 = "türkiye"
words = word1.upper() + " " + word2.upper()
print(words)

name = "Yakubi"
age = "16"

message = "My name is {} and my age is {} ".format(name, age)
message = "My name is {1} and my age is {0}".format(age, name)
message = "My name is {x} and my age is {y} ".format(x=name, y=age)
message = f"My name is {name} and my age is {age}"
print(message)

# STRİNG METHODS

article = "Ramazan boyunca her gün saat 13.00'da canlı mukabele etkinliğimize davetlisiniz! İnstagram hesabımızdan canlı yayın yapacağımız bu etkinlikte, her gün farklı bir hafızımız        Kur'an-ı Kerim tilaveti gerçekleştirecek. Siz de bizlerle birlikte bu mübarek ayda manevi bir yolculuğa çıkmak için takipte kalın..."

# Capitalize
print(article.capitalize())

# Upper
print(article.upper())

# lower
print(article.lower())

# title
print(article.title())

# strip()

text = "                                                       Hello World                                             "
print(text.strip())

print(text.rstrip())
print(text.lstrip())

print(article.strip("r"))

# replace

print(article.replace("ramazan", "Şehr-i Ramazan"))
print(article.replace("a", "e"))

# split
print(article.split())
print(article.split(". "))


# join
words = ["Hello", "My", "Name", "is", "Eren"]
sentences = ",".join(words)
sentences = " ".join(words)
print(sentences)

# count
print(article.count("a"))
print(article.count("Instagram")) # because it is İnstagram not Instagram

# endswidth

print(article.endswith("."))

# startswidth

print(article.startswith("Ş"))

# STRİNGS ESCAPE WAYS
# \" : " in string

print("Yakubi said \"my age is 16\" ")

# \n : New lane
print("Yakubi says: \n Mandolorians strong together")

# \t
print("Yakubi says: \n \t Mandolorians strong together")

# \\ = \

print("Yakubi \\ siuuuuu")