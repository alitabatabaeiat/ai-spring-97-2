def read_inputs():
    d, t = map(int, input().split())
    c = int(input())
    happiness = list(map(int, input().split()))
    p = int(input())

    for i in list(range(p)):
        professor_courses = list(map(int, input().split()))
        del professor_courses[0]

    sadness = []
    for i in list(range(c)):
        row = list(map(int, input().split()))
        sadness.append(row)

if __name__ == '__main__':
    read_inputs()