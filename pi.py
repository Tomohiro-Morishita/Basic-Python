text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
answer = ''
text = text.replace(",","")
text = text.replace(".","")
for i in map(len,text.split()):
    answer += str(i)
print(answer)
