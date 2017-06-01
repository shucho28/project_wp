import pickle

nodes = pickle.load(open('english.chow','rb'))
dict = pickle.load(open('english_struct.chow','rb'))

print(dict.searchWord(input(),nodes))