{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d2351952-297d-4d11-b8d5-79a145451210",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeableNote: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "Requirement already satisfied: pandas in c:\\users\\dmtro\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\\localcache\\local-packages\\python312\\site-packages (2.2.2)\n",
      "Requirement already satisfied: openpyxl in c:\\users\\dmtro\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\\localcache\\local-packages\\python312\\site-packages (3.1.5)\n",
      "Requirement already satisfied: scipy in c:\\users\\dmtro\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\\localcache\\local-packages\\python312\\site-packages (1.14.1)\n",
      "Requirement already satisfied: numpy in c:\\users\\dmtro\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\\localcache\\local-packages\\python312\\site-packages (2.1.0)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\dmtro\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\\localcache\\local-packages\\python312\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\dmtro\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\\localcache\\local-packages\\python312\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\dmtro\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\\localcache\\local-packages\\python312\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: et-xmlfile in c:\\users\\dmtro\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\\localcache\\local-packages\\python312\\site-packages (from openpyxl) (1.1.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\dmtro\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\\localcache\\local-packages\\python312\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "pip install pandas openpyxl scipy numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bb70a3f7-ceab-4fb1-841e-04ec929a0156",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SEM 0.5 mg (OZEMPIC) - Mean: 4.688888888888888, Variance: 4.504575163398692, Standard Deviation: 2.1223984459565295\n",
      "Diet and Exercise only - Mean: 6.85, Variance: 10.593000000000002, Standard Deviation: 3.254688925227725\n",
      "T-Statistic: -2.664837221010822, P-Value: 0.010890261350631628\n",
      "Alpha level: 0.05\n",
      "Reject null hypothesis: There is a significant difference in pounds lost between the two groups.\n",
      "95% Confidence Interval for SEM 0.5 mg (OZEMPIC): (np.float64(3.708408847873899), np.float64(5.669368929903877))\n",
      "95% Confidence Interval for Diet and Exercise only: (np.float64(5.598960842898794), np.float64(8.101039157101205))\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from scipy import stats\n",
    "\n",
    "# Load data from Excel\n",
    "file_path = 'Test 1 Data.xlsx' \n",
    "\n",
    "# Read data from the Excel\n",
    "# Use specific ranges to load the data\n",
    "sem_data = pd.read_excel(file_path, sheet_name='Sheet1', header=None, usecols='B', skiprows=4).dropna().values.flatten()\n",
    "diet_exercise_data = pd.read_excel(file_path, sheet_name='Sheet1', header=None, usecols='I', skiprows=3).dropna().values.flatten()\n",
    "\n",
    "# Check for empty arrays after conversion\n",
    "if len(sem_data) == 0 or len(diet_exercise_data) == 0:\n",
    "    raise ValueError(\"One of the data arrays is empty after cleaning. Check the input data.\")\n",
    "\n",
    "# 1. Mean value for each treatment group\n",
    "mean_sem = np.mean(sem_data)\n",
    "mean_diet_exercise = np.mean(diet_exercise_data)\n",
    "\n",
    "# 2. Variance for each treatment group\n",
    "variance_sem = np.var(sem_data, ddof=1)\n",
    "variance_diet_exercise = np.var(diet_exercise_data, ddof=1)\n",
    "\n",
    "# 3. Standard deviation for each treatment group\n",
    "std_dev_sem = np.sqrt(variance_sem)\n",
    "std_dev_diet_exercise = np.sqrt(variance_diet_exercise)\n",
    "\n",
    "# Results\n",
    "print(f\"SEM 0.5 mg (OZEMPIC) - Mean: {mean_sem}, Variance: {variance_sem}, Standard Deviation: {std_dev_sem}\")\n",
    "print(f\"Diet and Exercise only - Mean: {mean_diet_exercise}, Variance: {variance_diet_exercise}, Standard Deviation: {std_dev_diet_exercise}\")\n",
    "\n",
    "# 4. Define the null and alternative hypotheses\n",
    "# H0: The means of the two groups are equal (no difference in pounds lost)\n",
    "# H1: The means of the two groups are not equal (difference in pounds lost)\n",
    "\n",
    "# 5. Perform two-sample t-test to compare the means\n",
    "t_statistic, p_value = stats.ttest_ind(sem_data, diet_exercise_data, equal_var=False)\n",
    "\n",
    "# Print test statistic and p-value\n",
    "print(f\"T-Statistic: {t_statistic}, P-Value: {p_value}\")\n",
    "\n",
    "# 6. State results\n",
    "alpha = 0.05\n",
    "print(f\"Alpha level: {alpha}\")\n",
    "if p_value < alpha:\n",
    "    print(\"Reject null hypothesis: There is a significant difference in pounds lost between the two groups.\")\n",
    "else:\n",
    "    print(\"Fail to reject null hypothesis: There is not enough evidence to suggest a significant difference in pounds lost between the two groups.\")\n",
    "\n",
    "# 7. Additional Analysis: Calculate 95% Confidence\n",
    "confidence_interval_sem = stats.norm.interval(0.95, loc=mean_sem, scale=std_dev_sem/np.sqrt(len(sem_data)))\n",
    "confidence_interval_diet_exercise = stats.norm.interval(0.95, loc=mean_diet_exercise, scale=std_dev_diet_exercise/np.sqrt(len(diet_exercise_data)))\n",
    "\n",
    "print(f\"95% Confidence Interval for SEM 0.5 mg (OZEMPIC): {confidence_interval_sem}\")\n",
    "print(f\"95% Confidence Interval for Diet and Exercise only: {confidence_interval_diet_exercise}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0321d5e-7746-48a7-89e9-f38733ed5a9a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
