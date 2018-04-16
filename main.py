from Database import Database
from Population import Population
from Class import Class


def read_inputs():
    database = Database()

    d, t = map(int, input().split())
    c = int(input())
    happiness = list(map(int, input().split()))
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

    database.set_days(d)\
            .set_times(t)\
            .set_courses(c, happiness)\
            .set_professors(professors)

    for i in range(c):
        sadness = list(map(int, input().split()))
        database.get_course(i).set_sadness(sadness)
    return database


if __name__ == '__main__':

    c = Class(1)

    c.set_day(2).set_time(4).set_professor(1)

    print(c)

    db = read_inputs()
    db.set_population(100)\
        .set_repeat(100)
    # population = Population(db)
    # population.generate()
    # print(population)

