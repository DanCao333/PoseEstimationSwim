import numpy as np
import pandas as pd

def add_distance_column(csv_file_path, distances):
    df = pd.read_csv(csv_file_path)

    if len(distances) != len(df):
        raise ValueError("Invalid length")

    df["distance"] = distances

    df.to_csv(csv_file_path, index=False)

def add_padding(sequences, max_val=-1):
    if max_val > 0:
        max_sequence_len = max_val
    else:
        max_sequence_len = max(len(seq) - 1 for seq in sequences)

    print(f"MAX SEQ LEN {max_sequence_len}")
    padding_val = 0.0

    # Calculate the number of elements to pad
    padded_sequences = []

    for seq in sequences:
        speed = seq[-1]
        seq.pop()
        temp = np.concatenate((seq, np.full(max_sequence_len - len(seq), padding_val)))
        temp = np.append(temp, speed)
        
        padded_sequences.append(temp)
    
    return padded_sequences, max_sequence_len


def process_and_save_dataset(sequences, file_path):
    result, max_seq = add_padding(sequences)

    # path_components = file_path.split(".")
    # path_components[0] = path_components[0] + str(max_seq) + "."
    # file_path = "".join(path_components)

    print(f"SAVING TO: {file_path}")

    # Prepare the columns for DF
    n_frames = len(result[0]) // 5 # depends on how many data points you are including
    column_name = []
    for i in range(n_frames):
        column_name.append(f"Left Leg: {i}")
        column_name.append(f"Right Leg: {i}")
        column_name.append(f"Left Arm: {i}")
        column_name.append(f"Right Arm: {i}")
        column_name.append(f"Body Angle: {i}")
    column_name.append("Velocity")

    # DF creation
    df = pd.DataFrame(result, columns=column_name)

    # Save to CSV
    df.to_csv(file_path, index=False)

def process_dataset(sequences, max_pad=-1): # TODO: add second arg for max pad
    result, max_seq = add_padding(sequences, max_val=max_pad)

    print(f"Vince elements: {result}\nMAX SEQ: {max_seq}")

    # Prepare the columns for DF
    n_frames = len(result[0]) // 5 # depends on how many data points you are including
    column_name = []
    for i in range(n_frames):
        column_name.append(f"Left Leg: {i}")
        column_name.append(f"Right Leg: {i}")
        column_name.append(f"Left Arm: {i}")
        column_name.append(f"Right Arm: {i}")
        column_name.append(f"Body Angle: {i}")
    column_name.append("Velocity")

    # if max_pad > 0:
    #     column_name.append("Distance")

    # DF creation
    df = pd.DataFrame(result, columns=column_name)

    return df