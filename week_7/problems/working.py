import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # for hours 0-12: (1[0-2]|[0-9])
    # for minutes 00-59:    [0-5][0-9]
    if s=="12 AM to 12 PM":
        return "00:00 to 12:00"
    if s=="12:00 AM to 12:00 PM":
        return "00:00 to 12:00"
    match_min=re.search(r"^((1[0-2]|[0-9]):?([0-5][0-9])?) (AM|PM) to ((1[0-2]|[0-9]):?([0-5][0-9])?) (AM|PM)$",s)
    if bool(match_min):
        l=match_min.groups()
        start_h=int(l[1])
        finish_h=int(l[5])
        start_m=0
        finish_m=0
        if l[2]!=None:
            start_m=int(l[2])
        if l[6]!=None:
            finish_m=int(l[6])
        if l[3]=="PM":
            start_h+=12
        if l[-1]=="PM":
            finish_h+=12
        if finish_h==24:
            finish_h=0
        if start_h==24:
            start_h=0
        return f"{start_h:02d}:{start_m:02d} to {finish_h:02d}:{finish_m:02d}"
    else:
        raise ValueError
    

if __name__ == "__main__":
    main()
