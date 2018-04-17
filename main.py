from Database import Database
from Population import Population


def read_inputs():
    database = Database()

    d, t = map(int, input().split())
    c = int(input())
    happiness = list(map(int, input().split()))
    database.set_slots(d, t)\
            .set_courses(c, happiness)

    p = int(input())
    for i in range(p):
        professor = list(map(int, input().split()))
        del professor[0]
        for j in professor:
            database.add_professor_to_course(j - 1, i)
            # j is course id (**consider course ids starts from 1**)
            # i is professor id in the list of professors

    for i in range(c):
        sadness = list(map(int, input().split()))
        database.get_course(i).set_sadness(sadness)
    return database


if __name__ == '__main__':
    db = read_inputs()
    db.set_population(100)\
        .set_repeats(100)
    population = Population(db)
    population.generate()
    print(population)

