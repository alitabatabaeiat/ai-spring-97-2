from Database import Database


def read_inputs(db):
    d, t = map(int, input().split())
    db.set_days(d)
    db.set_times(t)

    c = int(input())
    happiness = list(map(int, input().split()))
    db.set_happiness(happiness)
    p = int(input())
    professors_courses = []
    for i in list(range(p)):
        row = list(map(int, input().split()))
        del row[0]
        professors_courses.append(row)
    db.set_professors(professors_courses)

    sadness = []
    for i in list(range(c)):
        row = list(map(int, input().split()))
        sadness.append(row)
    db.set_sadness(sadness)


if __name__ == '__main__':
    db = Database()
    read_inputs(db)
