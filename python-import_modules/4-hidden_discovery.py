#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
    lists = dir(hidden)
    for i in range(len(lists)):
        if (lists[i][0] != '_'):
            print(lists[i])
