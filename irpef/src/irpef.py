tabella_reddito_aliquota = (0, 23), (15000, 27), (28000, 38), (55000, 41), (75000, 43)

def calcola_irpef(reddito):

	imposta = float(0)
	R = reddito

	while R > 0:

		scaglione = calcolo_scaglione(R)
		aliquota_scaglione = scaglione[1]
		max_scaglione =	scaglione[0]

		extra_in_scaglione = R - max_scaglione

		imposta += float(extra_in_scaglione) * (float(aliquota_scaglione) / 100)

		R = R - extra_in_scaglione

	return imposta


def calcolo_scaglione(reddito):
	#reddito e' passato come float

	lista_risultante = [0, 0]

	if reddito == 0:
		lista_risultante[0] = tabella_reddito_aliquota[1][0]
		lista_risultante[1] = tabella_reddito_aliquota[0][1]
		return lista_risultante

	for tupla in tabella_reddito_aliquota:
		if reddito > float(tupla[0]):
			lista_risultante[0] = tupla[0]
			lista_risultante[1] = tupla[1]

	return lista_risultante


def reddito_corretto(reddito):
	try:
		number = float(reddito)
	except ValueError:
		return False
	else:
		if number >= 0:
			return True
		else:
			return False


def main():

	reddito = raw_input("Inserire reddito (formato numerico, es 28341.22): ")
	status = reddito_corretto(reddito)

	while (status == False):
		reddito = raw_input("Inserire reddito (formato numerico, es 28341.22): ")
		status = reddito_corretto(reddito)

	reddito = float(reddito)

	imposta = calcola_irpef(reddito)

	print imposta


#main()
