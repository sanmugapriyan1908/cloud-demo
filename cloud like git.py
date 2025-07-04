from multiprocessing import Pool, cpu_count
import time

# Function to compute sum of a chunk
def chunk_sum(chunk):
    return sum(chunk)

if __name__ == '__main__':
    N = 1_000_000
    A = [1] * N  # Large array of 1s

    # Number of processes = number of CPU cores
    num_procs = cpu_count()
    chunk_size = N // num_procs

    # Split data into chunks
    chunks = [A[i:i + chunk_size] for i in range(0, N, chunk_size)]

    start = time.time()
    with Pool(processes=num_procs) as pool:
        results = pool.map(chunk_sum, chunks)

    total = sum(results)
    end = time.time()

    print(f"Sum = {total}")
    print(f"Time taken: {end - start:.4f} seconds using {num_procs} cores")
