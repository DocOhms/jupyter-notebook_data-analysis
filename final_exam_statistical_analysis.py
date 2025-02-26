{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c50f5458-184b-4efa-b3f1-38797f089517",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: numpy in c:\\users\\dmtro\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\\localcache\\local-packages\\python312\\site-packages (2.1.0)\n",
      "Requirement already satisfied: scipy in c:\\users\\dmtro\\appdata\\local\\packages\\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\\localcache\\local-packages\\python312\\site-packages (1.14.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install numpy scipy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "de77ef35-7616-4b4e-812d-54c3f5b2921c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Section 01 - Mean: 61.0, Variance: 597.4166666666666, Standard Deviation: 24.442108474243106\n",
      "Section 02 - Mean: 63.4, Variance: 505.8315789473685, Standard Deviation: 22.490699832316658\n",
      "T-Statistic: -0.3422004491523506, P-Value: 0.7339022793372141\n",
      "Alpha level: 0.05\n",
      "Failed to reject null hypothesis\n",
      "There is not enough evidence to suggest a significant difference in performance between the two sections.\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from scipy import stats\n",
    "\n",
    "# Final exam grades for each section\n",
    "sec01_grades = np.array([75, 86, 82, 75, 56, 45, 23, 95, 87, 56, 55, 84, 25, 97, 33, 45, 87, 98, 45, 34, 56, 72, 23, 45, 46])\n",
    "sec02_grades = np.array([87, 67, 58, 65, 79, 89, 93, 34, 45, 36, 57, 87, 65, 45, 23, 48, 92, 75, 34, 89])\n",
    "\n",
    "# 1. Mean value for the grades for each section\n",
    "mean_sec01 = np.mean(sec01_grades)\n",
    "mean_sec02 = np.mean(sec02_grades)\n",
    "\n",
    "# 2. Variance for the grades for each section\n",
    "variance_sec01 = np.var(sec01_grades, ddof=1)\n",
    "variance_sec02 = np.var(sec02_grades, ddof=1)\n",
    "\n",
    "# 3. Standard deviation for the grades for each section\n",
    "std_dev_sec01 = np.sqrt(variance_sec01)\n",
    "std_dev_sec02 = np.sqrt(variance_sec02)\n",
    "\n",
    "# Results\n",
    "print(f\"Section 01 - Mean: {mean_sec01}, Variance: {variance_sec01}, Standard Deviation: {std_dev_sec01}\")\n",
    "print(f\"Section 02 - Mean: {mean_sec02}, Variance: {variance_sec02}, Standard Deviation: {std_dev_sec02}\")\n",
    "\n",
    "# 4. Define the null and alternative hypotheses\n",
    "# H0: The means of the two sections are equal (no difference in performance)\n",
    "# H1: The means of the two sections are not equal (difference in performance)\n",
    "\n",
    "# 5. Calculate degrees of freedom for the two-sample t-test\n",
    "# Welch's t-test does not assume equal variance\n",
    "df, _ = stats.ttest_ind(sec01_grades, sec02_grades, equal_var=False)\n",
    "\n",
    "# 6. Calculate test statistic\n",
    "t_statistic, p_value = stats.ttest_ind(sec01_grades, sec02_grades, equal_var=False)\n",
    "\n",
    "# Print test statistic and p-value\n",
    "print(f\"T-Statistic: {t_statistic}, P-Value: {p_value}\")\n",
    "\n",
    "# 7. State results\n",
    "alpha = 0.05\n",
    "print(f\"Alpha level: {alpha}\")\n",
    "if p_value < alpha:\n",
    "    print(\"Reject null hypothesis\")\n",
    "else:\n",
    "    print(\"Failed to reject null hypothesis\")\n",
    "\n",
    "# 8. State conclusions\n",
    "if p_value < alpha:\n",
    "    print(\"There is significant evidence to suggest the performance between the two sections is different.\")\n",
    "else:\n",
    "    print(\"There is not enough evidence to suggest a significant difference in performance between the two sections.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b7822df-40da-411c-86d4-2ddd4cb4a44c",
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
