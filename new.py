import json
def summe_noten(data, fachname):
	tmp1 = 0
	for k1, v1 in data.iteritems():	
			for k2, v2 in v1.iteritems():		
				if k2 == fachname:
					tmp1 = tmp1 + int(v2)
	return tmp1
	
def anzahl_schueler(data):
	tmp2 = 0
	for k1, _ in data.iteritems():
		tmp2 = tmp2 + 1
	return tmp2
	
def durchschnitt(tmp1, tmp2):
	return float(tmp1) / float(tmp2)
	
	
def beste_note(data, fachname):
	note_aktuell = 0
	note_beste = 0
	
	for k1, v1 in data.iteritems():	
		for k2, v2 in v1.iteritems():		
			if k2 == fachname:
				note_aktuell = int(v2)
				if note_aktuell < note_beste or note_beste == 0:
					note_beste = note_aktuell
	return note_beste
	

	
	
def main():
	
	with open('Noten.json') as f:
			data = json.load(f)
	
	print beste_note(data, "Mathe")
	
	
if __name__ == "__main__":
	main()