from person import Person

my_friends = [Person('Ivan Ivanov', 20, 'M'),
              Person('Artem Artemov', 23, 'M'),
              Person('Anna Petrovna', 25, 'F'),
              Person('Viktoria Secret', 27, 'F')]
for friends in my_friends:
    friends.print_person_info()
    print(friends.get_birth_year(), end="\n\n")

def get_oldest_person(friends: list):
    years = 0
    oldest = None
    for friend in friends:
        if friend.age > years:
            years = friend.age
            oldest = friend
    if oldest:
        oldest.print_person_info()


def filter_male_person(friends: list):
    [i.print_person_info() for i in friends if i.gender == 'M']


get_oldest_person(my_friends)
filter_male_person(my_friends)