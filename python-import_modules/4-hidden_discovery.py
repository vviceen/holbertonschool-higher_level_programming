#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    atrib = dir(hidden_4)
    for i in atrib:
        if i[:2] != "__":
            print("{}".format(i))
