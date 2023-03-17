x = input('input:')
turkish_wovels = 'aeıioöuüAEIİOÖUÜ'

# use str.maketrans() to delete all Turkish wovel letters from x
# check the documentation of str.maketrans(): https://www.w3schools.com/python/ref_string_maketrans.asp
string_mapper = str.maketrans('', '', turkish_wovels)
x = x.translate(string_mapper)

print(x)