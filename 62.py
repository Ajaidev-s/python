try:    
    n=int(input("enter a number"));
    if(n not in range(90,120)):
        raise ValueError
except ValueError:
    print("abnormal condiction");
