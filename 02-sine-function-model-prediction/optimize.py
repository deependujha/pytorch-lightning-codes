import numpy as np
import litdata as ld

def sine_function(x: int):
    # You can use any key:value pairs. Note that their types must not change between samples, and Python lists must
    # always contain the same number of elements with the same types.
    data = {"x": x, "sine": np.sin(x)}

    return data

if __name__ == "__main__":
    # The optimize function writes data in an optimized format.
    ld.optimize(
        fn=sine_function,                   # the function applied to each input
        inputs=list(np.linspace(-5,5,1000)),           # the inputs to the function (here it's a list of numbers)
        output_dir="optimize_sine_data",             # optimized data is stored here
        num_workers=4,                      # The number of workers on the same machine
        chunk_size=50,                  # size of each chunk
    )
