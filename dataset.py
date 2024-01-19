import numpy as np
import pandas as pd

def add_distance_column(csv_file_path, distances):
    df = pd.read_csv(csv_file_path)

    if len(distances) != len(df):
        raise ValueError("Invalid length")

    df["distance"] = distances

    df.to_csv(csv_file_path, index=False)

def add_padding(sequences):
    max_sequence_len = max(len(seq) - 1 for seq in sequences)
    padding_val = 0.0

    # Calculate the number of elements to pad
    padded_sequences = []

    for seq in sequences:
        speed = seq[-1]
        seq.pop()
        temp = np.concatenate((seq, np.full(max_sequence_len - len(seq), padding_val)))
        temp = np.append(temp, speed)
        
        padded_sequences.append(temp)
    
    return padded_sequences


def process_and_save_dataset(sequences, file_path):
    result = add_padding(sequences)

    # Prepare the columns for DF
    n_frames = len(result[0]) // 4 # depends on how many data points you are including
    column_name = []
    for i in range(n_frames):
        column_name.append(f"Left Leg: {i}")
        column_name.append(f"Right Leg: {i}")
        column_name.append(f"Left Arm: {i}")
        column_name.append(f"Right Arm: {i}")
    column_name.append("Velocity")

    # DF creation
    df = pd.DataFrame(result, columns=column_name)

    # Save to CSV
    df.to_csv(file_path, index=False)