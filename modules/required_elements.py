# This is a dictionary of all the required elements in order.
# Variables:
# TYPEOF: Determines the type of check done for the required element.
#   header: Will check the document to see if the header is there (the index of the dictionary)
#   content: Will check to see if the document matches the field in "text" exactly.
# REQUIREMENTS: WIP
# TEXT: If the TYPEOF variable is "content", then the document MUST contain this text or this check will fail.

required_elements = {
    ["General Education"]: {["typeof"]: "header", ["requirements"]: "N/A"}, # FILL IN WITH REQUIRED BOOL (GenEd)
    ["Course Description"]: {["typeof"]: "header"},
    ["Pre-requisite / Co-requisite"]: {["typeof"]: "header"},
    ["Course Learning Outcomes"]: {["typeof"]: "header"},
    ["Required Text/Materials"]: {["typeof"]: "header"},
    ["Communication Policy"]: {["typeof"]: "header"},
    ["Grades"]: {["typeof"]: "header"},
    ["Course Assignments"]: {["typeof"]: "header"},
    ["Course Schedule"]: {["typeof"]: "header"},
    ["Shared College Information"]: {["typeof"]: "content", ["text"]: """
Shared College Information
Consumer Information
The Higher Education Act of 1965 (amended in 1988 and 2008) requires all post-secondary institutions offering federal financial aid programs to provide key data to both prospective and current students. To comply with this requirement, LC State has developed a consumer information webpage (full URL: https://www.lcsc.edu/consumer-information) for your reference.
Student Rights and Responsibilities
Students are responsible for knowing their program requirements, course requirements, and other information associated with their enrollment at LC State. Students should review the LC State General Catalog (full URL: http://catalog.lcsc.edu/) and the LC State Student Handbook (full URL: https://www.lcsc.edu/student-affairs/student-code-of-conduct/student-resources-faqs) for more information.
State Law, Academic Freedom, and Course Expectations
Effective July 1, 2025, Idaho Code § 67-5909D establishes that courses “derived from or that promote” certain concepts associated with critical theory or diversity, equity, and inclusion (DEI) may be subject to additional state-level reporting and oversight. However, the statute also explicitly affirms that it does not “limit the free discussion of ideas in a classroom setting.” At LC State, this provision protects our ability to foster a learning environment grounded in open inquiry, respectful dialogue, and academic integrity.
As one of Idaho’s four public four-year institutions, LC State is governed by policies of the Idaho State Board of Education, including the following principles articulated in SBOE Policy III.B:
“Membership in the academic community imposes on administrators, faculty members, other institutional employees, and students an obligation to respect the dignity of others, to acknowledge the right of others to express differing opinions, and to foster and defend intellectual honesty, freedom of inquiry and instruction, and free expression on and off the campus of an institution.”
In line with these principles, this course is designed to encourage your academic development through thoughtfully selected readings, activities, and assignments. You are invited to engage critically with course materials, analyze competing viewpoints, and arrive at your own reasoned conclusions. While some content may challenge your perspective, you will not be asked or required to adopt any specific ideological or political position.
As you review the course syllabus and other instructional materials, please know they have been developed to support a respectful, engaging, and rigorous learning community. If at any point you decide that this course does not align with your academic preferences or goals, you are encouraged to contact your Academic Advisor (full email: advisor@lcsc.edu) to discuss available alternatives. Be sure to consult the LC State Academic Calendar for important deadlines related to course withdrawal or schedule changes. If you are receiving scholarships or financial aid, consult with the Financial Aid Office about potential impacts on scholarships or financial aid eligibility.
If you have questions about course content, instructional approach, or academic freedom policies, please contact the Provost/VP of Academic Affairs (full email: academicaffairs@lcsc.edu). We are committed to your success and to upholding LC State’s standards of academic excellence, respect, and transparency.
Academic Freedom
Lewis-Clark State promotes, values, encourages, and creates an environment that adheres to the principle of academic freedom.  Deep at the institutional core is the intellectual pursuit of all knowledge and theories, thought, reason, and perspective of truth for all LC State students, faculty, staff, and administrators.
A student’s right to academic freedom and expression are specifically identified in the student handbook, which essentially states concepts expressed in the classroom are for educational purposes, and a student’s adherence to any belief system will not be used as evaluative criteria.
Disclosures
During this course, if you elect to discuss information with your instructor that you consider to be sensitive or personal in nature, and not to be shared with others, please state this clearly. Your confidentiality in these circumstances will be respected unless upholding that confidentiality could reasonably put you, other students, or other members of the campus community in danger. In those cases, or when faculty are bound by law to report what you have shared, such as incidents involving sexual assault or other violent acts, a report will be submitted to appropriate campus authorities.
Student Health & Wellness
Students at LC State have access to health services at Student Health Services (full URL: https://www.lcsc.edu/student-health) and mental health services at the Student Counseling Center (full URL: https://www.lcsc.edu/student-counseling) on campus. In the event of an emergency, please seek medical help, and if necessary, report the incident to LC State Security (208-792-2226). Fieldtrips or other special student activities may also require students to submit a signed participation waiver (forms are obtained from the supporting Division Office).
Accessibility Accommodations
Students requiring special accommodations or course adaptations due to a permanent or temporary disability and/or health-related issue should contact Accessibility Services (LIB 161, 208-792-2677). Information can also be found on the Accessibility Services website (full URL: https://www.lcsc.edu/accessibility-services). Official documentation may be required to provide an accommodation and/or adaptation.
Academic Integrity
Academic dishonesty, which includes cheating and plagiarism, is not tolerated at LC State. Individual faculty members will impose their own policies and sanctions regarding academic integrity situations. Students who have been sanctioned for academic dishonesty may be referred to the VP for Student Affairs for official disciplinary action.
Artificial Intelligence (AI)
There is no formal policy for, or against, the use of AI tools for courses taken at LC State. This allows faculty to promote or restrict its use to best suit the needs of students and the course learning objectives. If you are unclear how you may use AI tools in a course, please review your syllabus and consult your instructor. Unauthorized use of AI in a course can be considered plagiarism and a violation of the Student Code of Conduct, Section 3: Prohibited Conduct (Full URL: https://www.lcsc.edu/student-affairs/student-code-of-conduct).
Illegal File Sharing
Students using LC State’s computers and/or computer network must comply with the college’s appropriate use policies and are prohibited from illegally downloading or sharing data files of any kind. Specific information about the college’s technology policies and its protocols for combating illegal file sharing is contained in LC State Policy 1.202 - Appropriate Use Policy for Technology (full URL: https://www.lcsc.edu/media/qzfbkswt/policy-1202-appropriate-use-for-technology.pdf).

 Testing Center for In-Person Proctoring (For Online & Hybrid Courses)
If your online or hybrid course has proctored exams, or you have assigned accommodations for testing, you may need to use the LC State Testing Center.  
If you are located at the Lewiston Campus, you can take proctored exams at the LC State Testing Center. It is located in the Library Building, Rm 161. Call to schedule your exam: 208-792-2100. 
If you are located near the Coeur d'Alene Center, you may use the NIC Testing Center. They are located on the second floor of Molstead Library. Call to schedule your exam: 208-616-7203.   
If you are unable to travel to these sites, you can arrange to use an approved proctor at your location.  You will need to contact the LC State Testing Center (full URL: https://www.lcsc.edu/testing-center) to have a proctor approved and arrange to have test passwords and/or materials sent to your local proctor."""
}
}