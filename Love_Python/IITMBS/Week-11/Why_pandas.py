
#using file handler
# Open the file
# f = open('StudentMarksDataset.csv', 'r')
# scores = f.readlines()[1:]  # Skip the header line
# max_score = 0
#
# for record in scores:
#     fields = record.split(',')
#     if int(fields[8]) > max_score:
#         max_score = int(fields[8])
#
# print(max_score)  # Print the maximum score after the loop

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# f = open('StudentMarksDataset.csv', 'r')
# scores = f.readlines()[1:]  # Skip the header line
#
# # Initialize the variable to store the maximum marks
# max_marks2 = 0.0
#
# # Iterate through the records
# for record in scores:
#     fields = record.split(',')
#
#     # Handle missing values in Std_Marks2
#     if fields[6].strip():  # Check if Std_Marks2 is not empty
#         marks2 = float(fields[6].strip())
#         if marks2 > max_marks2:
#             max_marks2 = marks2
#
# # Print the result
# print("Maximum in Std_Marks2:", max_marks2)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# import pandas as pd
#
# # Load the dataset into a DataFrame
# df = pd.read_csv('StudentMarksDataset.csv')

# Find the maximum value in the Std_Marks2 column
# max_marks2 = df['Std_Marks2'].max()

# Print the result
# print("Pandas Maximum in Std_Marks2:", max_marks2)
#print(df)
#print(df.shape) #tuple
#print(df.count())
# print(pd.read_csv('StudentMarksDataset.csv')['Std_Marks2'].min())
# print(pd.read_csv('StudentMarksDataset.csv')['Std_Marks2'].mean())
# print(df['Std_Marks2'].sum())
# print(pd.read_csv('StudentMarksDataset.csv')['Std_Marks2'].sort_values(ascending = False))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# scores=pd.read_csv('scores.csv')
# print(scores['Totral'].max())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv('StudentMarksDataset.csv')
# print(df)
# print(df,type(df)) #dataframe in2D
# print(df['Std_Name'],type(df['Std_Name']))

#sample row
# print(df.head()) #top 5
# print(df.tail()) #last row
# print(df[df['Std_Name'] == 'Ritika Katara']) #column wise


# print(df[df['Std_Course'] == 'B.Sc 1st year'])
# print(df[df['Std_Course'] == 'B.Sc 1st year']['Std_Marks1'])
# print(df[df['Std_Course'] == 'B.Sc 1st year']['Std_Marks1'].min())
# print(df[df['Std_Course'] == 'B.Sc 2nd Year']['Std_Marks2'].min())


#Student Categories
# print(df[df['Std_Marks1'] >85])
# print(df[df['Std_Marks1'].between(80,85)])
# print(df[df['Std_Marks1'] <80])

# print(df[df['Std_Marks1'] >85].shape[0])
# print(df[df['Std_Marks1'].between(80,85)].shape[0])
# print(df[df['Std_Marks1'] <80].shape[0])

#Two cond
# print(df[(df['Std_Branch'] == 'AGRICULTURE') & (df['Std_Marks1'] < 80)])
# print(df[(df['Std_Branch'] == 'AGRICULTURE') & (df['Std_Marks1'] < 80)].shape[0])


#Categories
print(df.groupby('Std_Branch').groups) #dict of list












