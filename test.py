

from chaininghashtable import ChainingHashTable
from linearprobinghashtable import LinearProbingHashTable


def main():
    table = LinearProbingHashTable(4, 1)
    table.insert("Luc", 68)
    table.insert("Ludde", 4)
    table.insert("Jörgen", 7)
    table.insert("Hasse", 8)
    table.insert("Hasse", 53)

    print(table.get_keys())
    

    print(table.get("Ludde"))
    print(table.get("Luc"))
    print(table.get("Jörgen"))
    print(table.get("Hasse"))
    table.remove("Hasse")
    print(table.get("Hasse"))
    
    


    # print("testing hash table")
    # table = ChainingHashTable(1)
    
    # table.insert("Luc", 68)
    # table.insert("Ludde", 4)
    # table.insert("Jörgen", 7)
    # table.insert("Hasse", 8)
    # table.insert("Hasse", 53)

    # print(table.get("Ludde"))
    # print(table.get("Luc"))
    # print(table.get("Jörgen"))
    # print("removing")
    # table.remove("Jörgen")
    # print(table.get("Jörgen"))
    # print(table.get("Hasse"))




if __name__ == "__main__":
    main()
