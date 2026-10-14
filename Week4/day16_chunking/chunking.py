from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter
)

text = """
Artificial Intelligence is transforming the modern world.
It enables machines to perform tasks that normally require human intelligence.

Machine Learning is a subset of Artificial Intelligence.
It allows computers to learn patterns from data without being explicitly programmed.

Deep Learning is a subset of Machine Learning.
It uses neural networks with multiple layers to learn complex patterns.
"""

# 1. Fixed separator-based chunking
fixed_splitter = CharacterTextSplitter(
    separator=" ",
    chunk_size=100,
    chunk_overlap=10,
    length_function=len
)

fixed_chunks = fixed_splitter.split_text(text)

print("\n--- Fixed Separator Chunking ---")
for i, chunk in enumerate(fixed_chunks, 1):
    print(f"Chunk {i}: {chunk}")


# 2. Paragraph-based chunking
paragraph_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=200,
    chunk_overlap=0,
    length_function=len
)

paragraph_chunks = paragraph_splitter.split_text(text)

print("\n--- Paragraph-Based Chunking ---")
for i, chunk in enumerate(paragraph_chunks, 1):
    print(f"Chunk {i}: {chunk}")


# 3. Recursive character chunking
recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separators=["\n\n", "\n", " ", ""],
    length_function=len
)

recursive_chunks = recursive_splitter.split_text(text)

print("\n--- Recursive Chunking ---")
for i, chunk in enumerate(recursive_chunks, 1):
    print(f"Chunk {i}: {chunk}")

