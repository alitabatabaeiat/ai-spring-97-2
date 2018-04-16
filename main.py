from Database import Database
from Population import Population


def read_inputs():
    database = Database()

    d, t = map(int, input().split())
    database.set_days(d)
    database.set_times(t)

    c = int(input())
    database.set_courses(c)
    happiness = list(map(int, input().split()))
    database.set_happiness(happiness)
    p = int(input())
    professors = []
    for i in range(p):
        row = list(map(int, input().split()))
        del row[0]
        for j in row:
            database.add_professor_to_course(j - 1, i)
            # j is course id (**consider course ids starts from 1**)
            # i is professor id in the list of professors
        professors.append(row)
    database.set_professors(professors)

    sadness = []
    for _ in range(c):
        row = list(map(int, input().split()))
        sadness.append(row)
    database.set_sadness(sadness)

    return database


if __name__ == '__main__':
    db = read_inputs()
    db.set_population(100)
    db.set_repeat(100)
    population = Population(db)
    population.generate()
    print(population)

