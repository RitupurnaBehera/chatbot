medical_terms = [
    # General Health
    "Nutrition", "Exercise", "Sleep", "Hydration", "Wellness", "Mental health", "Stress management", "Lifestyle choices",
    "Obesity", "Physical fitness", "Health screening", "Health promotion", "Health education", "Hygienic practices",

    # Medical Conditions and Diseases
    "Diabetes", "Hypertension", "Cardiovascular diseases", "Cancer", "Respiratory conditions", "Gastrointestinal disorders",
    "Neurological disorders", "Autoimmune diseases", "Infectious diseases", "Allergies", "Arthritis", "Osteoporosis",
    "Anemia", "Migraine", "Epilepsy", "Fibromyalgia", "Chronic kidney disease", "Liver disease", "Thyroid disorders",
    "Autoimmune hepatitis", "HIV/AIDS", "Tuberculosis", "Malaria", "Influenza", "Common cold", "Pneumonia", "COVID-19",

    # Medical Treatments and Therapies
    "Medications", "Surgery", "Physical therapy", "Occupational therapy", "Speech therapy", "Radiation therapy", "Chemotherapy",
    "Immunotherapy", "Antibiotics", "Pain management", "Anesthesia", "Cardiac rehabilitation", "Rehabilitation", "Psychotherapy",
    "Cognitive therapy", "Behavioral therapy", "Dialysis", "Blood transfusion", "Organ transplantation", "Palliative care",

    # Healthcare Professions and Specialists
    "Physician", "Surgeon", "Nurse", "Pharmacist", "Dietitian", "Physical therapist", "Occupational therapist", "Psychologist",
    "Psychiatrist", "Gastroenterologist", "Cardiologist", "Neurologist", "Oncologist", "Dermatologist", "Pediatrician",
    "Obstetrician", "Gynecologist", "Urologist", "Orthopedic surgeon", "Radiologist", "Anesthesiologist", "Ophthalmologist",
    "ENT specialist", "Dentist", "Paramedic", "Medical assistant", "Medical technologist", "Emergency medical technician",

    # Medical Procedures and Tests
    "X-ray", "MRI (Magnetic Resonance Imaging)", "CT (Computed Tomography) scan", "Ultrasound", "Blood tests", "Urinalysis",
    "Endoscopy", "Colonoscopy", "Echocardiogram", "Electrocardiogram (ECG/EKG)", "Biopsy", "Catheterization", "Colonoscopy",
    "Lumbar puncture", "Doppler ultrasound", "Angiography", "PET scan", "Bone marrow transplant",

    # Health and Medical Technology
    "Telemedicine", "Medical devices", "Wearable health trackers", "Electronic health records (EHR)", "Health apps and software",
    "Artificial intelligence in healthcare", "Robot-assisted surgery", "Medical imaging technology", "Nanotechnology in medicine",
    "3D printing in healthcare", "Bionics", "Implantable devices",

    # Preventive Health Measures
    "Vaccination", "Screening tests", "Health check-ups", "Regular exercise and physical activity", "Healthy eating habits",
    "Smoking cessation", "Immunizations", "Cancer screening", "Pap smear", "Mammogram", "Colonoscopy screening",

    # Alternative and Complementary Medicine
    "Acupuncture", "Chiropractic care", "Herbal medicine", "Homeopathy", "Ayurveda", "Naturopathy", "Traditional Chinese medicine",
    "Aromatherapy", "Reflexology", "Yoga", "Meditation", "Mindfulness", "Reiki", "Hypnotherapy",

    # Women's Health
    "Pregnancy", "Menopause", "Reproductive health", "Breast health", "Gynecological conditions", "Endometriosis", "Polycystic ovary syndrome",
    "Cervical cancer", "Ovarian cancer", "Uterine fibroids", "Infertility", "Menstrual disorders", "Premenstrual syndrome (PMS)",

    # Men's Health
    "Prostate health", "Erectile dysfunction", "Testicular health", "Prostate cancer", "Benign prostatic hyperplasia (BPH)",
    "Male infertility", "Andropause", "Prostate-specific antigen (PSA) test",

    # Child Health
    "Pediatric care", "Childhood vaccinations", "Growth and development milestones", "Common childhood illnesses", "Child nutrition",
    "Childhood obesity", "Childhood asthma", "Attention deficit hyperactivity disorder (ADHD)", "Autism spectrum disorder (ASD)",
    "Pediatric oncology", "Pediatric dentistry", "Childhood obesity",

    # Aging and Geriatrics
    "Elderly care", "Geriatric diseases", "Senior health concerns", "Fall prevention", "Long-term care options", "Elder abuse",
    "Age-related macular degeneration (AMD)", "Osteoarthritis", "Parkinson's disease", "Alzheimer's disease", "Geriatric oncology",
    "Geriatric psychiatry", "Geriatric dentistry", "Hospice care",

    # Mental Health and Psychology
    "Depression", "Anxiety disorders", "Bipolar disorder", "Schizophrenia", "Counseling and therapy", "Cognitive-behavioral therapy (CBT)",
    "Mental health stigma", "Post-traumatic stress disorder (PTSD)", "Obsessive-compulsive disorder (OCD)", "Borderline personality disorder",
    "Eating disorders", "Self-harm", "Substance use disorders", "Addiction recovery", "Psychiatric medications",

    # Addiction and Substance Abuse
    "Drug addiction", "Alcoholism", "Substance abuse treatment", "Rehabilitation centers", "12-step programs", "Detoxification",
    "Withdrawal symptoms", "Addiction counseling", "Dual diagnosis", "Relapse prevention", "Support groups",

    # Allergies and Immunology
    "Allergic reactions", "Seasonal allergies", "Food allergies", "Anaphylaxis", "Immunodeficiency disorders", "Asthma and allergy",
    "Atopic dermatitis", "Hives", "Allergy testing", "Desensitization",

    # Medical Disorders
    "Chronic diseases", "Metabolic disorders", "Genetic disorders", "Neurodevelopmental disorders", "Neurodegenerative disorders",
    "Autoinflammatory diseases", "Connective tissue disorders", "Hormonal disorders", "Skin disorders", "Blood disorders",
    "Autoimmune disorders", "Inflammatory disorders", "Sleep disorders", "Gastrointestinal disorders", "Liver disorders",
    "Kidney disorders", "Heart disorders", "Vascular disorders", "Blood clotting disorders", "Hemophilia", "Anemia",
    "Thyroid disorders", "Hormone imbalances", "Metabolic syndrome", "Cystic fibrosis", "Ehlers-Danlos syndrome", "Marfan syndrome",
    "Down syndrome", "Cerebral palsy", "Autism spectrum disorders", "Parkinson's disease", "Alzheimer's disease",

    # Dental Health
    "Oral hygiene", "Tooth decay", "Gum disease", "Dental procedures", "Orthodontics", "Root canal", "Dental implants",
    "Dentures", "Dental crowns", "Bruxism", "Halitosis", "Oral cancer",

    # Vision and Eye Health
    "Myopia", "Hyperopia", "Glaucoma", "Cataracts", "LASIK eye surgery", "Dry eyes", "Conjunctivitis", "Retinal disorders",
    "Macular degeneration", "Retinopathy", "Astigmatism", "Presbyopia",

    # Ear, Nose, and Throat (ENT) Health
    "Ear infections", "Sinusitis", "Tonsillitis", "Hearing loss", "Snoring and sleep apnea", "Otitis media", "Vertigo",
    "Allergic rhinitis", "Laryngitis", "Tinnitus", "Earwax buildup",

    # Dermatology and Skin Health
    "Acne", "Eczema", "Psoriasis", "Skin cancer", "Sun protection", "Rosacea", "Dermatitis", "Melanoma", "Hives", "Warts",
    "Vitiligo", "Scabies", "Moles", "Skin infections", "Keratosis pilaris",

    # Pain Management
    "Chronic pain", "Pain medications", "Non-pharmacological pain relief", "Analgesics", "Nerve blocks", "Pain scales",
    "Acupuncture for pain relief", "Transcutaneous electrical nerve stimulation (TENS)", "Physical therapy for pain management",

    # Physical and Occupational Health
    "Workplace ergonomics", "Occupational hazards", "Repetitive strain injuries", "Workplace wellness programs",
    "Occupational therapy interventions", "Physical therapy exercises", "Ergonomic equipment", "Work-related stress",

    # Cardiovascular Health
    "Heart disease", "High cholesterol", "Heart attack", "Stroke", "Blood pressure management", "Atherosclerosis",
    "Arrhythmia", "Congenital heart defects", "Angina", "Cardiac rehabilitation", "Cardiac catheterization",

    # Sexual and Reproductive Health
    "Contraception", "Sexually transmitted infections (STIs)", "Erectile dysfunction (ED)", "Menstrual health", "Sexual health",
    "Birth control methods", "Human papillomavirus (HPV)", "Gonorrhea", "Chlamydia", "Herpes", "Syphilis", "HIV testing",

    # Respiratory Health
    "Asthma", "Chronic bronchitis", "Pneumonia", "Respiratory hygiene", "Pulmonary function tests", "COPD exacerbation",
    "Oxygen therapy", "Bronchodilators", "Nebulizers", "Respiratory physiotherapy",

    # Gastrointestinal Health
    "Gastritis", "Peptic ulcers", "Gastroenteritis", "Gallstones", "Pancreatitis", "Liver cirrhosis", "Inflammatory bowel disease (IBD)",
    "Crohn's disease", "Ulcerative colitis", "Irritable bowel syndrome (IBS)", "Celiac disease", "Diverticulitis", "Colon polyps",

    # Endocrine Health
    "Diabetes mellitus", "Hyperthyroidism", "Hypothyroidism", "Thyroid nodules", "Graves' disease", "Addison's disease",
    "Cushing's syndrome", "Pituitary disorders", "Hyperparathyroidism", "Hypoparathyroidism", "Metabolic syndrome",

    # Immunology and Allergy
    "Immunodeficiency disorders", "Immunization schedule", "Allergy testing", "Allergy shots", "Immunoglobulins",
    "Hypersensitivity reactions", "Autoimmune diseases", "Immune system disorders", "Transplant rejection",

    # Hematology
    "Anemia", "Hemophilia", "Leukemia", "Lymphoma", "Thrombocytopenia", "Hemolytic disorders", "Bone marrow disorders",
    "Sickle cell disease", "Hemochromatosis", "Coagulation disorders", "Thrombosis", "Anticoagulant medications",

    # Neurology
    "Epilepsy", "Migraine", "Alzheimer's disease", "Parkinson's disease", "Multiple sclerosis", "Amyotrophic lateral sclerosis (ALS)",
    "Stroke", "Traumatic brain injury (TBI)", "Neuropathy", "Spinal cord injuries", "Brain tumors", "Neurodegenerative diseases",

    # Oncology
    "Cancer", "Chemotherapy", "Radiation therapy", "Surgery for cancer", "Cancer screening", "Oncogenes", "Tumor suppressor genes",
    "Metastasis", "Angiogenesis", "Tumor markers", "Hormone therapy for cancer", "Immunotherapy for cancer",

    # Nephrology
    "Chronic kidney disease", "Renal failure", "Kidney transplantation", "Dialysis", "Nephrotic syndrome", "Urinary tract infections",
    "Polycystic kidney disease", "Kidney stones",

    # Orthopedics
    "Fractures", "Osteoporosis", "Arthritis", "Joint replacements", "Sports injuries", "Orthopedic surgery", "Orthotics",
    "Back pain", "Scoliosis", "Tendonitis", "Carpal tunnel syndrome",

    # Psychiatry
    "Depression", "Anxiety disorders", "Schizophrenia", "Bipolar disorder", "Obsessive-compulsive disorder (OCD)",
    "Post-traumatic stress disorder (PTSD)", "Personality disorders", "Attention deficit hyperactivity disorder (ADHD)",
    "Eating disorders", "Substance use disorders", "Alcohol use disorder", "Drug addiction", "Gambling addiction", "Internet addiction",
    "Suicide prevention", "Mental health disorders", "Psychiatric medications",

    # Radiology and Imaging
    "X-ray", "CT scan", "MRI", "Ultrasound", "Nuclear medicine", "Mammography", "PET scan", "Fluoroscopy", "Angiography",
    "Interventional radiology",

    # Pharmacology
    "Antibiotics", "Analgesics", "Antidepressants", "Antipsychotics", "Anticoagulants", "Antihypertensives", "Diuretics",
    "Antihistamines", "Immunosuppressants", "Antivirals", "Vaccines", "Opioids", "Chemotherapeutic agents", "Nonsteroidal anti-inflammatory drugs (NSAIDs)",
    "Beta-blockers", "ACE inhibitors", "Statins",

    # Surgery and Surgical Procedures
    "Appendectomy", "Cholecystectomy", "Hysterectomy", "Mastectomy", "Laparoscopy", "Laparotomy", "Amputation", "Cesarean section",
    "Cardiac surgery", "Coronary artery bypass grafting (CABG)", "Joint replacement surgery", "Cataract surgery", "LASIK surgery",
    "Plastic surgery", "Cosmetic surgery", "Reconstructive surgery", "Organ transplantation", "Surgical instruments",

    # Anesthesiology
    "General anesthesia", "Local anesthesia", "Regional anesthesia", "Anesthetic agents", "Anesthesia complications",

    # Physical Therapy and Rehabilitation
    "Physical therapy exercises", "Occupational therapy interventions", "Speech therapy exercises", "Rehabilitation techniques",
    "Gait training", "Mobility aids", "Assistive devices", "Prosthetics", "Wheelchairs", "Cane", "Crutches", "Walkers",

    # Nutrition and Dietetics
    "Dietary guidelines", "Macronutrients", "Micronutrients", "Vitamins", "Minerals", "Dietary supplements", "Caloric intake",
    "Nutrition labeling", "Balanced diet", "Dietary restrictions", "Gluten-free diet", "Vegetarian diet", "Vegan diet",
    "Ketogenic diet", "Intermittent fasting",

    # Gynecology
    "Cervical cancer", "Ovarian cancer", "Endometrial cancer", "Uterine fibroids", "Polycystic ovary syndrome (PCOS)",
    "Endometriosis", "Premenstrual syndrome (PMS)", "Menopause symptoms", "Hormone replacement therapy (HRT)", "Pap smear",

    # Obstetrics
    "Prenatal care", "Antenatal testing", "Labor and delivery", "Cesarean section", "Postpartum care", "Breastfeeding",
    "Postpartum depression", "High-risk pregnancy", "Gestational diabetes", "Preterm labor", "Preeclampsia",

    # Urology
    "Urinary tract infection (UTI)", "Kidney stones", "Prostate cancer", "Benign prostatic hyperplasia (BPH)",
    "Urinary incontinence", "Erectile dysfunction", "Cystitis", "Interstitial cystitis", "Bladder cancer", "Testicular cancer",

    # Endocrinology
    "Diabetes mellitus", "Hyperthyroidism", "Hypothyroidism", "Thyroid nodules", "Cushing's syndrome", "Addison's disease",
    "Polycystic ovary syndrome (PCOS)", "Growth hormone deficiency", "Hyperparathyroidism", "Hypoparathyroidism",

    # Oncology
    "Breast cancer", "Lung cancer", "Colon cancer", "Prostate cancer", "Leukemia", "Lymphoma", "Melanoma", "Pancreatic cancer",
    "Brain tumor", "Ovarian cancer", "Testicular cancer", "Cervical cancer", "Bladder cancer", "Liver cancer", "Esophageal cancer",

    # Hematology
    "Anemia", "Hemophilia", "Leukemia", "Lymphoma", "Thrombocytopenia", "Hemolytic disorders", "Hemochromatosis",

    # Nephrology
    "Chronic kidney disease", "Kidney stones", "Glomerulonephritis", "Urinary tract infections", "Renal failure", "Dialysis",

    # Dermatology
    "Acne", "Eczema", "Psoriasis", "Rosacea", "Skin cancer", "Melanoma", "Basal cell carcinoma", "Squamous cell carcinoma",
    "Urticaria", "Dermatitis", "Melasma", "Vitiligo", "Cellulitis", "Warts", "Keloids",

    # Cardiology
    "Coronary artery disease", "Heart failure", "Arrhythmia", "Atherosclerosis", "Hypertension", "Myocardial infarction",
    "Angina pectoris", "Cardiac arrest", "Valvular heart disease", "Atrial fibrillation", "Cardiomyopathy",

    # Gastroenterology
    "Gastroesophageal reflux disease (GERD)", "Peptic ulcers", "Gastritis", "Gallstones", "Inflammatory bowel disease (IBD)",
    "Irritable bowel syndrome (IBS)", "Celiac disease", "Crohn's disease", "Ulcerative colitis", "Hepatitis", "Cirrhosis",
    "Pancreatitis", "Diverticulitis",

    # Pulmonology
    "Asthma", "Chronic obstructive pulmonary disease (COPD)", "Pneumonia", "Tuberculosis", "Pulmonary embolism", "Emphysema",
    "Pulmonary fibrosis", "Sleep apnea", "Bronchitis", "Lung cancer",

    # Ophthalmology
    "Myopia", "Hyperopia", "Astigmatism", "Cataracts", "Glaucoma", "Macular degeneration", "Retinal detachment", "Dry eye syndrome",
    "Conjunctivitis", "Uveitis", "Strabismus", "Amblyopia",

    # Orthopedics
    "Fractures", "Osteoarthritis", "Rheumatoid arthritis", "Joint replacements", "Sprains and strains", "Bursitis",
    "Tendinitis", "Scoliosis", "Herniated disc", "Carpal tunnel syndrome", "Rotator cuff injury",

    # Neurology
    "Epilepsy", "Migraine", "Stroke", "Alzheimer's disease", "Parkinson's disease", "Multiple sclerosis", "Amyotrophic lateral sclerosis (ALS)",
    "Huntington's disease", "Traumatic brain injury (TBI)", "Peripheral neuropathy", "Bell's palsy", "Guillain-Barré syndrome",

    # Psychiatry
    "Depression", "Anxiety disorders", "Bipolar disorder", "Schizophrenia", "Post-traumatic stress disorder (PTSD)",
    "Obsessive-compulsive disorder (OCD)", "Attention deficit hyperactivity disorder (ADHD)", "Autism spectrum disorder (ASD)",
    "Borderline personality disorder", "Eating disorders", "Substance use disorders", "Alcohol use disorder",

    # Urology
    "Urinary tract infection (UTI)", "Kidney stones", "Bladder stones", "Prostate enlargement", "Erectile dysfunction",
    "Cystitis", "Urinary incontinence", "Testicular cancer", "Kidney cancer", "Bladder cancer",

    # Endocrinology
    "Diabetes mellitus", "Hyperthyroidism", "Hypothyroidism", "Thyroid nodules", "Graves' disease", "Cushing's syndrome",
    "Addison's disease", "Polycystic ovary syndrome (PCOS)", "Hypogonadism", "Hirsutism", "Hyperparathyroidism",

    # Gynecology
    "Cervical cancer", "Ovarian cancer", "Endometrial cancer", "Uterine fibroids", "Polycystic ovary syndrome (PCOS)",
    "Endometriosis", "Premenstrual syndrome (PMS)", "Menopause symptoms", "Hormone replacement therapy (HRT)", "Pap smear",

    # Obstetrics
    "Prenatal care", "Antenatal testing", "Labor and delivery", "Cesarean section", "Postpartum care", "Breastfeeding",
    "Postpartum depression", "High-risk pregnancy", "Gestational diabetes", "Preterm labor", "Preeclampsia",

    # Pediatrics
    "Childhood vaccinations", "Growth and development milestones", "Common childhood illnesses", "Pediatric asthma",
    "Childhood obesity", "Attention deficit hyperactivity disorder (ADHD)", "Autism spectrum disorder (ASD)",
    "Pediatric oncology", "Pediatric dentistry", "Pediatric cardiology", "Pediatric gastroenterology", "Pediatric nephrology",

    # Geriatrics
    "Elderly care", "Age-related macular degeneration (AMD)", "Osteoporosis", "Alzheimer's disease", "Parkinson's disease",
    "Falls in the elderly", "Urinary incontinence in the elderly", "Polypharmacy in the elderly", "Elder abuse",

    # Pain Management
    "Chronic pain", "Acute pain", "Pain medications", "Nonsteroidal anti-inflammatory drugs (NSAIDs)", "Opioids",
    "Antidepressants for pain", "Nerve blocks", "Physical therapy for pain", "Chronic pain syndrome", "Pain scales",

    # Emergency Medicine
    "Cardiopulmonary resuscitation (CPR)", "First aid", "Emergency medical services (EMS)", "Trauma",
    "Fracture management in emergency", "Anaphylaxis management", "Emergency triage", "Emergency childbirth",

    # Infectious Diseases
    "Influenza", "COVID-19", "HIV/AIDS", "Tuberculosis", "Malaria", "Hepatitis", "Sexually transmitted infections (STIs)",
    "Lyme disease", "Dengue fever", "Zika virus", "Ebola virus", "Antibiotic resistance", "Vaccination and immunization", "fever",

    # Gastrointestinal Health
    "Gastritis", "Peptic ulcers", "Gastroenteritis", "Gallstones", "Pancreatitis", "Liver cirrhosis", "Inflammatory bowel disease (IBD)",
    "Crohn's disease", "Ulcerative colitis", "Irritable bowel syndrome (IBS)", "Celiac disease", "Diverticulitis", "Colon polyps",
    "Gastroesophageal reflux disease (GERD)", "Hemorrhoids", "Lactose intolerance",

    # Dermatology and Skin Health
    "Acne", "Eczema", "Psoriasis", "Skin cancer", "Melanoma", "Basal cell carcinoma", "Squamous cell carcinoma", "Urticaria",
    "Dermatitis", "Melasma", "Vitiligo", "Cellulitis", "Warts", "Keloids", "Hives", "Rosacea", "Scabies", "Ringworm",
    "Fungal nail infections", "Nail psoriasis",

    # Allergies and Immunology
    "Allergic reactions", "Seasonal allergies", "Food allergies", "Anaphylaxis", "Immunodeficiency disorders",
    "Allergy testing", "Allergy shots", "Immunoglobulins", "Allergen immunotherapy", "Desensitization",

    # Medical Disorders
    "Chronic diseases", "Metabolic disorders", "Genetic disorders", "Neurodevelopmental disorders", "Neurodegenerative disorders",
    "Autoinflammatory diseases", "Connective tissue disorders", "Hormonal disorders", "Skin disorders", "Blood disorders",
    "Autoimmune disorders", "Inflammatory disorders", "Sleep disorders", "Hormonal disorders", "Autoinflammatory diseases",

    # Dental Health
    "Oral hygiene", "Tooth decay", "Gum disease", "Dental procedures", "Orthodontics", "Root canal", "Dental implants",
    "Dentures", "Dental crowns", "Bruxism", "Halitosis", "Oral cancer", "Tooth sensitivity",

    # Vision and Eye Health
    "Myopia", "Hyperopia", "Astigmatism", "Cataracts", "Glaucoma", "Macular degeneration", "Retinal detachment",
    "Dry eye syndrome", "Conjunctivitis", "Uveitis", "Strabismus", "Amblyopia", "Presbyopia", "Floaters", "Corneal abrasion",

    # Ear, Nose, and Throat (ENT) Health
    "Ear infections", "Sinusitis", "Tonsillitis", "Hearing loss", "Snoring and sleep apnea", "Otitis media", "Vertigo",
    "Allergic rhinitis", "Laryngitis", "Tinnitus", "Earwax buildup", "Hoarseness",

    # Respiratory Health
    "Asthma", "Chronic bronchitis", "Pneumonia", "Respiratory hygiene", "Pulmonary function tests", "COPD exacerbation",
    "Oxygen therapy", "Bronchodilators", "Nebulizers", "Respiratory physiotherapy",

    # Dermatology and Skin Health
    "Acne", "Eczema", "Psoriasis", "Skin cancer", "Sun protection", "Rosacea", "Dermatitis", "Melanoma", "Hives", "Warts",
    "Vitiligo", "Scabies", "Moles", "Skin infections", "Keratosis pilaris",

    # Pain Management
    "Chronic pain", "Pain medications", "Non-pharmacological pain relief", "Analgesics", "Nerve blocks", "Pain scales",
    "Acupuncture for pain relief", "Transcutaneous electrical nerve stimulation (TENS)", "Physical therapy for pain management",

    # Physical and Occupational Health
    "Workplace ergonomics", "Occupational hazards", "Repetitive strain injuries", "Workplace wellness programs",
    "Occupational therapy interventions", "Physical therapy exercises", "Ergonomic equipment", "Work-related stress",

    # Chronic Conditions
    "Arthritis", "Chronic obstructive pulmonary disease (COPD)", "Multiple sclerosis (MS)", "Fibromyalgia", "Inflammatory bowel disease (IBD)",
    "Chronic kidney disease (CKD)", "Chronic heart failure (CHF)", "Chronic liver disease", "Chronic fatigue syndrome (CFS)",
    "Chronic pain syndrome",

    # Cardiovascular Health
    "Heart disease", "High cholesterol", "Heart attack", "Stroke", "Blood pressure management", "Atherosclerosis",
    "Arrhythmia", "Congenital heart defects", "Angina", "Cardiac rehabilitation", "Cardiac catheterization", "cough",

    # Sexual and Reproductive Health
    "Contraception", "Sexually transmitted infections (STIs)", "Erectile dysfunction (ED)", "Menstrual health", "Sexual health",
    "Birth control methods", "Human papillomavirus (HPV)", "Gonorrhea", "Chlamydia", "Herpes", "Syphilis", "HIV testing",

    # Respiratory Health
    "Asthma", "Chronic bronchitis", "Pneumonia", "Respiratory hygiene", "Pulmonary function tests", "COPD exacerbation",
    "Oxygen therapy", "Bronchodilators", "Nebulizers", "Respiratory physiotherapy",

    # Gastrointestinal Health
    "Gastritis", "Peptic ulcers", "Gastroenteritis", "Gallstones", "Pancreatitis", "Liver cirrhosis", "Inflammatory bowel disease (IBD)",
    "Crohn's disease", "Ulcerative colitis", "Irritable bowel syndrome (IBS)", "Celiac disease", "Diverticulitis", "Colon polyps",

    # Endocrine Health
    "Diabetes mellitus", "Hyperthyroidism", "Hypothyroidism", "Thyroid nodules", "Graves' disease", "Addison's disease",
    "Cushing's syndrome", "Pituitary disorders", "Hyperparathyroidism", "Hypoparathyroidism", "Metabolic syndrome",

    # Immunology and Allergy
    "Immunodeficiency disorders", "Immunization schedule", "Allergy testing", "Allergy shots", "Immunoglobulins",
    "Hypersensitivity reactions", "Autoimmune diseases", "Immune system disorders", "Transplant rejection",

    # Hematology
    "Anemia", "Hemophilia", "Leukemia", "Lymphoma", "Thrombocytopenia", "Hemolytic disorders", "Bone marrow disorders",
    "Sickle cell disease", "Hemochromatosis", "Coagulation disorders", "Thrombosis", "Anticoagulant medications",

    # Neurology
    "Epilepsy", "Migraine", "Alzheimer's disease", "Parkinson's disease", "Multiple sclerosis", "Amyotrophic lateral sclerosis (ALS)",
    "Stroke", "Traumatic brain injury (TBI)", "Neuropathy", "Spinal cord injuries", "Brain tumors", "Neurodegenerative diseases",

    # Oncology
    "Cancer", "Chemotherapy", "Radiation therapy", "Surgery for cancer", "Cancer screening", "Oncogenes", "Tumor suppressor genes",
    "Metastasis", "Angiogenesis", "Tumor markers", "Hormone therapy for cancer", "Immunotherapy for cancer",

    # Nephrology
    "Chronic kidney disease", "Renal failure", "Kidney transplantation", "Dialysis", "Nephrotic syndrome", "Urinary tract infections",
    "Polycystic kidney disease", "Kidney stones",

    # Orthopedics
    "Fractures", "Osteoporosis", "Arthritis", "Joint replacements", "Sports injuries", "Orthopedic surgery", "Orthotics",
    "Back pain", "Scoliosis", "Tendonitis", "Carpal tunnel syndrome",

    # Psychiatry
    "Depression", "Anxiety disorders", "Schizophrenia", "Bipolar disorder", "Obsessive-compulsive disorder (OCD)",
    "Post-traumatic stress disorder (PTSD)", "Personality disorders", "Attention deficit hyperactivity disorder (ADHD)",
    "Eating disorders", "Substance use disorders", "Alcohol use disorder", "Drug addiction", "Gambling addiction", "Internet addiction",
    "Suicide prevention", "Mental health disorders", "Psychiatric medications",

    # Radiology and Imaging
    "X-ray", "CT scan", "MRI", "Ultrasound", "Nuclear medicine", "Mammography", "PET scan", "Fluoroscopy", "Angiography",
    "Interventional radiology",

    # Pharmacology
    "Antibiotics", "Analgesics", "Antidepressants", "Antipsychotics", "Anticoagulants", "Antihypertensives", "Diuretics",
    "Antihistamines", "Immunosuppressants", "Antivirals", "Vaccines", "Opioids", "Chemotherapeutic agents", "Nonsteroidal anti-inflammatory drugs (NSAIDs)",
    "Beta-blockers", "ACE inhibitors", "Statins",

    # Surgery and Surgical Procedures
    "Appendectomy", "Cholecystectomy", "Hysterectomy", "Mastectomy", "Laparoscopy", "Laparotomy", "Amputation", "Cesarean section",
    "Cardiac surgery", "Coronary artery bypass grafting (CABG)", "Joint replacement surgery", "Cataract surgery", "LASIK surgery",
    "Plastic surgery", "Cosmetic surgery", "Reconstructive surgery", "Organ transplantation", "Surgical instruments",

    # Anesthesiology
    "General anesthesia", "Local anesthesia", "Regional anesthesia", "Anesthetic agents", "Anesthesia complications",

    # Physical Therapy and Rehabilitation
    "Physical therapy exercises", "Occupational therapy interventions", "Speech therapy exercises", "Rehabilitation techniques",
    "Gait training", "Mobility aids", "Assistive devices", "Prosthetics", "Wheelchairs", "Cane", "Crutches", "Walkers",

    # Nutrition and Dietetics
    "Dietary guidelines", "Macronutrients", "Micronutrients", "Vitamins", "Minerals", "Dietary supplements", "Caloric intake",
    "Nutrition labeling", "Balanced diet", "Dietary restrictions", "Gluten-free diet", "Vegetarian diet", "Vegan diet",
    "Ketogenic diet", "Intermittent fasting",

    # Gynecology
    "Cervical cancer", "Ovarian cancer", "Endometrial cancer", "Uterine fibroids", "Polycystic ovary syndrome (PCOS)",
    "Endometriosis", "Premenstrual syndrome (PMS)", "Menopause symptoms", "Hormone replacement therapy (HRT)", "Pap smear",

    # Obstetrics
    "Prenatal care", "Antenatal testing", "Labor and delivery", "Cesarean section", "Postpartum care", "Breastfeeding",
    "Postpartum depression", "High-risk pregnancy", "Gestational diabetes", "Preterm labor", "Preeclampsia",

    # Urology
    "Urinary tract infection (UTI)", "Kidney stones", "Prostate cancer", "Benign prostatic hyperplasia (BPH)",
    "Urinary incontinence", "Erectile dysfunction", "Cystitis", "Interstitial cystitis", "Bladder cancer", "Testicular cancer",

    # Endocrinology
    "Diabetes mellitus", "Hyperthyroidism", "Hypothyroidism", "Thyroid nodules", "Graves' disease", "Addison's disease",
    "Cushing's syndrome", "Pituitary disorders", "Hyperparathyroidism", "Hypoparathyroidism", "Metabolic syndrome",

    # Immunology and Allergy
    "Immunodeficiency disorders", "Immunization schedule", "Allergy testing", "Allergy shots", "Immunoglobulins",
    "Hypersensitivity reactions", "Autoimmune diseases", "Immune system disorders", "Transplant rejection",

    # Hematology
    "Anemia", "Hemophilia", "Leukemia", "Lymphoma", "Thrombocytopenia", "Hemolytic disorders", "Bone marrow disorders",
    "Sickle cell disease", "Hemochromatosis", "Coagulation disorders", "Thrombosis", "Anticoagulant medications",

    # Neurology
    "Epilepsy", "Migraine", "Alzheimer's disease", "Parkinson's disease", "Multiple sclerosis", "Amyotrophic lateral sclerosis (ALS)",
    "Stroke", "Traumatic brain injury (TBI)", "Neuropathy", "Spinal cord injuries", "Brain tumors", "Neurodegenerative diseases",

    # Oncology
    "Cancer", "Chemotherapy", "Radiation therapy", "Surgery for cancer", "Cancer screening", "Oncogenes", "Tumor suppressor genes",
    "Metastasis", "Angiogenesis", "Tumor markers", "Hormone therapy for cancer", "Immunotherapy for cancer",

    # Nephrology
    "Chronic kidney disease", "Renal failure", "Kidney transplantation", "Dialysis", "Nephrotic syndrome", "Urinary tract infections",
    "Polycystic kidney disease", "Kidney stones",

    # Orthopedics
    "Fractures", "Osteoporosis", "Arthritis", "Joint replacements", "Sports injuries", "Orthopedic surgery", "Orthotics",
    "Back pain", "Scoliosis", "Tendonitis", "Carpal tunnel syndrome",

    # Psychiatry
    "Depression", "Anxiety disorders", "Schizophrenia", "Bipolar disorder", "Obsessive-compulsive disorder (OCD)",
    "Post-traumatic stress disorder (PTSD)", "Personality disorders", "Attention deficit hyperactivity disorder (ADHD)",
    "Eating disorders", "Substance use disorders", "Alcohol use disorder", "Drug addiction", "Gambling addiction", "Internet addiction",
    "Suicide prevention", "Mental health disorders", "Psychiatric medications",

    # Radiology and Imaging
    "X-ray", "CT scan", "MRI", "Ultrasound", "Nuclear medicine", "Mammography", "PET scan", "Fluoroscopy", "Angiography",
    "Interventional radiology",

    # Pharmacology
    "Antibiotics", "Analgesics", "Antidepressants", "Antipsychotics", "Anticoagulants", "Antihypertensives", "Diuretics",
    "Antihistamines", "Immunosuppressants", "Antivirals", "Vaccines", "Opioids", "Chemotherapeutic agents", "Nonsteroidal anti-inflammatory drugs (NSAIDs)",
    "Beta-blockers", "ACE inhibitors", "Statins",

    # Surgery and Surgical Procedures
    "Appendectomy", "Cholecystectomy", "Hysterectomy", "Mastectomy", "Laparoscopy", "Laparotomy", "Amputation", "Cesarean section",
    "Cardiac surgery", "Coronary artery bypass grafting (CABG)", "Joint replacement surgery", "Cataract surgery", "LASIK surgery",
    "Plastic surgery", "Cosmetic surgery", "Reconstructive surgery", "Organ transplantation", "Surgical instruments",

    # Anesthesiology
    "General anesthesia", "Local anesthesia", "Regional anesthesia", "Anesthetic agents", "Anesthesia complications",

    # Physical Therapy and Rehabilitation
    "Physical therapy exercises", "Occupational therapy interventions", "Speech therapy exercises", "Rehabilitation techniques",
    "Gait training", "Mobility aids", "Assistive devices", "Prosthetics", "Wheelchairs", "Cane", "Crutches", "Walkers",

    # Nutrition and Dietetics
    "Dietary guidelines", "Macronutrients", "Micronutrients", "Vitamins", "Minerals", "Dietary supplements", "Caloric intake",
    "Nutrition labeling", "Balanced diet", "Dietary restrictions", "Gluten-free diet", "Vegetarian diet", "Vegan diet",
    "Ketogenic diet", "Intermittent fasting",

    # Gynecology
    "Cervical cancer", "Ovarian cancer", "Endometrial cancer", "Uterine fibroids", "Polycystic ovary syndrome (PCOS)",
    "Endometriosis", "Premenstrual syndrome (PMS)", "Menopause symptoms", "Hormone replacement therapy (HRT)", "Pap smear",

    # Obstetrics
    "Prenatal care", "Antenatal testing", "Labor and delivery", "Cesarean section", "Postpartum care", "Breastfeeding",
    "Postpartum depression", "High-risk pregnancy", "Gestational diabetes", "Preterm labor", "Preeclampsia",

    # Urology
    "Urinary tract infection (UTI)", "Kidney stones", "Prostate cancer", "Benign prostatic hyperplasia (BPH)",
    "Urinary incontinence", "Erectile dysfunction", "Cystitis", "Interstitial cystitis", "Bladder cancer", "Testicular cancer",

    # Endocrinology
    "Diabetes mellitus", "Hyperthyroidism", "Hypothyroidism", "Thyroid nodules", "Graves' disease", "Addison's disease",
    "Cushing's syndrome", "Pituitary disorders", "Hyperparathyroidism", "Hypoparathyroidism", "Metabolic syndrome",

    # Immunology and Allergy
    "Immunodeficiency disorders", "Immunization schedule", "Allergy testing", "Allergy shots", "Immunoglobulins",
    "Hypersensitivity reactions", "Autoimmune diseases", "Immune system disorders", "Transplant rejection",

    # Hematology
    "Anemia", "Hemophilia", "Leukemia", "Lymphoma", "Thrombocytopenia", "Hemolytic disorders", "Bone marrow disorders",
    "Sickle cell disease", "Hemochromatosis", "Coagulation disorders", "Thrombosis", "Anticoagulant medications",

    # Neurology
    "Epilepsy", "Migraine", "Alzheimer's disease", "Parkinson's disease", "Multiple sclerosis", "Amyotrophic lateral sclerosis (ALS)",
    "Stroke", "Traumatic brain injury (TBI)", "Neuropathy", "Spinal cord injuries", "Brain tumors", "Neurodegenerative diseases",

    # Oncology
    "Cancer", "Chemotherapy", "Radiation therapy", "Surgery for cancer", "Cancer screening", "Oncogenes", "Tumor suppressor genes",
    "Metastasis", "Angiogenesis", "Tumor markers", "Hormone therapy for cancer", "Immunotherapy for cancer",

    # Nephrology
    "Chronic kidney disease", "Renal failure", "Kidney transplantation", "Dialysis", "Nephrotic syndrome", "Urinary tract infections",
    "Polycystic kidney disease", "Kidney stones",

    # Orthopedics
    "Fractures", "Osteoporosis", "Arthritis", "Joint replacements", "Sports injuries", "Orthopedic surgery", "Orthotics",
    "Back pain", "Scoliosis", "Tendonitis", "Carpal tunnel syndrome",

    # Psychiatry
    "Depression", "Anxiety disorders", "Schizophrenia", "Bipolar disorder", "Obsessive-compulsive disorder (OCD)",
    "Post-traumatic stress disorder (PTSD)", "Personality disorders", "Attention deficit hyperactivity disorder (ADHD)",
    "Eating disorders", "Substance use disorders", "Alcohol use disorder", "Drug addiction", "Gambling addiction", "Internet addiction",
    "Suicide prevention", "Mental health disorders", "Psychiatric medications",

    # Radiology and Imaging
    "X-ray", "CT scan", "MRI", "Ultrasound", "Nuclear medicine", "Mammography", "PET scan", "Fluoroscopy", "Angiography",
    "Interventional radiology",

    # Pharmacology
    "Antibiotics", "Analgesics", "Antidepressants", "Antipsychotics", "Anticoagulants", "Antihypertensives", "Diuretics",
    "Antihistamines", "Immunosuppressants", "Antivirals", "Vaccines", "Opioids", "Chemotherapeutic agents", "Nonsteroidal anti-inflammatory drugs (NSAIDs)",
    "Beta-blockers", "ACE inhibitors", "Statins",

    # Surgery and Surgical Procedures
    "Appendectomy", "Cholecystectomy", "Hysterectomy", "Mastectomy", "Laparoscopy", "Laparotomy", "Amputation", "Cesarean section",
    "Cardiac surgery", "Coronary artery bypass grafting (CABG)", "Joint replacement surgery", "Cataract surgery", "LASIK surgery",
    "Plastic surgery", "Cosmetic surgery", "Reconstructive surgery", "Organ transplantation", "Surgical instruments",

    # Anesthesiology
    "General anesthesia", "Local anesthesia", "Regional anesthesia", "Anesthetic agents", "Anesthesia complications",

    # Physical Therapy and Rehabilitation
    "Physical therapy exercises", "Occupational therapy interventions", "Speech therapy exercises", "Rehabilitation techniques",
    "Gait training", "Mobility aids", "Assistive devices", "Prosthetics", "Wheelchairs", "Cane", "Crutches", "Walkers",

    # Nutrition and Dietetics
    "Dietary guidelines", "Macronutrients", "Micronutrients", "Vitamins", "Minerals", "Dietary supplements", "Caloric intake",
    "Nutrition labeling", "Balanced diet", "Dietary restrictions", "Gluten-free diet", "Vegetarian diet", "Vegan diet",
    "Ketogenic diet", "Intermittent fasting",

    # Gynecology
    "Cervical cancer", "Ovarian cancer", "Endometrial cancer", "Uterine fibroids", "Polycystic ovary syndrome (PCOS)",
    "Endometriosis", "Premenstrual syndrome (PMS)", "Menopause symptoms", "Hormone replacement therapy (HRT)", "Pap smear",

    # Obstetrics
    "Prenatal care", "Antenatal testing", "Labor and delivery", "Cesarean section", "Postpartum care", "Breastfeeding",
    "Postpartum depression", "High-risk pregnancy", "Gestational diabetes", "Preterm labor", "Preeclampsia",

    # Urology
    "Urinary tract infection (UTI)", "Kidney stones", "Prostate cancer", "Benign prostatic hyperplasia (BPH)",
    "Urinary incontinence", "Erectile dysfunction", "Cystitis", "Interstitial cystitis", "Bladder cancer", "Testicular cancer",

    # Endocrinology
    "Diabetes mellitus", "Hyperthyroidism", "Hypothyroidism", "Thyroid nodules", "Graves' disease", "Addison's disease",
    "Cushing's syndrome", "Pituitary disorders", "Hyperparathyroidism", "Hypoparathyroidism", "Metabolic syndrome",

    # Immunology and Allergy
    "Immunodeficiency disorders", "Immunization schedule", "Allergy testing", "Allergy shots", "Immunoglobulins",
    "Hypersensitivity reactions", "Autoimmune diseases", "Immune system disorders", "Transplant rejection",

    # Hematology
    "Anemia", "Hemophilia", "Leukemia", "Lymphoma", "Thrombocytopenia", "Hemolytic disorders", "Bone marrow disorders",
    "Sickle cell disease", "Hemochromatosis", "Coagulation disorders", "Thrombosis", "Anticoagulant medications",

    # Neurology
    "Epilepsy", "Migraine", "Alzheimer's disease", "Parkinson's disease", "Multiple sclerosis", "Amyotrophic lateral sclerosis (ALS)",
    "Stroke", "Traumatic brain injury (TBI)", "Neuropathy", "Spinal cord injuries", "Brain tumors", "Neurodegenerative diseases",

    # Oncology
    "Cancer", "Chemotherapy", "Radiation therapy", "Surgery for cancer", "Cancer screening", "Oncogenes", "Tumor suppressor genes",
    "Metastasis", "Angiogenesis", "Tumor markers", "Hormone therapy for cancer", "Immunotherapy for cancer",

    # Nephrology
    "Chronic kidney disease", "Renal failure", "Kidney transplantation", "Dialysis", "Nephrotic syndrome", "Urinary tract infections",
    "Polycystic kidney disease", "Kidney stones",

    # Orthopedics
    "Fractures", "Osteoporosis", "Arthritis", "Joint replacements", "Sports injuries", "Orthopedic surgery", "Orthotics",
    "Back pain", "Scoliosis", "Tendonitis", "Carpal tunnel syndrome",

    # Psychiatry
    "Depression", "Anxiety disorders", "Schizophrenia", "Bipolar disorder", "Obsessive-compulsive disorder (OCD)",
    "Post-traumatic stress disorder (PTSD)", "Personality disorders", "Attention deficit hyperactivity disorder (ADHD)",
    "Eating disorders", "Substance",
    "Fever", "Cold", "Headache", "Cough", "Sore throat", "Stomachache", "Nausea", "Vomiting", "Diarrhea",
    "Allergies", "Rash", "Fatigue", "Dizziness", "High blood pressure", "Diabetes", "Asthma", "Arthritis", "Heartburn",
    "Cholesterol", "Anemia", "Constipation", "Urinary tract infection (UTI)", "Depression", "Anxiety", "Insomnia",
    "Bruise", "Sprain", "Fracture", "Concussion", "Appendicitis", "Pneumonia", "Bronchitis", "Migraine", "Heart attack",
    "Stroke", "Cancer", "Diabetes mellitus", "Hypertension", "Obesity", "Alzheimer's disease", "Arthritis", "Osteoporosis",
    "Glaucoma", "Cataracts", "Hearing loss", "Erectile dysfunction (ED)", "Menopause", "Pregnancy", "Fertility",
    "Influenza (Flu)", "Gastroenteritis", "Sinusitis", "Pneumonia", "Bronchitis", "Tonsillitis", "Conjunctivitis (Pink eye)",
    "Eczema", "Psoriasis", "Acne", "Diabetic neuropathy", "Hypothyroidism", "Hyperthyroidism", "Astigmatism",
    "Cholecystitis (Gallbladder inflammation)", "Appendicitis", "Gastroesophageal reflux disease (GERD)", "Peptic ulcer",
    "Crohn's disease", "Irritable bowel syndrome (IBS)", "Osteoarthritis", "Rheumatoid arthritis", "Carpal tunnel syndrome",
    "Tendinitis", "Meniscus tear", "Anterior cruciate ligament (ACL) tear", "Hemorrhoids", "Varicose veins", "Anaphylaxis",
    "Hypoglycemia", "Hypertension (High blood pressure)", "Myocardial infarction (Heart attack)", "Atrial fibrillation",
    "Cardiac arrest", "Chronic obstructive pulmonary disease (COPD)", "Emphysema", "Thyroid nodules", "Hypogonadism",
    "Fibromyalgia", "Chronic fatigue syndrome", "Obsessive-compulsive disorder (OCD)", "Bipolar disorder", "Schizophrenia",
    "Panic disorder", "Post-traumatic stress disorder (PTSD)", "Down syndrome", "Autism spectrum disorder (ASD)",
    "Attention deficit hyperactivity disorder (ADHD)", "Cleft lip and palate", "Cerebral palsy","aphthous stomatitis","stomach rumble","bradykinesia",
    "Pneumonoultramicroscopicsilicovolcanoconiosis","cardialgia","fasciculation","Maple Syrup Urine disease","flu"

]


