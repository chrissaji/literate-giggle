from sys import argv


def main():
    # Sample code to read inputs from the file


    items = {  26:"TOI",
               19:"Hindu",
             34:"ET",
             10.5:"BM",
             18:"HT"

             }



    x=int(input())
    l=[]
    for i in items:
        ind=list(items).index(i)

        for j in items:
            if list(items).index(j)<=ind:
                continue
            else:
                if i+j<x:
                    l.append((items[i],items[j]))
    l=set(l)
    print(l)



if __name__ == "__main__":
    main()