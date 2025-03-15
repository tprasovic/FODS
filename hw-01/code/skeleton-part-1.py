"""
HW01 Part 1, Foundations of Data Science (376-1983-00L), Spring Semester 2024

Instructions for this homework:

Before you change anything in this script, make sure that it runs! It should first run without throwing an error message.
Only after you made sure that the script runs without an error message, start to fill in your solutions. Lines where you
should fill in your solutions are marked with "# your solution". You must replace the "None" in these lines with your
code. Further, you need to write some additional lines on your own as necessary.
"""

import pandas as pd
import seaborn as sns

# load data
hospitals = pd.read_csv("../data/data-part-1.csv", index_col=0)


# --------------------------------------------------------------------------------------
# ############################### #
# ##### Getting an overview ##### #
# ############################### #
# question 1
n_rows = hospitals.shape[0] # my solution

n_cols = hospitals.shape[1] # my solution

# question 2
n_hospitals = hospitals['Facility.Name'].nunique()  # my solution

# question 3
n_states = hospitals['Facility.State Name'].nunique()  # my solution

############################################ 
############################################ 
#selfmade for overall cost
cost_col=[col for col in hospitals.columns if 'Cost' in col] #creats list of all column titles with "Cost" in it
total_hospital_cost= hospitals[cost_col].sum(axis=1) #creats new series with total costs
############################################
############################################ 
# question 4
most_expensive_hip_and_knee = max(hospitals['Procedure.Hip Knee.Cost'])  # my solution
most_expensive_hip_and_knee_name = hospitals.loc[hospitals['Procedure.Hip Knee.Cost']== most_expensive_hip_and_knee,'Facility.Name'].values[0]  # my solution
most_expensive_hip_and_knee_city = hospitals.loc[hospitals['Procedure.Hip Knee.Cost']== most_expensive_hip_and_knee,'Facility.City'].values[0]  # my solution
most_expensive_hip_and_knee_state = hospitals.loc[hospitals['Procedure.Hip Knee.Cost']== most_expensive_hip_and_knee,'Facility.State Name'].values[0]  # my solution

most_expensive_hip_and_knee_delta = max(hospitals['Procedure.Hip Knee.Cost']) - min(hospitals['Procedure.Hip Knee.Cost'])  # my solution 
least_expensive_hip_and_knee = min(hospitals['Procedure.Hip Knee.Cost'])  # my solution
expense_delta_hip_and_knee = total_hospital_cost.max() - total_hospital_cost.min()# my solution, what is difference to most_expensive_hip_and_knee_delta ?

# question 5
least_expensive_total_name = hospitals.loc[total_hospital_cost.idxmin(), 'Facility.Name']  # my solution
least_expensive_total_city = hospitals.loc[total_hospital_cost.idxmin(), 'Facility.City']  # my solution
least_expensive_total_state = hospitals.loc[total_hospital_cost.idxmin(), 'Facility.State Name']  # my solution

# your solution
# ... to interpret quality of least expensive hospital, for example
# print(least_expensive_total[overall_rating_columns])
# print(least_expensive_total[procedure_quality_columns])
# Hint: The variables "overall_rating_columns" and "procedure_quality_columns" must be defined by yourself
least_expensive_total_series = hospitals.loc[total_hospital_cost.idxmin(),:] #creats pd series with index f.e. facility.name and value United Health Services Hospitals, Inc
least_expensive_quality_series = least_expensive_total_series[[ind for ind in least_expensive_total_series.index if 'Quality' in ind or 'Rating' in ind]]
least_expensive_procedure_quality = least_expensive_total_series[[ind for ind in least_expensive_total_series.index if 'Quality' in ind and 'Procedure' in ind]]


# ################################ #
# DO NOT change the following code #
# ################################ #
print("*" * 10 + " Getting an overview " + "*" * 10 + "\n"
      f"There are {n_rows} rows and {n_cols} columns in the data.\n"
      f"Data on {n_hospitals} distinct hospitals is reported across {n_states} states.\n"
      f"The most expensive hospital for hip and knee procedures is {most_expensive_hip_and_knee_name}"
      f"in {most_expensive_hip_and_knee_city}, {most_expensive_hip_and_knee_state}.\n"
      f"The least expensive hospital overall is {least_expensive_total_name}"
      f"in {least_expensive_total_city}, {least_expensive_total_state}.\n"
      f"The most expensive hospital is US${expense_delta_hip_and_knee} more expensive "
      "than the least expensive hospital.\n")

print("Overall rating of the least expensive hospital:")
print(least_expensive_quality_series) #my solution
print("Procedure and quality rating of the least expensive hospital:")
print(least_expensive_procedure_quality) #my solution

# --------------------------------------------------------------------------------------
# ##########################
# ##### Missing data ##### #
# ##########################

# question 1
columns_with_missing_data =  hospitals.columns[hospitals.isna().sum() > 0].tolist()# my solution -> if sum of number of missing values is bigger 
                                                                                   # than 0 it ads column title to the new data set
# question 2

# my solution
# Identify and summarize the missing data
missing_data_summary =  hospitals.isna().sum()[hospitals.isna().sum()>0] #[hospitals.isna().sum()>0] to only show columns with missing data
# ################################ #
# DO NOT change the following code #
# ################################ #
print("*" * 10 + " Missing data " + "*" * 10)

print(f"Missing data found in following columns: {columns_with_missing_data}.")

#by myself
print("\nSummary of missing data per column:\n")
print(missing_data_summary)
# --------------------------------------------------------------------------------------
# ############################### #
# ##### Basic visualisation ##### #
# ############################### #
# question 1
fig_pneumonia_cost = sns.displot(hospitals, x= 'Procedure.Pneumonia.Cost')  # my solution
fig_pneumonia_cost.set(xlabel="Cost (USD)",ylabel="Number of Patients",title="Costs for pneumonia treatment")
# DO NOT modify line below
fig_pneumonia_cost.savefig("../output/131_pneumonia.png")

# question 2
fig_heart_failure_cost_vs_quality = sns.displot(hospitals,x='Procedure.Heart Failure.Quality', y='Procedure.Heart Failure.Cost', kind='hist', cbar=True)
fig_heart_failure_cost_vs_quality.set(xlabel="Quality of heartfailure treatment", ylabel="Cost of heartfailure treatment (USD)", title="Procedure of heartfailure")  # my solution


# DO NOT modify line below
fig_heart_failure_cost_vs_quality.savefig("../output/132_heart-failure-cost-vs-quality.png")
