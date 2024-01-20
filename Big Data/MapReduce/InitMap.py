def carre(x):
    return x*x

if __name__=="__main__":
    itertor=map(carre, [1, 2, 3])
    print(list(itertor))