def fizz_buzz(n=50):
    c = {"Fizz":0,"Buzz":0,"FizzBuzz":0}
    for i in range(1, n+1):
        out = ""
        if i%3==0: out+="Fizz"
        if i%5==0: out+="Buzz"
        print(out or i)
        if out in c: c[out]+=1
    print("\nCounts:", c)

if __name__=="__main__":
    fizz_buzz()
