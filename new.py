import json



def main():
	
	with open('Noten.json') as f:
		data = json.load(f)
	
	
	# Note in Mathe fuer alle Schueler
	tmp1 = 0
	for k1, v1 in data.iteritems():	
		for k2, v2 in v1.iteritems():		
			if k2 == "Mathe":
				tmp1 = tmp1 + int(v2)
	print tmp1
	
	# Anzahl der SChueler
	tmp2 = 0
	for k1, _ in data.iteritems():
		tmp2 = tmp2 + 1
	print tmp2
	
	# BErechnung
	print float(tmp1) / float(tmp2)
	
	

if __name__ == "__main__":
	main()
