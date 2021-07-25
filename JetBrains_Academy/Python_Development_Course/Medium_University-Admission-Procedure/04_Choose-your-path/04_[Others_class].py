# write your code here
class University:

    def __init__(self):
        self.departments = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
        self.places = int(input())
        self.applicants = self.load_applicants()

    def load_applicants(self):
        file = open("applicant_list.txt", 'r')
        applicants = [applicant.strip('\n').split() for applicant in file]
        file.close()
        applicants.sort(key=lambda x: (-float(x[2]), x[0] + x[1]))  # sort based in GPA, then by Name
        return applicants

    def assign_applicants(self):  # launching logic per priority
        for i in range(3, 6):
            self.priority_lists(i)

    def priority_lists(self, priority):  # Actual logic to accept applicants into a department
        remaining_applicants = list(self.applicants)
        for applicant in self.applicants:
            for department in self.departments.keys():
                if applicant[priority] == department and len(self.departments.get(department)) < self.places:
                    self.departments[department].append(applicant)
                    remaining_applicants.remove(applicant)
                    break
        self.applicants = remaining_applicants


    def publish_results(self):
        for key in self.departments.keys():
            self.departments[key].sort(key=lambda x: (-float(x[2]), x[0] + x[1]))
            print(key)
            for student in self.departments[key]:
                print(" ".join(student[0:3]))
            print("")

mit = University()
mit.assign_applicants()
mit.publish_results()