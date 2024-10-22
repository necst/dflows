TIREX_FOLDER=./results
CICERO_FOLDER=./results

python3 generate_graphs.py -d $TIREX_FOLDER/tirex_exact_res/ -n -cic -tir --hypervolume tirex
python3 generate_graphs.py -d $TIREX_FOLDER/tirex_approxima_res/ -r $TIREX_FOLDER/tirex_exact_res/ -n -cic -tir --hypervolume tirex
python3 generate_graphs.py -d $CICERO_FOLDER/cicero_exact_res/ -n -cic --hypervolume cicero
python3 generate_graphs.py -d $CICERO_FOLDER/cicero_approximate_res/ -r $CICERO_FOLDER/cicero_exact_res/ -n -cic --hypervolume cicero

python3 generate_graphs.py -d results/corundum_exact_2 -n
python3 generate_graphs.py -d results/corundum_approx_2 -r results/corundum_exact_2 -n 
python3 generate_graphs.py -d results/neorv32_exact_2
python3 generate_graphs.py -d results/neorv32_approx_2 -r results/neorv32_exact_2

python3 generate_graphs.py -d results/neorv32_xa7a12_custom_exact
python3 generate_graphs.py -d results/neorv32_xa7a12_custom_approx -r results/neorv32_xa7a12_custom_exact

python3 generate_graphs.py -d results/neorv32_xa7a12_custom_exact
python3 generate_graphs.py -d results/neorv32_xa7a12_custom_approx -r results/neorv32_xa7a12_custom_exact
