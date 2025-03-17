import litdata as ld

ds = ld.StreamingDataset("optimize_sine_data")
dl = ld.StreamingDataLoader(ds, batch_size=4)

for batch in dl:
    print(f"{batch=}")
