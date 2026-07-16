import time
import random

# --- Configuration ---
NUM_DOCUMENTS = 5000  # Total number of "documents" to process
DOCUMENT_LENGTH = 1000 # Length of each simulated document string
BATCH_SIZE = 50      # Number of documents to process in one batch for optimized approach
SIMULATED_PROCESSING_TIME_PER_DOC = 0.001 # Simulate CPU work per document

def generate_dummy_document(length):
    """Generates a dummy document string."""
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz ', k=length))

def simulate_ai_processing(documents_batch):
    """
    Simulates AI model processing for a batch of documents.
    This function represents the CPU and memory intensive work.
    """
    # Simulate CPU-bound work: e.g., complex string operations, calculations
    for doc in documents_batch:
        # A simple, CPU-intensive operation (e.g., finding all occurrences of a char)
        _ = doc.count('a')
        _ = doc.upper()
        # Simulate actual AI model inference time
        time.sleep(SIMULATED_PROCESSING_TIME_PER_DOC)
    return f"Processed {len(documents_batch)} documents."

def main():
    print("--- Simulating AI Resource Consumption and Optimization ---")
    print(f"Total documents to process: {NUM_DOCUMENTS}")
    print(f"Document length: {DOCUMENT_LENGTH} characters")
    print(f"Batch size for optimized processing: {BATCH_SIZE}\n")

    # Generate all dummy documents upfront to simulate loading a large dataset
    print("Generating all dummy documents (this consumes memory)...")
    all_documents = [generate_dummy_document(DOCUMENT_LENGTH) for _ in range(NUM_DOCUMENTS)]
    # Note: Actual memory usage for Python strings is more complex due to object overhead.
    print(f"Generated {len(all_documents)} documents. Total data size in memory (rough estimate): ~{NUM_DOCUMENTS * DOCUMENT_LENGTH / (1024*1024):.2f} MB (string objects overhead not included).\n")
    print("Please observe your system's Task Manager/Activity Monitor for CPU and Memory usage during the next steps.\n")

    print("--- UNOPTIMIZED APPROACH: Processing all documents at once ---")
    print("Expect higher peak memory and sustained CPU usage during this phase.")
    start_time = time.time()
    # This simulates loading all data into memory and then processing it,
    # potentially leading to high memory spikes and sustained CPU load.
    # In a real LLM scenario, this could be feeding a very large prompt or many prompts
    # without proper batching or streaming.
    result_unoptimized = simulate_ai_processing(all_documents) # This is where the "machine starving" happens
    end_time = time.time()
    print(f"Unoptimized processing finished: {result_unoptimized}")
    print(f"Time taken (unoptimized): {end_time - start_time:.2f} seconds\n")


    print("--- OPTIMIZED APPROACH: Processing documents in batches ---")
    print(f"Processing in batches of {BATCH_SIZE}. Expect lower peak memory and more controlled CPU usage.")
    start_time = time.time()
    processed_count = 0
    # This simulates processing data in smaller, manageable chunks.
    # This reduces peak memory requirements and can allow for better resource scheduling.
    # For LLMs, this means sending smaller prompts or breaking down large tasks into sub-tasks.
    for i in range(0, NUM_DOCUMENTS, BATCH_SIZE):
        batch = all_documents[i:i + BATCH_SIZE]
        print(f"  Processing batch {i // BATCH_SIZE + 1}/{(NUM_DOCUMENTS + BATCH_SIZE - 1) // BATCH_SIZE} ({len(batch)} documents)...")
        batch_result = simulate_ai_processing(batch) # Resource consumption is now in smaller bursts
        processed_count += len(batch)
        # Optional: Clear batch memory if not needed for next step (Python's GC handles this)
        # del batch # Python's GC will handle this when 'batch' goes out of scope in the loop
        # time.sleep(0.05) # Simulate a small pause between batches if needed to spread out CPU further
    end_time = time.time()
    print(f"Optimized processing finished: Processed {processed_count} documents.")
    print(f"Time taken (optimized): {end_time - start_time:.2f} seconds\n")

    print("--- Comparison ---")
    print("Notice how the optimized approach spreads out the resource usage, potentially preventing system slowdowns.")
    print("While total time might be similar (or slightly more due to overhead), peak resource demands are reduced.")

if __name__ == "__main__":
    main()
