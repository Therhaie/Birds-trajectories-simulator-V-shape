import pandas as pd
import os
import numpy as np

def writting_to_csv(app, data):
    # Number of birds
    number_of_birds = app.num_birds

    # Create a list of lists, where each inner list contains the position of a bird at a specific time
    position = [[bird.position[0], bird.position[1], bird.position[2]] for bird in app.formation]

    # Convert the list of lists to a numpy array
    position = np.array(position)

    output_path = r'C:\Users\ththy\Desktop\Stage_Thales\birds_simulation_V_shape\my_file.csv'

    # Check if the file already exists
    if os.path.isfile(output_path):
        # Read the file into a DataFrame
        df = pd.read_csv(output_path)

        # Create a new DataFrame with the new data
        new_data = pd.DataFrame({'time': [data]})
        for j in range(number_of_birds):
            new_data = pd.concat([new_data, pd.DataFrame({f'x_{j}': [position[j, 0]], f'y_{j}': [position[j, 1]], f'z_{j}': [position[j, 2]]})], axis=1)
        # Append the new data to the DataFrame
        df = pd.concat([df, new_data], ignore_index=True)
    else:
        # Create a new DataFrame with initial data
        df = pd.DataFrame({'time': [data]})
        for j in range(number_of_birds):
            df = pd.concat([df, pd.DataFrame({f'x_{j}': [position[j, 0]], f'y_{j}': [position[j, 1]], f'z_{j}': [position[j, 2]]})], axis=1)

    # Write the DataFrame to the CSV file
    df.to_csv(output_path, index=False)



# #####################################################################################################
# functional code but provided a "error" message explaning that the code could be optimized
# import pandas as pd
# import os
# import numpy as np

# def writting_to_csv(app, data):
#     # Number of birds
#     number_of_birds = app.num_boids

#     # Create a list of lists, where each inner list contains the position of a bird at a specific time
#     position = [[boid.position[0], boid.position[1], boid.position[2]] for boid in app.boids_list]

#     # Convert the list of lists to a numpy array
#     position = np.array(position)

#     output_path = r'C:\Users\ththy\Desktop\Stage_Thales\birds_trajectories_simulation\Output_dataset\Local_flight_paths_of_nocturnally_migrating_birds\my_file.csv'

#     # Check if the file already exists
#     if os.path.isfile(output_path):
#         # Read the file into a DataFrame
#         df = pd.read_csv(output_path)

#         # Append the new data to the DataFrame
#         new_data = pd.DataFrame({f'time_{i}': [data] for i in range(number_of_birds)})
#         for i in range(number_of_birds):
#             new_data[f'x_{i}'] = position[i, 0]
#             new_data[f'y_{i}'] = position[i, 1]
#             new_data[f'z_{i}'] = position[i, 2]
#         df = pd.concat([df, new_data], ignore_index=True)
#     else:
#         # Create a new DataFrame with initial data
#         df = pd.DataFrame({f'time_{i}': [data] for i in range(number_of_birds)})
#         for i in range(number_of_birds):
#             df[f'x_{i}'] = position[i, 0]
#             df[f'y_{i}'] = position[i, 1]
#             df[f'z_{i}'] = position[i, 2]

#     # Write the DataFrame to the CSV file
#     df.to_csv(output_path, index=False)

####################################################################################################
# import pandas as pd
# import os
# import numpy as np

# def writting_to_csv(app, data):
#     # Number of birds
#     number_of_birds = app.num_boids

#     # Create a list of lists, where each inner list contains the position of a bird at a specific time
#     position = [[boid.position[0], boid.position[1], boid.position[2]] for boid in app.boids_list]

#     # Convert the list of lists to a numpy array
#     position = np.array(position)

#     output_path = r'C:\Users\ththy\Desktop\Stage_Thales\birds_trajectories_simulation\Output_dataset\Local_flight_paths_of_nocturnally_migrating_birds\my_file.csv'
#     # Check if the file already exists
#     if os.path.isfile('my_file.csv'):
#         # Read the file into a DataFrame
#         df = pd.read_csv(output_path)

#         # Append the new data to the DataFrame
#         new_data = pd.DataFrame({f'time_{i}': [data] for i in range(number_of_birds)})
#         for i in range(number_of_birds):
#             new_data[f'x_{i}'] = position[i, 0]
#             new_data[f'y_{i}'] = position[i, 1]
#             new_data[f'z_{i}'] = position[i, 2]
#         df = pd.concat([df, new_data], ignore_index=True)
#     else:
#         # Create a new DataFrame with initial data
#         df = pd.DataFrame({f'time_{i}': [data] for i in range(number_of_birds)})
#         for i in range(number_of_birds):
#             df[f'x_{i}'] = position[i, 0]
#             df[f'y_{i}'] = position[i, 1]
#             df[f'z_{i}'] = position[i, 2]

#     # Write the DataFrame to the CSV file
#     output = r'C:\Users\ththy\Desktop\Stage_Thales\birds_trajectories_simulation\Output_dataset\Local_flight_paths_of_nocturnally_migrating_birds\my_file.csv'
#     df.to_csv(output_path, index=False)
