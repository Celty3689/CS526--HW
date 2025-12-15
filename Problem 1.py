import sys
import heapq

def solve_dam_breaking(input_text: str) -> str:
    """Solve the dam breaking problem, return output string"""
    input_data = input_text.strip().split()
    if not input_data:
        return ""

    idx = 0
    n = int(input_data[idx]); idx += 1
    threshold = int(input_data[idx]); idx += 1
    drain = int(input_data[idx]); idx += 1

    cracks = []
    for _ in range(n):
        t = int(input_data[idx]); idx += 1
        s = int(input_data[idx]); idx += 1
        cracks.append((t, s))

    #Use max heap (by storing negative values)
    heap = []  #Max heap, stores negative size values
    water = 0
    max_water = 0
    crack_idx = 0
    total_cracks = len(cracks)
    current_time = 0

    offset = 0  #Track how many times cracks have grown
    total_unfixed_size = 0

    while crack_idx < total_cracks or heap:
        #Add new cracks that appear at current time
        while crack_idx < total_cracks and cracks[crack_idx][0] <= current_time:
            initial_size = cracks[crack_idx][1]
            #Use max heap, store negative value with offset adjustment
            heapq.heappush(heap, -initial_size + offset)
            total_unfixed_size += initial_size
            crack_idx += 1

        #Fix one crack (choose the largest one)
        if heap:
            #Get largest crack from max heap
            max_crack = -heapq.heappop(heap) + offset
            total_unfixed_size -= max_crack

        #Calculate water change
        water += total_unfixed_size - drain
        if water < 0:
            water = 0

        #Update maximum water level
        if water > max_water:
            max_water = water

        #Check for flood
        if water >= threshold:
            return f"FLOOD\n{current_time}\n{water}"

        #all unfixed cracks increase by 1
        offset += 1
        total_unfixed_size += len(heap)  #Each unfixed crack grows by 1

        current_time += 1

    return f"SAFE\n{max_water}"

def main():
    """Main function: test specified file list"""
    test_files = [
        'flood_1.txt','flood_2.txt', 'flood_3.txt','flood_4.txt','flood_5.txt',
        'flood_6.txt','flood_7.txt','flood_11.txt','flood_12.txt'
    ]

    for filename in test_files:
        try:
            with open(filename, 'r') as f:
                input_text = f.read()
                result = solve_dam_breaking(input_text)
                print(f"=== {filename} ===")
                print(result)
                print()
        except FileNotFoundError:
            print(f"=== {filename} ===")
            print(f"Error: File '{filename}' not found")
            print()
        except Exception as e:
            print(f"=== {filename} ===")
            print(f"Error processing file: {e}")
            print()

if __name__ == "__main__":
    main()