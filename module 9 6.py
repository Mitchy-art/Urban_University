def all_variants(text):
    len_text = len(text)
    for start in range(1, len_text + 1):
        for end in range(len_text - start + 1):
            yield text[end: end + start]


a = all_variants("abc")
for i in a:
    print(i)
    #print(a, b = b, a+b)