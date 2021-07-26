class UniversitySystem():
    def __init__(self):
        self.applicants = self.load_applicants()
        # based on applicant's prior departments _i.g pysics departments physic(which is 0th score of scores) and math(which is 3rd score in scores) scores- they will chosee right score and operate with it.
        self.departments = {"Biotech": (0,1), "Chemistry": (1,), "Engineering": (2, 3), "Mathematics": (2,), "Physics": (0, 2)}
        self.successful_candidates = {dept: [] for dept in self.departments.keys()}
        self.max_acceptance = int(input())

    def load_applicants(self):
        with open(r"D:\LocalServer\learning_repo\JetBrains_Academy\Python_Development_Course\Medium_University-Admission-Procedure\06_Extensive-training\example.txt") as f:
            lines, applicants = f.readlines(), []
            for line in lines:
                first_name, last_name, p, c, m, cs, *departments_by_priority = line.rstrip().split()
                # full_name, scores = f'{first_name} {last_name}', [int(p), int(c), int(m), int(cs)]
                # applicant = full_name, [c, c, cs, m, p], departments_by_priority)
                # print(applicant)
                applicants.append((f"{first_name} {last_name}", [int(p), int(c), int(m), int(cs)], departments_by_priority))
            return applicants

    def select_students(self, prior):
        # print(f"select_students({prior}) is executing....")
        for dept, targets in self.departments.items():
            current_applicants = self.applicants[:]
            # print(f"\tcurrent_applicants: {current_applicants}")
            for applicant in self.sort_by_score_name(self.applicants, dept, targets):
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

    def calculate_mean(self, applicant, targets):
        scores = [int(applicant[1][i]) for i in targets]
        return sum(scores) / len(scores)

    def sort_by_score_name(self, original_list, dept, targets):

        return sorted(original_list, key=lambda x: (-self.calculate_mean(x, targets), x[0]))

    
    def print_result(self):
        for dept, targets in self.departments.items():
            print(dept)
            for accepted in self.sort_by_score_name(self.successful_candidates[dept], dept, targets):
                print(accepted[0], self.calculate_mean(accepted, targets))
            print()

    def write_file(self):
        for dept, targets in self.departments.items():
            file_name = f"{dept}.txt"
            with open(file_name, 'w') as f:
                for accepted in self.sort_by_score_name(self.successful_candidates[dept], dept, targets):
                    f.write(f"{accepted[0]} {self.calculate_mean(accepted, targets)}\n")
jet_brain = UniversitySystem()
for prior in range(3):
    jet_brain.select_students(prior)
# jet_brain.print_result()
jet_brain.write_file()
