## ***Need Skills***
- ***Intro to computational thinking***
- ***Components of computational thinking***
- Slicing
- Dictionary
- Scopes
- ***Functional decomposition***
- Dictioinary methods
- Operations with dictionary
- Introduction to operating systems
- Files
- File types
- Command line overview
- Introduction to Linux
- File modes and permissions
- Files in Python
- Reading files

# Goal
- From now on, every potential student can apply for one particular department of their liking.<br>
The ranking takes place between applicants that chose the same department.

# Description
- Good news everyone: our university keeps growing larger!<br>
Five departments have been established;<br>
    - now our potential students can apply to the Mathematics, Physics, Biotech, Chemistry, or the Engineering Department.<br>
- Each applicant needs to choose three departments and rank them.
    1. First, the department with the highest priority;<br>
    1. second, the department in case the first option doesn't work out.
    1. The third department is Plan C.
- Your task for this stage is to develop an algorithm that will sort the applicants according to their GPA and take into account their priorities:<br>
    - if the applicant doesn't score high enough to get accepted to the department of first priority, they'll participate in the rankings for the second priority, and so on.
- In other words, the admission algorithm should work by the following rules:
    1. Firstly, the ranking list for every department is created according to the applicant's first priorities.<br>
    People who chose Physics as their first priority only participate in ranking for the Physics department, and so on.
    1. Applicants are scored according to their GPA.<br>
    People who have a higher GPA score are ranked higher in the department's ranking list.
    1. Each department accepts `N` (maximum number of students for the department) best students from the department's ranking list.<br>
    If there are fewer than `N` students on the department's list, all students from the list are accepted.
    1. The accepted students are removed from the general list of applicants and no longer participate in the ranking.
    1. The same procedure is repeated for the second priorities.<br>
    If there are departments that accepted fewer than `N` students in the first stage of admission, these departments try to accept more students to fill all `N` student positions.
    1. The same procedure is repeated for the third priority.
## Hint
- You may want to create a new list of applicants after each wave of admissions.<br>
In this list, you only need to include the applicants that weren't yet accepted to any department.<br>
Then, you repeat the procedure of admission using this new, updated list of applicants.
- The number of applicants is increasing, so instead of parsing the data through the manual input, we've created [the file](https://stepik.org/media/attachments/lesson/493610/applicant_list.txt) that contains the list of potential students for your program to read.<br>
It is much more convenient to provide your program with information on applicants in this way.

# Objective
- At this stage, your program should:
    1. Read an `N` integer from the input.<br>
    This integer represents the maximum number of students for each department.
    1. Read the file named *applicants.txt* (this file is already included in the project's files, even though it is not visible; so you only need to download it if you want to take a closer look at it).<br>
    Each line equals one applicant, their first name, last name, GPA, first priority department, second priority department, and third priority department.<br>
    Columns with values are separated by whitespace characters.<br>
    For example, `Laura Spungen 3.71 Physics Engineering Mathematics`.
    1. Sort applicants according to their GPA and priorities (and names, if their GPA score is the same).<br>
    As in the previous stage, if two applicants to the same department have the same GPA, sort them by their full names in alphabetical order.
    1. For each department, choose the `N` best candidates.<br>
    Some departments are less popular than others, so there may be fewer available candidates for a department.<br>
    However, their number shouldn't be more than `N`.
    1. Print the departments in the alphabetic order (Biotech, Chemistry, Engineering, Mathematics, Physics), output the names and the GPA of enrolled applicants for each department.<br>
    Separate the name and the GPA with a whitespace character.<br>
    Here's an example (you may add empty lines between the departments' lists to increase the text readability):
```
department1_name
applicant1 GPA1
applicant2 GPA2
applicant3 GPA3

department2_name
applicant1 GPA1
applicant2 GPA2
applicant3 GPA3
<...>
```
    
# Example
- The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the output.

