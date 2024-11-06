from src.betweenness import BetweennessCentrality

import os

def main():
    map_list = ['empty-8-8', 'empty-16-16', 'empty-32-32', 'empty-48-48',
                'random-32-32-10', 'random-32-32-20', 'random-64-64-10', 'random-64-64-20',
                'room-32-32-4', 'room-64-64-8', 'room-64-64-16',
                'maze-32-32-2', 'maze-32-32-4', 'maze-128-128-2', 'maze-128-128-10',
                'Berlin_1_256', 'Boston_0_256', 'Paris_1_256',
                'ht_chantry', 'ht_mansion_n', 'lak303d', 'lt_gallowstemplar_n', 'den312d', 'ost003d',
                'brc202d', 'den520d', 'w_woundedcoast']

    score_dir = os.path.join(os.getcwd(), "scored_benchmarks")
    if not os.path.isdir(score_dir):
        os.mkdir(score_dir)
        print("Making a new directory to hold the benchmark scorings.")

    for map_name in map_list:
        print(f"Scoring [{map_name}]...")
        bc = BetweennessCentrality(map_name)
        bc.Brandes()
        print("\t Done!")

if __name__=="__main__":
    main()
