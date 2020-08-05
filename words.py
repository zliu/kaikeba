

def list_words(file):
    content = []
    with open(file, 'r') as infile:
       content = infile.readlines()
    words = {}
    for line in content:
      for word in line:
        if not word in words:
           words[word] = 1
        else:
           words[word] += 1
    return sorted(words.items(), key=lambda word:word[1])



word_list = list_words('input.txt')
for w in word_list:
   print(w[0],w[1])