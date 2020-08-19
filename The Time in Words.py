ones = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'ninety']
tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty']
h = int(input())
m = int(input())
x = 60 - m
if m == 0:
    print(ones[h]+" o' clock")
elif m % 10 == 0 and m < 30:
    print(tens[int(m/10)-1]+" minutes past "+ones[h])
elif m == 1:
    print("one minute past "+ones[h])
elif m < 15:
    print(ones[m-1]+" minutes past "+ones[h])
elif m == 15:
    print("quarter past "+ones[h])
elif 15 < m < 30:
    if 15 < m < 20:
        print(ones[m-1]+" minutes past "+ones[h])
    else:
        print(tens[int(m/10)-1]+" "+ones[m%10]+" minutes past "+ones[h])
elif m == 30:
    print("half past "+ones[h])
elif x % 10 == 0 and x < 30:
    print(tens[int(x/10)-1]+" minutes to "+ones[h+1])
elif x < 15:
    print(ones[x]+" minutes to "+ones[h+1])
elif x == 15:
    print("quarter to "+ones[h+1])
elif 15 < x < 30:
    if 15 < x < 20:
        print(ones[x]+" minutes to "+ones[h+1])
    elif 20 <= x < 30:
        print(tens[int(x/10)-1]+" "+ones[x%10]+" minutes to "+ones[h+1])