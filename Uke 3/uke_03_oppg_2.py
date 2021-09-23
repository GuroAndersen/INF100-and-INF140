navn = input ("Hva er ditt navn? ")
adresse = input ("Hva er din adresse? ")
post = input ("Hva er ditt postnummer og poststed? ")
total = max (len(navn), len(adresse), len(post))
print ("")
if total == len(navn):
    print (navn)
if total == len(adresse):
    print (adresse)
if total == len(post):
    print (post)