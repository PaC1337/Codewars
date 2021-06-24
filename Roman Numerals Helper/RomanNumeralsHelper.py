class RomanNumerals:
	def to_roman(number):
		romset = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10 : 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
		val = ''
		i = 0
		for n in romset.keys():
			q = number // n
			val += romset[n] * q
			number -= n * q
			if number <= 0:
				break
		return val
	def from_roman(number):
		romset = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
		val = 0
		for n in range(len(number)):
			if n > 0 and romset[number[n]] > romset[number[n - 1]]:
				val += romset[number[n]] - 2 * romset[number[n - 1]]
			else:
				val += romset[number[n]]
		return val

