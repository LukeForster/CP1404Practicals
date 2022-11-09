from Prac7.project import Project

def main():
    choice = get_choice()
    while choice != 'Q':
        try:
            if choice == 'L':
                projects = load_projects()  # If the user selected watch then the watch_movie function is called
            elif choice == 'D':
                display_movies(movies)  # If the user selected watch then the watch_movie function is called
            elif choice == 'A':
                add_movie(movies)  # If the user selected watch then the add_movie function is called
            else:
                print('Invalid menu choice')  # If the user inputs anything other than the displayed options,
        except KeyError:  # or does not enter a string, an error message is printed.
            print('Invalid menu choice')
        choice = get_choice()


def get_choice():
    """This function will display the and get the user's input"""
    print('Menu:')
    print('L - Load Projects')
    print('S - Save Projects')
    print('A - Add Project')
    print('Q - Quit')
    choice = input('What would you like to do: ').upper()
    return choice


def load_projects():
    """The function will load the projects from the .txt in_file into a nested list"""
    in_file = open('projects.txt', 'r')  # open the in_file to be read
    projects = []
    for project in in_file:
        project = in_file.readline().split('\t')  # reads in_file's projects
        project[-1] = project[-1].strip()
        print(project)
        # project = Project(project[0], project[1], float(project[2]), project[3], project[4])
        # print(guitar)
        projects.append(project)
    in_file.close()  # closes in_file
    print(projects)
    return projects



main()
