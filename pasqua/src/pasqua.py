import datetime

def calcolo_pasqua(anno):
	
	#Calcolo della pasqua secondo il metodo di Gauss

  	tabella = 	{15:(22, 2), 16:(22, 2), 17:(23, 3), 18:(23, 4), 19:(24, 5),
				20:(24, 5), 21:(24, 6), 22:(25, 0), 23:(26, 1), 24:(25, 1)}
	m, n = tabella[anno//100]
	a=anno%19
	b=anno%4
	c=anno%7
	d=(19*a+m)%30
	e=(2*b+4*c+6*d+n)%7
	giorno=d+e
	if (d+e<10):
		giorno+=22
		mese=3
	else:
		giorno-=9
		mese=4
	if ((giorno==26) or ((giorno==25) and (d==28) and (e==6) and (a>10))):
		giorno-=7
	return datetime.date(anno, mese, giorno)

def is_year_correct(year):
	try:
		number = int(year)
	except ValueError:
		return False
	else:
		if number >= 1583 and number <=2499:
			return True
		else:
			return False

def main():
	
	year = raw_input('Insert year (>= 1583): ')
	status = is_year_correct(year)
	
	while (status == False):
		year = raw_input('Insert year (>= 1583): ')
		status = is_year_correct(year)
	
	number = int(year)
	print calcolo_pasqua(number).strftime("%d %B %Y")
	
#main()
