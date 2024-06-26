import pandas as pd
import numpy as np
from mpl_toolkits.basemap import Basemap
import os

# Path to the CSV file
path_migration_bird = r'C:\Users\ththy\Desktop\Stage_Thales\code\data_bird\Local_flight_paths_of_nocturnally_migrating_birds.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(path_migration_bird)

# Define parameters
unique_param = 'tag-local-identifier'
long_param = 'location-long'
lat_param = 'location-lat'
z_param = 'height-above-msl'

id = 0
# Iterate over unique tags to process each trajectory
for unique in df[unique_param].unique():
    traj_cur = df[df[unique_param] == unique]

    time = traj_cur['timestamp']
    long = traj_cur[long_param]
    lat = traj_cur[lat_param]
    z = traj_cur[z_param]

    m = Basemap(projection='merc', llcrnrlat=lat.min(), urcrnrlat=lat.max(), llcrnrlon=long.min(), urcrnrlon=long.max(), resolution='c')

    # Initialize empty lists for x and y coordinates
    x = []
    y = []

    # Convert longitude and latitude to x and y coordinates with error handling
    for lon, lat in zip(long.values, lat.values):
        try:
            x_coord, y_coord = m(lon, lat)
            x.append(x_coord)
            y.append(y_coord)
        except Exception as e:
            x.append(np.nan)
            y.append(np.nan)

    # Create a DataFrame for the current trajectory
    trajectory_df = pd.DataFrame({
        'time': time,
        'x': x,
        'y': y,
        'z': z
    })
    
    # Save the trajectory DataFrame to a CSV file
    output_path = f'C:\\Users\\ththy\\Desktop\\Stage_Thales\\birds_trajectories_simulation\\Dataset\\Local_flight_paths_of_nocturnally_migrating_birds\\data_processed\\trajectory_{id}_len{len(x)}.csv'
    trajectory_df.to_csv(output_path, index=False, encoding='utf-8')
    id += 1


# import pandas as pd
# import numpy as np
# from mpl_toolkits.basemap import Basemap
# import os

# # Path to the CSV file
# path_migration_bird = r'C:\Users\ththy\Desktop\Stage_Thales\code\data_bird\Local_flight_paths_of_nocturnally_migrating_birds.csv'

# # Read the CSV file into a DataFrame
# df = pd.read_csv(path_migration_bird)

# # Print the columns of the DataFrame
# print(df.columns)

# # Print the 'timestamp' column
# print(df['timestamp'])

# # Define parameters
# unique_param = 'tag-local-identifier'
# long_param = 'location-long'
# lat_param = 'location-lat'
# z_param = 'height-above-msl'

# # Print unique values of the 'tag-local-identifier' column
# print(df[unique_param].unique())

# # Get unique values of the 'tag-local-identifier' column
# unique_values = df[unique_param].unique()

# # Initialize an empty dictionary to store errors
# error_dic = {}

# # Initialize a flag to track if all tags are numeric
# passed = True

# # Check if all tags are numeric
# for tag in unique_values:
#     try:
#         int(tag)
#     except ValueError:
#         # If a non-numeric tag is found, set the flag to False
#         passed = False
#         break  # No need to check further since we found a non-numeric tag

# # If not all tags are numeric, populate the error dictionary
# if not passed:
#     for tag2 in unique_values:
#         error_dic[tag2] = id

# # Initialize an empty DataFrame to store trajectory data

# id = 0
# # Iterate over unique tags to process each trajectory
# for unique in df[unique_param].unique():
#     if id < 5:
#         output = pd.DataFrame()
#         traj_cur = df[df[unique_param] == unique]

#         time = traj_cur['timestamp']
#         long = traj_cur[long_param]
#         lat = traj_cur[lat_param]
#         z = traj_cur[z_param]

#         m = Basemap(projection='merc', llcrnrlat=lat.min(), urcrnrlat=lat.max(), llcrnrlon=long.min(), urcrnrlon=long.max(), resolution='c')
#         x, y = m(long.values, lat.values)

#         # Convert x and y to DataFrames
#         x_df = pd.DataFrame(x, columns=['x'])
#         y_df = pd.DataFrame(y, columns=['y'])
        
#         squeeze_x_df = np.squeeze(x_df)
#         squeeze_y_df = np.squeeze(y_df)
#         squeeze_z = np.squeeze(z)
#         squeeze_time = np.squeeze(time)


#         print("shape x", squeeze_x_df.shape)
#         print("shape y", squeeze_y_df.shape)
#         print("shape z", squeeze_z.shape)
#         print("shape time", squeeze_time.shape)
        
#         # Assuming you want to append the timestamp of the current trajectory to output_
#         # Note: This assumes traj_cur is not empty; otherwise, output_ remains empty
        
#         if not traj_cur.empty:
#             output = pd.DataFrame({'time': squeeze_time, 'x' : squeeze_x_df, 'y' : squeeze_y_df, 'z' : squeeze_z })
            
#             output_path = rf"C:\Users\ththy\Desktop\Stage_Thales\birds_trajectories_simulation\Dataset\trajectoire_{id}_len{traj_cur.shape[0]}"
#             output.to_csv(output_path, index=False, encoding='utf-8')
#             id += 1
#     else :
#         break

# # Print the columns of the output DataFrame
# print(output.columns)


# # 'time': [traj_cur['timestamp'].iloc[0]],

#             #output = pd.Series([traj_cur['timestamp'].iloc[0]] + x + y + z)
        
#         # if not traj_cur.empty:
#         #     output = output._append(traj_cur[['timestamp']], ignore_index=True)
#         #     output = output._append(x_df, ignore_index=True)
#         #     output = output._append(y_df, ignore_index=True)
#         #     output = output._append(z, ignore_index=True)

#             # Ensure the output DataFrame has the correct column names
#             #output.columns = ['timestamp', 'x', 'y', z_param]