months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    l_dates=get_input()
    data_printer(l_dates)

def get_input():
    while True:
        try:
            inp=input("Date: ")
            if inp[0].isalpha():
                inp=inp.split()
                if inp[1][-1]==",":
                    day=int(inp[1].split(",")[0])
                    mon=months.index(inp[0])+1
                    if day<=31:
                        return [int(inp[2]),mon,day]
            else:
                inp=inp.split("/")
                day=int(inp[1])
                mon=int(inp[0])
                if day<=31 and mon<=12:
                    return [int(inp[2]),mon,day]
        except EOFError:
            break
        except:
            continue

def data_printer(l):
    print(f"{l[0]:04}-{l[1]:02}-{l[2]:02}")

main()