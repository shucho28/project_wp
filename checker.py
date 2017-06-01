import pickle

nodes = pickle.load(open('english.chow','rb'))
dict = pickle.load(open('english_struct.chow','rb'))
while(1):
	print(dict.searchWord(input(),nodes))