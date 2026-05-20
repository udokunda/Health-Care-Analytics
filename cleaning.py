
import pandas as pd
import numpy as np
import re

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------
df = pd.read_csv(r"C:\\Users\\2539990\\Downloads\\healthcare_messy_data.csv")

print("Dataset Loaded Successfully")
print(df.head())

# ---------------------------------------------------------
# 1. CLEAN PATIENT NAMES
# ---------------------------------------------------------

df["Patient Name"] = df["Patient Name"].str.strip().str.title()

# ---------------------------------------------------------
# 2. CLEAN AGE COLUMN
# ---------------------------------------------------------

# Convert word ages into numbers
age_words = {
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70
}

def clean_age(age):

    # If value is missing
    if pd.isna(age):
        return np.nan

    age = str(age).lower().strip()

    # Convert words to numbers
    if age in age_words:
        return age_words[age]

    # Convert normal numbers
    try:
        age = float(age)

        # Remove impossible ages
        if age < 0 or age > 120:
            return np.nan

        return age

    except:
        return np.nan

# Apply function
df["Age"] = df["Age"].apply(clean_age)

# Fill missing ages with median
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)

# Convert to integer
df["Age"] = df["Age"].astype(int)

# ---------------------------------------------------------
# 3. CLEAN CONDITION COLUMN
# ---------------------------------------------------------

# Fill missing conditions with most common value
most_common_condition = df["Condition"].mode()[0]

df["Condition"] = df["Condition"].fillna(most_common_condition)

# ---------------------------------------------------------
# 4. CLEAN MEDICATION COLUMN
# ---------------------------------------------------------

df["Medication"] = df["Medication"].str.strip().str.title()

# ---------------------------------------------------------
# 5. CLEAN VISIT DATE
# ---------------------------------------------------------

# Convert dates into proper format
df["Visit Date"] = pd.to_datetime(
    df["Visit Date"],
    errors="coerce"
)

# Fill missing dates
df["Visit Date"] = df["Visit Date"].fillna(
    df["Visit Date"].mode()[0]
)

# Create new columns
df["Visit_Year"] = df["Visit Date"].dt.year
df["Visit_Month"] = df["Visit Date"].dt.month

# ---------------------------------------------------------
# 6. CLEAN BLOOD PRESSURE
# ---------------------------------------------------------

# Split blood pressure into 2 columns

df[["BP_Systolic", "BP_Diastolic"]] = (
    df["Blood Pressure"]
    .str.extract(r"(\d+)/(\d+)")
)

# Convert to numbers
df["BP_Systolic"] = pd.to_numeric(df["BP_Systolic"])
df["BP_Diastolic"] = pd.to_numeric(df["BP_Diastolic"])

# Fill missing values
df["BP_Systolic"] = df["BP_Systolic"].fillna(
    df["BP_Systolic"].median()
)

df["BP_Diastolic"] = df["BP_Diastolic"].fillna(
    df["BP_Diastolic"].median()
)

# ---------------------------------------------------------
# 7. CLEAN CHOLESTEROL
# ---------------------------------------------------------

df["Cholesterol"] = df["Cholesterol"].fillna(
    df["Cholesterol"].median()
)

# ---------------------------------------------------------
# 8. CLEAN EMAILS
# ---------------------------------------------------------

# Remove fake emails
fake_emails = [
    "name@hospital.org",
    "contact@domain.com",
    "patient@example.com"
]

def clean_email(email):

    if pd.isna(email):
        return np.nan

    email = str(email).lower().strip()

    # Remove fake emails
    if email in fake_emails:
        return np.nan

    # Check email format
    pattern = r"^[^@]+@[^@]+\.[^@]+$"

    if re.match(pattern, email):
        return email

    return np.nan

df["Email"] = df["Email"].apply(clean_email)

# ---------------------------------------------------------
# 9. CLEAN PHONE NUMBERS
# ---------------------------------------------------------

def clean_phone(phone):

    if pd.isna(phone):
        return np.nan

    # Keep only numbers
    phone = re.sub(r"\D", "", str(phone))

    # Remove fake number
    if phone == "5555555555":
        return np.nan

    return phone

df["Phone Number"] = df["Phone Number"].apply(clean_phone)

# ---------------------------------------------------------
# 10. REMOVE DUPLICATES
# ---------------------------------------------------------

df = df.drop_duplicates()

# =========================================================
# FEATURE ENGINEERING
# =========================================================

# ---------------------------------------------------------
# AGE GROUP
# ---------------------------------------------------------

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 30, 50, 70, 100],
    labels=["Young", "Adult", "Senior", "Elderly"]
)

# ---------------------------------------------------------
# HIGH CHOLESTEROL
# ---------------------------------------------------------

df["High_Cholesterol"] = np.where(
    df["Cholesterol"] > 200,
    1,
    0
)

# ---------------------------------------------------------
# ON MEDICATION
# ---------------------------------------------------------

df["On_Medication"] = np.where(
    df["Medication"] != "None",
    1,
    0
)

# =========================================================
# SAVE CLEAN DATA
# =========================================================

df.to_csv("healthcare_cleaned.csv", index=False)

print("\nCleaning Complete")
print("Clean dataset saved as healthcare_cleaned.csv")

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFirst 5 Clean Rows:")
print(df.head())