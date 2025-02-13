class CareerRules:
     def __init__(self):
        self.rules = {
            'Akuntan': {
            'traits': ['Analitis', 'Suka angka', 'Teliti'],
            'education': 'Sarjana Akuntansi',
            'salary_range': (50000000, 120000000),
            'job_outlook': 'Stabil',
            'skills_required': ['Pemahaman akuntansi', 'Microsoft Excel', 'Analisis laporan keuangan', 'Perpajakan', 'Software akuntansi', 'MYOB/Accurate'],
            'certifications': ['Certified Public Accountant (CPA)', 'Chartered Accountant (CA)', 'Certified Management Accountant (CMA)', 'Brevet A/B/C'],
            'career_growth': ['Junior Accountant', 'Senior Accountant', 'Finance Manager', 'Finance Controller', 'Chief Financial Officer']
            },

            'Desainer Grafis': {
                'traits': ['Kreatif', 'Komunikatif', 'Imajinatif'],
                'education': 'Sarjana Desain atau Seni Visual',
                'salary_range': (40000000, 85000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Adobe Photoshop', 'Adobe Illustrator', 'Adobe InDesign', 'Corel Draw', 'Design Thinking', 'Typography', 'Color Theory'],
                'certifications': ['Adobe Certified Professional', 'Certified Graphic Designer', 'Web Design Certification', 'UI/UX Design Certification'],
                'career_growth': ['Junior Graphic Designer', 'Senior Graphic Designer', 'Art Director', 'Creative Director', 'Design Manager']
            },

            'Pengembang Perangkat Lunak': {
                'traits': ['Logis', 'Suka memecahkan masalah', 'Keterampilan coding'],
                'education': 'Sarjana Ilmu Komputer',
                'salary_range': (60000000, 150000000),
                'job_outlook': 'Sangat berkembang',
                'skills_required': ['Java', 'Python', 'JavaScript', 'SQL', 'Git', 'Problem Solving', 'Algoritma dan Struktur Data'],
                'certifications': ['Oracle Certified Professional Java Developer', 'AWS Certified Developer', 'Microsoft Certified: Azure Developer Associate', 'Google Associate Android Developer'],
                'career_growth': ['Junior Developer', 'Senior Developer', 'Tech Lead', 'Software Architect', 'Chief Technology Officer']
            },

            'Konselor': {
                'traits': ['Empati', 'Komunikatif', 'Suka membantu orang'],
                'education': 'Magister Konseling atau Psikologi',
                'salary_range': (45000000, 70000000),
                'job_outlook': 'Stabil',
                'skills_required': ['Teknik konseling', 'Active listening', 'Psychological assessment', 'Crisis intervention', 'Case management'],
                'certifications': ['Licensed Professional Counselor (LPC)', 'National Certified Counselor (NCC)', 'Certified Clinical Mental Health Counselor'],
                'career_growth': ['Junior Counselor', 'Senior Counselor', 'Clinical Supervisor', 'Clinical Director', 'Private Practice Owner']
            },

            'Manajer Proyek': {
                'traits': ['Kepemimpinan', 'Strategis', 'Komunikatif'],
                'education': 'Sarjana Manajemen Bisnis',
                'salary_range': (65000000, 140000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Project management software', 'Risk management', 'Agile methodology', 'Budgeting', 'Microsoft Project', 'Leadership'],
                'certifications': ['Project Management Professional (PMP)', 'PRINCE2 Practitioner', 'Certified Associate in Project Management (CAPM)', 'Agile Certified Practitioner (PMI-ACP)'],
                'career_growth': ['Project Coordinator', 'Project Manager', 'Senior Project Manager', 'Program Manager', 'Portfolio Manager']
            },

            'Data Scientist': {
                'traits': ['Analitis', 'Keterampilan coding', 'Suka memecahkan masalah'],
                'education': 'Sarjana Ilmu Komputer atau Statistik',
                'salary_range': (70000000, 160000000),
                'job_outlook': 'Sangat berkembang',
                'skills_required': ['Python', 'R', 'SQL', 'Machine Learning', 'Statistical Analysis', 'Data Visualization', 'Big Data Tools'],
                'certifications': ['AWS Certified Machine Learning', 'Google Data Analytics Professional Certificate', 'IBM Data Science Professional Certificate', 'Microsoft Certified: Azure Data Scientist Associate'],
                'career_growth': ['Junior Data Scientist', 'Senior Data Scientist', 'Lead Data Scientist', 'Data Science Manager', 'Chief Data Officer']
            },

            'Marketing Manager': {
                'traits': ['Kreatif', 'Komunikatif', 'Strategis'],
                'education': 'Sarjana Pemasaran atau Manajemen Bisnis',
                'salary_range': (60000000, 140000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Digital marketing', 'Market research', 'Brand management', 'Social media marketing', 'Content strategy', 'Analytics'],
                'certifications': ['Professional Certified Marketer (PCM)', 'Digital Marketing Certification', 'Google Ads Certification', 'HubSpot Marketing Certification'],
                'career_growth': ['Marketing Coordinator', 'Marketing Manager', 'Senior Marketing Manager', 'Marketing Director', 'Chief Marketing Officer']
            },

            'Nurse': {
                'traits': ['Empati', 'Teliti', 'Komunikatif'],
                'education': 'Sarjana Keperawatan',
                'salary_range': (40000000, 90000000),
                'job_outlook': 'Sangat Stabil',
                'skills_required': ['Patient care', 'Medical procedures', 'Emergency response', 'Medical documentation', 'Clinical skills'],
                'certifications': ['Registered Nurse (RN)', 'Basic Life Support (BLS)', 'Advanced Cardiac Life Support (ACLS)', 'Specialty Nursing Certifications'],
                'career_growth': ['Staff Nurse', 'Charge Nurse', 'Nurse Manager', 'Director of Nursing', 'Chief Nursing Officer']
            },

            'Teacher': {
                'traits': ['Komunikatif', 'Sabar', 'Terorganisir'],
                'education': 'Sarjana Pendidikan',
                'salary_range': (35000000, 80000000),
                'job_outlook': 'Stabil',
                'skills_required': ['Lesson planning', 'Classroom management', 'Educational technology', 'Assessment methods', 'Curriculum development'],
                'certifications': ['Teaching License', 'Educational Technology Certificate', 'Special Education Certification', 'Subject Matter Certifications'],
                'career_growth': ['Assistant Teacher', 'Teacher', 'Senior Teacher', 'Department Head', 'School Principal']
            },

            'Digital Marketing Specialist': {
                'traits': ['Kreatif', 'Komunikatif', 'Teknologi-savvy'],
                'education': 'Sarjana Pemasaran atau Komunikasi',
                'salary_range': (50000000, 100000000),
                'job_outlook': 'Sangat Berkembang',
                'skills_required': ['SEO', 'SEM', 'Social media marketing', 'Content marketing', 'Google Analytics', 'Email marketing'],
                'certifications': ['Google Digital Marketing Certificate', 'Facebook Blueprint Certification', 'Hub Spot Inbound Marketing Certification', 'Hootsuite Social Media Marketing Certification'],
                'career_growth': ['Digital Marketing Coordinator', 'Digital Marketing Specialist', 'Senior Digital Marketing Specialist', 'Digital Marketing Manager', 'Digital Marketing Director']
            },

            'Sales Manager': {
                'traits': ['Komunikatif', 'Kepemimpinan', 'Persuasif'],
                'education': 'Sarjana Manajemen Bisnis atau Pemasaran',
                'salary_range': (60000000, 150000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Sales strategy', 'CRM software', 'Negotiation', 'Sales forecasting', 'Team management', 'Client relationship'],
                'certifications': ['Certified Sales Professional (CSP)', 'Certified Professional Sales Person (CPSP)', 'Certified Sales and Marketing Professional (CSMP)', 'HubSpot Sales Certification'],
                'career_growth': ['Sales Representative', 'Sales Manager', 'Senior Sales Manager', 'Sales Director', 'Vice President of Sales']
            },

            'IT Support Specialist': {
                'traits': ['Teknologi-savvy', 'Komunikatif', 'Problem-solving'],
                'education': 'Diploma atau Sarjana Ilmu Komputer',
                'salary_range': (40000000, 80000000),
                'job_outlook': 'Stabil',
                'skills_required': ['Troubleshooting', 'Network management', 'Hardware repair', 'Customer service', 'IT security'],
                'certifications': ['CompTIA A+', 'CompTIA Network+', 'CompTIA Security+', 'Cisco Certified Network Associate (CCNA)', 'Microsoft Certified: Azure Administrator Associate'],
                'career_growth': ['Help Desk Technician', 'IT Support Specialist', 'Senior IT Support Specialist', 'IT Manager', 'IT Director']
            },

            'Pharmacist': {
                'traits': ['Teliti', 'Empati', 'Detail-oriented'],
                'education': 'Sarjana Farmasi',
                'salary_range': (55000000, 120000000),
                'job_outlook': 'Stabil',
                'skills_required': ['Pharmaceutical knowledge', 'Drug dispensing', 'Patient consultation', 'Inventory management', 'Medical software'],
                'certifications': ['Licensed Pharmacist', 'Board Certified Pharmacotherapy Specialist (BCPS)', 'Certified Geriatric Pharmacist (CGP)', 'Certified Oncology Pharmacist (BCOP)'],
                'career_growth': ['Staff Pharmacist', 'Senior Pharmacist', 'Pharmacy Manager', 'Director of Pharmacy', 'Chief Pharmacy Officer']
            },

            'Journalist': {
                'traits': ['Komunikatif', 'Kreatif', 'Kritis'],
                'education': 'Sarjana Jurnalistik atau Komunikasi',
                'salary_range': (40000000, 90000000),
                'job_outlook': 'Stabil',
                'skills_required': ['Writing', 'Research', 'Interview techniques', 'Fact-checking', 'News judgment', 'Media law'],
                'certifications': ['Certified Journalist', 'Certified News Editor', 'Certified Broadcast Meteorologist (CBM)', 'Certified Investigative Reporter'],
                'career_growth': ['Junior Journalist', 'Senior Journalist', 'Editor', 'News Director', 'Publisher']
            },

            'Business Analyst': {
                'traits': ['Analitis', 'Detail-oriented', 'Komunikatif'],
                'education': 'Sarjana Manajemen Bisnis atau Ilmu Komputer',
                'salary_range': (60000000, 130000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Business process modeling', 'Requirements gathering', 'Data analysis', 'SQL', 'Project management'],
                'certifications': ['Certified Business Analyst Professional (CBAP)', 'Certified Associate Business Analyst (CABA)', 'Certified Analytics Professional (CAP)', 'Project Management Professional (PMP)'],
                'career_growth': ['Junior Business Analyst', 'Senior Business Analyst', 'Business Analyst Manager', 'Director of Business Analysis', 'Chief Business Analyst']
            },

            'UX/UI Designer': {
                'traits': ['Kreatif', 'Teknologi-savvy', 'Empati'],
                'education': 'Sarjana Desain Grafis atau Ilmu Komputer',
                'salary_range': (50000000, 120000000),
                'job_outlook': 'Sangat Berkembang',
                'skills_required': ['User  research', 'Wireframing', 'Prototyping', 'Usability testing', 'Interaction design', 'Visual design'],
                'certifications': ['Certified UX Designer', 'Certified UI Designer', 'Human-Centered Design Certification', 'Design Thinking Certification'],
                'career_growth': ['Junior UX/UI Designer ', 'Senior UX/UI Designer', 'UX/UI Design Manager', 'Director of UX/UI Design', 'Chief Design Officer']
            },

            'Event Coordinator': {
                'traits': ['Terorganisir', 'Komunikatif', 'Kreatif'],
                'education': 'Sarjana Manajemen Acara atau Pemasaran',
                'salary_range': (35000000, 80000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Event planning', 'Budgeting', 'Marketing', 'Communication', 'Problem-solving', 'Time management'],
                'certifications': ['Certified Event Planner (CEP)', 'Certified Meeting Professional (CMP)', 'Certified Wedding Planner (CWP)', 'Certified Conference Planner (CCP)'],
                'career_growth': ['Event Coordinator', 'Senior Event Coordinator', 'Event Manager', 'Director of Events', 'Chief Events Officer']
            },

            'Human Resource Manager': {
                'traits': ['Empati', 'Komunikatif', 'Strategis'],
                'education': 'Sarjana Manajemen Sumber Daya Manusia',
                'salary_range': (60000000, 130000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Recruitment', 'Training', 'Employee relations', 'Compensation', 'Benefits administration', 'Labor law'],
                'certifications': ['Society for Human Resource Management (SHRM) Certified Professional', 'HR Certification Institute (HRCI) Certified Professional', 'Certified Employee Benefit Specialist (CEBS)', 'Certified Compensation Professional (CCP)'],
                'career_growth': ['HR Coordinator', 'HR Manager', 'Senior HR Manager', 'Director of HR', 'Chief Human Resources Officer']
            },

            'Content Writer': {
                'traits': ['Kreatif', 'Kritis', 'Komunikatif'],
                'education': 'Sarjana Sastra atau Jurnalistik',
                'salary_range': (40000000, 90000000),
                'job_outlook': 'Stabil',
                'skills_required': ['Writing', 'Research', 'Editing', 'Content strategy', 'SEO', 'Social media marketing'],
                'certifications': ['Certified Content Marketer', 'Certified Copywriter', 'Certified Editor', 'Certified Social Media Marketing Professional'],
                'career_growth': ['Junior Content Writer', 'Senior Content Writer', 'Content Manager', 'Director of Content', 'Chief Content Officer']
            },

            'Financial Analyst': {
                'traits': ['Analitis', 'Suka angka', 'Detail-oriented'],
                'education': 'Sarjana Ekonomi atau Akuntansi',
                'salary_range': (60000000, 120000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Financial modeling', 'Data analysis', 'Accounting', 'Financial reporting', 'Budgeting', 'Forecasting'],
                'certifications': ['Chartered Financial Analyst (CFA)', 'Certified Financial Manager (CFM)', 'Certified Management Accountant (CMA)', 'Certified Public Accountant (CPA)'],
                'career_growth': ['Junior Financial Analyst', 'Senior Financial Analyst', 'Financial Manager', 'Director of Finance', 'Chief Financial Officer']
            },

            'Social Media Manager': {
                'traits': ['Kreatif', 'Komunikatif', 'Teknologi-savvy'],
                'education': 'Sarjana Pemasaran atau Komunikasi',
                'salary_range': (40000000, 90000000),
                'job_outlook': 'Sangat Berkembang',
                'skills_required': ['Social media marketing', 'Content creation', 'Community management', 'Analytics', 'Paid social media advertising'],
                'certifications': ['Hootsuite Social Media Marketing Certification', 'Facebook Blueprint Certification', 'Twitter Flight School Certification', 'Instagram Creator Certification'],
                'career_growth': ['Social Media Coordinator', 'Social Media Manager', 'Senior Social Media Manager', 'Director of Social Media', 'Chief Social Media Officer']
            },

            'Supply Chain Manager': {
                'traits': ['Strategis', 'Analitis', 'Terorganisir'],
                'education': 'Sarjana Manajemen Rantai Pasokan atau Bisnis',
                'salary_range': (60000000, 130000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Supply chain management', 'Logistics', 'Procurement', 'Inventory management', 'Transportation management'],
                'certifications': ['Certified Supply Chain Professional (CSCP)', 'Certified Professional in Supply Management (CPSM)', 'Certified Logistics and Transportation Professional (CLTP)', 'Certified Purchasing Professional (CPP)'],
                'career_growth': ['Supply Chain Coordinator', 'Supply Chain Manager', 'Senior Supply Chain Manager', 'Director of Supply Chain', 'Chief Supply Chain Officer']
            },

            'Public Relations Specialist': {
                'traits': ['Komunikatif', 'Kreatif', 'Persuasif'],
                'education': 'Sarjana Hubungan Masyarakat atau Komunikasi',
                'salary_range': (50000000, 100000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Media relations', 'Crisis communication', 'Event planning', 'Social media management', 'Content creation'],
                'certifications': ['Certified Public Relations Specialist (CPRS)', 'Accredited in Public Relations (APR)', 'Certified Communications Professional (CCP)', 'Certified Social Media Marketing Professional'],
                'career_growth': ['Public Relations Coordinator', 'Public Relations Specialist', 'Senior Public Relations Specialist', 'Director of Public Relations', 'Chief Communications Officer']
            },

            'Software Tester': {
                'traits': ['Teliti', 'Problem-solving', 'Keterampilan coding'],
                'education': 'Diploma atau Sarjana Ilmu Komputer',
                'salary_range': (40000000, 80000000),
                'job_outlook': 'Stabil',
                'skills_required': ['Testing methodologies', 'Test automation', 'Defect tracking', 'Test planning', 'Quality assurance'],
                'certifications': ['Certified Software Tester (CSTE)', 'Certified Associate in Software Testing (CAST)', 'Certified Test Manager (CTM)', 'Certified Quality Assurance Associate (CQAA)'],
                'career_growth': ['Junior Tester', 'Senior Tester', 'Test Manager', 'Quality Assurance Manager', 'Director of Quality Assurance']
            },
            
            'Research Scientist': {
                'traits': ['Analitis', 'Kreatif', 'Suka penelitian'],
                'education': 'Sarjana Sains atau Teknologi',
                'salary_range': (60000000, 130000000),
                'job_outlook': 'Sangat Berkembang',
                'skills_required': ['Research design', 'Data analysis', 'Statistical modeling', 'Scientific writing', 'Grant writing'],
                'certifications': ['Certified Research Administrator (CRA)', 'Certified Clinical Research Coordinator (CCRC)', 'Certified Research Scientist (CRS)', 'Certified Biomedical Research Scientist (CBRS)'],
                'career_growth': ['Research Assistant', 'Research Scientist', 'Senior Research Scientist', 'Principal Investigator', 'Research Director']
            },

            'E-commerce Specialist': {
                'traits': ['Kreatif', 'Strategis', 'Teknologi-savvy'],
                'education': 'Sarjana Pemasaran atau Bisnis',
                'salary_range': (50000000, 100000000),
                'job_outlook': 'Sangat Berkembang',
                'skills_required': ['E-commerce platform management', 'Digital marketing', 'SEO', 'Conversion rate optimization', 'Customer service'],
                'certifications': ['Certified E-commerce Specialist', 'Digital Marketing Certification', 'Shopify Certified Expert', 'Google Analytics Certification'],
                'career_growth': ['E-commerce Coordinator', 'E-commerce Manager', 'Senior E-commerce Manager', 'Director of E-commerce', 'Chief Digital Officer']
            },

            'Graphic Illustrator': {
                'traits': ['Kreatif', 'Imajinatif', 'Teliti'],
                'education': 'Sarjana Desain Grafis',
                'salary_range': (40000000, 90000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Illustration', 'Graphic design', 'Visual storytelling', 'Color theory', 'Typography'],
                'certifications': ['Adobe Certified Expert', 'Certified Professional Illustrator', 'Digital Illustration Certification', 'Visual Arts Certification'],
                'career_growth': ['Junior Illustrator', 'Senior Illustrator', 'Art Director', 'Creative Director', 'Independent Artist']
            },

            'Mobile App Developer': {
                'traits': ['Keterampilan coding', 'Logis', 'Suka memecahkan masalah'],
                'education': 'Sarjana Ilmu Komputer',
                'salary_range': (60000000, 150000000),
                'job_outlook': 'Sangat berkembang',
                'skills_required': ['Mobile app development', 'Programming languages', 'Database management', 'API integration', 'Cloud computing'],
                'certifications': ['Android Certified Developer', 'iOS App Development Certification', 'Google Mobile Web Specialist', 'AWS Mobile Developer'],
                'career_growth': ['Junior Mobile Developer', 'Senior Mobile Developer', 'Lead Mobile Developer', 'Mobile Architecture Manager', 'CTO']
            },

            'Real Estate Agent': {
                'traits': ['Komunikatif', 'Persuasif', 'Empati'],
                'education': 'Sarjana Manajemen Bisnis atau Pemasaran',
                'salary_range': (50000000, 100000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Real estate market knowledge', 'Sales', 'Negotiation', 'Customer service', 'Marketing'],
                'certifications': ['Licensed Real Estate Agent', 'Certified Residential Specialist (CRS)', 'Accredited Buyers Representative (ABR)', 'Certified Property Manager (CPM)'],
                'career_growth': ['Real Estate Agent', 'Senior Real Estate Agent', 'Broker', 'Agency Owner', 'Real Estate Developer']
            },

            'Entrepreneur': {
                'traits': ['Kreatif', 'Kepemimpinan', 'Berani mengambil risiko'],
                'education': 'Sarjana Manajemen Bisnis',
                'salary_range': (0, 1000000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Business planning', 'Marketing', 'Finance', 'Leadership', 'Risk management'],
                'certifications': ['Certified Entrepreneur', 'Business Management Certification', 'Project Management Professional (PMP)', 'Financial Management Certification'],
                'career_growth': ['Small Business Owner', 'Serial Entrepreneur', 'Angel Investor', 'Venture Capitalist', 'Business Mentor']
            },

            'Customer Service Representative': {
                'traits': ['Komunikatif', 'Sabar', 'Empati'],
                'education': 'SMA',
                'salary_range': (30000000, 60000000),
                'job_outlook': 'Stabil',
                'skills_required': ['Customer service', 'Communication', 'Problem-solving', 'Time management', 'Product knowledge'],
                'certifications': ['Certified Customer Service Professional (CCSP)', 'Customer Service Excellence Certification', 'Call Center Management Certification'],
                'career_growth': ['Customer Service Rep', 'Senior Customer Service Rep', 'Team Leader', 'Customer Service Manager', 'Customer Experience Director']
            },

            'Environmental Scientist': {
                'traits': ['Analitis', 'Peduli lingkungan', 'Suka penelitian'],
                'education': 'Sarjana Ilmu Lingkungan',
                'salary_range': (50000000, 100000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Environmental monitoring', 'Data analysis', 'Research design', 'Policy development', 'Sustainability'],
                'certifications': ['Certified Environmental Scientist', 'Professional Environmental Manager', 'Environmental Health & Safety Certification'],
                'career_growth': ['Environmental Scientist', 'Senior Environmental Scientist', 'Environmental Program Manager', 'Environmental Director', 'Chief Sustainability Officer']
            },

            'Fitness Trainer': {
                'traits': ['Energetik', 'Motivator', 'Disiplin'],
                'education': 'Diploma Pendidikan Jasmani',
                'salary_range': (35000000, 80000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Exercise science', 'Personal training', 'Group fitness instruction', 'Nutrition counseling', 'First aid'],
                'certifications': ['Certified Personal Trainer (CPT)', 'Group Fitness Instructor Certification', 'Nutrition Coach Certification', 'Sports Performance Coach'],
                'career_growth': ['Personal Trainer', 'Senior Trainer', 'Fitness Manager', 'Fitness Director', 'Gym Owner']
            },

            'Chef': {
                'traits': ['Kreatif', 'Detail-oriented', 'Tahan tekanan'],
                'education': 'Diploma Kuliner',
                'salary_range': (40000000, 120000000),
                'job_outlook': 'Stabil',
                'skills_required': ['Cooking techniques', 'Menu planning', 'Food safety', 'Kitchen management', 'Customer service'],
                'certifications': ['Certified Executive Chef (CEC)', 'Certified Culinary Professional (CCP)', 'Food Safety Manager Certification', 'Master Chef Certification'],
                'career_growth': ['Line Cook', 'Sous Chef', 'Executive Chef', 'Restaurant Owner', 'Culinary Director']
            },

            'Psychologist': {
                'traits': ['Empati', 'Analitis', 'Suka membantu orang'],
                'education': 'Magister Psikologi',
                'salary_range': (60000000, 150000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Assessment', ' Therapy', 'Research', 'Statistics', 'Counseling'],
                'certifications': ['Licensed Psychologist', 'Certified Professional Counselor (CPC)', 'Certified Clinical Mental Health Counselor (CCMHC)', 'Certified School Counselor (CSC)'],
                'career_growth': ['Clinical Psychologist', 'Research Psychologist', 'Counseling Psychologist', 'Neuropsychologist', 'Forensic Psychologist']
            },

            'Architect': {
                'traits': ['Kreatif', 'Detail-oriented', 'Keterampilan visual'],
                'education': 'Sarjana Arsitektur',
                'salary_range': (50000000, 150000000),
                'job_outlook': 'Stabil',
                'skills_required': ['Building design', 'Construction management', 'Project management', 'Sustainability', 'Building codes'],
                'certifications': ['Licensed Architect', 'Certified Professional Architect (CPA)', 'LEED AP Certification', 'NCARB Certification'],
                'career_growth': ['Intern Architect', 'Architect', 'Senior Architect', 'Project Manager', 'Principal Architect']
            },

            'Mechanical Engineer': {
                'traits': ['Logis', 'Problem-solving', 'Keterampilan teknis'],
                'education': 'Sarjana Teknik Mesin',
                'salary_range': (60000000, 140000000),
                'job_outlook': 'Berkembang',
                'skills_required': ['Mechanical design', 'Thermodynamics', 'Materials science', 'Manufacturing', 'Robotics'],
                'certifications': ['Professional Engineer (PE)', 'Certified Mechanical Engineer (CME)', 'Certified Energy Manager (CEM)', 'Certified Manufacturing Engineer (CMfgE)'],
                'career_growth': ['Mechanical Engineer', 'Senior Mechanical Engineer', 'Lead Mechanical Engineer', 'Mechanical Engineering Manager', 'Chief Engineer']
            },

            'Social Media Influencer': {
                'traits': ['Kreatif', 'Komunikatif', 'Teknologi-savvy'],
                'education': 'SMA',
                'salary_range': (30000000, 500000000),
                'job_outlook': 'Sangat Berkembang',
                'skills_required': ['Content creation', 'Social media marketing', 'Influencer marketing', 'Brand management', 'Audience engagement'],
                'certifications': ['Social Media Marketing Certification', 'Influencer Marketing Certification', 'Content Creation Certification', 'Brand Ambassador Certification'],
                'career_growth': ['Micro-Influencer', 'Mid-Tier Influencer', 'Top-Tier Influencer', 'Influencer Marketing Manager', 'Brand Ambassador']
            },

            'Biologist': {
                'traits': ['Analitis', 'Suka penelitian', 'Teliti'],
                'education': 'Sarjana Biologi',
                'salary_range': (45000000, 100000000),
                'job_outlook': 'Stabil',
                'skills_required': ['Research design', 'Data analysis', 'Laboratory techniques', 'Scientific writing', 'Conservation biology'],
                'certifications': ['Certified Biologist', 'Certified Wildlife Biologist', 'Certified Environmental Professional', 'Certified Conservation Biologist'],
                'career_growth': ['Research Biologist', 'Wildlife Biologist', 'Conservation Biologist', 'Environmental Consultant', 'Science Writer']
            }
        }
        self.trait_weights = {
            'Analitis': 0.95,           
            'Problem-solving': 0.95,     
            'Kepemimpinan': 0.90,       
            'Komunikatif': 0.90,        
            'Keterampilan coding': 0.90, 
            
            'Strategis': 0.89,         
            'Detail-oriented': 0.88,     
            'Teliti': 0.88,             
            'Terorganisir': 0.87,      
            'Suka memecahkan masalah': 0.87, 
            'Teknologi-savvy': 0.85,   
            
            'Kreatif': 0.84,           
            'Kritis': 0.83,             
            'Logis': 0.83,              
            'Persuasif': 0.82,          
            'Suka angka': 0.82,         
            'Empati': 0.80,             
            
            'Imajinatif': 0.79,         
            'Keterampilan visual': 0.78, 
            'Keterampilan teknis': 0.78, 
            'Suka penelitian': 0.77,     
            'Peduli lingkungan': 0.75,   
            
            'Sabar': 0.74,              
            'Motivator': 0.73,          
            'Suka membantu orang': 0.73, 
            'Energetik': 0.72,          
            'Disiplin': 0.72,           
            
            'Berani mengambil risiko': 0.69, 
            'Tahan tekanan': 0.68,      
            'Adaptif': 0.67,            
            'Inovatif': 0.66,           
            'Inisiatif': 0.65,
        }