if __name__ == '__main__':
    n = int(input())
    array = map(int, input().split())
    arr = list(array)
    arr.sort()
    arr.reverse()
    maxx=arr[0]
    for i in range(0,n):
        if arr[i]<maxx:
            print(arr[i])
            break