#### **Example 1.** There are enough students for all departments:
- Below is an example of the input file:
```
Natha Keefe 3.14 Engineering Biotech Chemistry
Crescentia Dow 3.79 Chemistry Physics Mathematics
Randon Bradhust 3.68 Biotech Engineering Chemistry
Dashawn Bosley 3.54 Mathematics Chemistry Biotech
Nicolasa Sumpter 3.82 Engineering Mathematics Biotech
Cressie Gillespie 3.10 Physics Mathematics Engineering
Tawny Crockett 3.01 Chemistry Biotech Physics
Kennon Inverarity 3.50 Mathematics Engineering Chemistry
Halima Brydone 3.72 Chemistry Physics Mathematics
Esther Bratby 2.67 Mathematics Chemistry Biotech
Lorry Bunger 3.79 Engineering Biotech Physics
Fatemah Desavigny 3.00 Physics Mathematics Engineering
Marti Mclaws 3.05 Engineering Chemistry Biotech
Estephanie Phelps 3.21 Chemistry Physics Mathematics
Tommi Peerless 3.85 Engineering Physics Mathematics
Cynthia Hermitton 3.10 Engineering Biotech Chemistry
Cheyla Hankinson 3.82 Engineering Mathematics Biotech
Giovanna Keel 3.25 Physics Mathematics Engineering
Narissa Worthington 3.30 Biotech Chemistry Mathematics
Aundria Guthrie 3.51 Mathematics Chemistry Engineering
Teneil Maclean 3.22 Mathematics Physics Chemistry
Shealynn Melville 3.02 Mathematics Chemistry Physics
Darrah Smyth 3.89 Physics Biotech Engineering
```
-  An example of the output:
```
> 4
Biotech
Randon Bradhust 3.68
Narissa Worthington 3.3
Natha Keefe 3.14
Cynthia Hermitton 3.1

Chemistry
Crescentia Dow 3.79
Halima Brydone 3.72
Estephanie Phelps 3.21
Tawny Crockett 3.01

Engineering
Tommi Peerless 3.85
Cheyla Hankinson 3.82
Nicolasa Sumpter 3.82
Lorry Bunger 3.79

Mathematics
Dashawn Bosley 3.54
Aundria Guthrie 3.51
Kennon Inverarity 3.5
Teneil Maclean 3.22

Physics
Darrah Smyth 3.89
Giovanna Keel 3.25
Cressie Gillespie 3.1
Fatemah Desavigny 3.0
```
#### **Example 2.** There aren't enough students for all departments:
- Below is an example of the input file:
```
Natha Keefe 3.14 Engineering Biotech Chemistry
Crescentia Dow 3.79 Chemistry Physics Mathematics
Randon Bradhust 3.68 Biotech Engineering Chemistry
Dashawn Bosley 3.54 Mathematics Chemistry Biotech
Nicolasa Sumpter 3.82 Engineering Mathematics Biotech
Cressie Gillespie 3.10 Physics Mathematics Engineering
Tawny Crockett 3.01 Chemistry Biotech Physics
Kennon Inverarity 3.50 Mathematics Engineering Chemistry
Halima Brydone 3.72 Chemistry Physics Mathematics
Esther Bratby 2.67 Mathematics Chemistry Biotech
Lorry Bunger 3.79 Engineering Biotech Physics
Fatemah Desavigny 3.00 Physics Mathematics Engineering
Marti Mclaws 3.05 Engineering Chemistry Biotech
Estephanie Phelps 3.21 Chemistry Physics Mathematics
Tommi Peerless 3.85 Engineering Physics Mathematics
Cynthia Hermitton 3.10 Engineering Biotech Chemistry
Cheyla Hankinson 3.82 Engineering Mathematics Biotech
Giovanna Keel 3.25 Physics Mathematics Engineering
Narissa Worthington 3.30 Biotech Chemistry Mathematics
Aundria Guthrie 3.51 Mathematics Chemistry Engineering
Teneil Maclean 3.22 Mathematics Physics Chemistry
Shealynn Melville 3.02 Mathematics Chemistry Physics
Darrah Smyth 3.89 Physics Biotech Engineering
```
- An example of the output:
```
> 8
Biotech
Randon Bradhust 3.68
Narissa Worthington 3.3

Chemistry
Crescentia Dow 3.79
Halima Brydone 3.72
Estephanie Phelps 3.21
Tawny Crockett 3.01

Engineering
Tommi Peerless 3.85
Cheyla Hankinson 3.82
Nicolasa Sumpter 3.82
Lorry Bunger 3.79
Natha Keefe 3.14
Cynthia Hermitton 3.1
Marti Mclaws 3.05

Mathematics
Dashawn Bosley 3.54
Aundria Guthrie 3.51
Kennon Inverarity 3.5
Teneil Maclean 3.22
Shealynn Melville 3.02
Esther Bratby 2.67

Physics
Darrah Smyth 3.89
Giovanna Keel 3.25
Cressie Gillespie 3.1
Fatemah Desavigny 3.0
```