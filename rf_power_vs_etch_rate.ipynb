{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c38c67eb-7f22-4825-b47a-456d3539a24e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overall Mean (μ): 617.75\n",
      "Mean for RF Power 160W (ȳ): 551.20\n",
      "Mean for RF Power 180W (ȳ): 587.40\n",
      "Mean for RF Power 200W (ȳ): 625.40\n",
      "Mean for RF Power 220W (ȳ): 707.00\n",
      "Treatment Effect for RF Power 160W (τ̂): -66.55\n",
      "Treatment Effect for RF Power 180W (τ̂): -30.35\n",
      "Treatment Effect for RF Power 200W (τ̂): 7.65\n",
      "Treatment Effect for RF Power 220W (τ̂): 89.25\n",
      "\n",
      "Significance Level (α): 0.05\n",
      "95% Confidence Interval for the mean of treatment 4: (684.32, 729.68)\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import scipy.stats as stats\n",
    "\n",
    "# Data for plasma etching experiment\n",
    "data = {\n",
    "    'RF_Power': [160, 160, 160, 160, 160, \n",
    "                 180, 180, 180, 180, 180, \n",
    "                 200, 200, 200, 200, 200, \n",
    "                 220, 220, 220, 220, 220],\n",
    "    'Etch_Rate': [575, 542, 530, 539, 570,\n",
    "                  565, 593, 590, 579, 610,\n",
    "                  600, 651, 610, 637, 629,\n",
    "                  725, 700, 715, 685, 710]\n",
    "}\n",
    "\n",
    "# Calculate overall mean\n",
    "overall_mean = np.sum(data['Etch_Rate']) / 20\n",
    "print(f\"Overall Mean (μ): {overall_mean:.2f}\")\n",
    "\n",
    "# Calculate treatment means\n",
    "treatment_means = {\n",
    "    160: np.mean(data['Etch_Rate'][0:5]),\n",
    "    180: np.mean(data['Etch_Rate'][5:10]),\n",
    "    200: np.mean(data['Etch_Rate'][10:15]),\n",
    "    220: np.mean(data['Etch_Rate'][15:20])\n",
    "}\n",
    "\n",
    "# Print treatment means\n",
    "for power, mean in treatment_means.items():\n",
    "    print(f\"Mean for RF Power {power}W (ȳ): {mean:.2f}\")\n",
    "\n",
    "# Calculate treatment effects (tau)\n",
    "treatment_effects = {k: v - overall_mean for k, v in treatment_means.items()}\n",
    "for power, effect in treatment_effects.items():\n",
    "    print(f\"Treatment Effect for RF Power {power}W (τ̂): {effect:.2f}\")\n",
    "\n",
    "# Parameters for confidence interval calculation\n",
    "mean_treatment_4 = treatment_means[220]  # Mean for RF Power 220W\n",
    "mean_square_error = 333.70  # From previous ANOVA results\n",
    "n_treatment_4 = 5  # Number of observations for treatment 4\n",
    "alpha = 0.05  # Significance level\n",
    "\n",
    "# Print alpha value\n",
    "print(f\"\\nSignificance Level (α): {alpha:.2f}\")\n",
    "\n",
    "# Critical t-value for 95% confidence and 4 degrees of freedom\n",
    "t_critical = stats.t.ppf(1 - alpha/2, n_treatment_4 - 1)\n",
    "\n",
    "# Confidence interval calculation\n",
    "margin_of_error = t_critical * np.sqrt(mean_square_error / n_treatment_4)\n",
    "ci_lower = mean_treatment_4 - margin_of_error\n",
    "ci_upper = mean_treatment_4 + margin_of_error\n",
    "\n",
    "# Print confidence interval\n",
    "print(f\"95% Confidence Interval for the mean of treatment 4: ({ci_lower:.2f}, {ci_upper:.2f})\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86514149-fc92-47fe-abe3-31c071723d21",
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
