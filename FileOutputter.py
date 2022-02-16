import pandas as pd
import numpy as np

def output_file(row_names, data, filename="output.txt"):
    row_names = [row_names]
    generated = data
    complete = row_names + generated

    df = pd.DataFrame(data=complete, columns=row_names)

    print(df.head())
    np.savetxt(filename, df, fmt='%s')