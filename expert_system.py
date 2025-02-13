from rules import CareerRules

class CareerExpertSystem:
    def __init__(self):
        self.career_rules = CareerRules()
        self.rules = self.career_rules.rules
        self.trait_weights = self.career_rules.trait_weights
        
    def calculate_confidence_score(self, job, user_traits, education_level, experience_years):
        job_info = self.rules[job]
        
        trait_score = 0
        required_traits = len(job_info['traits'])
        matched_traits = sum(trait in user_traits for trait in job_info['traits'])
        trait_weight = sum(self.trait_weights.get(trait, 0.5) for trait in user_traits if trait in job_info['traits'])
        trait_score = (trait_weight / required_traits) * 100
            
        education_levels = {"SMA": 1, "Diploma": 2, "Sarjana": 3, "Magister": 4, "Doktor": 5}
        required_edu = job_info['education'].split()[0]
        edu_score = max(0, min(100, (education_levels[education_level] / education_levels[required_edu]) * 100))
            
        exp_score = min(100, (experience_years / 10) * 100)
            
        final_score = (trait_score * 0.4) + (edu_score * 0.35) + (exp_score * 0.25)
            
        return final_score, {
            'trait_score': trait_score,
            'education_score': edu_score,
            'experience_score': exp_score
        }

    def get_career_recommendations(self, user_traits, education_level, experience_years):
        recommendations = []
        for job in self.rules:
            score, _ = self.calculate_confidence_score(job, user_traits, education_level, experience_years)
            recommendations.append((job, score))
        
        return sorted(recommendations, key=lambda x: x[1], reverse=True)[:5]

    def create_detailed_analysis(self, job, user_traits, education_level, experience_years):
        job_info = self.rules[job]
        score, subscores = self.calculate_confidence_score(job, user_traits, education_level, experience_years)
        
        analysis = {
            'overall_score': score,
            'subscores': subscores,
            'missing_traits': [trait for trait in job_info['traits'] if trait not in user_traits],
            'matching_traits': [trait for trait in job_info['traits'] if trait in user_traits],
            'education_gap': self.calculate_education_gap(education_level, job_info['education']),
            'salary_potential': self.calculate_salary_potential(job, experience_years),
            'career_growth': job_info.get('career_growth', []),
            'required_skills': job_info.get('skills_required', []),
            'recommended_certifications': job_info.get('certifications', [])
        }
        return analysis

    def calculate_education_gap(self, user_education, required_education):
        education_levels = ["SMA", "Diploma", "Sarjana", "Magister", "Doktor"]
        user_level = education_levels.index(user_education)
        required_level = education_levels.index(required_education.split()[0])
        return education_levels[required_level] if user_level < required_level else None

    def calculate_salary_potential(self, job, experience_years):
        base_range = self.rules[job]['salary_range']
        experience_factor = 1 + (experience_years * 0.1)
        return (
            base_range[0] * experience_factor,
            base_range[1] * experience_factor
        )