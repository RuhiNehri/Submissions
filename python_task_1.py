import pandas as pd
import numpy as np

# Car Matrix Generation

def generate_car_matrix(ds):
         
    # Load the dataset into a DataFrame
    df = pd.read_csv(ds)

    # Pivot the DataFrame to create a matrix
    df1 = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    # Set diagonal values to 0
    for idx in df1.index:
        df1.at[idx, idx] = 0

    return df1

ds = r'C:\Users\12AU\MapUp\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
result = generate_car_matrix(ds)
print(result)



# Car Type Count Calculation

def get_type_count(df):
    # Create a new column 'car_type' based on the conditions provided
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)

    # Calculate the count of occurrences for each car_type category
    type_counts = df['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts

dataset_path = r'C:\Users\12AU\MapUp\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
df = pd.read_csv(dataset_path)
result1 = get_type_count(df)
print(result1)


# Bus Count Index Retrieval

def get_bus_indexes(df):
    # Calculate the mean value of the 'bus' column
    mean_bus_value = df['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * mean_bus_value].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes

dataset_path = r'C:\Users\12AU\MapUp\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
df = pd.read_csv(dataset_path)
result2 = get_bus_indexes(df)
print(result2)


# Route Filtering

def filter_routes(df):
    # Calculate the average of values in the 'truck' column for each route
    route_avg_truck = df.groupby('route')['truck'].mean()

    # Filter routes where the average truck value is greater than 7
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    # Sort the list of selected routes
    selected_routes.sort()

    return selected_routes

dataset_path =  r'C:\Users\12AU\MapUp\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
df = pd.read_csv(dataset_path)
result3 = filter_routes(df)
print(result3)



# Matrix Value Modification

def multiply_matrix(matrix_df):
    # Apply the specified logic to modify each value in the DataFrame
    modified_df = result.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    # Round the values to 1 decimal place
    rounded_df = modified_df.round(1)

    return rounded_df

result_matrix = generate_car_matrix(r'C:\Users\12AU\MapUp\MapUp-Data-Assessment-F\datasets\dataset-1.csv')
modified_result = multiply_matrix(result_matrix)
print(modified_result)



