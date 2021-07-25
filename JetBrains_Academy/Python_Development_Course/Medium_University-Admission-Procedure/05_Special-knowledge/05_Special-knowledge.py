class UniversitySystem():
    def __init__(self):
        self.applicants = self.load_applicants()
        self.departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
        self.successful_candidates = {dept: [] for dept in self.departments}
        self.max_acceptance = int(input())

    def load_applicants(self):
        with open(r"D:\LocalServer\learning_repo\JetBrains_Academy\Python_Development_Course\Medium_University-Admission-Procedure\05_Special-knowledge\applicants.txt") as f:
            lines, applicants = f.readlines(), []
            for line in lines:
                first_name, last_name, p, c, m, cs, *departments_by_priority = line.rstrip().split()
                applicant = (f"{first_name} {last_name}", [c, c, cs, m, p], departments_by_priority)
                # print(applicant)
                applicants.append((f"{first_name} {last_name}", [c, c, cs, m, p], departments_by_priority))
            return applicants

    def select_students(self, prior):
        # print(f"select_students({prior}) is executing....")
        for idx, dept in enumerate(self.departments):
            current_applicants = self.applicants[:]
            # print(f"\tcurrent_applicants: {current_applicants}")
            for applicant in self.sort_by_score_name(self.applicants, idx):
                # print(f"\t\tApplicant: {applicant}")
                if applicant[2][prior] == dept:
                    # print(f"\t\t\t\tCurrent applicant: '{applicant[0], applicant[1], applicant[2]}' dept: '{dept}'")
                    # print(f"\t\t\t\tCurrent self.successful_candidates[{dept}] is '{self.successful_candidates[dept]}'")
                    if len(self.successful_candidates[dept]) < self.max_acceptance:
                        # print(f'****Current self.successful_candidates: {self.successful_candidates}')
                        self.successful_candidates[dept].append(applicant)
                        current_applicants.remove(applicant)
            self.applicants = current_applicants
            # print(f'****Changed self.successful_candidates: {self.successful_candidates}')
        # print(f'Changd jet_brain.applicants {self.applicants}')


    def sort_by_score_name(self, original_list, idx):
        return sorted(original_list, key=lambda x: (-int(x[1][idx]), x[0]))

    
    def print_result(self):
        for idx, dept in enumerate(self.departments):
            print(dept)
            for accepted in self.sort_by_score_name(self.successful_candidates[dept], idx):
                print(accepted[0], float(accepted[1][idx]))
            print()

jet_brain = UniversitySystem()
for prior in range(3):
    jet_brain.select_students(prior)
jet_brain.print_result()