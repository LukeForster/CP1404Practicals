from Prac7.project import Project
import datetime


def main():
    choice = get_choice()
    projects = []
    while choice != 'Q':
        try:
            if choice == 'L':
                projects = load_projects(projects)  # If the user selected watch then the watch_movie function is called
            elif choice == 'S':
                print('save')
            elif choice == 'D':
                display_projects(projects)
            elif choice == 'A':
                add_project(projects)# If the user selected watch then the add_movie function is called
            elif choice == 'U':
                update_project(projects)
                print('u')
            else:
                print('Invalid menu choice')  # If the user inputs anything other than the displayed options,
        except KeyError:  # or does not enter a string, an error message is printed.
            print('Invalid menu choice')
        choice = get_choice()


def update_project(projects):
    project_name = input('Name of Project: ')
    for project in projects:
        print('f')
        if project_name == project.name:
            updating_choice = input('Priority and/or Completion Pecentage (P/C): ').upper()
            while updating_choice != '':
                if updating_choice == 'P':
                    priority = int(input('New Priority: '))
                    project.priority = priority
                    print(project.priority)
                    # project[2] = project.priority = priority
                    updating_choice = input('Priority and/or Completion Pecentage (P/C): ').upper()
                elif updating_choice == 'C':
                    completion_percentage = int(input('New Percentage: '))
                    project[3] = project.completion = completion_percentage
                    updating_choice = input('Priority and/or Completion Pecentage (P/C): ').upper()
                else:
                    print('Invalid')
        else:
            print('Invalid Project')


def add_project(projects):
    project = []
    name = input('Name: ')
    start_date = input('Start Date: ')
    priority = int(input('Priority Level: '))
    cost = float(input('Cost: '))
    completion_percentage = int(input('Completion Percentage: '))
    project.append(name)
    project.append(start_date)
    project.append(priority)
    project.append(cost)
    project.append(completion_percentage)
    projects.append(project)
    return projects

def display_projects(projects):
    print(projects)
    projects.sort()
    for project in projects:
        print(project)  # If the user selected watch then the watch_movie function is called


def get_choice():
    """This function will display the and get the user's input"""
    print('Menu:')
    print('L - Load Projects')
    print('S - Save Projects')
    print('D - Display Projects')
    print('A - Add Project')
    print('F - Filter Project')
    print('U - Update Project')
    print('Q - Quit')
    choice = input('What would you like to do: ').upper()
    return choice


def load_projects(projects):
    """The function will load the projects from the .txt in_file into a nested list"""
    in_file = open('projects.txt', 'r')  # open the in_file to be read
    for project in in_file:
        project = in_file.readline().split('\t')  # reads in_file's projects
        project[-1] = project[-1].strip()
        # print(project)
        project = Project(project[0], project[1], int(project[2]), float(project[3]), int(project[4]))
        print(project)
        projects.append(project)
    in_file.close()  # closes in_file
    # print(projects)
    return projects


def filter_projects(projects):
    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date_req = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    print(f"That day is/was {date_req.strftime('%A')}")
    print(date_req.strftime("%d/%m/%Y"))


main()
