## Top Frequent Words

### Algorithm

1. Read the file **line by line** so the entire dataset is not loaded into memory.
2. Use a **hash map (dictionary)** to store the frequency of each word.
3. For every word in the file:
   - Remove whitespace using `strip()`
   - Increment its count in the dictionary.
4. After processing the entire file, **sort the dictionary by frequency in descending order**.
5. Return the **top 10 words with the highest frequencies**.

---

### Data Structures Used

#### Hash Map (Dictionary)

A *hash map (dictionary)* is used to store the frequency of each word.

This allows:
- **O(1) average lookup and update**
- Efficient counting of occurrences
- Scalable handling of large datasets

Example structure:
{
"apple": 3,
"banana": 2,
"orange": 1
}
