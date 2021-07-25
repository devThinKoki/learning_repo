class UniversitySystem():
    def __init__(self):
        self.applicants = self.load_applicants()
        self.departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
        self.successful_candidates = {dept: [] for dept in self.departments}
        self.max_acceptance = int(input())

    def load_applicants(self):
        with open(r"D:\LocalServer\learning_repo\JetBrains_Academy\Python_Development_Course\Medium_University-Admission-Procedure\04_Choose-your-path\example.txt") as f:
            lines, applicants = f.readlines(), []
            for line in lines:
                first_name, last_name, gpa, *departments_by_priority = line.rstrip().split()
                applicants.append((f"{first_name} {last_name}", float(gpa), departments_by_priority))
            return sorted(applicants, key=lambda x: (-x[1], x[0]))

    def select_students(self, prior):
        # print(f"select_students({prior}) is executing....")
        current_applicants = self.applicants[:]
        # print(f"\tcurrent_applicants: {current_applicants}")
        for applicant in self.applicants:
            # print(f"\t\tApplicant: {applicant}")
            for dept in self.departments:
                # print(f"\t\t\tdept: {dept}")
                if applicant[2][prior] == dept:
                    # print(f"\t\t\t\tCurrent applicant: '{applicant[0], applicant[2]}' dept: '{dept}'")
                    # print(f"\t\t\t\tCurrent self.successful_candidates[{dept}] is '{self.successful_candidates[dept]}'")
                    if len(self.successful_candidates[dept]) < self.max_acceptance:
                        # print(f'****Current self.successful_candidates: {self.successful_candidates}')
                        self.successful_candidates[dept].append(applicant)
                        current_applicants.remove(applicant)
                        # print(f'****Changed self.successful_candidates: {self.successful_candidates}')
                        break
        self.applicants = current_applicants
        # print(f'Changd jet_brain.applicants {self.applicants}')

    def print_result(self):
        for dept in self.departments:
            print(dept)
            for accepted in self.successful_candidates[dept]:
                print(accepted[0], accepted[1])
            print()

jet_brain = UniversitySystem()
# print(f'Initial applicants: {jet_brain.applicants}')
for i in range(3):
    jet_brain.select_students(i)
jet_brain.print_result()