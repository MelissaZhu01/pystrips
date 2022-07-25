echo
echo '>> Solving blocksworld/problems/probBLOCKS-04-0.pddl ...'
echo
python pystrips.py solve pddl/blocksworld/domain.pddl pddl/blocksworld/problems/probBLOCKS-04-0.pddl --heuristics $1 --weight $2