import random

random.random()

cho = input("want code or decode message:-")
if cho == "code":
    try:
        a = input("Enter a message:-")
    except:
        if len(a) < 2:
            raise ValueError("len should atleast 3 cher")

    if len(a) >= 2:
        b = a[1:] + a[0]
        c = [
            "srk",
            "joj",
            "yup",
            "kok",
            "uri",
            "xyz",
            "jio",
            "pok",
            "lmn",
            "qwe",
            "ert",
            "frt",
        ]
        d = [
            "fop",
            "zip",
            "mop",
            "kai",
            "sip",
            "uih",
            "jui",
            "zyx",
            "qrs",
            "frg",
            "khi",
            "wer",
        ]
        e = random.choice(c)
        f = random.choice(d)
        g = e + b + f
        h = g.split()
        print("Your coded message is:- ", g)

elif cho == "decode":
    a1 = input("Enter a code word ")
    if len(a1) < 2:
        b2 = a1.split()
        print("Your Decode word are:-", b2)
    else:
        c1 = a1[3:-3]
        d1 = c1[-1] + c1[:-1]
        print(d1)
else:
    raise ValueError("Invalid choice and input, pleasecorrect them!!")
    